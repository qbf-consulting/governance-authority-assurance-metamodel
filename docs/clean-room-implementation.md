---
title: "Clean-Room Implementation Exercise"
permalink: /clean-room-implementation/
artifact_type: "Implementation guidance"
normative_status: "Informative"
parent: Implement
nav_order: 5
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
python scripts/gaam.py run-vectors --pattern 'delegation-*.json' python conformance-kit/reference_adapter.py
python scripts/gaam.py run-vectors --suite v2 python conformance-kit/reference_adapter.py
python scripts/validate_clean_room.py
```

The final command additionally validates the synthetic report and evidence manifest, checks referenced bytes and Foundation membership, and rejects promotion of self-assessed evidence to independent acceptance. It also exercises specified positive/negative delegation and lifecycle cases and rejects an always-deny false-success probe.

## Delegated-authority adoption probe and limitations

The enhanced exercise deliberately checks two **separate** public test interfaces:

- **Legacy delegated authority (v1):** a valid attenuated delegation must be accepted; amplification and revoked-parent delegations must be rejected. These fixtures use abstract Boolean inputs.
- **Experimental raw authority lifecycle (v2):** a schema-valid active grant must admit the requested effect; expired, revoked, not-yet-effective and out-of-scope grants must reject with the fixture's expected reason codes. The evaluation clock is fixed.
- **False-success probe:** an always-deny adapter must fail the positive v2 authority test, despite agreeing with negative cases.

Run the listed commands from a clean checkout and retain `git rev-parse HEAD` and the emitted release, normative and semantic-baseline versions. The reference starting release is **v0.9.3**; later commits on `main` may modify only informative implementation tooling.

**Non-claim:** These are two separate repository-authored adapter exercises, **not a composed delegated-agent authorization implementation**. Typed delegated-scope comparisons, authenticated originating principals, live revocation freshness, missing/conflicting external evidence, receipt authenticity, replay and actual effect execution have not been proven. A successful exercise remains synthetic, self-assessed repository evidence, not independent E2/E3 conformance. Vector `requirements` references are not independent requirement-specific tests.

## Evidence produced

- `implementation-reports/fixtures/clean-room-implementation-report.json`
- `implementation-reports/fixtures/clean-room-evidence-manifest.json`

The report intentionally evaluates only the bounded starter requirement actually evidenced by the included authority artifact. It does **not** claim complete Foundation Profile coverage.

## What success means

A PASS means:

1. the published starter package is structurally consumable;
2. a published conformance claim can be validated;
3. the published v1 delegation and experimental v2 raw-authority vectors can be run with defined positive and negative outcomes and an always-deny negative control;
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
