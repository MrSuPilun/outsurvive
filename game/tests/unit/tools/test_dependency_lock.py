from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


PYTHON_BIN = os.environ.get("DEPENDENCY_LOCK_PYTHON", sys.executable)
REPO_ROOT = Path(__file__).resolve().parents[4]
CHECK_LOCK = REPO_ROOT / "infrastructure/ci/check_dependency_lock.py"
GENERATE_SBOM = REPO_ROOT / "infrastructure/ci/generate_sbom.py"
CHECK_ADR = REPO_ROOT / "infrastructure/ci/check_upgrade_adr.py"
EXPORT_GODOT_SHA256 = REPO_ROOT / "infrastructure/ci/export_godot_sha256.py"
REAL_LOCK = REPO_ROOT / "infrastructure/ci/dependency_lock.toml"
REAL_SBOM = REPO_ROOT / "infrastructure/ci/sbom/outsurvive.cdx.json"


VALID_LOCK = """
schema_version = 1

[[dependencies]]
id = "fixture.tool"
kind = "tool"
version = "1.2.3"
source = "https://example.invalid/fixture-tool/releases/1.2.3"
license = "MIT"
license_decision = "approved"
wrapper = "none: invoked only by infrastructure CI"
owner = "infrastructure"
platform_applicability = ["linux_x64"]
promotion_status = "toolchain"

[[dependencies.artifacts]]
id = "fixture-tool-1.2.3"
role = "archive"
platform = "linux_x64"
source = "https://example.invalid/fixture-tool-1.2.3.zip"
checksum_algorithm = "sha256"
checksum_hex = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
"""


VALID_ADR = """
---
title: Upgrade fixture.tool to 1.2.4
status: proposed
date: 2026-07-27
dependency_id: fixture.tool
from_version: 1.2.3
to_version: 1.2.4
compatibility_branch: compat/fixture-tool-1-2-4
protocol_impact: none - build-only tool
content_manifest_impact: none - build-only tool
license_decision: approved
cve_decision: cleared
adr20_spike_evidence: n/a - non-plugin tool
rollback_plan: Revert the lock and this ADR.
---

# Rationale

Exercise the upgrade gate.

## Impacted Platform Smoke Matrix

| Platform | Gate | Owner |
|---|---|---|
| linux_x64 | dependency lock verifier | infrastructure |
"""


