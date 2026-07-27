#!/usr/bin/env python3
"""Generate a deterministic CycloneDX 1.6 SBOM from dependency_lock.toml."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from check_dependency_lock import parse_lock, validate_lock


TYPE_MAP = {
    "engine": "application",
    "database": "application",
    "orchestrator": "application",
    "tool": "application",
    "plugin": "library",
    "sdk": "library",
    "framework": "framework",
}


def component_for(dependency: dict[str, object]) -> dict[str, object]:
    artifacts = dependency["artifacts"]
    assert isinstance(artifacts, list)
    hashes = sorted(
        (
            {
                "alg": (
                    "SHA-256"
                    if artifact["checksum_algorithm"].lower() == "sha256"
                    else "SHA-512"
                ),
                "content": artifact["checksum_hex"].lower(),
            }
            for artifact in artifacts
        ),
        key=lambda row: (row["alg"], row["content"]),
    )
    references = [
        {
            "type": "distribution",
            "url": artifact["source"],
            "comment": (
                f"{artifact['id']} ({artifact['role']}, {artifact['platform']})"
            ),
        }
        for artifact in sorted(artifacts, key=lambda row: row["id"])
    ]
    properties = [
        {
            "name": "outsurvive:license_decision",
            "value": dependency["license_decision"],
        },
        {
            "name": "outsurvive:promotion_status",
            "value": dependency["promotion_status"],
        },
        {"name": "outsurvive:owner", "value": dependency["owner"]},
        {"name": "outsurvive:wrapper", "value": dependency["wrapper"]},
        {
            "name": "outsurvive:platform_applicability",
            "value": ",".join(dependency["platform_applicability"]),
        },
    ]
    return {
        "type": TYPE_MAP.get(str(dependency["kind"]), "library"),
        "bom-ref": f"dependency:{dependency['id']}@{dependency['version']}",
        "name": dependency["id"],
        "version": dependency["version"],
        "licenses": [{"license": {"id": dependency["license"]}}],
        "hashes": hashes,
        "externalReferences": references,
        "properties": properties,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lock", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    data, violations = parse_lock(arguments.lock)
    dependencies: list[dict[str, object]] = []
    if not violations:
        violations, dependencies = validate_lock(data, arguments.lock)
    if violations:
        json.dump(
            {"status": "failure", "violations": violations},
            sys.stdout,
            sort_keys=True,
        )
        sys.stdout.write("\n")
        return 1

    lock_bytes = arguments.lock.read_bytes()
    lock_sha256 = hashlib.sha256(lock_bytes).hexdigest()
    components = [
        component_for(dependency)
        for dependency in sorted(dependencies, key=lambda row: row["id"])
    ]
    sbom = {
        "bomFormat": "CycloneDX",
        "specVersion": "1.6",
        "serialNumber": f"urn:uuid:{lock_sha256[:8]}-{lock_sha256[8:12]}-"
        f"{lock_sha256[12:16]}-{lock_sha256[16:20]}-{lock_sha256[20:32]}",
        "version": 1,
        "metadata": {
            "component": {
                "type": "application",
                "bom-ref": "application:outsurvive",
                "name": "outsurvive",
            },
            "properties": [
                {"name": "outsurvive:lock_sha256", "value": lock_sha256},
                {"name": "outsurvive:generated", "value": "do_not_edit"},
            ],
        },
        "components": components,
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(sbom, indent=2, ensure_ascii=True, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    json.dump(
        {
            "status": "pass",
            "component_count": len(components),
            "lock_sha256": lock_sha256,
            "output": str(arguments.output),
        },
        sys.stdout,
        sort_keys=True,
    )
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
