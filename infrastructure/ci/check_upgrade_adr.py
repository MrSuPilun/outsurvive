#!/usr/bin/env python3
"""Fail-closed validator for dependency upgrade ADR instances."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED_FIELDS = {
    "title",
    "status",
    "date",
    "dependency_id",
    "from_version",
    "to_version",
    "rationale",
    "compatibility_branch",
    "protocol_impact",
    "content_manifest_impact",
    "license_decision",
    "cve_decision",
    "adr20_spike_evidence",
    "rollback_plan",
}
FRONTMATTER_FIELDS = REQUIRED_FIELDS - {"rationale"}


def violation(path: str, message: str) -> dict[str, str]:
    return {
        "rule_id": "ADR_SCHEMA_INVALID",
        "path": path,
        "message": message,
    }


def parse_frontmatter(text: str) -> tuple[dict[str, str], list[dict[str, str]]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, [violation("frontmatter", "ADR must begin with YAML frontmatter")]
    try:
        end = next(
            index
            for index, line in enumerate(lines[1:], start=1)
            if line.strip() == "---"
        )
    except StopIteration:
        return {}, [violation("frontmatter", "frontmatter closing marker is missing")]
    fields: dict[str, str] = {}
    violations: list[dict[str, str]] = []
    for line_number, line in enumerate(lines[1:end], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            violations.append(
                violation(
                    f"frontmatter:{line_number}",
                    "frontmatter entries must use key: value",
                )
            )
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip("\"'")
    return fields, violations


def validate_adr(path: Path) -> list[dict[str, str]]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        return [violation(str(path), str(error))]
    fields, violations = parse_frontmatter(text)
    if re.search(r"^# Rationale\s*$", text, re.MULTILINE):
        fields["rationale"] = "section"
    for field in sorted(REQUIRED_FIELDS):
        if not fields.get(field):
            violations.append(
                violation(field, f"required ADR field is missing: {field}")
            )
    status = fields.get("status", "")
    if status not in {"proposed", "accepted", "rejected", "superseded"}:
        violations.append(
            violation("status", "status must be proposed, accepted, rejected, or superseded")
        )
    if fields.get("license_decision") not in {"approved", "undecided", "rejected"}:
        violations.append(
            violation(
                "license_decision",
                "license_decision must be approved, undecided, or rejected",
            )
        )
    cve_decision = fields.get("cve_decision", "")
    if not re.match(r"^(cleared|undecided|accepted_risk(?:\s*-\s*.+)?)$", cve_decision):
        violations.append(
            violation(
                "cve_decision",
                "cve_decision must be cleared, undecided, or accepted_risk with justification",
            )
        )
    if status == "accepted":
        if fields.get("license_decision") != "approved":
            violations.append(
                violation(
                    "license_decision",
                    "accepted ADR requires license_decision=approved",
                )
            )
        if cve_decision == "undecided":
            violations.append(
                violation(
                    "cve_decision",
                    "accepted ADR cannot leave CVE decision undecided",
                )
            )
    matrix_match = re.search(
        r"^## Impacted Platform Smoke Matrix\s*$([\s\S]*?)(?=^## |\Z)",
        text,
        re.MULTILINE,
    )
    if not matrix_match:
        violations.append(
            violation(
                "impacted_platform_smoke_matrix",
                "Impacted Platform Smoke Matrix section is missing",
            )
        )
    else:
        table_rows = [
            line
            for line in matrix_match.group(1).splitlines()
            if line.strip().startswith("|")
            and "---" not in line
            and not re.match(r"^\s*\|\s*Platform\s*\|", line, re.IGNORECASE)
        ]
        if not table_rows or any(len(row.split("|")) < 5 for row in table_rows):
            violations.append(
                violation(
                    "impacted_platform_smoke_matrix",
                    "smoke matrix requires at least one platform, gate, and owner row",
                )
            )
    return violations


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("adr", type=Path)
    arguments = parser.parse_args()
    violations = validate_adr(arguments.adr)
    json.dump(
        {
            "schema_version": 1,
            "status": "failure" if violations else "pass",
            "adr_path": str(arguments.adr),
            "checks": ["required_fields", "decisions", "smoke_matrix"],
            "violations": violations,
        },
        sys.stdout,
        sort_keys=True,
    )
    sys.stdout.write("\n")
    return 1 if violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
