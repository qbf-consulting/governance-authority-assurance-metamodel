---
title: Assurance Composition and Dependency
permalink: /docs/future-evolution/concepts/assurance-composition-and-dependency/
nav_exclude: true
artifact_type: Candidate future concept
normative_status: Informative
---
# Assurance Composition and Dependency

{% include gaam-meta.html %}

> This is an informative candidate concept for evaluation. It does not modify GAAM v0.9.0 requirements, schemas, profiles, vocabularies, or conformance semantics.

Assurance should identify its object, method, scope, depth, independence, competence, sampling, validity period, limitations, surveillance, and withdrawal conditions. Future systems need rules for inheritance, composition, supplementation, restriction, invalidation, and downgrade.

Assured components do not automatically produce an assured system, and a qualified provider does not make every output qualified.

## Evaluation questions

- Can the current GAAM model represent the concept without ambiguous interpretation?
- Do multiple implementation patterns require the same semantics?
- Is a draft profile, experimental schema, vocabulary, or behavioural vector necessary?
- What privacy, security, affected-party, market, and continuity consequences arise?
- What evidence would justify normative promotion?

## Temporal composition

A set of individually qualified claims cannot automatically become a qualified composite decision when their competent recording cutoffs, governing policy versions or historical coverage are incompatible. A relevant [experimental scenario](../../../experimental/temporal-governance/README.md) tests this non-amplification boundary. Compatible timestamps are necessary in some domains but not sufficient for actual authority or independent assurance; the governing composition policy remains material.
