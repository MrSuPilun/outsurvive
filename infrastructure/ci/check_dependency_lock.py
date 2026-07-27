#!/usr/bin/env python3
"""Validate the dependency lock and its generated CycloneDX SBOM."""

from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from pathlib import Path
from typing import Any


LOCK_SCHEMA_VERSION = 1
SBOM_SPEC_VERSION = "1.6"
PROMOTION_STATUSES = {"toolchain", "editor_only", "not_promoted", "promoted"}
LICENSE_DECISIONS = {"approved", "undecided", "rejected"}
REQUIRED_DEPENDENCY_FIELDS = {
    "id",
    "kind",
    "version",
    "source",
    "license",
    "license_decision",
    "wrapper",
    "owner",
    "platform_applicability",
    "promotion_status",
    "artifacts",
}
FLOATING_VERSION = re.compile(
    r"(^|[._-])(latest|main|master|head|trunk|snapshot)([._-]|$)|"
    r"(^[~^<>=*])|(\.\*)|(\bx\b)",
    re.IGNORECASE,
)
HEX_PATTERN = re.compile(r"^[0-9a-fA-F]+$")
SECRET_KEY_PATTERN = re.compile(
    r"(secret|token|password|credential|private[_-]?key|signing[_-]?key)",
    re.IGNORECASE,
)


def violation(
    rule_id: str,
    path: str,
    message: str,
    dependency_id: str | None = None,
) -> dict[str, str]:
    item = {"rule_id": rule_id, "path": path, "message": message}
    if dependency_id:
        item["dependency_id"] = dependency_id
    return item


def parse_lock(lock_path: Path) -> tuple[dict[str, Any], list[dict[str, str]]]:
    try:
        data = tomllib.loads(lock_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, tomllib.TOMLDecodeError) as error:
        return {}, [
            violation("LOCK_SCHEMA_INVALID", str(lock_path), str(error))
        ]
    return data, []


def _contains_version(reference: str, version: str) -> bool:
    escaped_version = re.escape(version.removesuffix("-stable"))
    normalized_version = escaped_version.replace(r"\.", r"[._-]")
    return bool(re.search(normalized_version, reference, re.IGNORECASE))


