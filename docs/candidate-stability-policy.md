---
title: "Candidate Stability and Change-Control Policy"
permalink: /governance/candidate-stability/
parent: Project & Evolution
artifact_type: "Governance policy"
normative_status: "Normative process"
nav_order: 5
---
# Candidate Stability and Change-Control Policy

{% include gaam-meta.html %}

## Status

This policy governs GAAM v0.9.x. Candidate status freezes requirement identifiers, profile identifiers and canonical schema identifiers except where a documented defect makes preservation unsafe or materially misleading.

## Specification edition and distribution governance

The current specification **edition** is declared by the authoritative document and `release.json.specificationEdition`; the distribution release is in `VERSION` and `release.json.version`. Legacy `normativeVersion` and `candidateBaseline` denote the Candidate **release** rather than the edition printed in the specification. These public fields remain compatible.

Distribution-only releases do not create a new normative edition. A revised normative document requires an approved distinct edition and retained historical permalink, with separate semantic, identifier, assurance and compatibility disposition. Never renumber frozen schema `$id` or profile identifiers merely to match the distribution release. The stable `/specification/` index MUST identify the current specification edition and distribution separately.

## Change classes

| Class | Effect | Required evidence | Version effect |
|---|---|---|---|
| Editorial | No semantic effect | Link and publication validation | Patch |
| Clarification | Narrows ambiguity without changing conforming behaviour | Requirement analysis and tests | Patch |
| Compatible extension | Adds optional vocabulary, schema or profile capability | Compatibility fixtures and migration note | Minor candidate |
| Breaking normative change | Invalidates previously conforming behaviour or changes authority | ADR, threat analysis, tests, migration plan and maintainer approval | New candidate or v1 decision |
| Security correction | Prevents unsafe or misleading conformance | Security analysis, revocation/errata notice and tests | Patch or expedited candidate |

## Authority and approval

Maintainers approve editorial and clarification changes. Breaking normative changes require an accepted ADR and explicit release decision. Every proposal MUST identify affected requirements, profiles, schemas, evidence, tests and migration consequences.

## Revocation and errata

A published artifact MAY be marked superseded or withdrawn when it creates an unsafe interpretation. Historical content remains available with machine-readable status and replacement references.

## v1.0.0 exit criteria

GAAM advances to v1.0.0 only after two independent implementation reports cover the Foundation Profile and at least one composed profile; no unresolved critical security issue remains; all normative requirements have dispositioned testability; canonical identifiers are demonstrated in publication; and the candidate review record contains no unresolved breaking issue.
