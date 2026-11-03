---
title: "Requirement-Level Evidence Dispositions"
artifact_type: "Informative evidence interpretation"
normative_status: "Informative"
parent: Test & Assure
nav_exclude: true
---
# Requirement-Level Evidence Dispositions

This page documents the audit boundary for the GAAM normative requirement matrix. The authoritative obligations remain in the Candidate Specification. The traceability matrix associates 190 requirement IDs with classes, evidence catalogues and illustrative tests, but is not a proof that those requirements have been satisfied.

Run `python scripts/audit_traceability.py > /tmp/gaam-traceability-audit.json` to obtain a deterministic, requirement-by-requirement inspection record. A `reference-only` disposition means that a behavioural vector filename is linked, not that its particular assertions establish the requirement. `non-test-placeholder` identifies entries such as `claim-level-evidence` which must never be counted as executable cases. `no-executable-reference` does not imply the requirement is unimportant or inapplicable; governance and procedural obligations may require non-machine evidence.

This audit deliberately sets `requirementSpecificallyVerified` to `false` for all entries. It is a conservative claim about **this audit**, not a judgment that all requirements are unfulfilled. To promote any entry to requirement-specific verification, provide an explicit falsifiable assertion, input provenance, a test or assessment ID, expected behavior, and independent review where required. The reference adapter is repository-authored and cannot establish L4 or E2/E3 evidence.

The L0–L4 levels describe claim maturity within a declared target and profile. The E1–E3 terminology in pilot guidance identifies the source and independence of evidence, not an alternative numeric conformance scale. They must be stated separately. No mechanical L-to-E equivalence is asserted.

Validation and package checks establish only their own enumerated invariants. Successful repository CI, a checksum manifest carried inside the same package, and linked test names must not be represented as independent assurance, package authenticity, or verified real-world authorization.

See the [coverage reading guide](requirement-evidence-coverage.md) and [conformance guide](conformance-guide.md).