def validate_lock(
    data: dict[str, Any], lock_path: Path
) -> tuple[list[dict[str, str]], list[dict[str, Any]]]:
    violations: list[dict[str, str]] = []
    if data.get("schema_version") != LOCK_SCHEMA_VERSION:
        violations.append(
            violation(
                "LOCK_SCHEMA_INVALID",
                "schema_version",
                f"schema_version must be {LOCK_SCHEMA_VERSION}",
            )
        )
    dependencies = data.get("dependencies")
    if not isinstance(dependencies, list) or not dependencies:
        violations.append(
            violation(
                "LOCK_SCHEMA_INVALID",
                "dependencies",
                "dependencies must be a non-empty array",
            )
        )
        return violations, []

    seen_ids: set[str] = set()
    for index, dependency in enumerate(dependencies):
        path = f"dependencies[{index}]"
        if not isinstance(dependency, dict):
            violations.append(
                violation("LOCK_SCHEMA_INVALID", path, "entry must be a table")
            )
            continue
        dependency_id = str(dependency.get("id", f"index-{index}"))
        missing = sorted(REQUIRED_DEPENDENCY_FIELDS - dependency.keys())
        if missing:
            violations.append(
                violation(
                    "LOCK_SCHEMA_INVALID",
                    path,
                    f"missing required field(s): {', '.join(missing)}",
                    dependency_id,
                )
            )
        if dependency_id in seen_ids:
            violations.append(
                violation(
                    "LOCK_SCHEMA_INVALID",
                    f"{path}.id",
                    f"duplicate dependency id: {dependency_id}",
                    dependency_id,
                )
            )
        seen_ids.add(dependency_id)

        for field in (
            "id",
            "kind",
            "version",
            "source",
            "license",
            "license_decision",
            "wrapper",
            "owner",
            "promotion_status",
        ):
            value = dependency.get(field)
            if not isinstance(value, str) or not value.strip():
                violations.append(
                    violation(
                        "LOCK_SCHEMA_INVALID",
                        f"{path}.{field}",
                        f"{field} must be a non-empty string",
                        dependency_id,
                    )
                )
        platforms = dependency.get("platform_applicability")
        if (
            not isinstance(platforms, list)
            or not platforms
            or not all(isinstance(item, str) and item for item in platforms)
        ):
            violations.append(
                violation(
                    "LOCK_SCHEMA_INVALID",
                    f"{path}.platform_applicability",
                    "platform_applicability must be a non-empty string array",
                    dependency_id,
                )
            )

        version = dependency.get("version")
        if isinstance(version, str) and FLOATING_VERSION.search(version):
            violations.append(
                violation(
                    "LOCK_FLOATING_VERSION",
                    f"{path}.version",
                    f"floating version is forbidden: {version}",
                    dependency_id,
                )
            )
        promotion = dependency.get("promotion_status")
        if promotion not in PROMOTION_STATUSES:
            violations.append(
                violation(
                    "LOCK_PROMOTION_INVALID",
                    f"{path}.promotion_status",
                    f"promotion_status must be one of {sorted(PROMOTION_STATUSES)}",
                    dependency_id,
                )
            )
        license_decision = dependency.get("license_decision")
        if license_decision not in LICENSE_DECISIONS:
            violations.append(
                violation(
                    "LOCK_SCHEMA_INVALID",
                    f"{path}.license_decision",
                    f"license_decision must be one of {sorted(LICENSE_DECISIONS)}",
                    dependency_id,
                )
            )
        if promotion == "promoted" and license_decision != "approved":
            violations.append(
                violation(
                    "LOCK_LICENSE_UNDECIDED_PROMOTE",
                    f"{path}.license_decision",
                    "promoted dependencies require license_decision=approved",
                    dependency_id,
                )
            )
        if dependency_id in {"godot.editor", "godot.export_templates"}:
            if (
                version != "4.7.1-stable"
                or dependency.get("flavor") != "standard"
            ):
                violations.append(
                    violation(
                        "LOCK_SCHEMA_INVALID",
                        path,
                        "Godot editor/templates must pin Standard 4.7.1-stable",
                        dependency_id,
                    )
                )
        if dependency_id == "godot.editor" and dependency.get("commit") != "a13da4feb":
            violations.append(
                violation(
                    "LOCK_SCHEMA_INVALID",
                    f"{path}.commit",
                    "Godot editor must pin official commit a13da4feb",
                    dependency_id,
                )
            )

        artifacts = dependency.get("artifacts")
        if not isinstance(artifacts, list) or not artifacts:
            violations.append(
                violation(
                    "LOCK_SCHEMA_INVALID",
                    f"{path}.artifacts",
                    "artifacts must be a non-empty array",
                    dependency_id,
                )
            )
            continue
        for artifact_index, artifact in enumerate(artifacts):
            artifact_path = f"{path}.artifacts[{artifact_index}]"
            required = {
                "id",
                "role",
                "platform",
                "source",
                "checksum_algorithm",
                "checksum_hex",
            }
            if not isinstance(artifact, dict):
                violations.append(
                    violation(
                        "LOCK_SCHEMA_INVALID",
                        artifact_path,
                        "artifact must be a table",
                        dependency_id,
                    )
                )
                continue
            artifact_missing = sorted(required - artifact.keys())
            if artifact_missing:
                violations.append(
                    violation(
                        "LOCK_SCHEMA_INVALID",
                        artifact_path,
                        f"missing artifact field(s): {', '.join(artifact_missing)}",
                        dependency_id,
                    )
                )
                continue
            algorithm = str(artifact["checksum_algorithm"]).lower()
            checksum = str(artifact["checksum_hex"])
            expected_length = {"sha256": 64, "sha512": 128}.get(algorithm)
            if (
                expected_length is None
                or len(checksum) != expected_length
                or not HEX_PATTERN.fullmatch(checksum)
            ):
                violations.append(
                    violation(
                        "LOCK_CHECKSUM_INVALID",
                        f"{artifact_path}.checksum_hex",
                        "checksum must be 64-char SHA-256 or 128-char SHA-512 hex",
                        dependency_id,
                    )
                )
            artifact_reference = f"{artifact.get('id', '')} {artifact.get('source', '')}"
            if (
                isinstance(version, str)
                and not FLOATING_VERSION.search(version)
                and not _contains_version(artifact_reference, version)
            ):
                violations.append(
                    violation(
                        "LOCK_CHECKSUM_MISMATCH",
                        artifact_path,
                        "artifact identity/source does not bind the dependency version",
                        dependency_id,
                    )
                )

    def inspect_secrets(value: object, path: str) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                child_path = f"{path}.{key}" if path else str(key)
                if SECRET_KEY_PATTERN.search(str(key)):
                    violations.append(
                        violation(
                            "LOCK_SCHEMA_INVALID",
                            child_path,
                            "secret or credential fields are forbidden in the lock",
                        )
                    )
                inspect_secrets(child, child_path)
        elif isinstance(value, list):
            for child_index, child in enumerate(value):
                inspect_secrets(child, f"{path}[{child_index}]")

    inspect_secrets(data, "")
    return violations, dependencies


