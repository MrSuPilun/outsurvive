#!/bin/sh

set -u

GAME_ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/../../.." && pwd)
PROJECT_FILE="$GAME_ROOT/project.godot"
IGNORE_FILE="$GAME_ROOT/.gitignore"
PASS_COUNT=0
FAIL_COUNT=0

assert_contains() {
	case_name=$1
	expected_text=$2
	target_file=$3
	if [ -f "$target_file" ] && grep -F "$expected_text" "$target_file" >/dev/null; then
		PASS_COUNT=$((PASS_COUNT + 1))
		printf 'PASS %s\n' "$case_name"
	else
		FAIL_COUNT=$((FAIL_COUNT + 1))
		printf 'FAIL %s\n' "$case_name" >&2
	fi
}

assert_not_contains() {
	case_name=$1
	unexpected_text=$2
	target_file=$3
	if [ -f "$target_file" ] && ! grep -F "$unexpected_text" "$target_file" >/dev/null; then
		PASS_COUNT=$((PASS_COUNT + 1))
		printf 'PASS %s\n' "$case_name"
	else
		FAIL_COUNT=$((FAIL_COUNT + 1))
		printf 'FAIL %s\n' "$case_name" >&2
	fi
}

assert_contains "project name is explicit" 'config/name="outsurvive"' "$PROJECT_FILE"
assert_contains "main scene is explicit" 'run/main_scene="res://scenes/boot/boot_root.tscn"' "$PROJECT_FILE"
assert_contains "desktop renderer is Forward+" 'renderer/rendering_method="forward_plus"' "$PROJECT_FILE"
assert_contains "mobile renderer override is Mobile" 'renderer/rendering_method.mobile="mobile"' "$PROJECT_FILE"
assert_contains "untyped declarations are errors" 'warnings/untyped_declaration=2' "$PROJECT_FILE"
assert_contains "build ID is explicit" 'build_id="local-dev"' "$PROJECT_FILE"
assert_contains "expected engine version key exists" 'expected_engine_version={' "$PROJECT_FILE"
assert_contains "BuildInfo is an autoload" 'BuildInfo="*res://src/shared/kernel/build_info.gd"' "$PROJECT_FILE"
assert_contains "AppKernel is an autoload" 'AppKernel="*res://src/client/bootstrap/app_kernel.gd"' "$PROJECT_FILE"
assert_not_contains "GameLog is not an autoload" 'GameLog="*' "$PROJECT_FILE"
assert_not_contains "PlatformGateway is not premature" 'PlatformGateway="*' "$PROJECT_FILE"
assert_contains "Godot import cache is ignored" '.godot/' "$IGNORE_FILE"
assert_contains "generated translation cache is ignored" '*.translation' "$IGNORE_FILE"

printf 'project config tests: %s passed, %s failed\n' "$PASS_COUNT" "$FAIL_COUNT"
test "$FAIL_COUNT" -eq 0
