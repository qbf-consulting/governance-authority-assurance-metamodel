---
title: "DTG/VTI Semantic Boundary Cases"
permalink: /mappings/dtg-vti-gaam-boundary-cases/
parent: "Mappings and Source Crosswalks"
grand_parent: "Project & Evolution"
nav_order: 9
artifact_type: "Informative metamodel research"
normative_status: "Informative"
---
# DTG/VTI Semantic Boundary Cases

{% include gaam-meta.html %}


This is a **semantic falsification exercise**, not a conformance suite or implementation test. Use the [pinned assessment](dtg-vti-gaam-expressivity.md) to interpret source versions, applicability and limits.

| Case | Valid representation | Counterexample and expected refusal or distinction | Relevant VTI | Relevant GAAM |
| --- | --- | --- | --- | --- |
| B1 Client access versus authority | Client has current permitted role, capability and scope. | Client has authentic key, active session and callable method but lacks authority for requested effect. Authentication cannot imply authorization. | VTI-ACL-001; VTI-ACL-030; VTI-CMP-030 | GAAM-AUTH-003; GAAM-ART-005; GAAM-EFF-002 |
| B2 Nested context delegation | Parent grant explicitly covers descendant and valid child scope. | Delegation expands beyond parent or ancestry scope. A technical path is not an additional independent authority source. | VTI-CTX-017; VTI-ACL-071; VTI-ACL-073 | GAAM-AUTH-002; GAAM-DEL-003; GAAM-DEL-010 |
| B3 Collective approval versus execution | Authorized electorate determines result; separately governed decision executes a bounded change. | A correctly counted election is treated as automatic authority for an unrelated ACL mutation. Voting protocol does not grant authority by itself. | VTI-VOT-010; VTI-VOT-071; VTI-VOT-081; VTI-VTC-022 | GAAM-GF-007; GAAM-POL-002; GAAM-EFF-002 |
| B4 Cross-community recognition | A locally recognizes B under explicit mapping and policy constraints. | A silently recognizes C because B recognizes C, or imports stronger foreign role rights than local equivalents. | VTI-REG-023; VTI-REG-024 | GAAM-CTX-002; GAAM-REG-006; GAAM-GRAPH-007 |
| B5 Unacknowledged listing and repudiation | VTN lists party without consent; acknowledgement/repudiation is separately represented and available for reliance. | VTN listing becomes two-sided membership or unqualified endorsement; repudiation is suppressed or treated as erasure. | VTI-VTN-010; VTI-VTN-011; VTI-VTN-012; VTI-VTN-013 | GAAM-GRAPH-008; GAAM-REG-004; GAAM-REL-001 |
| B6 Withdrawal and history | New decisions use current authority; historical records retain past operative state and observed effects. | Expired entry still grants new authority; current state is imposed retroactively; revoked grant is assumed to undo effects already completed. | VTI-ACL-080; VTI-CMP-040; VTI-OPR-032 | GAAM-LIFE-004; GAAM-RUN-003; GAAM-EVT-002 |

## Falsification standard

A **core GAAM expressivity failure** requires a material VTI governance distinction that cannot be represented by existing GAAM constructs *or an admissible VTI-specific specialization* without contradiction or semantic loss. Merely lacking a class named `TrustContext`, `VTC`, `BallotBox`, or `VTNListing` does not meet the test. A source that remains unresolved is **indeterminate**, not evidence of deficiency.

**B1–B2** test whether GAAM distinguishes institutional authority, local control and effective delegated scope. **B3** tests authority for collective formation separately from the ballot protocol and execution. **B4–B5** test directed, contested assertions without automatic consent or transitive recognition. **B6** tests temporal status, authority withdrawal, historical evidence and irreversible effects as independent facts.

All six scenarios can be represented with the cited normative GAAM concepts plus declared VTI context rules. This is an analysis of expressible outcomes; no fixture was executed and no third-party assessor reviewed an implementation. Material future changes in VTI or a concrete counterexample should trigger re-evaluation rather than speculative expansion of GAAM.
