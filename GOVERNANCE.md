---
title: "Project Governance"
permalink: /governance/
nav_order: 13
has_children: true
artifact_type: "Repository governance"
normative_status: "Normative process"
---
# Project Governance

{% include gaam-meta.html %}

## Purpose

This document governs development of the GAAM specification and supporting materials. It does not govern implementations or ecosystems that use GAAM.

## Repository authority and status

`PROJECT-STATUS.yaml` is the repository-local declaration of GAAM maturity, lifecycle, operational status, specification status, normative scope, validation evidence and known limitations. Portfolio or downstream systems may consume this declaration but do not acquire authority to rewrite GAAM-owned status.

GAAM owns the normative specification, first-party profiles, canonical schemas, governed vocabularies and conformance rules published by this repository. It does not govern downstream implementations, external ecosystems, or specifications that are merely mapped, referenced or aligned.

Status and normative-change authority may be exercised only within the roles and change classes defined here. Superseding or withdrawing a published GAAM artifact must preserve reconstructable history and must not erase prior evidence or dispositions.

## Roles

- **Maintainers** manage releases, repositories, review queues and editorial consistency.
- **Editors** prepare specification text and resolve accepted issues.
- **Contributors** submit issues, reviews, examples and pull requests.
- **Implementers** provide conformance and interoperability evidence.

One person may hold multiple roles, but approvals should disclose relevant conflicts of interest.

## Decision model

The project seeks reasoned consensus. Consensus means that material objections have been considered and documented; it does not require unanimity. Maintainers may merge editorial changes directly. Normative changes require public review and a recorded disposition.

## Change classes

- **Editorial:** no intended semantic change.
- **Clarifying:** resolves ambiguity without changing intended conformance.
- **Normative:** changes requirements, definitions, relationships or conformance.
- **Architectural:** adds, removes or materially reorganises a metamodel concept or profile.

## Release policy

Pre-1.0 minor releases may introduce normative changes. Patch releases are reserved for editorial corrections and defects that do not intentionally expand scope. Release notes must identify breaking or conformance-affecting changes.

## Appeals

A contributor may request reconsideration by opening a governance issue that states the disputed decision, unaddressed evidence and proposed remedy. The final disposition must be documented.
## v0.9.0 change control

Normative, schema, profile and conformance changes require an identified authority, traceability impact, validation evidence and maintainer approval. Revocation or supersession of published artifacts must preserve reconstructable history.
