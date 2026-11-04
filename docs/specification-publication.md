---
title: "Specification Publication and Reading Guide"
permalink: /specification/publication/
parent: Specification & Profiles
nav_order: 5
artifact_type: "Publication guide"
normative_status: "Informative"
---
# Specification Publication and Reading Guide

{% include gaam-meta.html %}

This guide distinguishes the current Candidate **distribution release v0.9.5** from the authoritative **normative specification edition v0.9.0**. It does not introduce normative requirements.

## Canonical reading surface

GAAM **v0.9.5 is the current Candidate distribution and implementation-tooling release**. The [Governance, Authority and Assurance Metamodel v0.9.0](../specification/governance-authority-assurance-metamodel.md) remains the current normative **specification edition**, incorporated unchanged. The [current edition and distribution pointer](current-specification.md) identifies that edition and the historical `/specification/gaam-v0.9.0/` permalink remains stable; the frozen `/specification/` index is retained.

The Markdown source is maintained in the repository and rendered by the existing Jekyll/Just the Docs publication pipeline. The rendered HTML is therefore a publication view of the same source, not a separately edited specification. Plain text is likewise a generated publication representation: it is derived from the same normative source and MUST NOT be edited independently.

The historical schema identifiers use a personal GitHub Pages host retained for compatibility. That host was reported unreachable in the November 2026 adversarial review; the identifier string must not be taken as proof of live retrieval. See the [schema resolution boundary](schema-resolution.md) for an informative, release-controlled mirror mapping and its remaining operational limitation.

## Version ontology and publication rules

| Version dimension | Current | Governed meaning |
| --- | --- | --- |
| `version` / `VERSION` | **0.9.5** | Distribution and test-suite release. Advances for compatible maintained tooling, evidence and documentation. |
| `normativeVersion` / `candidateBaseline` | **0.9.5** | **Legacy machine contract:** Candidate **release** identity. The name does not mean the printed normative document edition. Preserve it for existing consumers pending a separately governed migration. |
| `specificationEdition` | **0.9.0** | Version printed on the current authoritative normative document. Advances only when revised normative text is formally published as a distinct edition. |
| `semanticBaseline` | **0.9.0** | Normative semantic/conformance meaning, independently reassessed for substantive changes. |
| `canonicalArtifactVersion` | **0.9.0** | Retained schema `$id`, profile and requirement identifier lineage. Never mechanically renumber to match a distribution. |

`PROJECT-STATUS.yaml.project.specification_edition` mirrors the normative edition. Its existing `normative_baseline` continues to denote the **Candidate release** for compatibility. These definitions clarify current machine contracts; they do not reinterpret historic tagged source or change existing conformance obligations.

**Change rules:** (1) Distribution-only, editorial website or informative tooling maintenance advances distribution identity but **does not** create a new normative edition. (2) A governed revision of the normative document, including editorial clarification in that normative text, requires an explicit edition decision/publication; preserving semantic meaning does not justify retroactively rewriting an old edition. (3) A change to normative meaning, conformance or canonical identifiers additionally requires impact, tests, compatibility, migration and identifier disposition under Candidate change control. (4) New specification edition numbers must not be declared without a matching actual document, current-index entry and publication checks.

**Canonical citation:** “GAAM Candidate Specification **edition v0.9.0**, distributed with **GAAM v0.9.5**.” An implementation report separately identifies profile(s), test-suite release, requirements, evidence, exceptions and assessment independence.

**Historical provenance:** v0.9.1–v0.9.4 were maintenance distributions incorporating normative document v0.9.0. Their tags, historical assets and field names are not rewritten by this prospective v0.9.5 clarification.

## Frozen-section citation clarification

