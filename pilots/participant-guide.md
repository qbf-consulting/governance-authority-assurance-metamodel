---
title: Zero-to-Pilot Participant Guide
permalink: /pilots/participant-guide/
parent: Pilot GAAM
grand_parent: Implement
nav_order: 3
artifact_type: Informative participant runbook
normative_status: Informative
---
# Zero-to-Pilot Participant Guide

This route is for a team that has never used GAAM. Begin with the [charter](charter.md) and [design boundaries](design.md). Use the [gate catalogue](gates.json) as the structured checklist. A gate status is **not-assessed** until its owner can identify the actual evidence, review its limitations and make a disposition. An output that merely runs without an error is not automatically an approved gate.

## G0 — Pilot authorized

**Owner:** sponsor or competent institutional authority. **Entry:** intended effect, affected parties, scope and roles proposed. **Actions:** approve a versioned charter, identify legal/contractual or other valid source of test authority, define non-production safeguards and halt rules. **Evidence:** attributable approval, charter revision, scope and owners. **Stop:** no valid sponsor or ambiguous authority basis. Repo-owned synthetic examples do not constitute institutional approval.

## G1 — Baseline and environment ready

**Owner:** technical lead. **Entry:** approved G0. **Actions:** check out a fixed GAAM source revision; install documented dependencies and record exact versions. Select a declared conformance target and profile set with dependency closure. **Evidence:** commit SHA, environment description, selected profiles and mapped requirement IDs. **Stop:** missing publication, unresolved profiles, undocumented prerequisite or failed installation.

```bash
git clone https://github.com/qbf-consulting/governance-authority-assurance-metamodel.git
cd governance-authority-assurance-metamodel
python -m pip install -r requirements-dev.txt
python scripts/gaam.py validate-package conformance-kit/starter
```

The starter demonstrates the structural entry path only. Consult [profile selection](../implementation-reports/profile-selection-guide.md) before claiming more.

## G2 — Governance model expressed

**Owner:** governance designer and implementation lead. **Entry:** G1 and approved policy source. **Actions:** model authority origin, grants, attenuation, lifecycle, accountable parties, required evidence, policy precedence, notice and remedy. **Evidence:** versioned artifacts, applicable schema/profile checks and mapping to source requirements. **Stop:** ambiguous scope, invented authority, unsupported parent chain, or missing control document.

Use [Basic Governed Decision](../examples/basic-governed-decision/) to orient the model. Its fixture identifiers are synthetic, not real-world authority.

## G3 — Runtime path implemented

**Owner:** implementation lead and enforcement owner. **Entry:** G2 with current authority and evidence. **Actions:** implement contextual evaluation, constrained enforcement and a separate observation of actual execution; preserve decision and effect evidence. **Evidence:** real implementation source revision, environment, execution traces, policy decisions, enforcement outcomes, receipt and event identifiers. **Stop:** Boolean adapter output alone, unverified issuer, or missing enforcement result.

## G4 — Negative and lifecycle paths exercised

**Owner:** tester and security/review owner. **Entry:** G3. **Actions:** test valid scope, amplification, revoked parent, stale/unavailable evidence, conflicting status, partial execution and recovery. **Evidence:** reproducible tests, expected versus observed results, revocation effective time and limitations. **Stop:** permissive fallback, unrecorded unknowns, missing negative cases or inability to interrupt.

```bash
python scripts/gaam.py run-vectors --pattern 'delegation-*.json' python conformance-kit/reference_adapter.py
```

The reference adapter is repository-authored and only checks its abstract vector contract. Replace it with your own independent implementation for a genuine pilot. See [test and evidence guidance](test-and-evidence.md).

## G5 — Evidence and claims reviewed

**Owner:** evidence custodian and reviewer. **Entry:** G0–G4 with attributable evidence. **Actions:** prepare implementation report, evidence manifest, evaluated requirement set, assessment relationship, exceptions, privacy and retention disclosures. **Evidence:** accepted-by-pilot-review report and integrity-checked references; any claimed GAAM assurance level must be separately justified. **Stop:** unverifiable provenance, missing limitations, self-review presented as independence, or missing externally run implementation.

Use [implementation reports](../implementation-reports/README.md). An independently implemented pilot is *not* automatically accepted into the repository's external E2 readiness gate; it must pass that intake's distinct acceptance process.

## G6 — Pilot disposition and closeout

**Owner:** sponsor and review authority. **Entry:** a defensible G5 result **or** a documented failed/blocked pilot. **Actions:** publish outcomes, unresolved issues, affected-party observations, necessary specification clarifications, residual risks and explicit continuation/termination decision. **Evidence:** signed/dispositioned closeout, references to findings and follow-up owners. **Stop:** an undocumented claim of production readiness, certification, independence or interoperability.

## Local dry run, distinct from pilot acceptance

```bash
python scripts/validate_pilot_readiness.py --run
```

This executes selected published validators and the negative boundary self-tests; it checks **entry-path reproducibility**, not G0 sponsor approval, not a deployed policy enforcement point, and not independent implementation. Treat its result as repository-authored E1 tooling evidence only. The reviewer must not pre-check G0–G6 simply because this command prints PASS.
