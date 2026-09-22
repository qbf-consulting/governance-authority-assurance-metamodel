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

Each crosswalk declares a **case role** so complementary ecosystems can be compared without collapsing them into one architecture. The current benchmark roles are:

- `explicit-authority-benchmark` — authority, delegation or assurance are already represented comparatively explicitly and the primary GAAM test is whether scope, dependency and reliance boundaries remain machine-testable; and
- `distributed-authority-benchmark` — authority is validly distributed across multiple legal, institutional, registry, certification or protocol sources and the primary GAAM test is whether it can still be deterministically resolved.

Each finding must identify:

1. the external target and version;
2. the applicable GAAM requirements;
3. the observed governance condition and bounded readiness status;
4. authority sources, governed actors, relationships and effects;
5. enforcement, revocation and assurance mechanisms where applicable;
6. what the mapped artifact or relationship **establishes**;
7. what it **does not establish**;
8. an actionable takeaway;
9. expected evidence;
10. candidate positive, negative or boundary tests; and
11. known limitations.

The machine-readable contract is [`ecosystem-crosswalk.schema.json`](ecosystem-crosswalk.schema.json), currently schema version **1.1**. The richer fields are intended to make validation cases test-generating and dependency-aware, not to create a parallel conformance model.

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

## Promotion boundary

Crosswalk findings are hypotheses and implementation-validation evidence inputs. They MUST NOT become new normative GAAM requirements merely because the same concern appears in more than one ecosystem.

A normative change requires the existing GAAM change-control path: requirement analysis, compatibility or breaking-change classification, attributable decision authority, tests, migration consequences where applicable, and the version effect required by the Candidate Stability and Change-Control Policy.

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


## Complementary benchmark sequence

For the current paired validation cases, the recommended sequence is:

1. use the **vLEI EGF v4.0** case to test explicit delegation, authority lineage, assurance scope, reliance boundaries and dependency-aware revocation;
2. use the **EUDI Wallet ARF v3.0.0** case to test distributed authority resolution, precedence, registry semantics, multi-party assurance and runtime accountability;
3. compare failures and ambiguities across both cases;
4. derive executable tests or implementation evidence where practical; and
5. raise a GAAM normative change only when evidence demonstrates that the existing normative model is insufficient.

This ordering is methodological rather than a ranking of the external ecosystems.
