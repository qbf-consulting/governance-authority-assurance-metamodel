---
title: "Basic Governed Decision"
nav_exclude: true
search_exclude: true
published: false
artifact_type: Informative implementation pattern
normative_status: Informative
---
# Basic Governed Decision

This pattern demonstrates **governed decision evaluation** using GAAM concepts and existing candidate profiles. It is informative: identifiers, policies, actors and evidence are illustrative and do not establish conformance for a production deployment.

## Governance problem

The implementation must make authority, accountability, lifecycle state, enforcement, evidence, review and remedy independently inspectable. A successful technical action is not sufficient evidence that the action was legitimate.

## Actors

- policy authority
- decision service
- enforcement point
- review authority
- affected party

## Pattern flow

1. Resolve the governing source and accountable authority.
2. Verify current lifecycle and assurance state.
3. evaluate the requested effect against scope and constraints.
4. enforce permit, deny or indeterminate outcomes.
5. emit attributable evidence and preserve review linkage.
6. propagate suspension, revocation, correction and remedy downstream.

## Included guidance

- [Architecture and Trust Boundaries](architecture.md)
- [Authority Model](authority-model.md)
- [Lifecycle and Revocation](lifecycle-and-revocation.md)
- [End-to-end walkthrough](walkthrough.md)
- [Runtime Sequence](runtime-sequence.md)
- [Evidence and Assurance Model](evidence-model.md)
- [Notice, Review, and Remedy](notice-review-remedy.md)
- [Privacy, Security, and Affected-Party Analysis](privacy-security-analysis.md)
- [Requirement Mapping](requirement-mapping.md)

## Limitations

This pattern does not prescribe a credential format, identifier method, policy engine, contractual form or jurisdiction-specific control. Independent implementation and interoperability evidence are not claimed.