The retained v0.9.0 source has two headings numbered **18**: the first is *Implementation guidance* (before Annex A), and the second is *Feature-complete governance artifacts* (after Annex B). This is an editorial numbering defect in the frozen semantic publication, not an additional requirement or competing section authority. Until a governed version updates the source, citations must use the full heading and, where applicable, the stable `GAAM-...` requirement identifier rather than the ambiguous number alone. Annex B.1 is a separately named annex and should be cited by that identifier. The current v0.9.5 Candidate distribution preserves the original source bytes and historical references.

## Normative precedence

For the v0.9.5 distribution, normative specification edition v0.9.0 and its retained semantic/canonical artifacts have the following precedence:

1. the human-readable specification defines normative semantics;
2. JSON Schemas are normative for the structure of artifacts in their declared scope;
3. governed vocabularies define controlled values in their declared scope;
4. profiles define composable conformance targets;
5. executable tests and validation reports provide evidence about repository conformance and publication integrity; and
6. generated catalogues, indexes and reading aids are derivative and non-authoritative.

Where a machine-actionable artifact and human-readable normative semantics conflict, the precedence rules in the Candidate Specification apply.

## Stable requirement identifiers

Normative statements use stable `GAAM-<SECTION>-<NUMBER>` identifiers. The [Normative Requirement Catalogue](https://github.com/qbf-consulting/governance-authority-assurance-metamodel/blob/v0.9.5/artifacts/gaam-v0.9.0-requirements.md) is generated directly from the Candidate Specification and is checked in CI for exact regeneration and duplicate identifiers.

The machine-readable catalogue is published in the repository at `artifacts/gaam-v0.9.0-requirements.json`. It is intended for traceability tooling, conformance tooling and downstream mappings. It is not a second normative source.

## Publication integrity

A change to the Candidate Specification publication surface is acceptable only when:

- the existing canonical specification permalink remains available;
- the complete Jekyll site builds with strict front matter;
- existing diagram and guided-learning validation continues to pass;
- generated requirement catalogues exactly match the normative source;
- the plain-text renderer passes deterministic and semantic-preservation tests;
- duplicate normative requirement identifiers are rejected; and
- the existing post-deployment canonical-publication verifier remains able to validate the deployed site and retained v0.9.0 artifacts.

## Plain-text publication

`scripts/generate_plaintext_spec.py` produces a deterministic UTF-8 text representation from `specification/governance-authority-assurance-metamodel.md`. It removes Jekyll front matter, Liquid presentation includes and Markdown emphasis while preserving headings, prose, lists, tables, code examples, requirement identifiers and link destinations.

The output filename uses `release.json.semanticBaseline` because the generated bytes reproduce the frozen semantic specification text, while `release.json.normativeVersion` is the legacy Candidate distribution identity. `release.json.specificationEdition` identifies the authoritative normative document edition:

```text
dist/gaam-specification-v<semanticBaseline>.txt
```

Generate it locally with:

```bash
python scripts/generate_plaintext_spec.py
```

The renderer intentionally does not reproduce RFC pagination, page headers or boilerplate. The purpose is presentation-neutral publication, archival use, diffing and low-dependency consumption.

If any generated representation diverges from the tagged normative source, the tagged normative source governs and the divergence is a publication defect.

### Release boundary

Plain-text publication is prospective. Historical GitHub Releases are not retrofitted. For a newly created GAAM release, the release workflow generates and attaches the text representation with the existing reproducible distribution and validation evidence. A workflow run against an already-existing release does not add this artifact retroactively.

## Print and archival use

The GitHub Pages rendering includes print-oriented styling so the authoritative HTML reading surface can be printed or saved as PDF without maintaining a second editable specification. A printed or saved copy is a derivative snapshot and should be identified by GAAM version and retrieval date when cited.

The generated plain-text representation is also a derivative publication snapshot. Its filename version denotes the semantic artifact baseline it renders; current normative release status is declared separately in `release.json` and repository publication metadata.

## Change control

Publication-only changes MUST NOT silently alter normative semantics. Normative changes continue to follow GAAM candidate change control, versioning and release governance.
