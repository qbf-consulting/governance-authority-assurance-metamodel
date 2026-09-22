---
title: "Specification Publication and Reading Guide"
permalink: /specification/publication/
parent: "Documentation"
nav_order: 7
artifact_type: "Publication guide"
normative_status: "Informative"
---
# Specification Publication and Reading Guide

{% include gaam-meta.html %}

This page describes how the GAAM Candidate Specification is published and how its normative and derivative artifacts relate. It does not add requirements to GAAM v0.9.0.

## Canonical reading surface

The [Governance, Authority and Assurance Metamodel v0.9.0](../specification/governance-authority-assurance-metamodel.md) is the authoritative human-readable Candidate Specification. Its canonical GitHub Pages permalink remains `/specification/gaam-v0.9.0/`.

The Markdown source is maintained in the repository and rendered by the existing Jekyll/Just the Docs publication pipeline. The rendered HTML is therefore a publication view of the same source, not a separately edited specification.

## Normative precedence

For GAAM v0.9.0:

1. the human-readable specification defines normative semantics;
2. JSON Schemas are normative for the structure of artifacts in their declared scope;
3. governed vocabularies define controlled values in their declared scope;
4. profiles define composable conformance targets;
5. executable tests and validation reports provide evidence about repository conformance and publication integrity; and
6. generated catalogues, indexes and reading aids are derivative and non-authoritative.

Where a machine-actionable artifact and human-readable normative semantics conflict, the precedence rules in the Candidate Specification apply.

## Stable requirement identifiers

Normative statements use stable `GAAM-<SECTION>-<NUMBER>` identifiers. The [Normative Requirement Catalogue](requirements.md) is generated directly from the Candidate Specification and is checked in CI for exact regeneration and duplicate identifiers.

The machine-readable catalogue is published in the repository at `artifacts/gaam-v0.9.0-requirements.json`. It is intended for traceability tooling, conformance tooling and downstream mappings. It is not a second normative source.

## Publication integrity

A change to the Candidate Specification publication surface is acceptable only when:

- the existing canonical specification permalink remains available;
- the complete Jekyll site builds with strict front matter;
- existing diagram and guided-learning validation continues to pass;
- generated requirement catalogues exactly match the normative source;
- duplicate normative requirement identifiers are rejected; and
- the existing post-deployment canonical-publication verifier remains able to validate the deployed site and retained v0.9.0 artifacts.

## Print and archival use

The GitHub Pages rendering includes print-oriented styling so the authoritative HTML reading surface can be printed or saved as PDF without maintaining a second editable specification. A printed or saved copy is a derivative snapshot and should be identified by GAAM version and retrieval date when cited.

## Change control

Publication-only changes MUST NOT silently alter normative semantics. Normative changes continue to follow GAAM candidate change control, versioning and release governance.
