---
title: Pilot Tests and Evidence
permalink: /pilots/test-and-evidence/
parent: Pilot GAAM
grand_parent: Implement
nav_order: 4
artifact_type: Informative pilot evidence guidance
normative_status: Informative
---
# Pilot Tests and Evidence

The pilot's purpose is to challenge whether GAAM's published concepts lead to reliably governed effects, not to maximize the number of tests. The **canonical** requirement, schema, profile and evidence-report contracts continue to reside outside this guide.

## Minimum scenario matrix

| Scenario | Expected safeguard | Evidence required from the implementation |
| --- | --- | --- |
| Valid bounded authority and current evidence | Permit only if applicable policy permits; constrain execution | Input, policy/authority sources, disposition, enforcement and observed effect |
| Authority amplification | Reject effects beyond parent-grant scope | Chain and attenuation check, refusal and receipt |
| Revoked or expired parent | Reject dependent authority, handle propagation and in-flight work | Authoritative status and effective time, dependent operations, interruption results |
| Required evidence stale or unavailable | No unqualified permit; explicit indeterminate/denial/review disposition | Freshness standard, failed resolution and safe handling |
| Conflicting sources or policy precedence | No arbitrary most-permissive interpretation | Conflicts, resolution authority or recorded escalation |
| Execution failed, partially completed or unknown | Do not report completion merely because authorization succeeded | Decision receipt **plus separate** observable execution state and reconciliation record |
| Correction / affected-party challenge | Accessible challenge and accountable remedy path | Notice, review decision, downstream correction and verification evidence |

Record **both expected and observed outcomes**. A test fails if a prohibited effect executes or if a purported PASS cannot be reconstructed. Unexecuted or unavailable cases are **not-assessed** or **blocked**, not successful.

## Evidence package

Every gate record needs a named **role/owner**, disposition, source reference, observed result, timestamp/revision and exceptions. The [gate catalogue](gates.json) defines the pilot-level expected outcomes. Implementation-report and evidence-manifest schemas govern corresponding external claims; the pilot catalogue does not replace them.

For local evidence, use a content-addressed relative file path and SHA-256 digest. `scripts/validate_pilot_readiness.py` checks these local references for integrity and rejects missing evidence or dishonest independence labels. A digest authenticates bytes **at the checked path**, not the authority of their author or the truth of their contents. External evidence must disclose authorship, assessor relationships and verification method. Never use arbitrary URLs alone as proof that gate conditions have been satisfied.

## Distinguish evidence classes

| Evidence class | What it establishes | What it cannot establish |
| --- | --- | --- |
| GAAM internal dry run | Repository tooling can execute selected contracts | G0 sponsor approval, actual authorization, E2 independent implementation |
| Participant self-assessment | Operator-reported implementation behavior in declared scope | Independent assessment or cross-implementation interoperability |
| Independent implementation report | Separately attributable source and test results, subject to review | Automatic E2 acceptance or production safety |
| Cross-implementation test | Behavior across distinct systems in tested scenarios | Universal portability or unrestricted ecosystem recognition |
| Pilot closeout | Sponsor's informed disposition | Certification or GAAM Stable specification status |

## Reproduction and falsification

```bash
python scripts/validate_pilot_readiness.py --run
python scripts/validate_clean_room.py
python scripts/gaam.py validate-package conformance-kit/starter
python scripts/gaam.py run-vectors --pattern 'delegation-*.json' python conformance-kit/reference_adapter.py
```

The dry run is a **separate E1 source-bound exercise** from a participant's actual implementation. For external evidence use the [independent implementation intake](../implementation-reports/independent-implementation-intake.md); for cross-implementation evidence use the [cross-implementation protocol](../implementation-reports/cross-implementation-protocol.md). Missing external participants are an evidence gap, not a reason to change the definition of independence.
