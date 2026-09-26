# GAAM Affected-Party Review Handoff

## Purpose

This handoff completes the repository-controlled preparation for an independent affected-party/redress review. It does not constitute independent review or attestation.

## Review baseline

- Semantic/canonical baseline: GAAM v0.9.0
- Current normative Candidate release: v0.9.2
- Frozen review baseline: `governance/reviews/review-baseline.json`
- Review register: `governance/reviews/affected-party-review.json`
- Structured preparation dossier: `governance/reviews/evidence/pre-review/affected-party-review-preparation.json`
- Finding schema: `governance/reviews/finding.schema.json`

## Reviewer execution

For each `GAAM-AP-PT-*` pressure test:

1. verify the cited normative requirement and evidence surfaces;
2. inspect or reproduce the listed behavioural vectors;
3. assess the falsification condition from the perspective of a materially affected party;
4. record findings using `governance/reviews/finding.schema.json`;
5. identify whether a failure is documentation, implementation guidance, schema/profile, security/privacy, or normative-semantics related;
6. disclose independence and conflicts;
7. identify responsible disposition authority and verification evidence.

## Review focus

| Pressure test | Executable evidence | Residual reviewer task |
|---|---|---|
| GAAM-AP-PT-001 notice/intelligibility | traceable/unattributed decision and missing-notice vectors | Assess whether notice is intelligible enough to support meaningful challenge. |
| GAAM-AP-PT-002 standing | high-impact remedy path | Assess whether materially affected non-participants can initiate review. |
| GAAM-AP-PT-003 review independence | independent-review negative vector | Assess conflicts, escalation and practical independence. |
| GAAM-AP-PT-004 interim protection | fail-closed runtime/degraded-operation vectors | Assess whether harmful ongoing effects can actually be suspended or constrained pending review. |
| GAAM-AP-PT-005 remedy execution | remedy-positive/negative, propagation, and nominal-remedy-without-state-change vectors | Verify that remedy has an attributable consequential outcome rather than merely recording an appeal. |
| GAAM-AP-PT-006 accountability continuity | unattributed decision, delegation lifecycle and remedy propagation vectors | Assess continuity after delegation, agent replacement, provider exit or authority revocation. |

## Required output

The independent review is complete only when:

- reviewer identity, organisation, independence and conflicts are recorded;
- findings are attributable and schema-valid;
- any blocking finding has a governed disposition;
- remediated findings have verification evidence;
- `governance/reviews/affected-party-review.json` is updated to `complete` only after independent attestation.

## Non-substitution boundary

Repository preparation and executable vectors may support the reviewer, but they MUST NOT be relabelled as independent affected-party evidence.
