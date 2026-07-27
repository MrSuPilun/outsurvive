#!/bin/sh

set -u

REPO_ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)

if [ -n "${MODULE_BOUNDARIES_PYTHON:-}" ]; then
	PYTHON_BIN=$MODULE_BOUNDARIES_PYTHON
elif command -v python3.12 >/dev/null 2>&1; then
	PYTHON_BIN=$(command -v python3.12)
elif command -v python3 >/dev/null 2>&1; then
	PYTHON_BIN=$(command -v python3)
else
	printf '%s\n' '{"status":"fail","error":"Python 3.12+ is required"}' >&2
	exit 2
fi

"$PYTHON_BIN" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 12) else 2)'
if [ "$?" -ne 0 ]; then
	printf '%s\n' '{"status":"fail","error":"Python 3.12+ is required"}' >&2
	exit 2
fi

cd "$REPO_ROOT" || exit 2
"$PYTHON_BIN" -m unittest game/tests/unit/tools/test_module_boundaries.py || exit $?
"$PYTHON_BIN" infrastructure/ci/check_module_boundaries.py \
	--repo-root "$REPO_ROOT" \
	--policy "$REPO_ROOT/infrastructure/ci/module_boundaries.toml"
