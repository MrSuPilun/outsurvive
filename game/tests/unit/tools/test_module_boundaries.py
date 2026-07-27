from __future__ import annotations

import json
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
SCANNER = REPO_ROOT / "infrastructure/ci/check_module_boundaries.py"
REAL_POLICY = REPO_ROOT / "infrastructure/ci/module_boundaries.toml"


POLICY = """
schema_version = 1

[scan]
exclude = [".git/**", ".godot/**"]
dependency_suffixes = [".gd", ".tscn", ".tres"]
owner_executable_suffixes = [".py", ".sh"]
owner_metadata_suffixes = [".gd.uid", ".toml", ".yml", ".yaml", ".json", ".md"]
governed_source_roots = ["game/src", "game/scenes", "game/tools", "game/tests", "backend", "native"]

[godot]
project_file = "game/project.godot"
allowed_shared_symbols = ["Node", "RefCounted", "String", "bool", "int", "void"]
presentation_symbols = ["Control", "RenderingServer", "AudioStreamPlayer"]

[[modules]]
id = "shared"
owner = "Shared"
layer = "domain"
include = ["game/src/shared/**"]
exclude = []
allowed_edges = ["shared"]

[[modules]]
id = "client_composition"
owner = "Client"
layer = "composition-root"
include = ["game/src/client/bootstrap/**"]
exclude = []
allowed_edges = ["shared", "platform_port", "platform_adapter"]

[[modules]]
id = "client_presentation"
owner = "Presentation"
layer = "presentation"
include = ["game/src/client/ui/**", "game/scenes/**"]
exclude = []
allowed_edges = ["shared"]

[[modules]]
id = "client"
owner = "Client"
layer = "application"
include = ["game/src/client/**"]
exclude = ["game/src/client/bootstrap/**", "game/src/client/ui/**"]
allowed_edges = ["shared", "client", "client_presentation", "platform_port"]

[[modules]]
id = "server"
owner = "Server"
layer = "authority"
include = ["game/src/server/**"]
exclude = []
allowed_edges = ["shared", "server", "platform_port"]

[[modules]]
id = "platform_port"
owner = "Platform"
layer = "port"
include = ["game/src/platform/ports/**"]
exclude = []
allowed_edges = ["shared", "platform_port"]

[[modules]]
id = "platform_adapter"
owner = "Platform"
layer = "adapter"
include = ["game/src/platform/adapters/**"]
exclude = []
allowed_edges = ["shared", "platform_port", "platform_adapter", "native"]

[[modules]]
id = "game_config"
owner = "Game"
layer = "config"
include = ["game/project.godot"]
exclude = []
allowed_edges = ["shared", "client_composition"]

[[modules]]
id = "game_tools"
owner = "Tools"
layer = "tooling"
include = ["game/tools/**"]
exclude = []
allowed_edges = ["shared", "game_tools"]

[[modules]]
id = "game_tests"
owner = "Tests"
layer = "testing"
include = ["game/tests/**"]
exclude = []
allowed_edges = ["shared", "client", "client_composition", "client_presentation", "server", "platform_port", "platform_adapter", "game_tests"]

[[modules]]
id = "backend"
owner = "Backend"
layer = "service"
include = ["backend/**"]
exclude = []
allowed_edges = ["backend"]

[[modules]]
id = "native"
owner = "Native"
layer = "bridge"
include = ["native/**"]
exclude = []
allowed_edges = ["shared", "platform_port", "native"]

[[modules]]
id = "content_source"
owner = "Content"
layer = "raw"
include = ["content-source/**"]
exclude = []
allowed_edges = ["content_source"]

[[modules]]
id = "quarantine"
owner = "Assets"
layer = "quarantine"
include = ["prepare-asset/**"]
exclude = []
allowed_edges = ["quarantine"]

[[modules]]
id = "test_harness"
owner = "Tests"
layer = "harness"
include = ["test-harness/**"]
exclude = []
allowed_edges = ["shared", "test_harness"]

[[composition_roots]]
path = "game/src/client/bootstrap/**"

[[providers]]
id = "fixture_sdk"
symbols = ["FixtureSdk"]
path_patterns = ["res://fixture_sdk/**"]
provider_path = "native/fixture_sdk/**"
adapter_module = "platform_adapter"
port_module = "platform_port"
"""


