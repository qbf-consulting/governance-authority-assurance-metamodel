---
title: "Clean-Room Implementation Exercise"
permalink: /clean-room-implementation/
artifact_type: "Implementation guidance"
normative_status: "Informative"
---
# Clean-Room Implementation Exercise

{% include gaam-meta.html %}

This exercise tests a narrow adoption proposition: **can a competent implementer use only GAAM's published repository artifacts to enter the implementation/evidence workflow without maintainer-only knowledge?**

It does **not** test independent implementation. The repository executes the exercise itself, so every result remains synthetic, self-assessed and bounded to L1 repository evidence.

## Published artifacts used

The exercise uses only artifacts an external implementer can discover from the repository:

- `profiles/manifests/foundation.json` — authoritative Foundation Profile closure;
- `conformance-kit/starter/` — minimum package shape and included authority/decision/conformance artifacts;
- `scripts/gaam.py` — portable package, claim and behavioural-vector validator;
- `conformance-kit/reference_adapter.py` — reference adapter for the portable vectors;
- `implementation-reports/implementation-report.schema.json` — machine-readable report contract;
- `implementation-reports/evidence-manifest.schema.json` — evidence manifest contract.

## Reproducible path

From a fresh checkout with the documented development dependencies installed:

```bash
python scripts/gaam.py validate-package conformance-kit/starter
python scripts/gaam.py validate-claim conformance-kit/starter/artifacts/conformance-claim.json
python scripts/gaam.py run-vectors python conformance-kit/reference_adapter.py
python scripts/validate_clean_room.py
```

The final command additionally validates the synthetic implementation report and evidence manifest fixtures, verifies evidence checksums, confirms that evaluated requirements belong to the Foundation Profile, and prevents repository-controlled evidence from being misclassified as independent or accepted candidate-readiness evidence.

## Evidence produced

- `implementation-reports/fixtures/clean-room-implementation-report.json`
- `implementation-reports/fixtures/clean-room-evidence-manifest.json`

The report intentionally evaluates only the bounded starter requirement actually evidenced by the included authority artifact. It does **not** claim complete Foundation Profile coverage.

## What success means

A PASS means:

1. the published starter package is structurally consumable;
2. a published conformance claim can be validated;
3. the published behavioural vectors can be run through the reference adapter;
4. the published implementation-report and evidence-manifest contracts can represent the resulting bounded evidence; and
5. the evidence boundary remains machine-verifiable as `synthetic: true`, `independence.classification: self`, and a non-`accepted` report state.

A PASS therefore proves the **entry path**, not external implementation maturity.

## What would falsify clean-room implementability

The exercise must fail or produce a follow-up defect if any required step depends on:

- an unpublished schema, fixture, command or configuration;
- maintainer-only transformation or undocumented local state;
- an evidence reference whose bytes cannot be verified;
- a report state that could accidentally contribute to independent implementation readiness; or
- a requirement/profile relationship that cannot be derived from the published profile manifest.

## External implementation hand-off

An actual external implementer should replace the synthetic starter implementation with its own code and evidence, expand `requirementsEvaluated` to the requirements actually assessed, disclose assessor relationships, and follow the lifecycle in [Implementation Reports](../implementation-reports/). Only a non-synthetic report that reaches governed `accepted` state can contribute to candidate readiness; independent implementation additionally requires an independent assessor and disclosed relationships.

The clean-room exercise is therefore intentionally useful but non-authoritative: it reduces adoption friction without manufacturing the external evidence GAAM still lacks.
