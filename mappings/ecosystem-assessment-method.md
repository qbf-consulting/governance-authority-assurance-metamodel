---
title: "Ecosystem Assessment Method"
permalink: /mappings/ecosystem-assessment-method/
parent: "Mappings and Source Crosswalks"
grand_parent: "Appendices"
nav_order: 3
artifact_type: "Informative assessment method"
normative_status: "Informative"
---
# Ecosystem Assessment Method

{% include gaam-meta.html %}

This method turns GAAM application reviews into reproducible, machine-readable readiness mappings without converting external frameworks into GAAM dependencies or making unsupported conformance claims.

## Assessment boundary

An ecosystem assessment **does not establish GAAM conformance**. It records whether the assessed source material appears to cover, partially cover, omit, exclude or leave unknown a GAAM concern at the architectural or governance-document level.

The allowed readiness states are:

- `covered` — the assessed source clearly represents the relevant governance semantics or control intent;
- `partial` — relevant mechanisms exist, but scope, evidence, lifecycle, interoperability or testability remains incomplete;
- `gap` — the assessment identified no adequate mechanism for the mapped concern;
- `not-applicable` — the concern is outside the declared assessment boundary; and
- `unknown` — available evidence is insufficient to reach a bounded conclusion.

These states are deliberately **not** GAAM evidence levels and must not be transformed into L0-L4 conformance claims.

## Required assessment record

Each finding should identify:

1. the external target and version;
2. the applicable GAAM requirements;
3. the observed governance condition;
4. a bounded readiness status;
5. an actionable takeaway;
6. expected evidence; and
7. candidate positive, negative or boundary tests.

The machine-readable shape is defined by [`ecosystem-crosswalk.schema.json`](ecosystem-crosswalk.schema.json).

## Interpretation rules

### Recognition is not authority

Identity, registration, qualification, certification, accreditation, registry inclusion, role and technical capability must remain semantically distinct from authority unless the governing framework explicitly establishes authority semantics for the relevant effect.

### Coverage is not implementation evidence

A requirement mapped as `covered` means the reviewed framework contains a corresponding governance mechanism. It does not prove that an implementation enforces that mechanism.

### Assurance must remain scoped

An assessment must record what each assurance mechanism establishes, what it does not establish, and any blind spots. Separate assurance mechanisms may compose only where the supported claim and dependencies are explicit.

### Revocation must follow dependencies

Where authority, qualification, registry state, credentials or assurance results depend on an upstream artifact, the assessment should identify propagation semantics rather than assume that every downstream relationship fails identically.

### Reliance needs positive and negative semantics

For externally consumed trust artifacts, a mapping should state both what a valid artifact establishes and what it **does not by itself establish**. This guards against semantic broadening by downstream relying systems.

### Correction and remedy are distinct

Correcting or revoking trust data changes future reliance state. It does not necessarily remedy consequential effects that already occurred. Ecosystem assessments should track those stages separately.

## Evidence-oriented workflow

A reusable assessment sequence is:

```text
source authority and scope
        ↓
roles and governed relationships
        ↓
authority and delegation semantics
        ↓
registry / credential / recognition semantics
        ↓
runtime decision and effect controls
        ↓
revocation and dependency propagation
        ↓
assurance scope and composition
        ↓
accountability, challenge and remedy
        ↓
expected evidence and executable tests
```

The output should be suitable for later promotion into an [Implementation Report](../implementation-reports/) only when implementation evidence exists. The crosswalk itself remains an informative source mapping.
