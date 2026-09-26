---
title: "Maturity and Evidence Dashboard"
permalink: /governance/candidate-readiness/
parent: Assurance and Governance Tracking
artifact_type: "Generated governance view"
normative_status: "Informative"
grand_parent: Documentation
nav_order: 2
---
# Maturity and Evidence Dashboard

{% include gaam-meta.html %}

> **Generated view.** Do not edit by hand. Run `python scripts/build_candidate_readiness.py`.

GAAM tracks **specification maturity** separately from **external evidence maturity**. Missing evidence controlled exclusively by independent actors does not become a veto over specification development; it remains an explicit unproven evidence claim. External evidence can still falsify assumptions and trigger governed reassessment.

## Current decision state

**Eligible for a Stable specification release decision:** **YES**  
**Specification blockers:** 0  
**External evidence maturity:** **E1**  
**Accepted independent implementation reports:** 0

A Stable/E1 state asserts specification stability and repository validation only. It does **not** assert independent implementation, independent assurance, interoperability, operational fitness, certification, or deployment validation.

## Gate classification

| Gate | State | Control boundary | Blocks Stable | Evidence level | Proposition |
|---|---|---|---:|---|---|
| Two independent implementations | Not started | external | No | E2 | E2 independent implementation evidence |
| Foundation implementation coverage | Not started | external | No | E2 | E2 independent Foundation Profile implementation coverage |
| Composed-profile implementation coverage | Not started | external | No | E2 | E2 independent composed-profile implementation coverage |
| Requirement testability disposition | Complete | repository-controlled | Yes | E1 | Normative requirements are deterministically indexed and testable |
| Canonical identifier publication | Complete | repository-controlled | Yes | E1 | Canonical/versioned normative identifiers are stable and publication-bound |
| Independent privacy review | Not started | shared | No | E2 | Independent privacy attestation at E2; repository preparation and disposition remain maintainer-controlled |
| Independent security review | Not started | shared | No | E2 | Independent security attestation at E2; repository threat analysis and disposition remain maintainer-controlled |
| Independent affected-party review | Not started | shared | No | E2 | Independent affected-party/redress attestation at E2; repository preparation and disposition remain maintainer-controlled |
| Cross-implementation interoperability | Not started | external | No | E3 | E3 cross-implementation interoperability evidence |
| Governed ecosystem applicability | In progress | shared | No | E2 | Independent applicability evidence for the declared ecosystem boundary |
| Repository-controlled candidate issue disposition | Complete | repository-controlled | Yes | E1 | All repository-controlled candidate findings that affect the Stable claim have governed disposition |

## Specification blockers

No repository-controlled Stable blocker is currently open.

## Evidence boundary

Synthetic, self-assessed, maintainer-authored and repository-owned fixtures never satisfy independent E2/E3 claims. Independent implementation and review evidence advances E2; cross-implementation evidence advances E3. Missing external evidence leaves those claims unproven rather than making the specification unstable.

## Reassessment rule

If external implementation, review or interoperability evidence exposes a material ambiguity, security/privacy defect, semantic divergence or invalid normative assumption, that finding enters the governed change lifecycle and may invalidate Stable readiness until disposition and reassessment complete.
