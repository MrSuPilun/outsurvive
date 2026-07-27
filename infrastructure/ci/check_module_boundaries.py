#!/usr/bin/env python3
"""Fail-closed repository module-boundary scanner.

The scanner intentionally implements a bounded lexical model for Godot dependency
constructs. It emits exactly one deterministic JSON document on stdout.
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import re
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any


SCHEMA_VERSION = 1
DEPENDENCY_KINDS = {
    ".gd": "gdscript",
    ".tscn": "resource",
    ".tres": "resource",
}
RUNTIME_MODULES = {
    "shared",
    "client",
    "client_composition",
    "client_presentation",
    "server",
    "platform_port",
    "platform_adapter",
}
TOOLING_MODULES = {
    "game_tools",
    "game_tests",
    "test_harness",
    "content_source",
    "quarantine",
}


@dataclass(frozen=True)
class Module:
    module_id: str
    include: tuple[str, ...]
    exclude: tuple[str, ...]
    allowed_edges: frozenset[str]
    layer: str


class BoundaryFailure(Exception):
    def __init__(
        self,
        rule_id: str,
        message: str,
        *,
        source_file: str = "<policy>",
        line: int = 1,
        from_module: str = "unknown",
        to_module: str | None = None,
        unresolved_target: str | None = None,
        forbidden_edge: str | None = None,
    ) -> None:
        super().__init__(message)
        self.violation = make_violation(
            rule_id,
            source_file,
            line,
            from_module,
            to_module=to_module,
            unresolved_target=unresolved_target or message,
            forbidden_edge=forbidden_edge or rule_id,
        )


def make_violation(
    rule_id: str,
    source_file: str,
    line: int,
    from_module: str,
    *,
    to_module: str | None = None,
    unresolved_target: str | None = None,
    forbidden_edge: str,
) -> dict[str, Any]:
    item: dict[str, Any] = {
        "rule_id": rule_id,
        "source_file": source_file,
        "line": line,
        "from_module": from_module,
    }
    if to_module is not None:
        item["to_module"] = to_module
    else:
        item["unresolved_target"] = unresolved_target or "unknown"
    item["forbidden_edge"] = forbidden_edge
    return item


def path_matches(path: str, pattern: str) -> bool:
    normalized = path.replace("\\", "/").lstrip("./")
    normalized_pattern = pattern.replace("\\", "/").lstrip("./")
    if normalized_pattern.endswith("/**"):
        prefix = normalized_pattern[:-3].rstrip("/")
        return normalized == prefix or normalized.startswith(prefix + "/")
    return fnmatch.fnmatchcase(normalized, normalized_pattern)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def strip_gdscript_comments(line: str) -> str:
    quote = ""
    escaped = False
    output: list[str] = []
    for character in line:
        if escaped:
            output.append(character)
            escaped = False
            continue
        if character == "\\" and quote:
            output.append(character)
            escaped = True
            continue
        if character in {'"', "'"}:
            if quote == character:
                quote = ""
            elif not quote:
                quote = character
            output.append(character)
            continue
        if character == "#" and not quote:
            break
        output.append(character)
    return "".join(output)


def mask_strings(text: str) -> str:
    output: list[str] = []
    quote = ""
    escaped = False
    for character in text:
        if escaped:
            output.append(" ")
            escaped = False
            continue
        if character == "\\" and quote:
            output.append(" ")
            escaped = True
            continue
        if character in {'"', "'"}:
            if quote == character:
                quote = ""
            elif not quote:
                quote = character
            output.append(" ")
            continue
        output.append(" " if quote else character)
    return "".join(output)


class Scanner:
    def __init__(self, repo_root: Path, policy_path: Path, policy_bytes: bytes) -> None:
        self.repo_root = repo_root.resolve()
        self.policy_path = policy_path
        self.policy_sha256 = hashlib.sha256(policy_bytes).hexdigest()
        try:
            data = tomllib.loads(policy_bytes.decode("utf-8"))
        except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
            raise BoundaryFailure("BOUNDARY_POLICY_INVALID", str(error)) from error
        self.policy = self._validate_policy(data)
        self.modules = tuple(
            Module(
                module_id=row["id"],
                include=tuple(row["include"]),
                exclude=tuple(row.get("exclude", [])),
                allowed_edges=frozenset(row["allowed_edges"]),
                layer=row["layer"],
            )
            for row in self.policy["modules"]
        )
        self.module_by_id = {module.module_id: module for module in self.modules}
        self.scan_config = self.policy["scan"]
        self.godot_config = self.policy["godot"]
        self.composition_patterns = tuple(
            row["path"] for row in self.policy.get("composition_roots", [])
        )
        self.providers = tuple(self.policy.get("providers", []))
        self.files: list[str] = []
        self.owners: dict[str, str] = {}
        self.edges: list[dict[str, Any]] = []
        self.violations: list[dict[str, Any]] = []
        self.class_symbols: dict[str, tuple[str, str, int]] = {}
        self.uid_paths: dict[str, str] = {}

    @staticmethod
    def _validate_policy(data: dict[str, Any]) -> dict[str, Any]:
        if data.get("schema_version") != SCHEMA_VERSION:
            raise BoundaryFailure(
                "BOUNDARY_POLICY_INVALID",
                f"schema_version must be {SCHEMA_VERSION}",
            )
        for key in ("scan", "godot", "modules"):
            if key not in data:
                raise BoundaryFailure(
                    "BOUNDARY_POLICY_INVALID", f"missing policy key: {key}"
                )
        modules = data["modules"]
        if not isinstance(modules, list) or not modules:
            raise BoundaryFailure(
                "BOUNDARY_POLICY_INVALID", "modules must be a non-empty array"
            )
        seen: set[str] = set()
        for row in modules:
            required = {"id", "owner", "layer", "include", "allowed_edges"}
            if not isinstance(row, dict) or not required.issubset(row):
                raise BoundaryFailure(
                    "BOUNDARY_POLICY_INVALID", "module row is incomplete"
                )
            module_id = row["id"]
            if module_id in seen:
                raise BoundaryFailure(
                    "BOUNDARY_POLICY_INVALID", f"duplicate module id: {module_id}"
                )
            seen.add(module_id)
            if not row["include"] or not all(
                isinstance(pattern, str) for pattern in row["include"]
            ):
                raise BoundaryFailure(
                    "BOUNDARY_POLICY_INVALID",
                    f"module {module_id} requires include patterns",
                )
        for row in modules:
            unknown_edges = set(row["allowed_edges"]) - seen
            if unknown_edges:
                raise BoundaryFailure(
                    "BOUNDARY_POLICY_INVALID",
                    f"module {row['id']} has unknown edges: {sorted(unknown_edges)}",
                )
        return data

    def scan(self) -> dict[str, Any]:
        self._walk()
        self._index_uid_sidecars()
        self._index_class_names()
        for relative_path in self.files:
            self._scan_file(relative_path)
        self.edges = unique_sorted(
            self.edges, ("source_file", "line", "kind", "target")
        )
        self.violations = unique_sorted(
            self.violations,
            ("source_file", "line", "rule_id", "forbidden_edge"),
        )
        return {
            "schema_version": SCHEMA_VERSION,
            "status": "fail" if self.violations else "pass",
            "policy_sha256": self.policy_sha256,
            "files_scanned": len(self.files),
            "edges": self.edges,
            "violations": self.violations,
        }

    def _walk(self) -> None:
        excluded = tuple(self.scan_config["exclude"])
        governed_roots = tuple(self.scan_config["governed_source_roots"])
        known_suffixes = tuple(
            self.scan_config["dependency_suffixes"]
            + self.scan_config["owner_executable_suffixes"]
            + self.scan_config["owner_metadata_suffixes"]
        )
        for path in sorted(self.repo_root.rglob("*")):
            relative = path.relative_to(self.repo_root).as_posix()
            if any(path_matches(relative, pattern) for pattern in excluded):
                continue
            if path.is_symlink():
                self.violations.append(
                    make_violation(
                        "BOUNDARY_DEPENDENCY_UNRESOLVED",
                        relative,
                        1,
                        "unknown",
                        unresolved_target=relative,
                        forbidden_edge="symlink/path escape",
                    )
                )
                continue
            if not path.is_file():
                continue
            owners = self._matching_modules(relative)
            governed = any(
                relative == root or relative.startswith(root.rstrip("/") + "/")
                for root in governed_roots
            )
            if not owners:
                if governed:
                    self.violations.append(
                        make_violation(
                            "BOUNDARY_UNKNOWN_OWNER",
                            relative,
                            1,
                            "unknown",
                            unresolved_target=relative,
                            forbidden_edge="unknown -> unknown",
                        )
                    )
                continue
            if len(owners) > 1:
                self.violations.append(
                    make_violation(
                        "BOUNDARY_AMBIGUOUS_OWNER",
                        relative,
                        1,
                        "ambiguous",
                        unresolved_target=",".join(sorted(owners)),
                        forbidden_edge="ambiguous ownership",
                    )
                )
                continue
            owner = owners[0]
            if governed and not relative.endswith(known_suffixes):
                self.violations.append(
                    make_violation(
                        "BOUNDARY_SOURCE_TYPE_UNGOVERNED",
                        relative,
                        1,
                        owner,
                        unresolved_target=PurePosixPath(relative).suffix or "<none>",
                        forbidden_edge=f"{owner} -> ungoverned source type",
                    )
                )
            self.owners[relative] = owner
            self.files.append(relative)

    def _matching_modules(self, relative_path: str) -> list[str]:
        matches: list[str] = []
        for module in self.modules:
            included = any(
                path_matches(relative_path, pattern) for pattern in module.include
            )
            excluded = any(
                path_matches(relative_path, pattern) for pattern in module.exclude
            )
            if included and not excluded:
                matches.append(module.module_id)
        return matches

    def _index_uid_sidecars(self) -> None:
        for relative_path in self.files:
            if not relative_path.endswith(".uid"):
                continue
            owner = self.owners[relative_path]
            if owner == "quarantine":
                continue
            text = (self.repo_root / relative_path).read_text(
                encoding="utf-8", errors="replace"
            )
            match = re.search(r"uid://[A-Za-z0-9_]+", text)
            sibling = relative_path.removesuffix(".uid")
            if match and sibling in self.owners:
                uid = match.group(0)
                if uid in self.uid_paths and self.uid_paths[uid] != sibling:
                    self.violations.append(
                        make_violation(
                            "BOUNDARY_POLICY_INVALID",
                            relative_path,
                            1,
                            owner,
                            unresolved_target=uid,
                            forbidden_edge="duplicate UID",
                        )
                    )
                self.uid_paths[uid] = sibling

    def _index_class_names(self) -> None:
        pattern = re.compile(r"(?m)^[ \t]*class_name[ \t]+([A-Za-z_]\w*)")
        for relative_path in self.files:
            if not relative_path.endswith(".gd"):
                continue
            text = (self.repo_root / relative_path).read_text(encoding="utf-8")
            clean = "\n".join(strip_gdscript_comments(line) for line in text.splitlines())
            match = pattern.search(clean)
            if not match:
                continue
            symbol = match.group(1)
            if symbol in self.class_symbols:
                self.violations.append(
                    make_violation(
                        "BOUNDARY_POLICY_INVALID",
                        relative_path,
                        line_number(clean, match.start()),
                        self.owners[relative_path],
                        unresolved_target=symbol,
                        forbidden_edge="duplicate class_name",
                    )
                )
                continue
            self.class_symbols[symbol] = (
                relative_path,
                self.owners[relative_path],
                line_number(clean, match.start()),
            )

    def _scan_file(self, relative_path: str) -> None:
        owner = self.owners[relative_path]
        if owner == "quarantine":
            return
        if relative_path.endswith(".gd"):
            self._scan_gdscript(relative_path, owner)
        elif relative_path.endswith((".tscn", ".tres")):
            self._scan_resource(relative_path, owner)
        elif relative_path == self.godot_config["project_file"]:
            self._scan_project_config(relative_path, owner)

    def _scan_gdscript(self, relative_path: str, owner: str) -> None:
        text = (self.repo_root / relative_path).read_text(encoding="utf-8")
        clean_lines = [strip_gdscript_comments(line) for line in text.splitlines()]
        clean = "\n".join(clean_lines)
        masked = mask_strings(clean)

        assignments: dict[str, str] = {}
        assignment_pattern = re.compile(
            r"(?m)^[ \t]*(?:const|var)[ \t]+([A-Za-z_]\w*)"
            r"(?:[ \t]*:[^=\n]+)?[ \t]*=[ \t]*([\"'])([^\"']+)\2"
        )
        for match in assignment_pattern.finditer(clean):
            assignments[match.group(1)] = match.group(3)

        consumed_calls: set[tuple[int, int]] = set()
        literal_call = re.compile(
            r"\b(preload|load)[ \t]*\([ \t]*([\"'])([^\"']+)\2[ \t]*\)"
        )
        for match in literal_call.finditer(clean):
            consumed_calls.add((match.start(), match.end()))
            self._add_path_dependency(
                relative_path,
                owner,
                line_number(clean, match.start()),
                match.group(3),
                match.group(1),
            )

        quoted_extends = re.compile(
            r"(?m)^[ \t]*extends[ \t]+([\"'])([^\"']+)\1"
        )
        for match in quoted_extends.finditer(clean):
            self._add_path_dependency(
                relative_path,
                owner,
                line_number(clean, match.start()),
                match.group(2),
                "extends",
            )

        any_call = re.compile(r"\b(preload|load)[ \t]*\([ \t]*([^)\n]+)[ \t]*\)")
        for match in any_call.finditer(clean):
            if any(
                match.start() >= start and match.end() <= end
                for start, end in consumed_calls
            ):
                continue
            argument = match.group(2).strip()
            if argument in assignments:
                self._add_path_dependency(
                    relative_path,
                    owner,
                    line_number(clean, match.start()),
                    assignments[argument],
                    match.group(1),
                )
            else:
                rule_id = (
                    "BOUNDARY_DYNAMIC_RESOURCE_PATH"
                    if re.fullmatch(r"[A-Za-z_]\w*", argument)
                    else "BOUNDARY_PARSE_UNSUPPORTED"
                )
                self.violations.append(
                    make_violation(
                        rule_id,
                        relative_path,
                        line_number(clean, match.start()),
                        owner,
                        unresolved_target=argument,
                        forbidden_edge=(
                            f"{owner} -> dynamic resource path"
                            if rule_id == "BOUNDARY_DYNAMIC_RESOURCE_PATH"
                            else f"{owner} -> unsupported dependency syntax"
                        ),
                    )
                )

        declaration = re.search(
            r"(?m)^[ \t]*class_name[ \t]+([A-Za-z_]\w*)", masked
        )
        own_symbol = declaration.group(1) if declaration else None
        for symbol, (target_path, _, _) in sorted(self.class_symbols.items()):
            if symbol == own_symbol:
                continue
            for match in re.finditer(rf"\b{re.escape(symbol)}\b", masked):
                self._add_edge(
                    relative_path,
                    owner,
                    line_number(masked, match.start()),
                    target_path,
                    "class_name",
                    symbol,
                )

        if owner == "shared":
            allowed_symbols = set(self.godot_config["allowed_shared_symbols"])
            referenced_types: dict[str, int] = {}
            type_patterns = (
                r"(?m)\bextends[ \t]+([A-Z]\w*)",
                r":[ \t]*([A-Z]\w*)",
                r"->[ \t]*([A-Z]\w*)",
                r"\b([A-Z]\w*)[ \t]*\.",
            )
            for type_pattern in type_patterns:
                for match in re.finditer(type_pattern, masked):
                    referenced_types.setdefault(
                        match.group(1), line_number(masked, match.start(1))
                    )
            for symbol, symbol_line in sorted(referenced_types.items()):
                if (
                    symbol == own_symbol
                    or symbol in allowed_symbols
                    or symbol in self.class_symbols
                    or symbol.isupper()
                ):
                    continue
                self.violations.append(
                    make_violation(
                        "BOUNDARY_DEPENDENCY_UNRESOLVED",
                        relative_path,
                        symbol_line,
                        owner,
                        unresolved_target=symbol,
                        forbidden_edge=f"shared -> unapproved Godot symbol:{symbol}",
                    )
                )
            for symbol in self.godot_config["presentation_symbols"]:
                match = re.search(rf"\b{re.escape(symbol)}\b", masked)
                if match:
                    self.violations.append(
                        make_violation(
                            "BOUNDARY_FORBIDDEN_EDGE",
                            relative_path,
                            line_number(masked, match.start()),
                            owner,
                            to_module="godot_presentation",
                            forbidden_edge="shared -> godot_presentation",
                        )
                    )

        for provider in self.providers:
            for symbol in provider.get("symbols", []):
                match = re.search(rf"\b{re.escape(symbol)}\b", masked)
                if match and owner not in {"platform_adapter", "native"}:
                    self.violations.append(
                        make_violation(
                            "BOUNDARY_PLATFORM_PROVIDER_OUTSIDE_ADAPTER",
                            relative_path,
                            line_number(masked, match.start()),
                            owner,
                            to_module="native",
                            forbidden_edge=f"{owner} -> provider:{provider['id']}",
                        )
                    )
            for provider_pattern in provider.get("path_patterns", []):
                for match in re.finditer(r"([\"'])([^\"']+)\1", clean):
                    if path_matches(match.group(2), provider_pattern) and owner not in {
                        "platform_adapter",
                        "native",
                    }:
                        self.violations.append(
                            make_violation(
                                "BOUNDARY_PLATFORM_PROVIDER_OUTSIDE_ADAPTER",
                                relative_path,
                                line_number(clean, match.start()),
                                owner,
                                to_module="native",
                                forbidden_edge=(
                                    f"{owner} -> provider:{provider['id']}"
                                ),
                            )
                        )

        if owner == "platform_port":
            self._validate_port(relative_path, clean)
        if owner == "platform_adapter":
            self._validate_adapter(relative_path, masked)

    def _validate_port(self, relative_path: str, clean: str) -> None:
        owner = "platform_port"
        class_match = re.search(r"(?m)^[ \t]*class_name[ \t]+(\w+)", clean)
        extends_match = re.search(r"(?m)^[ \t]*extends[ \t]+(\w+)", clean)
        if (
            not class_match
            or not class_match.group(1).endswith("Port")
            or not extends_match
            or extends_match.group(1) != "RefCounted"
        ):
            self.violations.append(
                make_violation(
                    "BOUNDARY_POLICY_INVALID",
                    relative_path,
                    1,
                    owner,
                    unresolved_target="port declaration",
                    forbidden_edge="invalid typed port declaration",
                )
            )
        function_pattern = re.compile(
            r"(?m)^[ \t]*func[ \t]+([A-Za-z_]\w*)[ \t]*\(([^)]*)\)"
            r"[ \t]*(?:->[ \t]*([A-Za-z_]\w*(?:\[[^\]]+\])?))?"
        )
        for match in function_pattern.finditer(clean):
            if match.group(1).startswith("_"):
                continue
            parameters = match.group(2).strip()
            typed_parameters = not parameters or all(
                ":" in parameter for parameter in parameters.split(",")
            )
            if not typed_parameters or not match.group(3):
                self.violations.append(
                    make_violation(
                        "BOUNDARY_PORT_UNTYPED",
                        relative_path,
                        line_number(clean, match.start()),
                        owner,
                        unresolved_target=match.group(1),
                        forbidden_edge="platform_port -> untyped public API",
                    )
                )

    def _validate_adapter(self, relative_path: str, masked: str) -> None:
        class_match = re.search(r"(?m)^[ \t]*class_name[ \t]+(\w+)", masked)
        references_port = any(
            re.search(rf"\b{re.escape(symbol)}\b", masked)
            for symbol, (_, module_id, _) in self.class_symbols.items()
            if module_id == "platform_port"
        )
        if (
            not class_match
            or not class_match.group(1).endswith("Adapter")
            or not references_port
        ):
            self.violations.append(
                make_violation(
                    "BOUNDARY_POLICY_INVALID",
                    relative_path,
                    1,
                    "platform_adapter",
                    unresolved_target="adapter declaration",
                    forbidden_edge="adapter must reference a declared Port",
                )
            )

    def _scan_resource(self, relative_path: str, owner: str) -> None:
        text = (self.repo_root / relative_path).read_text(encoding="utf-8")
        for match in re.finditer(
            r"\bpath[ \t]*=[ \t]*([\"'])([^\"']+)\1", text
        ):
            self._add_path_dependency(
                relative_path,
                owner,
                line_number(text, match.start()),
                match.group(2),
                "ext_resource",
            )
        for match in re.finditer(r"([\"'])(uid://[^\"']+)\1", text):
            target = match.group(2)
            if "::" in target:
                target = target.split("::", 1)[1]
            self._add_path_dependency(
                relative_path,
                owner,
                line_number(text, match.start()),
                target,
                "ext_resource_uid",
            )

    def _scan_project_config(self, relative_path: str, owner: str) -> None:
        text = (self.repo_root / relative_path).read_text(encoding="utf-8")
        in_autoload = False
        for index, raw_line in enumerate(text.splitlines(), start=1):
            line = raw_line.strip()
            if line.startswith("[") and line.endswith("]"):
                in_autoload = line == "[autoload]"
                continue
            if not in_autoload:
                continue
            match = re.search(r"([\"'])(\*?(?:res|uid)://[^\"']+)\1", line)
            if match:
                self._add_path_dependency(
                    relative_path,
                    owner,
                    index,
                    match.group(2).removeprefix("*"),
                    "autoload",
                )

    def _add_path_dependency(
        self,
        source_file: str,
        from_module: str,
        line: int,
        target: str,
        kind: str,
    ) -> None:
        target_path = self._resolve_target(target)
        if target_path is None:
            self.violations.append(
                make_violation(
                    "BOUNDARY_DEPENDENCY_UNRESOLVED",
                    source_file,
                    line,
                    from_module,
                    unresolved_target=target,
                    forbidden_edge=f"{from_module} -> unresolved:{target}",
                )
            )
            return
        self._add_edge(
            source_file, from_module, line, target_path, kind, target
        )

    def _resolve_target(self, target: str) -> str | None:
        normalized = target.removeprefix("*")
        if "::" in normalized:
            uid, fallback = normalized.split("::", 1)
            normalized = self.uid_paths.get(uid, fallback)
        elif normalized.startswith("uid://"):
            return self.uid_paths.get(normalized)
        if normalized.startswith("res://"):
            relative = "game/" + normalized.removeprefix("res://")
        else:
            return None
        pure = PurePosixPath(relative)
        if ".." in pure.parts or pure.is_absolute():
            return None
        canonical = pure.as_posix()
        absolute = (self.repo_root / canonical).resolve()
        try:
            absolute.relative_to(self.repo_root)
        except ValueError:
            return None
        if canonical not in self.owners:
            return None
        return canonical

    def _add_edge(
        self,
        source_file: str,
        from_module: str,
        line: int,
        target_path: str,
        kind: str,
        target: str,
    ) -> None:
        to_module = self.owners.get(target_path)
        if not to_module:
            self.violations.append(
                make_violation(
                    "BOUNDARY_DEPENDENCY_UNRESOLVED",
                    source_file,
                    line,
                    from_module,
                    unresolved_target=target,
                    forbidden_edge=f"{from_module} -> unresolved:{target}",
                )
            )
            return
        edge = {
            "source_file": source_file,
            "line": line,
            "from_module": from_module,
            "to_module": to_module,
            "kind": kind,
            "target": target,
        }
        self.edges.append(edge)
        allowed = to_module in self.module_by_id[from_module].allowed_edges
        if allowed:
            return
        rule_id = (
            "BOUNDARY_RUNTIME_DEPENDS_ON_TOOLING"
            if from_module in RUNTIME_MODULES and to_module in TOOLING_MODULES
            else "BOUNDARY_FORBIDDEN_EDGE"
        )
        self.violations.append(
            make_violation(
                rule_id,
                source_file,
                line,
                from_module,
                to_module=to_module,
                forbidden_edge=f"{from_module} -> {to_module}",
            )
        )


def unique_sorted(
    items: list[dict[str, Any]], keys: tuple[str, ...]
) -> list[dict[str, Any]]:
    unique: dict[str, dict[str, Any]] = {}
    for item in items:
        encoded = json.dumps(item, sort_keys=True, separators=(",", ":"))
        unique[encoded] = item
    return sorted(
        unique.values(),
        key=lambda item: tuple(item.get(key, "") for key in keys),
    )


def failure_document(
    policy_sha256: str, violation: dict[str, Any]
) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "fail",
        "policy_sha256": policy_sha256,
        "files_scanned": 0,
        "edges": [],
        "violations": [violation],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--policy", type=Path, required=True)
    arguments = parser.parse_args()

    policy_bytes = b""
    try:
        policy_bytes = arguments.policy.read_bytes()
        scanner = Scanner(arguments.repo_root, arguments.policy, policy_bytes)
        evidence = scanner.scan()
    except (OSError, BoundaryFailure) as error:
        policy_sha256 = hashlib.sha256(policy_bytes).hexdigest()
        if isinstance(error, BoundaryFailure):
            violation = error.violation
        else:
            violation = make_violation(
                "BOUNDARY_POLICY_INVALID",
                "<policy>",
                1,
                "unknown",
                unresolved_target=str(error),
                forbidden_edge="policy unavailable",
            )
        evidence = failure_document(policy_sha256, violation)
    print(json.dumps(evidence, sort_keys=False, separators=(",", ":")))
    return 0 if evidence["status"] == "pass" else 2


if __name__ == "__main__":
    sys.exit(main())
