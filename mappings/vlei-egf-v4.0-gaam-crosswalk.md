---
title: "vLEI EGF v4.0 GAAM Readiness Crosswalk"
permalink: /mappings/vlei-egf-v4.0/
parent: "Mappings and Source Crosswalks"
grand_parent: "Appendices"
nav_order: 5
artifact_type: "Informative ecosystem readiness crosswalk"
normative_status: "Informative"
---
# vLEI EGF v4.0 GAAM Readiness Crosswalk

{% include gaam-meta.html %}

> This is an informative GAAM application exercise. It is not a GLEIF or QVI qualification assessment, formal audit or GAAM conformance claim.

## Target

- **Target:** GLEIF vLEI Ecosystem Governance Framework
- **Assessed version:** 4.0
- **Assessment date:** 2026-08-10
- **Machine-readable record:** [`vlei-egf-v4.0-gaam-crosswalk.json`](vlei-egf-v4.0-gaam-crosswalk.json)
- **Method:** [Ecosystem Assessment Method](ecosystem-assessment-method.md)

## Executive finding

The vLEI ecosystem already implements substantial executable governance. Identity, organizational role, issuer qualification, authorization, delegation, credential lifecycle and cryptographic state are meaningfully separated. The strongest GAAM opportunities occur at the **reliance boundary**: how far an artifact's authority extends, how assurance composes, how upstream revocation propagates and who remains accountable for downstream effects.

## Actionable findings

### GAAM-VLEI-01 — Credential authority is not unlimited transaction authority

**Readiness:** `partial`

A vLEI artifact may establish organizational identity, role or credential-governance authority without authorizing every transaction associated with that role.

**Action:** downstream systems must evaluate effect-specific authority unless the artifact explicitly establishes it.

### GAAM-VLEI-02 — Authorization vLEI as a delegated-authority reference pattern

**Readiness:** `covered`

Authorization credentials and delegated identifiers provide a strong implementation case for GAAM delegation source, scope, activation, lineage and revocation requirements.

**Action:** use this model as a GAAM reference benchmark rather than merely an illustrative example.

### GAAM-VLEI-03 — Preserve role semantics downstream

**Readiness:** `partial`

Official Organizational Role and Engagement Context Role relationships are meaningfully typed, but a downstream verifier can still broaden their meaning.

**Action:** publish explicit `establishes` and `does-not-establish` semantics for each relationship class.

### GAAM-VLEI-04 — Revocation propagation across delegation lineage

**Readiness:** `partial`

Different changes to qualification, delegated identifiers, authorization credentials and role credentials can have different descendant effects.

**Action:** model dependency classes and explicit propagation rules rather than applying one global revocation assumption.

### GAAM-VLEI-05 — Assurance composition is a strong reference case

**Readiness:** `covered`

The Trust Assurance Framework provides differentiated governance, qualification, certification and software assurance mechanisms.

**Action:** use vLEI to test GAAM's requirement that every assurance form state what it establishes, its limitations and how it may compose.

### GAAM-VLEI-06 — Assurance blind spots should remain explicit

**Readiness:** `covered`

The framework usefully exposes areas outside the direct assurance perimeter.

**Action:** GAAM should support bounded states such as assessed, externally assured, self-attested, unobserved and unknown rather than forcing binary trust conclusions.

### GAAM-VLEI-07 — Periodic versus continuous assurance

**Readiness:** `partial`

Recurring qualification and operational evidence are strong inputs but should remain distinct from explicit event-driven continuous governance assurance.

**Action:** define monitoring frequency, evidence freshness, drift, trigger, escalation and suspension semantics per control.

### GAAM-VLEI-08 — Resolve institutional authority provenance

**Readiness:** `partial`

Technical and credential authority can be highly machine-verifiable while higher institutional authority remains documentary.

**Action:** require resolvable provenance from technical authority through ecosystem governance to the institutional authority source without requiring constitutional governance to become executable code.

### GAAM-VLEI-09 — Reliance semantics

**Readiness:** `partial`

Validity, provenance, role and qualification do not automatically answer what a relying application may conclude.

**Action:** define positive and negative reliance semantics for governed artifact and relationship classes.

### GAAM-VLEI-10 — Correction is not downstream remedy

**Readiness:** `partial`

Correcting or revoking trust data fixes future reliance state but may not repair effects that already occurred.

**Action:** represent challenge, correction and consequential remedy as related but distinct lifecycle stages.

### GAAM-VLEI-11 — Accountability across the reliance boundary

**Readiness:** `partial`

A valid vLEI credential can be interpreted too broadly by an external application.

**Action:** keep issuer responsibility, holder authority and relying-party decision accountability explicitly separated.

### GAAM-VLEI-12 — Machine-actionable reference crosswalk

**Readiness:** `covered`

The ecosystem's structured governance, roles, schemas, delegation, lifecycle and assurance evidence make it suitable for a reproducible GAAM benchmark.

**Action:** use the vLEI mapping to validate GAAM crosswalk methodology against an ecosystem that already has significant executable governance.

## Reusable GAAM takeaway

The vLEI case demonstrates that GAAM must add value even where governance is already mature. Its strongest contribution is to make **authority boundaries, assurance boundaries and reliance boundaries between governed ecosystems** explicit enough to test and compose safely.
