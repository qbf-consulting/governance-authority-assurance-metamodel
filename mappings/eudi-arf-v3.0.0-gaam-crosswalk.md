---
title: "EUDI Wallet ARF v3.0.0 GAAM Readiness Crosswalk"
permalink: /mappings/eudi-arf-v3.0.0/
parent: "Mappings and Source Crosswalks"
grand_parent: "Appendices"
nav_order: 4
artifact_type: "Informative ecosystem readiness crosswalk"
normative_status: "Informative"
---
# EUDI Wallet ARF v3.0.0 GAAM Readiness Crosswalk

{% include gaam-meta.html %}

> This is an informative GAAM application exercise. It is not an EUDI compliance assessment, certification, formal audit or GAAM conformance claim.

## Target

- **Target:** EU Digital Identity Wallet Architecture and Reference Framework
- **Assessed version:** 3.0.0
- **Assessment date:** 2026-08-10
- **Machine-readable record:** [`eudi-arf-v3.0.0-gaam-crosswalk.json`](eudi-arf-v3.0.0-gaam-crosswalk.json)
- **Method:** [Ecosystem Assessment Method](ecosystem-assessment-method.md)

## Executive finding

The EUDI Wallet architecture contains substantial governance, protocol, lifecycle, certification, registration and assurance machinery. The principal GAAM opportunity is to make the chain from **authority source → bounded authority → runtime decision → consequential effect → evidence → accountability → challenge/remedy** more explicit and machine-testable across organizational boundaries.

## Actionable findings

### GAAM-ARF-01 — Action-level authority

**Readiness:** `partial`

Authority is often inferred from combinations of role, registration, certification, trusted-list state and protocol rules. GAAM suggests a resolvable authority record for consequential effects that binds source, actor, action, subject or resource, scope, constraints, validity and revocation state.

**Testable outcome:** a technically valid identity or credential must fail when the requested effect is outside the actor's current authority.

### GAAM-ARF-02 — Role-to-authority resolution

**Readiness:** `partial`

Role definitions and operative authority can be distributed across legal, regulatory, certification and technical sources.

**Action:** publish a role-to-authority register with source, effect, constraint, jurisdiction and lifecycle semantics.

### GAAM-ARF-03 — Authority conflict and precedence

**Readiness:** `partial`

Overlapping authority sources require explicit precedence, coordination, refusal or escalation rules.

**Testable outcome:** the system must not silently choose an authority when two applicable sources conflict and no precedence rule exists.

### GAAM-ARF-04 — Runtime governance envelope

**Readiness:** `partial`

Protocol validation is strong, but a common runtime governance envelope could improve reconstructability of consequential decisions while preserving data minimisation.

**Action:** record resolvable policy, authority, evidence, constraint, outcome and timing references rather than unnecessary transaction content.

### GAAM-ARF-05 — Decision receipts

**Readiness:** `gap`

A general privacy-preserving receipt connecting a material decision to its governance basis is not systemic.

**Action:** prototype bounded receipts that support audit and challenge without creating cross-context correlation identifiers.

### GAAM-ARF-06 — Revocation dependency propagation

**Readiness:** `partial`

Status and revocation mechanisms exist, but downstream consequences are not represented through one explicit dependency model.

**Action:** attach propagation semantics to authority, certification, registration and recognition dependencies.

### GAAM-ARF-07 — Registry semantics

**Readiness:** `partial`

Trusted Lists, LoTEs, relying-party registers and other authoritative directories encode different kinds of recognition and reliance.

**Action:** publish typed semantics stating what inclusion establishes, what it does not establish, accepted purposes, assurance thresholds and withdrawal conditions.

### GAAM-ARF-08 — Assurance composition

**Readiness:** `partial`

Certification, functional conformance, security and interoperability assurance establish different claims.

**Action:** define positive scope, limitations and composition rules so one assurance form cannot silently satisfy another claim class.

### GAAM-ARF-09 — Continuous governance assurance

**Readiness:** `partial`

Lifecycle controls and continuing obligations are strong inputs, but changing governance relationships, evidence freshness and blind spots should be represented as current assurance state.

### GAAM-ARF-10 — Multi-party accountability

**Readiness:** `partial`

A consequential interaction can depend on several actors and evidence sources.

**Action:** preserve accountable decision and evidence lineage without collapsing responsibility into a generic ecosystem actor.

### GAAM-ARF-11 — Challenge and remedy lifecycle

**Readiness:** `partial`

Legal and institutional remedies exist, but the technical decision-to-challenge-to-correction-to-remedy path is not represented as one common lifecycle.

### GAAM-ARF-12 — Systemic effect observability

**Readiness:** `partial`

Component conformance does not by itself demonstrate acceptable combined outcomes.

**Action:** high-impact deployments should define measurable effect classes, affected-party indicators and escalation thresholds.

### GAAM-ARF-13 — Machine-actionable governance package

**Readiness:** `partial`

Substantial machine-readable infrastructure exists, but authority, registry semantics, assurance scope, dependencies and remedy do not yet form one interoperable governance package.

**Action:** prototype a package containing authority, governance-source, registry-semantics, assurance and dependency registers plus runtime and remedy evidence profiles.

## Reusable GAAM takeaway

The EUDI case demonstrates that mature technical and regulatory governance can still leave **cross-boundary authority semantics** implicit. GAAM's value is not to replace the governing framework, but to make authority, reliance, assurance and remedy boundaries explicit enough to validate.
