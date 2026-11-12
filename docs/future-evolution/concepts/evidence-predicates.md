---
title: Evidence Predicates
permalink: /docs/future-evolution/concepts/evidence-predicates/
nav_exclude: true
artifact_type: Candidate future concept
normative_status: Informative
---
# Evidence Predicates

{% include gaam-meta.html %}

> This is an informative candidate concept for evaluation. It does not modify GAAM v0.9.0 requirements, schemas, profiles, vocabularies, or conformance semantics.

A signed or registered assertion may be authentic yet irrelevant, stale, incomplete, methodologically weak, or impermissible for the intended purpose. Candidate evidence predicates include authenticity, integrity, provenance, validity, freshness, relevance, producer competence, independence, completeness, consistency, sufficiency, permitted use, and contestability.

Systems should avoid collapsing these predicates into one undifferentiated `verified` result.

## Evaluation questions

- Can the current GAAM model represent the concept without ambiguous interpretation?
- Do multiple implementation patterns require the same semantics?
- Is a draft profile, experimental schema, vocabulary, or behavioural vector necessary?
- What privacy, security, affected-party, market, and continuity consequences arise?
- What evidence would justify normative promotion?

## Temporal evidence qualification

The [temporal governance model](temporal-governance.md) distinguishes the effective applicability of evidence from authoritative recording, collection and later reconstruction. In this research interpretation, validity and authenticity of the evidence object do not by themselves establish when its competent source recorded it. Completeness of the relevant historical source window is a separate predicate; absent source history must not become an authoritative negative. Mixed recording cutoffs require governed composition rather than an undifferentiated `verified` label. These are informative candidate constraints, not new v0.9.0 requirements.
