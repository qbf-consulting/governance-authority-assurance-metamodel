---
title: "Conformance and Assurance Guide"
permalink: /docs/conformance/
parent: Assurance and Governance Tracking
grand_parent: Test & Assure
nav_order: 1
---
# Conformance and Assurance Guide

GAAM conformance applies to declared targets and profiles. It does not certify universal trustworthiness.

| Level | Evidence meaning |
|---|---|
| L0 — Documented | Required governance statements and artifacts exist |
| L1 — Structurally Valid | Machine-readable artifacts validate against GAAM schemas |
| L2 — Behaviourally Tested | Required lifecycle and governance invariants pass |
| L3 — Evidence Supported | Claims have traceable execution or assessment evidence |
| L4 — Independently Assessed | An independent party assessed the declared scope |

## Claim requirements

A claim identifies GAAM version, profiles, target, evidence level, evidence references, issuer, issue time and limitations. Profile dependency closure is mandatory. Partial implementations must not claim full profile conformance.

## Validation layers

1. Repository and publication integrity.
2. Normative requirement traceability.
3. Schema and fixture validation.
4. Governance invariants and lifecycle behaviour.
5. Profile composition and evidence completeness.


## Candidate assurance-level rules

| Level | Meaning | Minimum evidence | Independence |
|---|---|---|---|
| L0 | Documented | Declared target, profiles and limitations | Self-asserted permitted |
| L1 | Structurally Valid | Passing schemas, vocabularies and package checks | Self-asserted permitted |
| L2 | Behaviourally Tested | Passing applicable invariant and scenario tests | Self-asserted permitted with disclosure |
| L3 | Evidence Supported | Operational evidence, traceable receipts and lifecycle records | Assessor relationship disclosed |
| L4 | Independently Assessed | Independent assessment report, scope, method, exceptions and validity period | Independent assessor required |

A claim MUST NOT exceed the lowest level supported by its evidence. L4 MUST NOT be issued by the implementation operator or an entity under its control.
