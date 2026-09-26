# Independent Review Handoff

This directory contains repository-controlled preparation for independent GAAM candidate reviews.

The preparation is intentionally bounded: it may assemble questions, existing evidence, executable vectors and expected reviewer outputs, but it **cannot satisfy an independent review gate** and must not be presented as independent assurance.

## Review packages

### Security

Use `security-review-preparation.json` together with:

- `governance/reviews/security-review.json`
- `governance/reviews/finding.schema.json`
- `governance/reviews/finding-vocabulary.json`
- `governance/reviews/review-methodology.md`
- `governance/reviews/review-baseline.json`

Every security pressure test declares a `coverageDisposition`.

- `executable-plus-review` means repository behavioural evidence exists but does not replace independent review.
- `review-required` means no repository-owned vector is allowed to stand in for the reviewer judgement.

The reviewer must return attributable findings, threat-register reconciliation, independence/conflict disclosure, closure evidence for remediated blockers, and completion attestation.

### Affected-party

Use `affected-party-review-preparation.json` together with:

- `governance/reviews/affected-party-review.json`
- `governance/reviews/finding.schema.json`
- `governance/reviews/finding-vocabulary.json`
- `governance/reviews/review-methodology.md`
- `governance/reviews/review-baseline.json`

The existing vector `tests/behavioural/appeal-record-without-state-change-rejected.json` explicitly exercises the proposition that a completed appeal/remedy record without a governed state change or other consequential outcome is **not** effective remedy. It satisfies the repository-controlled negative-test portion of issue #15 but does not establish that real affected parties can obtain effective remedy.

## Reviewer procedure

1. Confirm the frozen review baseline and the scope of the review.
2. Record reviewer identity, organisation, independence classification and conflicts.
3. Execute or inspect the referenced repository evidence.
4. Test each pressure-test falsification condition independently.
5. Record findings using `governance/reviews/finding.schema.json`.
6. Mark material/critical findings as blocking where warranted; unknown or indeterminate states must not be converted to pass.
7. Provide evidence references for each finding and any closure claim.
8. Return an attestation only after the applicable review register exit criteria are satisfied.

## Authority and closure

Independent reviewers produce review evidence. GAAM maintainers retain authority to disposition findings, accept remediation or residual risk within `GOVERNANCE.md`, and determine release impact.

Repository preparation remains `prepared-not-attested` until an attributable independent review is received. No maintainer-authored fixture, vector, review note or synthetic report can be relabelled as independent evidence.
