---
title: "Pilot GAAM"
permalink: /pilots/
parent: Implement
nav_order: 6
has_children: true
artifact_type: Informative pilot adoption guide
normative_status: Informative
---
# Pilot GAAM

This is a **zero-to-pilot route** for a team wishing to apply GAAM v0.9.2 to a bounded governance problem. It is based on the participant-oriented, evidence-gated approach used in the [UN/CEFACT GRID Pilots](https://grid.unece.org/docs/draft/Pilots/), adapted to GAAM's protocol-neutral metamodel rather than GRID's infrastructure-specific implementation. These pilot gates are **informative operational controls**, not GAAM normative requirements, conformance levels, certification, or an alternative specification.

A pilot tests a proposition: can an independently governed implementation identify the authority for a proposed effect, enforce a contextual decision, handle revoked or stale authority and missing evidence, and preserve reconstructable accountability? Completing a synthetic repository dry run establishes only that GAAM's **published onboarding and tool entry path** can be exercised. A real independent implementation must produce separate, attributable external evidence.

## Use this sequence

1. [Pilot Design and Boundaries](design.md): decide what remains under institutional, operator, implementer and assessor authority.
2. [Pilot Charter](charter.md): define hypothesis, parties, governed effect, applicable baseline, exclusions, success and stop rules before implementation.
3. [Participant Guide](participant-guide.md): work from G0 to G6; do not skip unknown prerequisites.
4. [Pilot Tests and Evidence](test-and-evidence.md): run published tooling, examine adverse cases, and assemble the actual evidence.
5. [Pilot Gate Catalogue](gates.json): machine-readable descriptions of owners, outcomes, required artifacts and stop conditions.

**First runnable result:** from a fresh checkout, install `requirements-dev.txt` and execute `python scripts/validate_pilot_readiness.py --run`. This runs a bounded repository-owned dry run and explicit negative tests; it does not certify or mark participant gates as passed.

## Completion thresholds

**Pilot implementation demonstrated:** G0–G5 are passed with real, attributable evidence belonging to the participant's declared scope and implementation. **Pilot closed:** G6 records findings, residual risks, and an accountable decision to continue, expand, terminate or remediate. A completed G6 does not imply production readiness. A participant who cannot meet a gate records **blocked**, **failed** or **not-assessed**, with the missing evidence and accountable next action. No passage is inferred from a green CI badge.

The [existing conformance guide](../docs/conformance-guide.md), [implementation-report intake](../implementation-reports/README.md), [Foundation Profile](../profiles/foundation-profile.md), and [Basic Governed Decision walkthrough](../examples/basic-governed-decision/walkthrough.md) remain the authoritative resources for their respective contracts. Pilot examples do not amend them.

## What participation does not prove

This guide does not award L2–L4 assurance, establish E2 independent implementation, E3 interoperability or authorize production. GAAM represents authority; it does not create the underlying lawful or institutional competence. No registry listing, signed artifact, test-vector pass, or pilot gate status should be interpreted as such competence without evidence and independent judgment.
