---
title: "Candidate Review Methodology"
published: false
nav_exclude: true
artifact_type: "Review methodology"
normative_status: "Informative governance process"
---
# Candidate Review Methodology

## Purpose

This methodology governs how candidate Privacy, Security, Affected-Party, Interoperability and Implementation-Evidence reviews are recorded. It governs review evidence and disposition; it does not modify GAAM normative semantics.

## Review sequence

1. **Freeze the baseline.** Review the version and content identity recorded in `review-baseline.json`.
2. **Attribute the reviewer.** Record reviewer identity, role, organisation where applicable, independence and conflicts.
3. **Record evidence-backed findings.** Findings identify severity, scope, evidence, affected requirements or profiles where known, v1 blocking status and release impact.
4. **Separate review from disposition.** Reviewers make findings. The decision authority records acceptance, remediation, risk acceptance, deferral or rejection with rationale.
5. **Verify remediation.** A merged change is not closure evidence by itself. The record must identify the test, review or other evidence demonstrating that the accepted disposition is satisfied.
6. **Attest completion.** A review may be `complete` only when its exit criteria are met and no unresolved blocking finding remains.

## Independence

`independent` means the reviewer is not the author or decision authority for the work being assessed and discloses relevant relationships. `not-independent` evidence remains useful but cannot satisfy an independent-review claim. `conflicted` records a relationship material enough that reliance requires an explicit disposition.

## Risk acceptance and deferral

An `accepted-risk` finding records the authority accepting the residual risk and must retain supporting evidence. A `deferred` finding identifies an owner and target date. Neither state may silently remove a v1 blocker unless the recorded decision authority explicitly changes `blockingV1` with rationale.

## Closure rule

A finding may be `closed` only when `closureEvidence` contains at least one resolvable evidence reference. Closed findings remain in the register to preserve audit history.
