---
title: Continuity, Caching, and Revocation Propagation
permalink: /docs/future-evolution/concepts/continuity-caching-and-revocation/
nav_exclude: true
artifact_type: Candidate future concept
normative_status: Informative
---
# Continuity, Caching, and Revocation Propagation

{% include gaam-meta.html %}

> This is an informative candidate concept for evaluation. It does not modify GAAM v0.9.0 requirements, schemas, profiles, vocabularies, or conformance semantics.

Authority withdrawal may cross registries, federated copies, caches, policy engines, orchestration layers, and ongoing effects. Each boundary introduces a revocation lag gradient. Candidate semantics should cover authoritative sources, replicas, maximum staleness, consistency levels, offline verification, partition behaviour, negative caching, recovery, and historical-state queries.

Controlled degradation states may include read-only, no-new-issuance, status-only, emergency-revocation-only, supervised fallback, continuity transfer, and safe shutdown.

## Evaluation questions

- Can the current GAAM model represent the concept without ambiguous interpretation?
- Do multiple implementation patterns require the same semantics?
- Is a draft profile, experimental schema, vocabulary, or behavioural vector necessary?
- What privacy, security, affected-party, market, and continuity consequences arise?
- What evidence would justify normative promotion?

## Temporal boundary

Source effective time, competent recording time, replica observation and actual enforcement are different predicates. A complete as-known-at reconstruction does not prove revocation propagation or enforcement convergence; a bounded-delay claim needs independently supported timing and acknowledgement evidence. The [temporal governance model](temporal-governance.md) preserves this distinction without prescribing a particular cache, replication or event mechanism.
