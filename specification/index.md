---
title: "Normative Specification"
permalink: /specification/
nav_order: 2
has_children: true
artifact_type: Specification index
normative_status: Normative
---
# Normative Specification

{% include gaam-meta.html %}

**Current specification edition:** v0.9.0  
**Current Candidate distribution and implementation kit:** v0.9.5  
**Normative semantic baseline:** v0.9.0  
**Canonical artifact identifier lineage:** v0.9.0

The [Governance, Authority and Assurance Metamodel v0.9.0](governance-authority-assurance-metamodel.md) is the current authoritative **normative specification edition**, incorporated unchanged by the v0.9.5 Candidate distribution. The v0.9.1–v0.9.5 distributions are not separate normative specification editions.

This permanent `/specification/` entry point identifies the current edition. Its historical permalink `/specification/gaam-v0.9.0/` remains stable and its title-page version is correctly **0.9.0**. Do not infer a v0.9.5 normative document from the v0.9.5 release tag.

## Citation and change rules

Cite normative requirements as **GAAM Candidate Specification edition v0.9.0** and applicable `GAAM-...` requirement IDs. Separately record distribution/test-suite v0.9.5, the selected profile, canonical schema IDs, evidence versions and assessment independence. The two versions need not be numerically identical.

The [publication and version identity guide](../docs/specification-publication.md) and [Candidate Stability Policy](../docs/candidate-stability-policy.md) define future edition, semantic, artifact and distribution changes.

## Publication model

- The human-readable specification defines normative semantics.
- JSON Schemas are normative for artifact structure under their retained `$id` values.
- Controlled vocabularies and profiles define their governed semantic and conformance boundaries.
- Executable tests produce repository-controlled evidence, not independent assurance.
- A maintenance release does not create a new normative specification edition; a changed normative document requires governed edition publication.
