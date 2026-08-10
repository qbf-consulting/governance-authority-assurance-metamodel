---
title: GAAM v0.9.0 Validation Report
permalink: /validation-report/
nav_exclude: true
artifact_type: Validation evidence
normative_status: Repository generated
---
# GAAM v0.9.0 Validation Report

{% include gaam-meta.html %}

**Status:** PASS  
**Checks:** 305  
**Passed:** 305  
**Failed:** 0  

This report evidences repository publication, structural and included behavioural checks. It is not an independent L4 assessment.

| ID | Kind | Status | Evidence |
|---|---|---|---|
| `PUB-001-version-source` | publication | PASS | authoritative version=0.9.0 |
| `PUB-002-active-version-coherence` | publication | PASS | no stale active v0.5.0 references |
| `PUB-003-specification-identity` | publication | PASS | normative specification identifies candidate release |
| `PUB-HYG-README-EXCLUDE` | publication | PASS | all implementation-pattern README files excluded from Jekyll publication |
| `PUB-HYG-LANDINGS` | publication | PASS | 18 canonical pattern landing pages use clean directory URLs |
| `PUB-HYG-SUPPORT-NAV` | publication | PASS | all supporting pattern pages excluded from primary navigation |
| `PUB-HYG-CHANGELOG` | publication | PASS | changelog begins with valid canonical front matter |
| `PUB-IA-DOCUMENTATION` | publication | PASS | Documentation is grouped into four validated reader routes |
| `PUB-IA-APPENDICES` | publication | PASS | Appendices consolidates reference material without changing URLs |
| `PUB-IA-REPORTS` | publication | PASS | Implementation Reports is a top-level workflow with intact children |
| `PUB-IA-TOP-ORDER` | publication | PASS | top-level workflow order is deterministic |
| `PUB-FUTURE-EVOLUTION` | publication | PASS | future-evolution programme published as informative research |
| `GOV-FUTURE-REGISTER` | governance | PASS | 25 future enhancements classified with controlled delivery and promotion states |
| `GOV-FUTURE-DRAFT-PROFILES` | governance | PASS | 7 draft profiles are explicitly non-conformant |
| `SCH-EXPERIMENTAL` | schema | PASS | 10 experimental schemas and examples validated outside the canonical surface |
| `GOV-FUTURE-NO-NORMATIVE-IMPORT` | governance | PASS | canonical v0.9.0 artifacts do not import experimental identifiers |
| `GOV-FUTURE-BOUNDARY` | governance | PASS | future-evolution assets cannot be mistaken for GAAM v0.9.0 conformance material |
| `GOV-FUTURE-READINESS` | governance | PASS | 25 candidates assessed with explicit non-normative dispositions and independent-review boundary |
| `REQ-001-unique` | normative | PASS | 190 identifiers |
| `REQ-002-index-exact` | normative | PASS | 190 indexed requirements |
| `REQ-003-normative-language` | normative | PASS | 190 indexed statements classified |
| `MAP-ECOSYSTEM-CROSSWALKS` | mapping | PASS | 2 informative ecosystem crosswalks validated against mapping schema and normative requirement identifiers |
| `SCH-decision-receipt` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-evidence` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-remedy` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-appeal` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-conformance-claim` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-governance-event` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-gaam-package` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-agent-governance-identity` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-runtime-envelope` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-authority` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-profile-manifest` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-delegation` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-assurance` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-IDS` | schema | PASS | 13 unique canonical identifiers |
| `SCH-CATALOG` | schema | PASS | catalog covers all schemas |
| `VOC-assurance-statuses` | vocabulary | PASS | 7 governed values |
| `VOC-decision-outcomes` | vocabulary | PASS | 9 governed values |
| `VOC-governance-event-types` | vocabulary | PASS | 11 governed values |
| `VOC-lifecycle-states` | vocabulary | PASS | 14 governed values |
| `VOC-relationship-types` | vocabulary | PASS | 19 governed values |
| `PRO-agentic-systems` | profile | PASS | 51 requirements; dependencies=True; document=True |
| `PRO-continuous-assurance` | profile | PASS | 19 requirements; dependencies=True; document=True |
| `PRO-delegated-authority` | profile | PASS | 32 requirements; dependencies=True; document=True |
| `PRO-foundation` | profile | PASS | 36 requirements; dependencies=True; document=True |
| `PRO-high-impact-systems` | profile | PASS | 22 requirements; dependencies=True; document=True |
| `PRO-machine-actionable-governance` | profile | PASS | 26 requirements; dependencies=True; document=True |
| `PRO-runtime-governance` | profile | PASS | 21 requirements; dependencies=True; document=True |
| `PRO-trust-graph` | profile | PASS | 9 requirements; dependencies=True; document=True |
| `PRO-DEPENDENCIES` | profile | PASS | all profile dependencies resolve |
| `PAT-agent-state-change-control-CONTRACT` | pattern | PASS | required files present |
| `PAT-agent-state-change-control-MANIFEST` | pattern | PASS | manifest conforms |
| `PAT-agent-state-change-control-REFERENCES` | pattern | PASS | profile, requirement, artifact and behavioural references resolve |
| `PAT-agent-state-change-control-MATURITY` | pattern | PASS | behavioural claim supported |
| `PAT-agent-state-change-control-CATALOG` | pattern | PASS | catalogue entry present |
| `CLM-agent-state-change-control` | conformance | PASS | schema, evidence, limitations and independence rules satisfied |
| `PAT-assurance-composition-CONTRACT` | pattern | PASS | required files present |
| `PAT-assurance-composition-MANIFEST` | pattern | PASS | manifest conforms |
| `PAT-assurance-composition-REFERENCES` | pattern | PASS | profile, requirement, artifact and behavioural references resolve |
| `PAT-assurance-composition-MATURITY` | pattern | PASS | behavioural claim supported |
| `PAT-assurance-composition-CATALOG` | pattern | PASS | catalogue entry present |
| `CLM-assurance-composition` | conformance | PASS | schema, evidence, limitations and independence rules satisfied |
| `PAT-authority-lifecycle-and-revocation-CONTRACT` | pattern | PASS | required files present |
| `PAT-authority-lifecycle-and-revocation-MANIFEST` | pattern | PASS | manifest conforms |
| `PAT-authority-lifecycle-and-revocation-REFERENCES` | pattern | PASS | profile, requirement, artifact and behavioural references resolve |
| `PAT-authority-lifecycle-and-revocation-MATURITY` | pattern | PASS | assurance-ready claim supported |
| `PAT-authority-lifecycle-and-revocation-CATALOG` | pattern | PASS | catalogue entry present |
| `FIX-authority-lifecycle-and-revocation-authority.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-authority-lifecycle-and-revocation-authority.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-authority-lifecycle-and-revocation-decision-receipt.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-authority-lifecycle-and-revocation-decision-receipt.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-authority-lifecycle-and-revocation-delegation.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-authority-lifecycle-and-revocation-delegation.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-authority-lifecycle-and-revocation-governance-event.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-authority-lifecycle-and-revocation-governance-event.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-authority-lifecycle-and-revocation-remedy.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-authority-lifecycle-and-revocation-remedy.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `CLM-authority-lifecycle-and-revocation` | conformance | PASS | schema, evidence, limitations and independence rules satisfied |
| `PAT-basic-governed-decision-CONTRACT` | pattern | PASS | required files present |
| `PAT-basic-governed-decision-MANIFEST` | pattern | PASS | manifest conforms |
| `PAT-basic-governed-decision-REFERENCES` | pattern | PASS | profile, requirement, artifact and behavioural references resolve |
| `PAT-basic-governed-decision-MATURITY` | pattern | PASS | assurance-ready claim supported |
| `PAT-basic-governed-decision-CATALOG` | pattern | PASS | catalogue entry present |
| `FIX-basic-governed-decision-authority.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-basic-governed-decision-authority.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-basic-governed-decision-decision-receipt.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-basic-governed-decision-decision-receipt.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-basic-governed-decision-delegation.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-basic-governed-decision-delegation.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-basic-governed-decision-governance-event.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-basic-governed-decision-governance-event.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-basic-governed-decision-remedy.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-basic-governed-decision-remedy.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `CLM-basic-governed-decision` | conformance | PASS | schema, evidence, limitations and independence rules satisfied |
| `PAT-cross-jurisdiction-policy-conflict-CONTRACT` | pattern | PASS | required files present |
| `PAT-cross-jurisdiction-policy-conflict-MANIFEST` | pattern | PASS | manifest conforms |
| `PAT-cross-jurisdiction-policy-conflict-REFERENCES` | pattern | PASS | profile, requirement, artifact and behavioural references resolve |
| `PAT-cross-jurisdiction-policy-conflict-MATURITY` | pattern | PASS | behavioural claim supported |
| `PAT-cross-jurisdiction-policy-conflict-CATALOG` | pattern | PASS | catalogue entry present |
| `CLM-cross-jurisdiction-policy-conflict` | conformance | PASS | schema, evidence, limitations and independence rules satisfied |
| `PAT-cross-registry-recognition-CONTRACT` | pattern | PASS | required files present |
| `PAT-cross-registry-recognition-MANIFEST` | pattern | PASS | manifest conforms |
| `PAT-cross-registry-recognition-REFERENCES` | pattern | PASS | profile, requirement, artifact and behavioural references resolve |
| `PAT-cross-registry-recognition-MATURITY` | pattern | PASS | assurance-ready claim supported |
| `PAT-cross-registry-recognition-CATALOG` | pattern | PASS | catalogue entry present |
| `FIX-cross-registry-recognition-authority.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-cross-registry-recognition-authority.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-cross-registry-recognition-decision-receipt.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-cross-registry-recognition-decision-receipt.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-cross-registry-recognition-delegation.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-cross-registry-recognition-delegation.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-cross-registry-recognition-governance-event.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-cross-registry-recognition-governance-event.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-cross-registry-recognition-remedy.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-cross-registry-recognition-remedy.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `CLM-cross-registry-recognition` | conformance | PASS | schema, evidence, limitations and independence rules satisfied |
| `PAT-degraded-trust-service-operation-CONTRACT` | pattern | PASS | required files present |
| `PAT-degraded-trust-service-operation-MANIFEST` | pattern | PASS | manifest conforms |
| `PAT-degraded-trust-service-operation-REFERENCES` | pattern | PASS | profile, requirement, artifact and behavioural references resolve |
| `PAT-degraded-trust-service-operation-MATURITY` | pattern | PASS | behavioural claim supported |
| `PAT-degraded-trust-service-operation-CATALOG` | pattern | PASS | catalogue entry present |
| `CLM-degraded-trust-service-operation` | conformance | PASS | schema, evidence, limitations and independence rules satisfied |
| `PAT-delegated-agent-purchase-CONTRACT` | pattern | PASS | required files present |
| `PAT-delegated-agent-purchase-MANIFEST` | pattern | PASS | manifest conforms |
| `PAT-delegated-agent-purchase-REFERENCES` | pattern | PASS | profile, requirement, artifact and behavioural references resolve |
| `PAT-delegated-agent-purchase-MATURITY` | pattern | PASS | assurance-ready claim supported |
| `PAT-delegated-agent-purchase-CATALOG` | pattern | PASS | catalogue entry present |
| `FIX-delegated-agent-purchase-authority.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-delegated-agent-purchase-authority.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-delegated-agent-purchase-decision-receipt.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-delegated-agent-purchase-decision-receipt.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-delegated-agent-purchase-delegation.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-delegated-agent-purchase-delegation.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-delegated-agent-purchase-governance-event.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-delegated-agent-purchase-governance-event.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-delegated-agent-purchase-remedy.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-delegated-agent-purchase-remedy.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `CLM-delegated-agent-purchase` | conformance | PASS | schema, evidence, limitations and independence rules satisfied |
| `PAT-downstream-remedy-propagation-CONTRACT` | pattern | PASS | required files present |
| `PAT-downstream-remedy-propagation-MANIFEST` | pattern | PASS | manifest conforms |
| `PAT-downstream-remedy-propagation-REFERENCES` | pattern | PASS | profile, requirement, artifact and behavioural references resolve |
| `PAT-downstream-remedy-propagation-MATURITY` | pattern | PASS | behavioural claim supported |
| `PAT-downstream-remedy-propagation-CATALOG` | pattern | PASS | catalogue entry present |
| `CLM-downstream-remedy-propagation` | conformance | PASS | schema, evidence, limitations and independence rules satisfied |
| `PAT-governed-ecosystem-operations-CONTRACT` | pattern | PASS | required files present |
| `PAT-governed-ecosystem-operations-MANIFEST` | pattern | PASS | manifest conforms |
| `PAT-governed-ecosystem-operations-REFERENCES` | pattern | PASS | profile, requirement, artifact and behavioural references resolve |
| `PAT-governed-ecosystem-operations-MATURITY` | pattern | PASS | assurance-ready claim supported |
| `PAT-governed-ecosystem-operations-CATALOG` | pattern | PASS | catalogue entry present |
| `FIX-governed-ecosystem-operations-authority.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-governed-ecosystem-operations-authority.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-governed-ecosystem-operations-decision-receipt.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-governed-ecosystem-operations-decision-receipt.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-governed-ecosystem-operations-delegation.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-governed-ecosystem-operations-delegation.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-governed-ecosystem-operations-governance-event.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-governed-ecosystem-operations-governance-event.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-governed-ecosystem-operations-remedy.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-governed-ecosystem-operations-remedy.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `CLM-governed-ecosystem-operations` | conformance | PASS | schema, evidence, limitations and independence rules satisfied |
| `PAT-high-impact-multi-agent-service-CONTRACT` | pattern | PASS | required files present |
| `PAT-high-impact-multi-agent-service-MANIFEST` | pattern | PASS | manifest conforms |
| `PAT-high-impact-multi-agent-service-REFERENCES` | pattern | PASS | profile, requirement, artifact and behavioural references resolve |
| `PAT-high-impact-multi-agent-service-MATURITY` | pattern | PASS | assurance-ready claim supported |
| `PAT-high-impact-multi-agent-service-CATALOG` | pattern | PASS | catalogue entry present |
| `FIX-high-impact-multi-agent-service-authority.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-high-impact-multi-agent-service-authority.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-high-impact-multi-agent-service-decision-receipt.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-high-impact-multi-agent-service-decision-receipt.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-high-impact-multi-agent-service-delegation.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-high-impact-multi-agent-service-delegation.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-high-impact-multi-agent-service-governance-event.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-high-impact-multi-agent-service-governance-event.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-high-impact-multi-agent-service-remedy.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-high-impact-multi-agent-service-remedy.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `CLM-high-impact-multi-agent-service` | conformance | PASS | schema, evidence, limitations and independence rules satisfied |
| `PAT-independent-assurance-assessment-CONTRACT` | pattern | PASS | required files present |
| `PAT-independent-assurance-assessment-MANIFEST` | pattern | PASS | manifest conforms |
| `PAT-independent-assurance-assessment-REFERENCES` | pattern | PASS | profile, requirement, artifact and behavioural references resolve |
| `PAT-independent-assurance-assessment-MATURITY` | pattern | PASS | assurance-ready claim supported |
| `PAT-independent-assurance-assessment-CATALOG` | pattern | PASS | catalogue entry present |
| `FIX-independent-assurance-assessment-authority.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-independent-assurance-assessment-authority.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-independent-assurance-assessment-decision-receipt.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-independent-assurance-assessment-decision-receipt.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-independent-assurance-assessment-delegation.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-independent-assurance-assessment-delegation.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-independent-assurance-assessment-governance-event.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-independent-assurance-assessment-governance-event.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-independent-assurance-assessment-remedy.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-independent-assurance-assessment-remedy.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `CLM-independent-assurance-assessment` | conformance | PASS | schema, evidence, limitations and independence rules satisfied |
| `PAT-inferred-evidence-governance-CONTRACT` | pattern | PASS | required files present |
| `PAT-inferred-evidence-governance-MANIFEST` | pattern | PASS | manifest conforms |
| `PAT-inferred-evidence-governance-REFERENCES` | pattern | PASS | profile, requirement, artifact and behavioural references resolve |
| `PAT-inferred-evidence-governance-MATURITY` | pattern | PASS | behavioural claim supported |
| `PAT-inferred-evidence-governance-CATALOG` | pattern | PASS | catalogue entry present |
| `CLM-inferred-evidence-governance` | conformance | PASS | schema, evidence, limitations and independence rules satisfied |
| `PAT-institutional-authority-succession-CONTRACT` | pattern | PASS | required files present |
| `PAT-institutional-authority-succession-MANIFEST` | pattern | PASS | manifest conforms |
| `PAT-institutional-authority-succession-REFERENCES` | pattern | PASS | profile, requirement, artifact and behavioural references resolve |
| `PAT-institutional-authority-succession-MATURITY` | pattern | PASS | behavioural claim supported |
| `PAT-institutional-authority-succession-CATALOG` | pattern | PASS | catalogue entry present |
| `CLM-institutional-authority-succession` | conformance | PASS | schema, evidence, limitations and independence rules satisfied |
| `PAT-machine-actionable-governance-package-CONTRACT` | pattern | PASS | required files present |
| `PAT-machine-actionable-governance-package-MANIFEST` | pattern | PASS | manifest conforms |
| `PAT-machine-actionable-governance-package-REFERENCES` | pattern | PASS | profile, requirement, artifact and behavioural references resolve |
| `PAT-machine-actionable-governance-package-MATURITY` | pattern | PASS | assurance-ready claim supported |
| `PAT-machine-actionable-governance-package-CATALOG` | pattern | PASS | catalogue entry present |
| `FIX-machine-actionable-governance-package-authority.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-machine-actionable-governance-package-authority.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-machine-actionable-governance-package-decision-receipt.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-machine-actionable-governance-package-decision-receipt.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-machine-actionable-governance-package-delegation.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-machine-actionable-governance-package-delegation.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-machine-actionable-governance-package-governance-event.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-machine-actionable-governance-package-governance-event.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-machine-actionable-governance-package-remedy.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-machine-actionable-governance-package-remedy.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `CLM-machine-actionable-governance-package` | conformance | PASS | schema, evidence, limitations and independence rules satisfied |
| `PAT-notice-challenge-and-remedy-CONTRACT` | pattern | PASS | required files present |
| `PAT-notice-challenge-and-remedy-MANIFEST` | pattern | PASS | manifest conforms |
| `PAT-notice-challenge-and-remedy-REFERENCES` | pattern | PASS | profile, requirement, artifact and behavioural references resolve |
| `PAT-notice-challenge-and-remedy-MATURITY` | pattern | PASS | assurance-ready claim supported |
| `PAT-notice-challenge-and-remedy-CATALOG` | pattern | PASS | catalogue entry present |
| `FIX-notice-challenge-and-remedy-authority.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-notice-challenge-and-remedy-authority.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-notice-challenge-and-remedy-decision-receipt.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-notice-challenge-and-remedy-decision-receipt.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-notice-challenge-and-remedy-delegation.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-notice-challenge-and-remedy-delegation.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-notice-challenge-and-remedy-governance-event.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-notice-challenge-and-remedy-governance-event.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `FIX-notice-challenge-and-remedy-remedy.invalid` | fixture | PASS | rejected as expected; manifest declaration matched |
| `FIX-notice-challenge-and-remedy-remedy.valid` | fixture | PASS | accepted as expected; manifest declaration matched |
| `CLM-notice-challenge-and-remedy` | conformance | PASS | schema, evidence, limitations and independence rules satisfied |
| `PAT-post-decision-obligation-lifecycle-CONTRACT` | pattern | PASS | required files present |
| `PAT-post-decision-obligation-lifecycle-MANIFEST` | pattern | PASS | manifest conforms |
| `PAT-post-decision-obligation-lifecycle-REFERENCES` | pattern | PASS | profile, requirement, artifact and behavioural references resolve |
| `PAT-post-decision-obligation-lifecycle-MATURITY` | pattern | PASS | behavioural claim supported |
| `PAT-post-decision-obligation-lifecycle-CATALOG` | pattern | PASS | catalogue entry present |
| `CLM-post-decision-obligation-lifecycle` | conformance | PASS | schema, evidence, limitations and independence rules satisfied |
| `PAT-revocation-propagation-boundaries-CONTRACT` | pattern | PASS | required files present |
| `PAT-revocation-propagation-boundaries-MANIFEST` | pattern | PASS | manifest conforms |
| `PAT-revocation-propagation-boundaries-REFERENCES` | pattern | PASS | profile, requirement, artifact and behavioural references resolve |
| `PAT-revocation-propagation-boundaries-MATURITY` | pattern | PASS | behavioural claim supported |
| `PAT-revocation-propagation-boundaries-CATALOG` | pattern | PASS | catalogue entry present |
| `CLM-revocation-propagation-boundaries` | conformance | PASS | schema, evidence, limitations and independence rules satisfied |
| `PAT-IDS` | pattern | PASS | 18 unique pattern identifiers |
| `PAT-CATALOG-COVERAGE` | pattern | PASS | 18 pattern directories catalogued |
| `PAT-FUTURE-EVOLUTION` | pattern | PASS | 9 future-evolution patterns are behavioural, traceable and non-normative |
| `BEH-agent-state-change-reauthorised-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-assurance-expired-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-assurance-independence-insufficient-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-authority-active-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-authority-expired-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-authority-not-yet-effective-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-authority-revoked-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-authority-source-invalid-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-decision-missing-evidence-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-decision-policy-superseded-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-decision-stale-evidence-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-decision-traceable-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-degraded-operation-fail-safe-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-delegation-amplification-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-delegation-attenuated-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-delegation-child-outlives-parent-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-delegation-depth-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-delegation-parent-revoked-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-delegation-redelegation-prohibited-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-future-assurance-composition-bounded-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-high-impact-no-remedy-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-high-impact-notice-missing-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-high-impact-remedy-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-high-impact-review-not-independent-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-inferred-evidence-bounded-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-institutional-succession-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-jurisdiction-conflict-escalated-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-lifecycle-event-order-invalid-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-lifecycle-event-order-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-obligation-fulfilled-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-profile-composition-foundation-delegated-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-profile-composition-missing-foundation-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-remedy-propagation-verified-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-revocation-propagation-bounded-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-runtime-revocation-fail-closed-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-runtime-stale-state-fail-open-rejected` | behavioural | PASS | expected=False; actual=False |
| `TRC-REQUIREMENTS` | traceability | PASS | 190 requirements have testability and evidence dispositions |
| `TRC-TEST-ORPHANS` | traceability | PASS | 36 behavioural tests referenced by requirement traceability |
| `THR-TRACE` | threat | PASS | 7 threats mapped to requirements and tests |
| `DOC-PAGE-TITLE-CONTRACT` | documentation | PASS | all rendered Markdown pages declare exactly one H1 matching front matter |
| `DOC-CTWG-GLOSSARY-ALIGNMENT` | documentation | PASS | 26 glossary terms covered by CTWG alignment register |
| `DOC-LOCAL-LINKS` | documentation | PASS | all local links resolve |
| `DOC-TSMM-CANONICAL` | provenance | PASS | canonical TSMM repository link present |
| `CI-WORKFLOW` | automation | PASS | validation workflow present |
| `GOV-CANDIDATE-REGISTER` | governance | PASS | 5 candidate issues have valid authority, scope, evidence and disposition fields |
| `GOV-CANDIDATE-IDS` | governance | PASS | 5 unique candidate issue identifiers |
| `GOV-REVIEW-REGISTERS` | governance | PASS | 5 required review registers are structurally complete |
| `GOV-ECO-EVIDENCE` | governance | PASS | governed ecosystem evidence package complete |
| `GOV-ECO-DISPOSITION` | governance | PASS | 12 ecosystem capabilities classified with controlled dispositions |
| `GOV-CONTRIBUTION-CONTROLS` | governance | PASS | candidate issue forms and pull-request governance template present |
| `GOV-V1-READINESS-STATE` | governance | PASS | 5 explicitly recorded open v1 blockers: GAAM-CR-001, GAAM-CR-002, GAAM-CR-003, GAAM-CR-004, GAAM-CR-005 |
| `PKG-MANIFEST` | package | PASS | package manifest conforms |
| `PKG-INTEGRITY` | package | PASS | 439 checksums verified |