class ModuleBoundaryTests(unittest.TestCase):
    def _scan(
        self,
        files: dict[str, str],
        *,
        policy: str = POLICY,
    ) -> tuple[subprocess.CompletedProcess[str], dict[str, object]]:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for relative_path, content in files.items():
                path = root / relative_path
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")
            policy_path = root / "fixture_policy.toml"
            policy_path.write_text(textwrap.dedent(policy), encoding="utf-8")
            result = subprocess.run(
                [
                    "python3",
                    str(SCANNER),
                    "--repo-root",
                    str(root),
                    "--policy",
                    str(policy_path),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertTrue(result.stdout, result.stderr)
            return result, json.loads(result.stdout)

    def _assert_violation(
        self,
        files: dict[str, str],
        rule_id: str,
        *,
        source_file: str | None = None,
        policy: str = POLICY,
    ) -> dict[str, object]:
        result, evidence = self._scan(files, policy=policy)
        self.assertNotEqual(0, result.returncode, evidence)
        self.assertEqual("fail", evidence["status"])
        matching = [
            item
            for item in evidence["violations"]
            if item["rule_id"] == rule_id
            and (source_file is None or item["source_file"] == source_file)
        ]
        self.assertTrue(matching, evidence)
        item = matching[0]
        self.assertIn("line", item)
        self.assertIn("from_module", item)
        self.assertIn("forbidden_edge", item)
        return item

    def test_positive_client_shared_adapter_port_and_composition_injection(self) -> None:
        result, evidence = self._scan(
            {
                "game/src/shared/contracts/account.gd": """
                    class_name AccountContract
                    extends RefCounted
                """,
                "game/src/platform/ports/account_port.gd": """
                    class_name AccountPort
                    extends RefCounted
                    func account_id(slot: int) -> String:
                        return ""
                """,
                "game/src/platform/adapters/fixture_account_adapter.gd": """
                    class_name FixtureAccountAdapter
                    extends AccountPort
                    var _contract: AccountContract
                """,
                "game/src/client/bootstrap/composition_root.gd": """
                    extends Node
                    var _port: AccountPort
                    func _init() -> void:
                        _port = FixtureAccountAdapter.new()
                """,
                "game/src/client/domain/account_consumer.gd": """
                    extends RefCounted
                    var _port: AccountPort
                    var _contract: AccountContract
                """,
            }
        )
        self.assertEqual(0, result.returncode, evidence)
        self.assertEqual("pass", evidence["status"])
        self.assertGreaterEqual(len(evidence["edges"]), 5)

    def test_explicit_path_and_local_literal_load_are_resolved(self) -> None:
        result, evidence = self._scan(
            {
                "game/src/shared/value.gd": "class_name SharedValue\nextends RefCounted\n",
                "game/src/client/domain/consumer.gd": """
                    extends RefCounted
                    const VALUE = preload("res://src/shared/value.gd")
                    func open() -> void:
                        var scene_path: String = "res://scenes/menu.tscn"
                        load(scene_path)
                """,
                "game/scenes/menu.tscn": '[gd_scene format=3]\n',
            }
        )
        self.assertEqual(0, result.returncode, evidence)

    def test_comments_and_unrelated_strings_do_not_create_edges(self) -> None:
        result, evidence = self._scan(
            {
                "game/src/shared/value.gd": """
                    extends RefCounted
                    # ClientThing and load("res://src/client/bad.gd")
                    var label: String = "ClientThing res://src/client/bad.gd"
                """,
            }
        )
        self.assertEqual(0, result.returncode, evidence)
        self.assertEqual([], evidence["edges"])

    def test_shared_forbidden_edges_by_path_and_implicit_symbol(self) -> None:
        path_item = self._assert_violation(
            {
                "game/src/shared/bad.gd": 'extends "res://src/client/domain/client_thing.gd"\n',
                "game/src/client/domain/client_thing.gd": "class_name ClientThing\nextends RefCounted\n",
            },
            "BOUNDARY_FORBIDDEN_EDGE",
            source_file="game/src/shared/bad.gd",
        )
        self.assertEqual("shared -> client", path_item["forbidden_edge"])

        symbol_item = self._assert_violation(
            {
                "game/src/shared/bad.gd": "extends RefCounted\nvar thing: ClientThing\n",
                "game/src/client/domain/client_thing.gd": "class_name ClientThing\nextends RefCounted\n",
            },
            "BOUNDARY_FORBIDDEN_EDGE",
            source_file="game/src/shared/bad.gd",
        )
        self.assertEqual("client", symbol_item["to_module"])

    def test_shared_rejects_server_presentation_platform_and_backend(self) -> None:
        targets = {
            "server": "game/src/server/authority.gd",
            "client_presentation": "game/src/client/ui/hud.gd",
            "platform_port": "game/src/platform/ports/account_port.gd",
            "platform_adapter": "game/src/platform/adapters/account_adapter.gd",
            "backend": "backend/service.md",
        }
        for module_id, target in targets.items():
            with self.subTest(module_id=module_id):
                item = self._assert_violation(
                    {
                        "game/src/shared/bad.gd": f'extends "res://../{target}"\n'
                        if module_id == "backend"
                        else f'extends "res://{target.removeprefix("game/")}"\n',
                        target: "extends RefCounted\n" if target.endswith(".gd") else "# service\n",
                    },
                    "BOUNDARY_FORBIDDEN_EDGE"
                    if module_id != "backend"
                    else "BOUNDARY_DEPENDENCY_UNRESOLVED",
                )
                self.assertTrue(item["forbidden_edge"])

    def test_shared_rejects_presentation_api(self) -> None:
        item = self._assert_violation(
            {"game/src/shared/bad.gd": "extends RefCounted\nvar panel: Control\n"},
            "BOUNDARY_FORBIDDEN_EDGE",
        )
        self.assertEqual("shared -> godot_presentation", item["forbidden_edge"])

    def test_domain_server_and_runtime_tooling_edges_are_rejected(self) -> None:
        self._assert_violation(
            {
                "game/src/client/domain/bad.gd": 'extends "res://src/server/authority.gd"\n',
                "game/src/server/authority.gd": "extends RefCounted\n",
            },
            "BOUNDARY_FORBIDDEN_EDGE",
        )
        self._assert_violation(
            {
                "game/src/server/bad.gd": 'extends "res://scenes/hud.tscn"\n',
                "game/scenes/hud.tscn": "[gd_scene format=3]\n",
            },
            "BOUNDARY_FORBIDDEN_EDGE",
        )
        self._assert_violation(
            {
                "game/src/client/domain/bad.gd": 'const TOOL = preload("res://tools/tool.gd")\n',
                "game/tools/tool.gd": "extends RefCounted\n",
            },
            "BOUNDARY_RUNTIME_DEPENDS_ON_TOOLING",
        )

    def test_provider_outside_adapter_is_rejected(self) -> None:
        self._assert_violation(
            {"game/src/client/domain/bad.gd": "extends RefCounted\nvar sdk = FixtureSdk\n"},
            "BOUNDARY_PLATFORM_PROVIDER_OUTSIDE_ADAPTER",
        )

    def test_port_and_adapter_contracts_are_enforced(self) -> None:
        self._assert_violation(
            {
                "game/src/platform/ports/bad_port.gd": """
                    class_name BadPort
                    extends RefCounted
                    func account_id(slot):
                        return ""
                """,
            },
            "BOUNDARY_PORT_UNTYPED",
        )
        self._assert_violation(
            {
                "game/src/platform/adapters/bad.gd": """
                    class_name BadImplementation
                    extends RefCounted
                """,
            },
            "BOUNDARY_POLICY_INVALID",
        )

    def test_concrete_adapter_bypass_is_rejected(self) -> None:
        self._assert_violation(
            {
                "game/src/platform/ports/account_port.gd": """
                    class_name AccountPort
                    extends RefCounted
                    func id() -> String:
                        return ""
                """,
                "game/src/platform/adapters/account_adapter.gd": """
                    class_name AccountAdapter
                    extends AccountPort
                """,
                "game/src/client/domain/bad.gd": "extends RefCounted\nvar adapter: AccountAdapter\n",
            },
            "BOUNDARY_FORBIDDEN_EDGE",
        )

    def test_scene_resource_autoload_and_uid_edges_are_scanned(self) -> None:
        for source_path, source_text in {
            "game/scenes/hud.tscn": (
                '[gd_scene load_steps=2 format=3]\n'
                '[ext_resource type="Script" path="res://src/shared/value.gd" id="1"]\n'
            ),
            "game/project.godot": (
                '[autoload]\nValue="*res://src/shared/value.gd"\n'
            ),
            "game/src/client/domain/uid_consumer.gd": (
                'const VALUE = preload("uid://fixturevalue")\n'
            ),
        }.items():
            with self.subTest(source_path=source_path):
                files = {
                    source_path: source_text,
                    "game/src/shared/value.gd": "class_name SharedValue\nextends RefCounted\n",
                }
                if "uid://" in source_text:
                    files["game/src/shared/value.gd.uid"] = "uid://fixturevalue\n"
                result, evidence = self._scan(files)
                self.assertEqual(0, result.returncode, evidence)
                self.assertEqual(1, len(evidence["edges"]))

    def test_unknown_uid_dynamic_load_and_path_escape_fail_closed(self) -> None:
        self._assert_violation(
            {"game/src/client/domain/bad.gd": 'const VALUE = preload("uid://missing")\n'},
            "BOUNDARY_DEPENDENCY_UNRESOLVED",
        )
        self._assert_violation(
            {
                "game/src/client/domain/bad.gd": """
                    extends RefCounted
                    func open(scene_path: String) -> void:
                        load(scene_path)
                """
            },
            "BOUNDARY_DYNAMIC_RESOURCE_PATH",
        )
        self._assert_violation(
            {"game/src/client/domain/bad.gd": 'const BAD = preload("res://../../escape.gd")\n'},
            "BOUNDARY_DEPENDENCY_UNRESOLVED",
        )

    def test_shared_builtin_allowlist_and_unsupported_syntax_fail_closed(self) -> None:
        self._assert_violation(
            {"game/src/shared/bad.gd": "extends RefCounted\nvar socket: PacketPeerUDP\n"},
            "BOUNDARY_DEPENDENCY_UNRESOLVED",
        )
        self._assert_violation(
            {
                "game/src/client/domain/bad.gd": """
                    extends RefCounted
                    const PREFIX: String = "res://src/shared/"
                    const BAD = preload(PREFIX + "value.gd")
                """
            },
            "BOUNDARY_PARSE_UNSUPPORTED",
        )

    def test_unknown_ambiguous_owner_unknown_source_and_symlink_fail_closed(self) -> None:
        self._assert_violation(
            {"game/src/unknown/file.gd": "extends RefCounted\n"},
            "BOUNDARY_UNKNOWN_OWNER",
        )
        ambiguous = POLICY.replace(
            "[[composition_roots]]",
            '[[modules]]\nid = "overlap"\nowner = "Overlap"\nlayer = "bad"\ninclude = ["game/src/shared/**"]\nexclude = []\nallowed_edges = ["overlap"]\n\n[[composition_roots]]',
        )
        self._assert_violation(
            {"game/src/shared/file.gd": "extends RefCounted\n"},
            "BOUNDARY_AMBIGUOUS_OWNER",
            policy=ambiguous,
        )
        self._assert_violation(
            {"game/src/shared/file.cpp": "int main() { return 0; }\n"},
            "BOUNDARY_SOURCE_TYPE_UNGOVERNED",
        )

    def test_malformed_policy_fails_with_structured_json(self) -> None:
        self._assert_violation(
            {},
            "BOUNDARY_POLICY_INVALID",
            policy="schema_version = [\n",
        )

    def test_output_is_deterministic(self) -> None:
        files = {
            "game/src/shared/b.gd": "class_name BValue\nextends RefCounted\n",
            "game/src/shared/a.gd": "class_name AValue\nextends RefCounted\nvar value: BValue\n",
        }
        first_result, first = self._scan(files)
        second_result, second = self._scan(files)
        self.assertEqual(0, first_result.returncode)
        self.assertEqual(0, second_result.returncode)
        self.assertEqual(first, second)

    def test_real_repository_scan_passes_and_bootstrap_edges_are_present(self) -> None:
        result = subprocess.run(
            [
                "python3",
                str(SCANNER),
                "--repo-root",
                str(REPO_ROOT),
                "--policy",
                str(REAL_POLICY),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        evidence = json.loads(result.stdout)
        self.assertEqual(0, result.returncode, evidence)
        bootstrap_edges = [
            edge
            for edge in evidence["edges"]
            if edge["from_module"] == "client_composition"
            and edge["to_module"] == "shared"
        ]
        self.assertTrue(bootstrap_edges, evidence)

    def test_narrow_entrypoint_and_workflow_contract(self) -> None:
        entrypoint = REPO_ROOT / "infrastructure/ci/verify_module_boundaries.sh"
        workflow = REPO_ROOT / ".github/workflows/module_boundaries.yml"
        self.assertTrue(entrypoint.is_file())
        self.assertTrue(workflow.is_file())
        entrypoint_text = entrypoint.read_text(encoding="utf-8")
        workflow_text = workflow.read_text(encoding="utf-8")
        self.assertIn("test_module_boundaries.py", entrypoint_text)
        self.assertIn("check_module_boundaries.py", entrypoint_text)
        self.assertIn("name: module-boundaries", workflow_text)
        self.assertIn("module_boundaries:", workflow_text)
        self.assertIn("name: module_boundaries", workflow_text)
        self.assertIn("python-version: '3.12'", workflow_text)
        self.assertNotIn("continue-on-error", workflow_text)
        self.assertNotIn("godot", workflow_text.lower())


if __name__ == "__main__":
    unittest.main()
