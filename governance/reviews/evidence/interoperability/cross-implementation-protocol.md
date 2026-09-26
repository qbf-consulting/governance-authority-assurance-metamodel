# Cross-Implementation Interoperability Protocol

## Purpose

This protocol defines the evidence-producing exercise required for GAAM cross-implementation interoperability evidence under issue #21.

The protocol is fixed before participant results are evaluated so success criteria cannot be adjusted after observing differences.

## Preconditions

The exercise requires at least two implementations whose provenance and independence are disclosed. Each implementation must have a bounded GAAM profile/requirement scope and a validator or adapter capable of evaluating artifacts produced by the other implementation where the portable contract permits.

Repository-owned reference vectors may seed the exercise but cannot substitute for independently produced implementation artifacts.

## Exercise matrix

For two implementations A and B:

```text
Implementation A artifacts  -> Validator/adapter B -> Result B(A)
Implementation B artifacts  -> Validator/adapter A -> Result A(B)
```

Where feasible, each implementation also evaluates its own artifact so cross-validator differences can be distinguished from artifact defects.

## Required scenarios

The evidence bundle MUST exercise, within the participants' declared scope:

1. a positive Foundation-profile case;
2. at least one composed-profile case when supported;
3. decision receipt semantics;
4. lifecycle/revocation state;
5. unknown or unsupported extension handling;
6. at least one negative authority/delegation case;
7. at least one stale/unknown-state case;
8. at least one mismatch case where validators disagree or reject different aspects of the same input.

## Result states

Results MUST preserve at least:

- pass;
- fail;
- indeterminate/unknown where the implementation cannot safely decide;
- not-applicable where outside the declared scope.

Failures and indeterminate results MUST NOT be converted into interoperability success.

## Evidence bundle

Each participant pair must preserve:

- implementation identity and source revision;
- validator/adapter identity and version;
- GAAM version/profile scope;
- exact input artifact bytes or content-addressed references;
- exact cross-validator output;
- timestamps and environment information sufficient for reproduction;
- semantic-difference notes;
- relationship and independence disclosure;
- unresolved exceptions.

Evidence should be placed under `governance/reviews/evidence/interoperability/` or referenced from an accepted evidence manifest where direct retention is impractical.

## Evaluation rule

Cross-implementation interoperability is evidenced only when both directions of the exercise are reproducible and the resulting semantic differences are documented.

The exercise does not require identical internal architecture. It requires that independently produced artifacts and validators agree on the governed semantics inside the declared GAAM claim boundary, or that any disagreement is explicitly preserved and dispositioned.

## Closure rule for #21

Issue #21 can close only when:

- at least two independent implementations participated;
- both cross-validation directions were executed;
- evidence is attributable and reproducible;
- lifecycle/receipt semantics and negative/mismatch cases were exercised;
- failures and indeterminate results remain visible;
- semantic differences are recorded and, where material, dispositioned;
- `governance/reviews/interoperability-review.json` is completed and attested from the resulting evidence.

## Reassessment trigger

A semantic disagreement that indicates ambiguity, incompatible interpretation, unsafe fail-open behaviour or invalid normative assumption enters the governed GAAM finding/change lifecycle and may affect specification Stable-readiness independently of the E3 evidence claim.
