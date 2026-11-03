---
title: "Assurance Interpretations and Unresolved Candidate Decisions"
artifact_type: "Informative adversarial review disposition"
normative_status: "Informative"
nav_exclude: true
---
# Assurance Interpretations and Unresolved Candidate Decisions

This note accompanies the November 2026 GAAM adversarial review. It does **not** modify the frozen v0.9.0 normative text incorporated by candidate release v0.9.3. The specification, governed profiles, schemas and Candidate Stability Policy remain authoritative.

## Effect classification and conformance by omission

EFF-001 delegates identification of consequential effects to a governed framework without establishing a universal minimum effect class. The absence of a declared consequential effect is not positive assurance that there are none. Until a new normative candidate establishes an effect floor, implementers should document excluded in-scope effect classes, rationale, accountable reviewer and evidence of review. The [informative exclusion example](consequential-effect-exclusion-register.example.json) is not a new v0.9.x conformance requirement.

A future normative revision should evaluate whether irreversible actions, personal-data disclosures, value commitments and non-participant rights effects require a minimum consequential classification. The rule would be potentially breaking and needs an ADR, threat analysis, compatibility review and migration evidence. A framework must not treat the absence of a self-declared High-Impact profile as proof of negligible risk.

## Receipt presence versus proportionate content

RUN-005 describes risk-proportionate receipt handling, while Annex C describes mandatory receipts for consequential effects. For current reading, the conservative reconciliation is that *content depth* may be proportionate, while a required receipt cannot silently disappear. This is interpretive guidance, not a replacement for either source requirement. Evidence of authentic origin, non-backfill and completeness remains separate from JSON Schema acceptance.

## Scope and time

An opaque `delegatedScope` object is not an executable attenuation proof. Comparison of amount ceilings, resources, purposes and jurisdictions requires governed comparators and failure behavior for unknown dimensions. Candidate typed structures under `experimental/v0.10.0` are representations, not an approved semantic ordering.

Freshness requires observation provenance, a usable evaluation clock and a policy-bound maximum age. `bounded-delay` without a numeric bound does not prove a timely revocation response. Reference vectors and candidate fields do not attest an actual registry read or trusted clock.

## Profiles, test references and normative source defects

The specification's §14 lists seven named profiles, while the governed manifests include a runtime-governance manifest. This needs controlled editorial resolution before the normative text is represented as explicitly enumerating all eight. The label `foundation-or-contextual` in derived matrices does not itself establish applicability; claimants must resolve actual selected manifest membership and dependencies. An unresolved contextual obligation is not a PASS.

The frozen specification contains duplicate §18 numbering and stray requirement-prefix/section alignments. Preserve stable GAAM requirement IDs and cite headings until a governed publication revision corrects the numbering. Overlapping obligations should be annotated before deduplication; deleting IDs would affect dependent crosswalks.

The existing replay rejection vector is informative. It is not evidence that the normative text already contains a general nonce or replay MUST. A new mandatory replay rule requires separate scope and compatibility analysis.

## Evidence, autonomy and authority

L0–L4 describe bounded conformance claim levels; E1–E3 describe evidence provenance and independence in adoption/pilot material. They are not equivalent scales and must not be mapped one-to-one. Fixture references, structural PASS, checksum-only validation, and reference-adapter verdicts cannot be promoted to independent implementation, authentic authority or runtime enforcement without additional evidence.

All proposals that would change a MUST, a conformance profile or an authorization decision require the existing governed approval path. These unresolved points remain visible rather than being closed by editorial wording.
