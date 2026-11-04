---
title: "Delegated Agent Purchasing"
permalink: /examples/delegated-agent-purchase/
parent: "Implementation Patterns"
nav_order: 10
artifact_type: Informative implementation pattern
normative_status: Informative
---
# Delegated Agent Purchasing
This assurance-ready implementation pattern demonstrates **bounded agent purchasing** using GAAM v0.9.0. It is informative and does not alter normative requirements or conformance semantics.

## Governance objective

The pattern makes authority, policy, runtime enforcement, evidence, assurance, lifecycle, review and remedy separately inspectable.

## Actors

- principal
- delegated agent
- agent operator
- merchant
- policy decision point
- policy enforcement point
- transaction system
- assurance provider
- review authority
- affected principal

## Included documentation

- [Architecture and Trust Boundaries](architecture.md)
- [Authority and Delegation Model](authority-model.md)
- [Runtime Decision Sequence](sequence.md)
- [Evidence and Assurance Model](evidence-model.md)
- [Lifecycle and Revocation](lifecycle-and-revocation.md)
- [Notice, Review, and Remedy](notice-review-remedy.md)
- [Privacy and Security Analysis](privacy-security-analysis.md)
- [Affected-Party Analysis](affected-party-analysis.md)
- [Requirement Mapping](requirement-mapping.md)
- [Adopter Gateway Evaluation Exercise](adopter-gateway-exercise.md) — executable composed decision with explicit E1 limitations

## Validation

Run `python scripts/validate.py` from the repository root. See `pattern.json` for exact artifact, fixture, behavioural-vector and requirement references.

## Conformance boundary

The included claim is self-assessed implementation evidence. It is not an L4 independent assessment and does not establish interoperability testing.
