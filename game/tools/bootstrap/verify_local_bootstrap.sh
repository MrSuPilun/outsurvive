#!/bin/sh

set -u

EXPECTED_MAJOR=4
EXPECTED_MINOR=7
EXPECTED_PATCH=1
EXPECTED_STATUS=stable
EXPECTED_TEMPLATE_VERSION=4.7.1.stable
GAME_ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
ACTIVE_LOG=""

cleanup() {
	if [ -n "$ACTIVE_LOG" ] && [ -f "$ACTIVE_LOG" ]; then
		rm -f "$ACTIVE_LOG"
	fi
}

trap cleanup EXIT HUP INT TERM

emit_failure() {
	error_code=$1
	error_message=$2
	printf '{"status":"failure","error":{"code":"%s","message":"%s"}}\n' \
		"$error_code" "$error_message" >&2
	exit 2
}

find_godot_binary() {
	if [ -n "${GODOT_BIN:-}" ]; then
		if command -v "$GODOT_BIN" >/dev/null 2>&1; then
			command -v "$GODOT_BIN"
			return 0
		fi
		if [ -f "$GODOT_BIN" ] && [ -x "$GODOT_BIN" ]; then
			printf '%s\n' "$GODOT_BIN"
			return 0
		fi
		return 1
	fi

	if command -v godot >/dev/null 2>&1; then
		command -v godot
		return 0
	fi

	if command -v godot4 >/dev/null 2>&1; then
		command -v godot4
		return 0
	fi

	return 1
}

sha256_file() {
	if command -v sha256sum >/dev/null 2>&1; then
		sha256sum "$1" | awk '{print $1}'
		return 0
	fi

	if command -v shasum >/dev/null 2>&1; then
		shasum -a 256 "$1" | awk '{print $1}'
		return 0
	fi

	return 1
}

detect_template_version() {
	if [ -n "${GODOT_EXPORT_TEMPLATE_VERSION:-}" ]; then
		printf '%s\n' "$GODOT_EXPORT_TEMPLATE_VERSION"
		return
	fi

	if [ -n "${GODOT_EXPORT_TEMPLATES_DIR:-}" ] &&
		[ -d "$GODOT_EXPORT_TEMPLATES_DIR/$EXPECTED_TEMPLATE_VERSION" ]; then
		printf '%s\n' "$EXPECTED_TEMPLATE_VERSION"
		return
	fi

	if [ -d "${HOME}/Library/Application Support/Godot/export_templates/$EXPECTED_TEMPLATE_VERSION" ] ||
		[ -d "${XDG_DATA_HOME:-${HOME}/.local/share}/godot/export_templates/$EXPECTED_TEMPLATE_VERSION" ]; then
		printf '%s\n' "$EXPECTED_TEMPLATE_VERSION"
	fi
}

