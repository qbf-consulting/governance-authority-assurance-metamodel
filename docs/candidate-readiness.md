---
title: "Candidate Readiness Dashboard"
permalink: /governance/candidate-readiness/
parent: Assurance and Governance Tracking
artifact_type: "Generated governance view"
normative_status: "Informative"
grand_parent: Documentation
nav_order: 2
---
# Candidate Readiness Dashboard

{% include gaam-meta.html %}

> **Generated view.** Do not edit the gate table by hand. Run `python scripts/build_candidate_readiness.py` after changing candidate issues, review registers, or implementation reports.

This dashboard exposes the evidence currently available for progression from GAAM v0.9.0 to v1.0.0. Its authoritative machine-readable state is [`governance/candidate-readiness.json`](../governance/candidate-readiness.json).

## Current decision state

**Eligible for a v1.0.0 release decision:** **NO**  
**Blocking gates:** 9  
**Accepted implementation reports:** 0

## Candidate gates

| Gate | State | Blocking | Closure predicate |
|---|---|---:|---|
| Two independent implementations | Not started | Yes | At least two non-synthetic accepted implementation reports declare independent assessment with disclosed relationships and contain no failed or indeterminate result or open exception. |
| Foundation implementation coverage | Not started | Yes | At least one accepted independent implementation report includes the Foundation Profile. |
| Composed-profile implementation coverage | Not started | Yes | At least one accepted independent implementation report covers Foundation plus at least one additional GAAM profile. |
| Requirement testability disposition | Complete | Yes | The normative requirement index and requirement-test coverage matrix remain validator-clean. |
| Canonical identifier publication | In progress | Yes | GAAM-CR-003 is closed with resolvable versioned identifiers, checksum verification and historical-retention evidence. |
| Privacy review | Not started | Yes | The privacy review is complete, attested, and has no unresolved blocking findings. |
| Security review | Not started | Yes | The security review is complete, attested, and has no unresolved blocking findings or unresolved critical security issue. |
| Affected-party review | Not started | Yes | The affected-party review is complete, attested, and has no unresolved blocking findings. |
| Cross-implementation interoperability | Not started | Yes | The interoperability review is complete and GAAM-CR-002 is closed with cross-validator evidence from independent implementations. |
| Governed ecosystem applicability | In progress | No | The governed ecosystem capability assessment receives independent attestation and candidate enhancement dispositions are reviewed. |
| Breaking candidate issue disposition | Not started | Yes | Every candidate issue with blockingV1=true is closed with its required evidence. |

## Current blockers

- `independent-implementations` — Two independent implementations. Source issue(s): GAAM-CR-001.
- `foundation-implementation` — Foundation implementation coverage. Source issue(s): GAAM-CR-001.
- `composed-profile-implementation` — Composed-profile implementation coverage. Source issue(s): GAAM-CR-001.
- `canonical-identifiers` — Canonical identifier publication. Source issue(s): GAAM-CR-003.
- `privacy-review` — Privacy review. Source issue(s): GAAM-CR-004.
- `security-review` — Security review. Source issue(s): GAAM-CR-005.
- `affected-party-review` — Affected-party review. Source issue(s): GAAM-CR-004.
- `cross-implementation-interoperability` — Cross-implementation interoperability. Source issue(s): GAAM-CR-002.
- `candidate-issue-disposition` — Breaking candidate issue disposition. Source issue(s): GAAM-CR-001, GAAM-CR-002, GAAM-CR-003, GAAM-CR-004, GAAM-CR-005.

## Evidence acceptance boundary

Only non-synthetic implementation reports with `reportStatus: accepted` are candidate-readiness inputs. An accepted report contributes to the independent-implementation gate only when it declares `independence.classification: independent` and `relationshipsDisclosed: true`. Schema-valid examples and fixtures never satisfy candidate exit criteria.

## Decision rule

A v1.0.0 release decision is eligible only when every blocking gate in `governance/candidate-readiness.json` is `satisfied`. Eligibility permits a governed release decision; it does not itself approve or publish v1.0.0.

## How to submit evidence

Use the repository issue forms and the [Implementation Reports](../implementation-reports/) workflow. Machine-readable reports must validate against `implementation-reports/implementation-report.schema.json`, reference a valid evidence manifest, disclose assessment independence, and remain within their stated claim boundary.