class DependencyLockTests(unittest.TestCase):
    def _write(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")

    def _run_json(self, *arguments: object) -> tuple[subprocess.CompletedProcess[str], dict[str, object]]:
        result = subprocess.run(
            [PYTHON_BIN, *(str(argument) for argument in arguments)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertTrue(result.stdout, result.stderr)
        return result, json.loads(result.stdout)

    def _assert_lock_rejected(
        self, lock_text: str, expected_rule_id: str
    ) -> dict[str, object]:
        with tempfile.TemporaryDirectory() as temp_dir:
            lock_path = Path(temp_dir) / "dependency_lock.toml"
            self._write(lock_path, lock_text)
            result, evidence = self._run_json(
                CHECK_LOCK, "--lock", lock_path, "--skip-sbom"
            )
        self.assertNotEqual(0, result.returncode, evidence)
        violations = evidence["violations"]
        matching = [
            violation
            for violation in violations
            if violation["rule_id"] == expected_rule_id
        ]
        self.assertTrue(matching, evidence)
        self.assertIn("path", matching[0])
        self.assertIn("message", matching[0])
        return matching[0]

    def test_minimal_lock_is_valid_and_emits_structured_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            lock_path = Path(temp_dir) / "dependency_lock.toml"
            self._write(lock_path, VALID_LOCK)
            result, evidence = self._run_json(
                CHECK_LOCK, "--lock", lock_path, "--skip-sbom"
            )
        self.assertEqual(0, result.returncode, evidence)
        self.assertEqual("pass", evidence["status"])
        self.assertEqual(1, evidence["dependency_count"])
        self.assertEqual([], evidence["violations"])

    def test_lock_drift_is_rejected_when_version_and_artifact_disagree(self) -> None:
        drifted = VALID_LOCK.replace('version = "1.2.3"', 'version = "9.9.9"')
        self._assert_lock_rejected(drifted, "LOCK_CHECKSUM_MISMATCH")

    def test_corrupt_checksum_is_rejected(self) -> None:
        corrupt = VALID_LOCK.replace(
            'checksum_hex = "' + "a" * 64 + '"',
            'checksum_hex = "not-hex"',
        )
        self._assert_lock_rejected(corrupt, "LOCK_CHECKSUM_INVALID")

    def test_missing_required_dependency_fields_are_rejected(self) -> None:
        for field in ("source", "license", "wrapper", "owner"):
            with self.subTest(field=field):
                lines = [
                    line
                    for line in VALID_LOCK.splitlines()
                    if not line.startswith(f"{field} =")
                ]
                violation = self._assert_lock_rejected(
                    "\n".join(lines), "LOCK_SCHEMA_INVALID"
                )
                self.assertIn(field, violation["message"])

    def test_floating_versions_are_rejected(self) -> None:
        for version in ("latest", "main", "^1.2", ">=1.2"):
            with self.subTest(version=version):
                lock_text = VALID_LOCK.replace(
                    'version = "1.2.3"', f'version = "{version}"'
                )
                self._assert_lock_rejected(lock_text, "LOCK_FLOATING_VERSION")

    def test_promoted_dependency_requires_decided_license(self) -> None:
        lock_text = VALID_LOCK.replace(
            'license_decision = "approved"', 'license_decision = "undecided"'
        ).replace(
            'promotion_status = "toolchain"', 'promotion_status = "promoted"'
        )
        self._assert_lock_rejected(
            lock_text, "LOCK_LICENSE_UNDECIDED_PROMOTE"
        )

    def test_godot_baseline_rejects_wrong_version_or_flavor(self) -> None:
        godot_lock = VALID_LOCK.replace(
            'id = "fixture.tool"',
            'id = "godot.editor"\ncommit = "a13da4feb"\nflavor = "standard"',
        )
        for old, new in (
            ('version = "4.7.1-stable"', 'version = "4.8.0-stable"'),
            ('flavor = "standard"', 'flavor = "mono"'),
        ):
            with self.subTest(new=new):
                candidate = godot_lock.replace(
                    'version = "1.2.3"', 'version = "4.7.1-stable"'
                )
                candidate = candidate.replace(
                    "fixture-tool-1.2.3", "fixture-tool-4.7.1"
                ).replace(
                    "fixture-tool-1.2.3.zip", "fixture-tool-4.7.1.zip"
                )
                candidate = candidate.replace(old, new)
                self._assert_lock_rejected(candidate, "LOCK_SCHEMA_INVALID")

    def test_secret_fields_are_rejected(self) -> None:
        lock_text = VALID_LOCK.replace(
            'owner = "infrastructure"',
            'owner = "infrastructure"\nplatform_token = "forbidden"',
        )
        violation = self._assert_lock_rejected(
            lock_text, "LOCK_SCHEMA_INVALID"
        )
        self.assertIn("secret or credential", violation["message"])

    def test_sbom_is_complete_deterministic_and_matches_lock_hashes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            lock_path = root / "dependency_lock.toml"
            first_path = root / "first.cdx.json"
            second_path = root / "second.cdx.json"
            self._write(lock_path, VALID_LOCK)
            first, first_evidence = self._run_json(
                GENERATE_SBOM, "--lock", lock_path, "--output", first_path
            )
            second, second_evidence = self._run_json(
                GENERATE_SBOM, "--lock", lock_path, "--output", second_path
            )
            self.assertEqual(0, first.returncode, first_evidence)
            self.assertEqual(0, second.returncode, second_evidence)
            self.assertEqual(first_path.read_bytes(), second_path.read_bytes())
            sbom = json.loads(first_path.read_text(encoding="utf-8"))
        self.assertEqual("CycloneDX", sbom["bomFormat"])
        self.assertEqual("1.6", sbom["specVersion"])
        self.assertEqual(1, len(sbom["components"]))
        component = sbom["components"][0]
        self.assertEqual("MIT", component["licenses"][0]["license"]["id"])
        self.assertEqual("SHA-256", component["hashes"][0]["alg"])
        self.assertEqual("a" * 64, component["hashes"][0]["content"])
        self.assertEqual("distribution", component["externalReferences"][0]["type"])

    def test_sbom_missing_component_and_hash_mismatch_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            lock_path = root / "dependency_lock.toml"
            sbom_path = root / "fixture.cdx.json"
            self._write(lock_path, VALID_LOCK)
            generated, _ = self._run_json(
                GENERATE_SBOM, "--lock", lock_path, "--output", sbom_path
            )
            self.assertEqual(0, generated.returncode)
            sbom = json.loads(sbom_path.read_text(encoding="utf-8"))
            sbom["components"] = []
            sbom_path.write_text(json.dumps(sbom), encoding="utf-8")
            missing, missing_evidence = self._run_json(
                CHECK_LOCK, "--lock", lock_path, "--sbom", sbom_path
            )
            self.assertNotEqual(0, missing.returncode)
            self.assertIn(
                "SBOM_INCOMPLETE",
                {item["rule_id"] for item in missing_evidence["violations"]},
            )

            self._run_json(GENERATE_SBOM, "--lock", lock_path, "--output", sbom_path)
            sbom = json.loads(sbom_path.read_text(encoding="utf-8"))
            sbom["components"][0]["hashes"][0]["content"] = "b" * 64
            sbom_path.write_text(json.dumps(sbom), encoding="utf-8")
            mismatch, mismatch_evidence = self._run_json(
                CHECK_LOCK, "--lock", lock_path, "--sbom", sbom_path
            )
        self.assertNotEqual(0, mismatch.returncode)
        self.assertIn(
            "SBOM_HASH_MISMATCH",
            {item["rule_id"] for item in mismatch_evidence["violations"]},
        )

    def test_upgrade_adr_schema_accepts_complete_instance(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            adr_path = Path(temp_dir) / "upgrade.md"
            self._write(adr_path, VALID_ADR)
            result, evidence = self._run_json(CHECK_ADR, adr_path)
        self.assertEqual(0, result.returncode, evidence)
        self.assertEqual("pass", evidence["status"])

    def test_godot_digest_helper_exports_installed_binary_digest(self) -> None:
        lock_text = VALID_LOCK.replace(
            'id = "fixture.tool"',
            'id = "godot.editor"\ncommit = "a13da4feb"\nflavor = "standard"',
        ).replace(
            'version = "1.2.3"', 'version = "4.7.1-stable"'
        ).replace(
            "fixture-tool-1.2.3", "fixture-tool-4.7.1"
        ).replace(
            'role = "archive"', 'role = "installed_binary"'
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            lock_path = Path(temp_dir) / "dependency_lock.toml"
            self._write(lock_path, lock_text)
            result = subprocess.run(
                [
                    PYTHON_BIN,
                    str(EXPORT_GODOT_SHA256),
                    "--lock",
                    str(lock_path),
                    "--platform",
                    "linux_x64",
                ],
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(f"export GODOT_SHA256={'a' * 64}\n", result.stdout)

    def test_godot_digest_helper_fails_closed_without_binary_digest(self) -> None:
        lock_text = VALID_LOCK.replace(
            'id = "fixture.tool"',
            'id = "godot.editor"\ncommit = "a13da4feb"\nflavor = "standard"',
        ).replace(
            'version = "1.2.3"', 'version = "4.7.1-stable"'
        ).replace(
            "fixture-tool-1.2.3", "fixture-tool-4.7.1"
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            lock_path = Path(temp_dir) / "dependency_lock.toml"
            self._write(lock_path, lock_text)
            result = subprocess.run(
                [
                    PYTHON_BIN,
                    str(EXPORT_GODOT_SHA256),
                    "--lock",
                    str(lock_path),
                    "--platform",
                    "linux_x64",
                ],
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertNotEqual(0, result.returncode)
        evidence = json.loads(result.stderr)
        self.assertEqual("LOCK_BINARY_DIGEST_MISSING", evidence["rule_id"])

    def test_upgrade_adr_rejects_missing_smoke_branch_and_spike_evidence(self) -> None:
        cases = {
            "smoke": VALID_ADR.replace(
                "## Impacted Platform Smoke Matrix", "## Removed Matrix"
            ),
            "branch": VALID_ADR.replace(
                "compatibility_branch: compat/fixture-tool-1-2-4", ""
            ),
            "spike": VALID_ADR.replace(
                "adr20_spike_evidence: n/a - non-plugin tool", ""
            ),
        }
        for name, adr_text in cases.items():
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temp_dir:
                adr_path = Path(temp_dir) / "upgrade.md"
                self._write(adr_path, adr_text)
                result, evidence = self._run_json(CHECK_ADR, adr_path)
                self.assertNotEqual(0, result.returncode, evidence)
                self.assertIn(
                    "ADR_SCHEMA_INVALID",
                    {item["rule_id"] for item in evidence["violations"]},
                )

    def test_accepted_adr_rejects_undecided_cve_or_license(self) -> None:
        for field in ("cve_decision", "license_decision"):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as temp_dir:
                adr_text = VALID_ADR.replace("status: proposed", "status: accepted")
                current_value = "cleared" if field == "cve_decision" else "approved"
                adr_text = adr_text.replace(
                    f"{field}: {current_value}", f"{field}: undecided"
                )
                adr_path = Path(temp_dir) / "upgrade.md"
                self._write(adr_path, adr_text)
                result, evidence = self._run_json(CHECK_ADR, adr_path)
                self.assertNotEqual(0, result.returncode, evidence)
                self.assertIn(
                    "ADR_SCHEMA_INVALID",
                    {item["rule_id"] for item in evidence["violations"]},
                )

    def test_real_repository_lock_and_sbom_verify(self) -> None:
        result, evidence = self._run_json(
            CHECK_LOCK, "--lock", REAL_LOCK, "--sbom", REAL_SBOM
        )
        self.assertEqual(0, result.returncode, evidence)
        self.assertGreaterEqual(evidence["dependency_count"], 11)
        self.assertEqual(
            evidence["dependency_count"], evidence["sbom_component_count"]
        )


if __name__ == "__main__":
    unittest.main()