run_preflight() {
	godot_binary=$(find_godot_binary) || emit_failure "BOOT_ENGINE_MISSING" "Godot binary was not provided through GODOT_BIN and was not found in PATH"
	if [ ! -f "$godot_binary" ] || [ ! -x "$godot_binary" ]; then
		emit_failure "BOOT_ENGINE_MISSING" "Selected Godot binary does not exist or is not executable"
	fi

	version_text=$("$godot_binary" --version 2>/dev/null | tr -d '\r\n')
	case "$version_text" in
		4.7.1.stable.official.*) ;;
		*)
			emit_failure "BOOT_ENGINE_VERSION_MISMATCH" "Godot must be the official Standard 4.7.1-stable build"
			;;
	esac

	case "$version_text" in
		*.mono.*|*.net.*)
			emit_failure "BOOT_ENGINE_FLAVOR_MISMATCH" "Godot Mono/.NET builds are not supported"
			;;
	esac

	commit_hash=${version_text#4.7.1.stable.official.}
	commit_hash_lower=$(printf '%s' "$commit_hash" | tr 'A-F' 'a-f')
	case "$commit_hash_lower" in
		""|*[!0-9a-f]*)
			emit_failure "BOOT_ENGINE_VERSION_MALFORMED" "Official engine commit hash is missing or malformed"
			;;
	esac

	observed_sha256=$(sha256_file "$godot_binary") || emit_failure "BOOT_CHECKSUM_TOOL_MISSING" "Neither sha256sum nor shasum is available"

	trusted_state=not_provided
	checksum_status=observed_only
	if [ -n "${GODOT_SHA256:-}" ]; then
		case "$GODOT_SHA256" in
			*[!0-9a-fA-F]*)
				emit_failure "BOOT_ENGINE_CHECKSUM_MALFORMED" "GODOT_SHA256 must contain hexadecimal characters only"
				;;
		esac
		if [ "${#GODOT_SHA256}" -ne 64 ]; then
			emit_failure "BOOT_ENGINE_CHECKSUM_MALFORMED" "GODOT_SHA256 must contain exactly 64 hexadecimal characters"
		fi
		trusted_sha256=$(printf '%s' "$GODOT_SHA256" | tr 'A-F' 'a-f')
		if [ "$observed_sha256" != "$trusted_sha256" ]; then
			emit_failure "BOOT_ENGINE_CHECKSUM_MISMATCH" "Selected Godot binary does not match GODOT_SHA256"
		fi
		trusted_state=provided
		checksum_status=pass
	fi

	template_version=$(detect_template_version)
	template_status=not_applicable
	if [ -n "$template_version" ]; then
		if [ "$template_version" != "$EXPECTED_TEMPLATE_VERSION" ]; then
			emit_failure "BOOT_EXPORT_TEMPLATE_VERSION_MISMATCH" "Selected export templates must be 4.7.1-stable"
		fi
		template_status=pass
	fi

	printf '{"status":"pass","engine":{"major":%s,"minor":%s,"patch":%s,"status":"%s","build":"official","commit":"%s","flavor":"standard"},"sha256":{"observed":"%s","trusted":"%s","status":"%s"},"export_templates":{"status":"%s","version":"%s"}}\n' \
		"$EXPECTED_MAJOR" "$EXPECTED_MINOR" "$EXPECTED_PATCH" "$EXPECTED_STATUS" "$commit_hash" \
		"$observed_sha256" "$trusted_state" "$checksum_status" "$template_status" "$template_version"
}

run_checked() {
	check_name=$1
	required_pattern=$2
	shift 2
	ACTIVE_LOG=$(mktemp "${TMPDIR:-/tmp}/outsurvive-bootstrap-check.XXXXXX")

	"$@" >"$ACTIVE_LOG" 2>&1
	check_status=$?
	sed 's/^/  /' "$ACTIVE_LOG"

	if [ "$check_status" -ne 0 ]; then
		emit_failure "BOOT_VERIFY_CHECK_FAILED" "$check_name returned exit code $check_status"
	fi

	if grep -E '(^|[[:space:]])(SCRIPT ERROR|ERROR|WARNING):' "$ACTIVE_LOG" >/dev/null; then
		emit_failure "BOOT_VERIFY_DIAGNOSTIC_FAILURE" "$check_name emitted an error or warning"
	fi

	if [ -n "$required_pattern" ] && ! grep -F "$required_pattern" "$ACTIVE_LOG" >/dev/null; then
		emit_failure "BOOT_VERIFY_EVIDENCE_MISSING" "$check_name did not emit required evidence"
	fi

	rm -f "$ACTIVE_LOG"
	ACTIVE_LOG=""
}

run_full_verification() {
	run_preflight
	selected_godot=$(find_godot_binary)

	run_checked \
		"project configuration tests" \
		"project config tests: 13 passed, 0 failed" \
		"$GAME_ROOT/tests/unit/tools/test_project_config.sh"
	run_checked \
		"headless import" \
		"Godot Engine v4.7.1.stable.official." \
		"$selected_godot" --headless --path "$GAME_ROOT" --import
	run_checked \
		"bootstrap unit smoke" \
		'"event":"bootstrap_tests_passed"' \
		"$selected_godot" --headless --path "$GAME_ROOT" \
		--script res://tests/unit/client/test_bootstrap.gd
	run_checked \
		"main-scene smoke" \
		'"trigger":"bootstrap_smoke"' \
		"$selected_godot" --headless --path "$GAME_ROOT" -- --bootstrap-smoke

	printf '{"status":"pass","checks":["preflight","project_config","headless_import","unit_smoke","main_scene_smoke"]}\n'
}

case "${1:-}" in
	"")
	run_full_verification
	;;
	--preflight-only)
	run_preflight
	;;
	*)
	emit_failure "BOOT_VERIFY_ARGUMENT_INVALID" "Unsupported verifier argument"
	;;
esac
