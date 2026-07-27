#!/bin/sh

set -u

REPO_ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
LOCK_PATH="$REPO_ROOT/infrastructure/ci/dependency_lock.toml"
SBOM_PATH="$REPO_ROOT/infrastructure/ci/sbom/outsurvive.cdx.json"
ADR_FIXTURE="$REPO_ROOT/game/tests/fixtures/dependency_lock/valid_upgrade_adr.md"
TEMP_SBOM=""

cleanup() {
	if [ -n "$TEMP_SBOM" ] && [ -f "$TEMP_SBOM" ]; then
		rm -f "$TEMP_SBOM"
	fi
}

trap cleanup EXIT HUP INT TERM

if [ -n "${DEPENDENCY_LOCK_PYTHON:-}" ]; then
	PYTHON_BIN=$DEPENDENCY_LOCK_PYTHON
elif command -v python3.12 >/dev/null 2>&1; then
	PYTHON_BIN=$(command -v python3.12)
elif command -v python3 >/dev/null 2>&1; then
	PYTHON_BIN=$(command -v python3)
else
	printf '%s\n' '{"status":"failure","violations":[{"rule_id":"LOCK_PYTHON_MISSING","path":"python","message":"Python 3.12+ is required"}]}'
	exit 2
fi

"$PYTHON_BIN" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 12) else 2)'
if [ "$?" -ne 0 ]; then
	printf '%s\n' '{"status":"failure","violations":[{"rule_id":"LOCK_PYTHON_VERSION","path":"python","message":"Python 3.12+ is required"}]}'
	exit 2
fi

cd "$REPO_ROOT" || exit 2
DEPENDENCY_LOCK_PYTHON="$PYTHON_BIN" \
	"$PYTHON_BIN" -m unittest game/tests/unit/tools/test_dependency_lock.py >&2 || exit $?

TEMP_SBOM=$(mktemp "${TMPDIR:-/tmp}/outsurvive-sbom.XXXXXX")
"$PYTHON_BIN" infrastructure/ci/generate_sbom.py \
	--lock "$LOCK_PATH" \
	--output "$TEMP_SBOM" >/dev/null || exit $?

if ! cmp -s "$TEMP_SBOM" "$SBOM_PATH"; then
	printf '%s\n' '{"status":"failure","violations":[{"rule_id":"SBOM_NONDETERMINISTIC","path":"infrastructure/ci/sbom/outsurvive.cdx.json","message":"tracked SBOM differs from deterministic regeneration"}]}'
	exit 1
fi

"$PYTHON_BIN" infrastructure/ci/check_upgrade_adr.py "$ADR_FIXTURE" >/dev/null || exit $?
"$PYTHON_BIN" infrastructure/ci/check_dependency_lock.py \
	--lock infrastructure/ci/dependency_lock.toml \
	--sbom infrastructure/ci/sbom/outsurvive.cdx.json