def validate_sbom(
    sbom_path: Path, dependencies: list[dict[str, Any]]
) -> tuple[list[dict[str, str]], int, str]:
    try:
        sbom = json.loads(sbom_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        return [
            violation("SBOM_INCOMPLETE", str(sbom_path), str(error))
        ], 0, ""
    violations: list[dict[str, str]] = []
    if (
        sbom.get("bomFormat") != "CycloneDX"
        or sbom.get("specVersion") != SBOM_SPEC_VERSION
    ):
        violations.append(
            violation(
                "SBOM_INCOMPLETE",
                str(sbom_path),
                f"SBOM must be CycloneDX {SBOM_SPEC_VERSION}",
            )
        )
    components = sbom.get("components")
    if not isinstance(components, list):
        return violations + [
            violation(
                "SBOM_INCOMPLETE",
                "components",
                "components must be an array",
            )
        ], 0, str(sbom.get("specVersion", ""))
    components_by_name = {
        component.get("name"): component
        for component in components
        if isinstance(component, dict)
    }
    for dependency in dependencies:
        dependency_id = dependency["id"]
        component = components_by_name.get(dependency_id)
        if component is None:
            violations.append(
                violation(
                    "SBOM_INCOMPLETE",
                    "components",
                    "lock dependency is absent from SBOM",
                    dependency_id,
                )
            )
            continue
        license_rows = component.get("licenses", [])
        license_ids = {
            row.get("license", {}).get("id")
            for row in license_rows
            if isinstance(row, dict)
        }
        references = component.get("externalReferences", [])
        if dependency["license"] not in license_ids or not references:
            violations.append(
                violation(
                    "SBOM_INCOMPLETE",
                    f"components.{dependency_id}",
                    "component must include lock license and source reference",
                    dependency_id,
                )
            )
        actual_hashes = {
            (row.get("alg"), str(row.get("content", "")).lower())
            for row in component.get("hashes", [])
            if isinstance(row, dict)
        }
        expected_hashes = {
            (
                "SHA-256"
                if artifact["checksum_algorithm"].lower() == "sha256"
                else "SHA-512",
                artifact["checksum_hex"].lower(),
            )
            for artifact in dependency["artifacts"]
        }
        if actual_hashes != expected_hashes:
            violations.append(
                violation(
                    "SBOM_HASH_MISMATCH",
                    f"components.{dependency_id}.hashes",
                    "SBOM hashes do not exactly match the lock",
                    dependency_id,
                )
            )
    if len(components) != len(dependencies):
        violations.append(
            violation(
                "SBOM_INCOMPLETE",
                "components",
                "SBOM component count must equal dependency count",
            )
        )
    return violations, len(components), str(sbom.get("specVersion", ""))


def evidence_document(
    lock_path: Path,
    dependencies: list[dict[str, Any]],
    violations: list[dict[str, str]],
    sbom_path: Path | None,
    sbom_component_count: int,
    sbom_spec_version: str,
) -> dict[str, object]:
    return {
        "schema_version": 1,
        "status": "failure" if violations else "pass",
        "lock_path": str(lock_path),
        "lock_schema_version": LOCK_SCHEMA_VERSION,
        "dependency_count": len(dependencies),
        "sbom_path": str(sbom_path) if sbom_path else "",
        "sbom_component_count": sbom_component_count,
        "sbom_spec_version": sbom_spec_version,
        "checks": ["schema", "checksums", "promotion"]
        + (["sbom"] if sbom_path else []),
        "violations": violations,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lock", type=Path, required=True)
    parser.add_argument("--sbom", type=Path)
    parser.add_argument("--skip-sbom", action="store_true")
    arguments = parser.parse_args()
    data, violations = parse_lock(arguments.lock)
    dependencies: list[dict[str, Any]] = []
    if not violations:
        lock_violations, dependencies = validate_lock(data, arguments.lock)
        violations.extend(lock_violations)
    sbom_count = 0
    sbom_version = ""
    sbom_path = None if arguments.skip_sbom else arguments.sbom
    if not violations and sbom_path:
        sbom_violations, sbom_count, sbom_version = validate_sbom(
            sbom_path, dependencies
        )
        violations.extend(sbom_violations)
    document = evidence_document(
        arguments.lock,
        dependencies,
        violations,
        sbom_path,
        sbom_count,
        sbom_version,
    )
    json.dump(document, sys.stdout, ensure_ascii=True, sort_keys=True)
    sys.stdout.write("\n")
    return 1 if violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
