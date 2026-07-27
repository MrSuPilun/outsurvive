# Module boundaries

`infrastructure/ci/module_boundaries.toml` is the machine-readable source of truth
for repository ownership and allowed dependency edges. This document explains the
model; it is not a second allowlist.

## Canonical graph

```text
client application ───────────┐
server application ───────────┼──> shared contracts/simulation/data
platform ports/adapters ──────┘

composition roots ───────────────> typed port + concrete adapter (injection only)
game tools/devtools ─────────────> shared schemas/contracts
backend ─────────────────────────> generated contracts
shared ──────────────────────────> shared + approved Godot core primitives only

production runtime -X-> tools | tests | test-harness | content-source | prepare-asset
shared             -X-> client | server | presentation | platform | backend
client domain      -X-> server implementation | concrete provider adapter
server             -X-> scenes | UI | audio | visual assets
```

Platform-neutral contracts belong in `game/src/platform/ports` and use typed
`*Port` classes. Provider implementations belong in
`game/src/platform/adapters` or a declared native bridge. Only a declared
composition root may reference a concrete adapter for injection; consumers depend
on the port.

## Ownership partition

Every governed file must match exactly one module row. Parent patterns explicitly
exclude child partitions: for example `client` excludes `client/bootstrap` and
`client/ui`, while `game_tests` excludes deliberate boundary fixtures. Matching
zero modules is an unknown owner; matching multiple modules is an ambiguous owner.
Both are errors.

The root owner markers describe roots that do not yet have runtime consumers.
`content-source` remains raw authoring/DCC input and `prepare-asset` remains
untrusted quarantine. Production runtime code may not depend on either root.

## Adding a module or dependency

1. Identify the domain owner and narrowest non-overlapping path partition.
2. Add or update the policy row, including all parent exclusions.
3. Add a positive fixture for the intended edge and a negative fixture for the
   nearest forbidden edge.
4. Run `infrastructure/ci/verify_module_boundaries.sh`.
5. If the change alters an architecture decision instead of encoding an existing
   one, update Game Architecture and record an ADR before merging.

Do not add filename waivers, permissive fallback owners, or warning-only rules.
Policy/schema errors, unresolved dependencies, unsupported governed syntax, and
unknown source types fail closed.

## CI evidence

The narrow workflow exposes the stable check
`module-boundaries / module_boundaries`. It runs policy/fixture tests followed by a
real working-tree scan and publishes no game artifact. Canonical build aggregation
belongs to Story 1.4.
