#!/bin/sh

set -u

TEST_ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/../../.." && pwd)
VERIFY_SCRIPT="$TEST_ROOT/tools/bootstrap/verify_local_bootstrap.sh"
FIXTURE_DIR=$(mktemp -d "${TMPDIR:-/tmp}/outsurvive-preflight.XXXXXX")
PASS_COUNT=0
FAIL_COUNT=0

cleanup() {
	rm -rf "$FIXTURE_DIR"
}

trap cleanup EXIT HUP INT TERM

make_fake_godot() {
	fixture_path=$1
	version_text=$2
	{
		printf '%s\n' '#!/bin/sh'
		printf '%s\n' "printf '%s\\n' '$version_text'"
	} >"$fixture_path"
	chmod +x "$fixture_path"
}

sha256_file() {
	if command -v sha256sum >/dev/null 2>&1; then
		sha256sum "$1" | awk '{print $1}'
	else
		shasum -a 256 "$1" | awk '{print $1}'
	fi
}

record_pass() {
	PASS_COUNT=$((PASS_COUNT + 1))
	printf 'PASS %s\n' "$1"
}

record_fail() {
	FAIL_COUNT=$((FAIL_COUNT + 1))
	printf 'FAIL %s\n' "$1" >&2
}

expect_success() {
	case_name=$1
	shift
	if "$@" >"$FIXTURE_DIR/stdout" 2>"$FIXTURE_DIR/stderr"; then
		record_pass "$case_name"
	else
		record_fail "$case_name"
		sed 's/^/  /' "$FIXTURE_DIR/stderr" >&2
	fi
}

expect_failure() {
	case_name=$1
	shift
	if "$@" >"$FIXTURE_DIR/stdout" 2>"$FIXTURE_DIR/stderr"; then
		record_fail "$case_name"
	else
		record_pass "$case_name"
	fi
}

VALID_GODOT="$FIXTURE_DIR/godot-valid"
WRONG_VERSION_GODOT="$FIXTURE_DIR/godot-wrong-version"
MONO_GODOT="$FIXTURE_DIR/godot-mono"

make_fake_godot "$VALID_GODOT" "4.7.1.stable.official.a13da4feb"
make_fake_godot "$WRONG_VERSION_GODOT" "4.7.0.stable.official.abcdef012"
make_fake_godot "$MONO_GODOT" "4.7.1.stable.mono.official.abcdef012"

expect_failure "missing binary fails closed" \
	env GODOT_BIN="$FIXTURE_DIR/missing" "$VERIFY_SCRIPT" --preflight-only

expect_failure "wrong engine version is rejected" \
	env GODOT_BIN="$WRONG_VERSION_GODOT" "$VERIFY_SCRIPT" --preflight-only

expect_failure "Mono build is rejected" \
	env GODOT_BIN="$MONO_GODOT" "$VERIFY_SCRIPT" --preflight-only

expect_failure "trusted checksum mismatch is rejected" \
	env GODOT_BIN="$VALID_GODOT" GODOT_SHA256="0000000000000000000000000000000000000000000000000000000000000000" \
	"$VERIFY_SCRIPT" --preflight-only

VALID_SHA256=$(sha256_file "$VALID_GODOT")
expect_success "official Standard build and trusted checksum pass" \
	env GODOT_BIN="$VALID_GODOT" GODOT_SHA256="$VALID_SHA256" \
	"$VERIFY_SCRIPT" --preflight-only

if grep -F '"engine":{"major":4,"minor":7,"patch":1,"status":"stable","build":"official","commit":"a13da4feb","flavor":"standard"}' "$FIXTURE_DIR/stdout" >/dev/null &&
	grep -F '"export_templates":{"status":"not_applicable"' "$FIXTURE_DIR/stdout" >/dev/null &&
	grep -F "\"sha256\":{\"observed\":\"$VALID_SHA256\",\"trusted\":\"provided\",\"status\":\"pass\"}" "$FIXTURE_DIR/stdout" >/dev/null; then
	record_pass "success evidence is structured and complete"
else
	record_fail "success evidence is structured and complete"
fi

expect_failure "selected mismatched export templates are rejected" \
	env GODOT_BIN="$VALID_GODOT" GODOT_EXPORT_TEMPLATE_VERSION="4.7.0.stable" \
	"$VERIFY_SCRIPT" --preflight-only

expect_success "selected matching export templates pass" \
	env GODOT_BIN="$VALID_GODOT" GODOT_EXPORT_TEMPLATE_VERSION="4.7.1.stable" \
	"$VERIFY_SCRIPT" --preflight-only

if grep -F '"export_templates":{"status":"pass","version":"4.7.1.stable"}' "$FIXTURE_DIR/stdout" >/dev/null; then
	record_pass "matching template evidence is explicit"
else
	record_fail "matching template evidence is explicit"
fi

expect_failure "full verification rejects a version-only fake binary" \
	env GODOT_BIN="$VALID_GODOT" "$VERIFY_SCRIPT"

printf 'preflight tests: %s passed, %s failed\n' "$PASS_COUNT" "$FAIL_COUNT"
test "$FAIL_COUNT" -eq 0
