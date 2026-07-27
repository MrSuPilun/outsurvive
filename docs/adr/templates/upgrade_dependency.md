---
title: Upgrade <dependency_id> to <to_version>
status: proposed
date: YYYY-MM-DD
dependency_id: <lock id>
from_version: <current pinned version>
to_version: <proposed pinned version>
compatibility_branch: <branch containing compatibility work>
protocol_impact: <none with reason, or migration description>
content_manifest_impact: <none with reason, or migration description>
license_decision: <approved|undecided|rejected>
cve_decision: <cleared|undecided|accepted_risk - justification>
adr20_spike_evidence: <path/link, or n/a with reason for non-plugin/native>
rollback_plan: <how to restore the prior lock and artifacts>
---

# Rationale

<Why the upgrade is needed and why this version is selected.>

## Compatibility and migration

<Compatibility details, including exact protocol/content migration evidence.>

## Impacted Platform Smoke Matrix

| Platform | Gate | Owner |
|---|---|---|
| <platform> | <smoke/parity gate> | <team owner> |

## Evidence

<Checksums, release notes, license/CVE review, spike reports and CI run links.>
