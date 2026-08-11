---
title: "GAAM Implementation Report Template"
permalink: /implementation-reports/template/
parent: "Implementation Reports"
nav_order: 7
artifact_type: "Implementation report template"
normative_status: "Informative"
---
# GAAM Implementation Report Template

{% include gaam-meta.html %}

> This template records the scope, method, evidence and limitations of an implementation assessment. Completing it does not by itself establish GAAM conformance or assessment independence.

> **Machine-readable companion:** reports intended for candidate-readiness evaluation should include a JSON record conforming to [`implementation-report.schema.json`](implementation-report.schema.json) and an evidence manifest conforming to [`evidence-manifest.schema.json`](evidence-manifest.schema.json). Repository acceptance of that record is a separate governance decision.

## 1. Report control

| Field | Entry |
|---|---|
| Report identifier |  |
| Report version and status |  |
| Author and organisation |  |
| Reviewer or approver |  |
| Issue date |  |
| Confidentiality or access classification |  |
| Supersedes |  |

## 2. Implementation identity

| Field | Entry |
|---|---|
| Implementer |  |
| Target identifier |  |
| Target name and version |  |
| Environment |  |
| GAAM version | 0.9.0 |
| Profiles claimed |  |
| Proposed evidence level |  |
| Evaluation period |  |
| Test-suite and validator versions |  |
| Source revision or package digest |  |

## 3. Evaluation scope

Describe the organisational and technical boundary, governed effects, authority sources, accountable parties, material service providers, included interfaces and excluded components.

### Profile-selection record

| Profile | Included | Rationale | Dependencies satisfied | Evidence locations | Material exclusions |
|---|---:|---|---:|---|---|
| Foundation |  |  |  |  |  |
| Delegated Authority |  |  |  |  |  |
| Runtime Governance |  |  |  |  |  |
| Agentic Systems |  |  |  |  |  |
| Continuous Assurance |  |  |  |  |  |
| High-Impact Systems |  |  |  |  |  |
| Machine-Actionable Governance |  |  |  |  |  |
| Trust Graph |  |  |  |  |  |

## 4. Authority, delegation and accountability

Describe:

- authority sources and competence;
- scope, purpose, jurisdiction and time bounds;
- delegation chains and attenuation;
- enforcement, suspension, revocation and expiry;
- accountable parties and review authorities;
- dependencies whose failure may change authority or decision validity.

## 5. Assessment method

Record the methods, tools, sampling, environments, test data, observation windows and limitations. Explain how another reviewer can reproduce structural and behavioural results.

## 6. Requirement and test coverage

| Requirement or control set | Method | Evidence IDs | Result | Exceptions or limitations |
|---|---|---|---|---|
|  |  |  |  |  |

Summarise passed, failed, skipped and indeterminate checks. Do not report only successful cases.

## 7. Evidence register

| Evidence ID | Type | Subject and supported claim | Source and provenance | Collected at and valid until | Verification and integrity method | Independence | Disposition |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

Use the [Implementation Evidence Guide](evidence-guide.md) and [Evidence Quality Model](evidence-quality-model.md) when completing this section.

## 8. Behavioural, lifecycle and interoperability results

Describe positive, negative and boundary testing for applicable controls, including:

- authority and delegation validity;
- revocation, expiry and stale-state behaviour;
- decision receipt completeness;
- event ordering and lifecycle transitions;
- profile composition;
- cross-implementation processing, where tested;
- high-impact notice, review and remedy, where applicable.

## 9. Deviations, failures and residual risks

| ID | Requirement or control | Deviation or failure | Affected scope and period | Compensating control | Residual risk | Owner | Due date | Status |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

Record contradictory and superseded evidence. Explain whether a failure restricts, suspends, invalidates or prevents the proposed claim.

## 10. Privacy, security and affected-party review

Describe:

- data minimisation, access, disclosure, retention and disposal;
- receipt, graph and relationship-correlation risks;
- relevant security findings and incident history;
- notice and accessibility;
- standing and challenge channels;
- review authority and independence;
- interim protection, correction and remedy execution evidence.

## 11. Assurance and independence statement

State who produced the evidence, who performed the assessment, and how each party relates to the target, operator and claim issuer. Disclose control, funding, shared management and subcontracting relationships that may affect independence.

## 12. Conclusion and claim boundary

State:

- the exact conclusion supported by the evidence;
- the proposed conformance level, if any;
- profiles and target covered;
- material exclusions and limitations;
- validity or review period;
- events that trigger reassessment, restriction, suspension, withdrawal or supersession.

## 13. Approval and revision history

| Version | Date | Author or approver | Change | Status |
|---|---|---|---|---|
|  |  |  |  |  |
