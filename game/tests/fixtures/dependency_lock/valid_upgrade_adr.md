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

Exercise the repository upgrade gate.

## Impacted Platform Smoke Matrix

| Platform | Gate | Owner |
|---|---|---|
| linux_x64 | dependency lock verifier | infrastructure |
