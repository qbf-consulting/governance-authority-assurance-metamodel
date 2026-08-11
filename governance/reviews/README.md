---
title: "Candidate Review Method and Registers"
published: false
nav_exclude: true
artifact_type: "Review governance guide"
normative_status: "Informative governance process"
---
# Candidate Review Method and Registers

GAAM candidate reviews are evidence-bearing governance processes. These files do not assert that an independent review has occurred merely because a register exists.

## Authoritative review baseline

[`review-baseline.json`](review-baseline.json) freezes the candidate version and normative-surface digest used for review. Because the supplied archive contains no Git metadata, the initial baseline is content-addressed by the normative-surface SHA-256 rather than by an invented commit identifier.

## Registers

- [`privacy-review.json`](privacy-review.json)
- [`security-review.json`](security-review.json)
- [`affected-party-review.json`](affected-party-review.json)
- [`interoperability-review.json`](interoperability-review.json)
- [`implementation-evidence.json`](implementation-evidence.json)
- [`joint-disposition-register.json`](joint-disposition-register.json)

Each review separates reviewer identity and independence from the GAAM decision authority. A finding is not closed merely because remediation was merged; closure requires verification evidence.

## Machine-verifiable contracts

- [`review-register.schema.json`](review-register.schema.json) defines the common review envelope.
- [`finding.schema.json`](finding.schema.json) defines attributable review findings.
- [`finding-vocabulary.json`](finding-vocabulary.json) governs statuses, severities, independence and release-impact values.
- [`review-methodology.md`](review-methodology.md) defines the operating method and closure rules.

## Evidence

Review evidence belongs under [`evidence/`](evidence/README.md). Evidence references use repository-relative paths so the validation and package-integrity machinery can verify their presence.
