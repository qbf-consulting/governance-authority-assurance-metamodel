# GAAM Security Review Handoff

## Purpose

This handoff makes the repository-controlled portion of the GAAM candidate security review complete and reviewable without converting maintainer preparation into independent assurance.

The independent reviewer remains responsible for attributable findings, conflict disclosure, attestation, and any conclusion that the security-review evidence level has advanced.

## Review baseline

- Semantic/canonical baseline: GAAM v0.9.0
- Current normative Candidate release: v0.9.2
- Frozen review baseline: `governance/reviews/review-baseline.json`
- Review register: `governance/reviews/security-review.json`
- Structured preparation dossier: `governance/reviews/evidence/pre-review/security-review-preparation.json`
- Threat register: `threat-model/threat-register.json`
- Finding schema: `governance/reviews/finding.schema.json`

## Reviewer execution

For each `GAAM-SEC-PT-*` pressure test:

1. verify the cited normative requirements and threat-register mappings;
2. reproduce or inspect the listed behavioural tests and repository validation evidence;
3. test the stated falsification condition against at least one realistic implementation or implementation design;
4. record any finding using `governance/reviews/finding.schema.json`;
5. classify severity, evidence, affected requirements and whether the finding blocks the declared review boundary;
6. disclose reviewer independence and conflicts;
7. identify whether remediation requires documentation, tests, implementation guidance, security correction or normative change.

## Threat coverage matrix

| Pressure test | Threat(s) | Existing executable evidence | Residual reviewer task |
|---|---|---|---|
| GAAM-SEC-PT-001 authority laundering | GAAM-THR-001 | authority active/revoked/source/scope vectors | Assess whether identity, authentication or registry status can still be operationally mistaken for scoped authority. |
| GAAM-SEC-PT-002 delegation amplification/circularity | GAAM-THR-002 | attenuation, amplification, cycle, depth and redelegation vectors | Assess multi-hop and implementation-specific constraint propagation. |
| GAAM-SEC-PT-003 stale revocation/races | GAAM-THR-003 | revoked-parent, upstream-revoked, runtime fail-closed and stale-state vectors | Assess cache/concurrency windows and freshness policy under realistic runtime conditions. |
| GAAM-SEC-PT-004 evidence substitution/assurance laundering | GAAM-THR-004 | assurance expiry, independence, freshness and stale-evidence vectors | Assess subject, purpose and context substitution not reducible to repository fixtures. |
| GAAM-SEC-PT-005 governance package substitution | GAAM-THR-007 | package checksum/publication controls and receipt-digest mismatch vector | Assess authoritative provenance substitution where structure remains valid. |
| GAAM-SEC-PT-006 remedy bypass/accountability fragmentation | GAAM-THR-005, GAAM-THR-006 | unattributed decision, remedy, review-independence and propagation vectors | Assess whether accountability survives provider/agent/delegation changes in realistic operating models. |

## Required output

The independent review is complete only when:

- the reviewer identity, organisation, independence classification and conflicts are recorded;
- findings are attributable and schema-valid;
- all critical findings have governed dispositions;
- testable remediations have regression evidence;
- residual risks identify the decision authority accepting them;
- `governance/reviews/security-review.json` is updated to `complete` only after attestation.

## Non-substitution boundary

Repository maintainers prepared this package and may disposition findings, but they MUST NOT mark the independent security attestation satisfied on the strength of this preparation alone.
