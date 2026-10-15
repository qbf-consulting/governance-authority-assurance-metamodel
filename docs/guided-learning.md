---
layout: default
title: Guided Learning Paths
permalink: /docs/guided-learning/
parent: Orientation
nav_order: 1
has_toc: true
grand_parent: Start Here
---
# Guided Learning Paths

GAAM is a concept-to-conformance specification. Readers should first understand the semantic model, then select a profile, implement machine-verifiable artifacts and finally produce evidence against normative requirements. Choose the route aligned to your authority and review role.

```mermaid
flowchart LR
  A[Governance intent] --> B[Authority and delegation model]
  B --> C[Applicable profile]
  C --> D[Machine-verifiable artifacts]
  D --> E[Runtime enforcement]
  E --> F[Evidence and conformance]
  F --> G[Assurance and accountable decision]
```

## Route 1: policy owner or governance designer

1. [Design principles](design-principles.md)
2. [Architecture overview](architecture-overview.md)
3. [Lifecycle model](lifecycle-model.md)
4. [Architecture diagrams](../diagrams/architecture-diagrams.md)
5. [Implementation patterns](../examples/index.md)

**Completion test:** you can identify the source of authority, delegation scope, enforcement and revocation mechanisms, evidence obligations and accountable assurance decision.

## Route 2: architect, profile author or implementer

1. [Normative specification](../specification/index.md)
2. [Foundation profile](../profiles/foundation-profile.md)
3. [Implementation guide](implementation-guide.md)
4. [Canonical schemas](../schemas/index.md)
5. [Controlled vocabularies](../vocabularies/index.md)
6. [Conformance and assurance](../conformance/index.md)

**Completion test:** each implemented governance claim maps to a normative requirement, canonical structure, enforcement behaviour and testable evidence item.

## Route 3: reviewer, auditor or assurance body

1. [Reviewer guide](reviewer-guide.md)
2. [Normative requirements index](../matrices/normative-requirements-index.md)
3. [Requirement-test coverage](../matrices/requirement-test-coverage.md)
4. [Threat and misuse-case model](../threat-model/README.md)
5. [Threat-control-test matrix](../matrices/threat-control-test-matrix.md)
6. [Conformance matrix](../matrices/conformance-matrix.md)

**Completion test:** the review can reproduce the applicable requirement set, inspect test coverage, locate evidence, identify exceptions and record an accountable disposition.

## Normative reading rule

Informative guidance explains how to apply GAAM but does not replace the normative specification, profiles, schemas or conformance requirements. Record the exact version and profile used whenever making a conformance or assurance claim.

[Continue to the documentation architecture →](documentation-architecture.md)

## Foundational-to-ecosystem pattern path

1. [Basic Governed Decision](../examples/basic-governed-decision/)
2. [Authority Lifecycle and Revocation](../examples/authority-lifecycle-and-revocation/)
3. [Independent Assurance Assessment](../examples/independent-assurance-assessment/)
4. [Notice, Challenge, and Remedy](../examples/notice-challenge-and-remedy/)
5. [Machine-Actionable Governance Package](../examples/machine-actionable-governance-package/)
6. [Delegated Agent Purchasing](../examples/delegated-agent-purchase/)
7. [Cross-Registry Recognition](../examples/cross-registry-recognition/)
8. [High-Impact Multi-Agent Service](../examples/high-impact-multi-agent-service/)
9. [Governed Ecosystem Operations](../examples/governed-ecosystem-operations/)
