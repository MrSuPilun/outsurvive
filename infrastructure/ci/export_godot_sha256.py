#!/usr/bin/env python3
"""Export the trusted installed Godot binary digest from the dependency lock."""

from __future__ import annotations

import argparse
import json
import platform
import sys
from pathlib import Path

from check_dependency_lock import parse_lock, validate_lock


def detect_platform() -> str | None:
    system = platform.system().lower()
    machine = platform.machine().lower()
    if system == "darwin" and machine in {"arm64", "aarch64", "x86_64", "amd64"}:
        return "macos_universal"
    if system == "linux" and machine in {"x86_64", "amd64"}:
        return "linux_x64"
    if system == "windows" and machine in {"x86_64", "amd64"}:
        return "windows_x64"
    return None


def emit_error(rule_id: str, message: str, path: str) -> None:
    json.dump(
        {"status": "failure", "rule_id": rule_id, "path": path, "message": message},
        sys.stderr,
        sort_keys=True,
    )
    sys.stderr.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lock", type=Path, required=True)
    parser.add_argument("--platform")
    parser.add_argument("--allow-observed-only", action="store_true")
    arguments = parser.parse_args()
    data, violations = parse_lock(arguments.lock)
    dependencies: list[dict[str, object]] = []
    if not violations:
        violations, dependencies = validate_lock(data, arguments.lock)
    if violations:
        emit_error(
            "LOCK_INVALID",
            "dependency lock must validate before exporting a trusted digest",
            str(arguments.lock),
        )
        return 1

    raw_platform = arguments.platform or detect_platform()
    if raw_platform is None:
        emit_error(
            "LOCK_HOST_UNSUPPORTED",
            "host platform cannot be mapped to a locked Godot binary",
            "host_platform",
        )
        return 1
    host_platform = {
        "darwin": "macos_universal",
        "linux": "linux_x64",
        "win32": "windows_x64",
        "windows": "windows_x64",
    }.get(raw_platform.lower(), raw_platform)
    editor = next(
        (
            dependency
            for dependency in dependencies
            if dependency.get("id") == "godot.editor"
        ),
        None,
    )
    artifacts = editor.get("artifacts", []) if editor else []
    installed_binary = next(
        (
            artifact
            for artifact in artifacts
            if artifact.get("role") == "installed_binary"
            and artifact.get("platform") == host_platform
            and artifact.get("checksum_algorithm", "").lower() == "sha256"
        ),
        None,
    )
    if installed_binary is None:
        if arguments.allow_observed_only:
            sys.stdout.write("export GODOT_SHA256=''\n")
            json.dump(
                {
                    "status": "observed_only",
                    "rule_id": "LOCK_BINARY_DIGEST_MISSING",
                    "path": f"godot.editor.artifacts.{host_platform}",
                    "message": "no installed binary SHA-256 is pinned for this host",
                },
                sys.stderr,
                sort_keys=True,
            )
            sys.stderr.write("\n")
            return 0
        emit_error(
            "LOCK_BINARY_DIGEST_MISSING",
            "no installed binary SHA-256 is pinned for this host",
            f"godot.editor.artifacts.{host_platform}",
        )
        return 1
    checksum = installed_binary.get("checksum_hex")
    if not checksum or not isinstance(checksum, str):
        emit_error(
            "LOCK_BINARY_DIGEST_INVALID",
            "installed binary SHA-256 digest is missing or invalid",
            f"godot.editor.artifacts.{host_platform}",
        )
        return 1
    sys.stdout.write(f"export GODOT_SHA256={checksum.lower()}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
