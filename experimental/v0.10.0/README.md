---
title: "Versioned Schema Extensions (Informative Candidate)"
artifact_type: "Experimental schema contract"
normative_status: "Informative"
nav_exclude: true
---
# Versioned Schema Extensions (Informative Candidate)

These separately identified schemas are **informative candidate extensions**. The current GAAM candidate release remains v0.9.2 with the retained v0.9.0 semantic and schema baseline. Publishing these files does not revise its normative conformance requirements, profiles or canonical 0.9.0 identifiers. Existing clients must explicitly opt in to these additional fields.

- The receipt `integrity` structure records a stated digest and canonicalization label. **Schema validation does not perform hashing, proof verification, timestamp attestation, issuer authentication or trustworthy backfill detection.** An in-package digest is not an authenticity proof. `proofRef` is a pointer only; a future verification profile must establish the exact signed bytes, verification method, trust anchor, and status semantics.
- `contributions` makes individual accountable material contributions representable; its optional presence does not enforce AGT-016. Actual contribution provenance and completeness require separate evidence.
- `freshness` contains a declared bound, observation time and source. An implementation must independently establish the observation, evaluate an explicit trusted clock, and reject unknown/stale evidence where applicable. A policy flag alone does not authorize fail-open.
- `delegation.acceptance`, `originatingPrincipal` and bounded propagation are representations only. `structuredScope` is intentionally separate from opaque legacy `delegatedScope`. A candidate evaluator may compare exact identifier sets, but cannot safely assume ordering for policy expressions, wildcard resource patterns, mixed-currency ceilings or unfamiliar dimensions.
- `releaseVersion` names the distribution used by a claim and does not silently alter the legacy `gaamVersion` semantic baseline.

Tests validate legacy and extended representations, malformed digest shape, unknown scope dimensions, missing required acceptance parts and invalid freshness bounds. They do not assert cryptographic authenticity or independently implemented runtime governance.

Promotion to the normative baseline requires the Candidate Stability Policy, ADR, migration guidance and versioned release evidence. Avoid publishing any claim of v0.10.0 conformance before those gates.
