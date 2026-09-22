---
title: "Normative Requirement Catalogue"
permalink: /specification/requirements/
parent: "Documentation"
nav_order: 6
artifact_type: "Generated normative requirement catalogue"
normative_status: "Derivative index"
---
# Normative Requirement Catalogue

{% include gaam-meta.html %}

> This catalogue is generated from the authoritative human-readable Candidate Specification. It is a navigation and traceability aid, not an independent normative source. If this catalogue and the specification differ, the specification controls.

**Source:** [Governance, Authority and Assurance Metamodel v0.9.0](../specification/governance-authority-assurance-metamodel.md)  
**Requirement count:** 190  
**Identifier form:** `GAAM-<SECTION>-<NUMBER>`

## CORE

| Requirement | Normative text |
|---|---|
| `GAAM-CORE-001` | A governance framework **MUST** identify the classes of governed entities within its scope. |
| `GAAM-CORE-002` | Where a governed entity is a machine, software component or agent, the framework **MUST** identify one or more accountable persons or organisations and the basis of their accountability. |
| `GAAM-CORE-003` | A framework **MUST** define each governed actor role, including its responsibilities, eligibility, authority limits, obligations and lifecycle. |
| `GAAM-CORE-004` | A framework permitting agent participation **MUST** state which agent classes are permitted and which effects each class may request, recommend, approve or perform. |
| `GAAM-CORE-005` | A role definition **MUST** specify the conditions under which the role is assigned, activated, suspended, transferred and terminated. |

## AUTH

| Requirement | Normative text |
|---|---|
| `GAAM-AUTH-001` | Every authority recognised by a framework **MUST** identify its source. |
| `GAAM-AUTH-002` | Authority **MUST** be bounded by sufficient scope information to determine whether a proposed effect falls within it. |
| `GAAM-AUTH-003` | Identification, authentication, possession of a credential, registry inclusion or technical capability **MUST NOT** be treated as sufficient proof of authority unless the framework explicitly defines and validates the authority semantics represented by that artifact or state. |
| `GAAM-AUTH-004` | A framework **MUST** distinguish capability from authority. |
| `GAAM-AUTH-005` | Systems enforcing a framework **MUST NOT** admit a consequential effect solely because an actor possesses the technical means to cause it. |
| `GAAM-AUTH-006` | A framework **MUST** identify conflicts that may arise among authorities and the procedure for resolving or containing them. |
| `GAAM-AUTH-007` | Where authorities overlap, the framework **MUST** define precedence, coordination, refusal or escalation semantics. |
| `GAAM-AUTH-008` | Emergency authority **MUST** be narrowly scoped, time-limited, attributable, reviewable and subject to post-event accountability. |

## DEL

| Requirement | Normative text |
|---|---|
| `GAAM-DEL-001` | A delegation **MUST** identify the delegator, delegate, delegated authority, effective period and termination conditions. |
| `GAAM-DEL-002` | Redelegation **MUST** be expressly authorised. |
| `GAAM-DEL-003` | Each delegation hop **MUST NOT** enlarge the authority available at the parent hop unless an independently valid authority source authorises the enlargement. |
| `GAAM-DEL-004` | Delegated authority **MUST** remain traceable to its authority source and, where applicable, to the originating principal. |
| `GAAM-DEL-005` | Suspension, revocation or expiry of parent authority **MUST** affect descendant authority according to explicit propagation rules. |
| `GAAM-DEL-006` | Delegation **MUST NOT** extinguish the accountability of a delegator, principal, operator, provider or other party whose accountability is established by law, agreement or framework policy. |
| `GAAM-DEL-007` | A delegation **MUST NOT** become active before required acceptance, registration, verification or other activation conditions are met. |
| `GAAM-DEL-008` | The framework **MUST** define whether delegation is transferable and whether an agent or actor may substitute another delegate. |
| `GAAM-DEL-009` | Material substitution of an agent, model, operator, toolchain or execution environment **MUST** trigger reassessment where it may affect authority, assurance or risk. |
| `GAAM-DEL-010` | A multi-hop delegation decision **MUST** validate each active hop, parent-child scope compatibility, originating-principal continuity, redelegation permission and revocation state. |
| `GAAM-DEL-011` | A framework **MUST** define maximum delegation depth or the policy by which depth is determined. |
| `GAAM-DEL-012` | Where authority is divided among multiple delegates, the framework **MUST** define whether branches are independent, cumulative, mutually exclusive or jointly controlled. |
| `GAAM-DEL-013` | Where delegated branches converge on one effect, the aggregate effect **MUST** be evaluated against the originating authority and applicable aggregate limits. |

## POL

| Requirement | Normative text |
|---|---|
| `GAAM-POL-001` | A framework **MUST** define how conflicts among permissions, prohibitions, obligations and constraints are resolved. |
| `GAAM-POL-002` | A framework **MUST** identify the authority under which a permission, prohibition, obligation or constraint is established. |
| `GAAM-POL-003` | Machine-actionable rules **MUST** be traceable to their normative policy source and the authority that approved that source. |
| `GAAM-POL-004` | A governance framework **MUST** define precedence when human-readable normative text and machine-actionable representations conflict. |
| `GAAM-POL-005` | Unless the framework explicitly designates a machine-actionable representation as co-normative and defines equivalence tests, the human-readable normative text **MUST** prevail. |

## EVID

| Requirement | Normative text |
|---|---|
| `GAAM-EVID-001` | A framework **MUST** define the classes of claims that may be relied upon and the evidence, provenance, status and assurance needed for each class. |
| `GAAM-EVID-002` | Evidence relied upon for a consequential decision **MUST** have sufficient provenance to identify its origin and relevant transformations. |
| `GAAM-EVID-003` | A framework **MUST** define freshness requirements for evidence whose relevance may change over time. |
| `GAAM-EVID-004` | An inability to validate required evidence **MUST** result in denial, restriction, suspension or human review according to framework policy; it **MUST NOT** silently result in acceptance. |

## ASSUR

| Requirement | Normative text |
|---|---|
| `GAAM-ASSUR-001` | A framework **MUST** distinguish verification results from broader assurance conclusions. |
| `GAAM-ASSUR-002` | Verification and assessment results **MUST** identify the criteria, evaluator, time, scope, limitations and evidence used. |
| `GAAM-ASSUR-003` | Assurance **MUST NOT** be represented as permanent where the underlying conditions, evidence or system state may change. |
| `GAAM-ASSUR-004` | A framework **MUST** define the validity, renewal, suspension, withdrawal and review conditions of each assurance conclusion it recognises. |
| `GAAM-ASSUR-005` | The framework **MUST** define what each assurance form establishes and what it does not establish. |
| `GAAM-ASSUR-006` | Assurance providers **MUST** disclose material conflicts of interest and the basis of their competence and authority. |
| `GAAM-ASSUR-007` | Assurance results **MUST** be challengeable and correctable when materially wrong. |
| `GAAM-ASSUR-008` | A Continuous Assurance Profile framework **MUST** define monitored controls, evidence sources, sampling or event frequency, thresholds, drift conditions, escalation and suspension actions. |
| `GAAM-ASSUR-009` | A continuous assurance service **MUST** identify data gaps, blind spots and periods during which assurance could not be maintained. |
| `GAAM-ASSUR-010` | A trust mark **MUST** identify or resolve to its issuer, scope, criteria, validity, status and limitations. |
| `GAAM-ASSUR-011` | A trust mark **MUST NOT** imply broader assurance than the underlying assessment supports. |

## DEC

| Requirement | Normative text |
|---|---|
| `GAAM-DEC-001` | A trust decision **MUST** be attributable to a decision-maker or accountable decision service. |
| `GAAM-DEC-002` | A trust path, credential, registry entry, reputation value or assurance mark **MUST NOT** by itself constitute a trust decision. |
| `GAAM-DEC-003` | A decision **MUST** be evaluated in the context of the relying party’s applicable policy, purpose and risk tolerance. |
| `GAAM-DEC-004` | A receipt **MUST** minimise disclosed information while preserving sufficient provenance for review and reconstruction. |

## EFF

| Requirement | Normative text |
|---|---|
| `GAAM-EFF-001` | A framework **MUST** identify the consequential effect classes within its scope. |
| `GAAM-EFF-002` | A consequential effect **MUST NOT** be admitted unless the applicable authority, policy, evidence and runtime conditions have been evaluated to the level required by the framework. |

## CTX

| Requirement | Normative text |
|---|---|
| `GAAM-CTX-001` | A framework **MUST** identify the governance contexts in which its requirements apply. |
| `GAAM-CTX-002` | Cross-context reliance **MUST** be governed by explicit recognition, mapping or conflict-resolution rules. |

## EVT

| Requirement | Normative text |
|---|---|
| `GAAM-EVT-001` | A framework **MUST** define the governance events that materially affect authority, assurance, status, eligibility, policy or accountability. |
| `GAAM-EVT-002` | Material governance events **MUST** be attributable, time-stamped and reconstructable. |

## ACC

| Requirement | Normative text |
|---|---|
| `GAAM-ACC-001` | Every consequential effect **MUST** have at least one identifiable accountable party. |
| `GAAM-ACC-002` | Machine actors and agents **MUST NOT** be treated as the terminal point of accountability. |
| `GAAM-ACC-003` | A framework **MUST** define how accountability is allocated when multiple actors, agents, services, registries or authorities contribute to an effect. |

## HARM

| Requirement | Normative text |
|---|---|
| `GAAM-HARM-001` | A framework **MUST** identify material harms that may arise from governed effects, including cumulative and systemic harms where applicable. |
| `GAAM-HARM-002` | A framework governing consequential effects **MUST** define accessible challenge, review and remedy mechanisms. |
| `GAAM-HARM-003` | A framework **MUST** consider harms arising cumulatively across repeated low-level decisions where such harms are reasonably foreseeable. |
| `GAAM-HARM-004` | A framework **SHOULD** identify concentration, lock-in, exclusion, manipulation and market-power risks created by trust infrastructure. |

## REL

| Requirement | Normative text |
|---|---|
| `GAAM-REL-001` | A relationship used in an automated trust decision **MUST** have an unambiguous type and declared semantics. |
| `GAAM-REL-002` | A relationship **MUST NOT** imply broader authority or recognition than its declared scope. |
| `GAAM-REL-003` | Recognition **MUST NOT** be treated as delegation unless the relationship explicitly grants authority. |
| `GAAM-REL-004` | Accreditation **MUST NOT** be treated as a guarantee of every output produced by the accredited actor. |
| `GAAM-REL-005` | Registry inclusion **MUST NOT** be treated as universal trustworthiness. |
| `GAAM-REL-006` | Revocation and suspension semantics **MUST** identify the affected relationship, effective time, authority and propagation consequences. |

## GF

| Requirement | Normative text |
|---|---|
| `GAAM-GF-001` | A conforming governance framework **MUST** include a Primary Document and an authoritative Schedule of Controlled Documents. |
| `GAAM-GF-002` | The Primary Document **MUST** identify the exact framework version using a persistent identifier. |
| `GAAM-GF-003` | The framework **MUST** publish a conformance statement identifying the profiles and conformance targets claimed. |
| `GAAM-GF-004` | The framework **MUST** identify its official language or languages and SHOULD use BCP 47 language tags. |
| `GAAM-GF-005` | Where multiple official versions exist, the framework **MUST** define how inconsistencies are resolved. |
| `GAAM-GF-006` | The framework **MUST** identify where decision rights, enforcement powers, revision powers and emergency powers reside. |
| `GAAM-GF-007` | Where no single governing authority exists, the framework **MUST** identify the authority topology and the process by which valid governance decisions are formed. |
| `GAAM-GF-008` | Every framework **MUST** declare whether agents may participate and, if so, whether they may recommend, decide, transact, delegate, use tools, create sub-agents or produce binding effects. |
| `GAAM-GF-009` | Governance state required for a runtime decision **MUST** be discoverable, authenticated and sufficiently current for the decision context. |
| `GAAM-GF-010` | The framework **MUST** define how revisions are proposed, reviewed, approved, versioned, published, deprecated and withdrawn. |
| `GAAM-GF-011` | A publicly available framework **SHOULD** include a public review period for substantive revisions. |
| `GAAM-GF-012` | Material policy changes affecting active authority or runtime decisions **MUST** define transition and notification rules. |

## RUN

| Requirement | Normative text |
|---|---|
| `GAAM-RUN-001` | A framework governing consequential effects **MUST** define the minimum runtime governance envelope required for each effect class. |
| `GAAM-RUN-002` | A runtime decision **MUST** fail safely when required authority, policy, evidence, status or context cannot be validated. |
| `GAAM-RUN-003` | Runtime governance **MUST** evaluate current revocation and suspension state to the freshness required by the effect’s risk. |
| `GAAM-RUN-004` | Outcome semantics **MUST** be unambiguous to the enforcement point. |
| `GAAM-RUN-005` | Each consequential effect **MUST** produce or reference a decision receipt proportionate to the effect’s risk and accountability requirements. |
| `GAAM-RUN-006` | A receipt **MUST NOT** expose confidential evidence beyond what is necessary for authorised audit, review or challenge. |
| `GAAM-RUN-007` | The framework **MUST** define retention, access, disclosure, correction and deletion rules for receipts. |
| `GAAM-RUN-008` | Where authority, risk or evidence may materially change during execution, the framework **MUST** define conditions for re-evaluation, interruption or containment. |
| `GAAM-RUN-009` | Runtime revocation **MUST** be capable of stopping or constraining ongoing activity where technically and legally feasible. |

## AGT

| Requirement | Normative text |
|---|---|
| `GAAM-AGT-001` | A framework **MUST** define the attributes needed to identify an agent for governance purposes. |
| `GAAM-AGT-002` | A framework **MUST** define when changes to model, instructions, memory, tools, operator, provider, execution environment or policy configuration constitute a material change of agent state or identity. |
| `GAAM-AGT-003` | Material changes **MUST** trigger re-registration, renewed assurance, restricted operation or another declared lifecycle response where necessary. |
| `GAAM-AGT-004` | An agent performing an effect on behalf of a principal **MUST** carry or reference verifiable authority for that effect. |
| `GAAM-AGT-005` | The framework **MUST** identify the principal, operator, provider, deployer and supervisor roles applicable to each agent class and allocate accountability among them. |
| `GAAM-AGT-006` | Agent authority **SHOULD** be bound to a task, purpose or effect class wherever practical. |
| `GAAM-AGT-007` | Tool access **SHOULD** be limited to what is necessary for the authorised task. |
| `GAAM-AGT-008` | An agent **MUST NOT** infer authority from mere access to accounts, credentials, data, APIs or tools. |
| `GAAM-AGT-009` | An agent or supervising service **MUST** evaluate applicable governance constraints before executing a consequential plan step. |
| `GAAM-AGT-010` | Where an agent cannot determine whether a planned effect is authorised, it **MUST** deny, restrict or escalate rather than assume permission. |
| `GAAM-AGT-011` | An agent **MUST NOT** create a sub-agent, substitute another agent or redelegate authority unless explicitly permitted. |
| `GAAM-AGT-012` | A sub-agent **MUST** receive no more authority than the delegating agent is authorised to redelegate. |
| `GAAM-AGT-013` | The originating principal and accountable-party chain **MUST** remain discoverable across sub-agent relationships. |
| `GAAM-AGT-014` | A framework permitting multi-agent coordination **MUST** define how authority, task state, evidence, obligations and accountability are partitioned and reconciled. |
| `GAAM-AGT-015` | Coordination protocols **MUST NOT** be assumed to provide governance semantics unless those semantics are explicitly defined and validated. |
| `GAAM-AGT-016` | Where multiple agents contribute to one effect, the decision receipt **MUST** identify the material contributions and accountable parties. |
| `GAAM-AGT-017` | Tools capable of producing consequential effects **MUST** enforce or receive sufficient authority and policy context to prevent unauthorised invocation. |
| `GAAM-AGT-018` | Tool outputs used as evidence **MUST** carry provenance and integrity appropriate to the decision. |
| `GAAM-AGT-019` | A framework requiring human oversight **MUST** specify who performs it, when it occurs, what information is available, and what intervention powers exist. |
| `GAAM-AGT-020` | A guardian or supervisory agent **MUST** itself be governed by explicit authority, constraints and accountability. |
| `GAAM-AGT-021` | A framework **MUST** define mechanisms to suspend, isolate, contain or terminate an agent when authority, assurance or safety conditions fail. |
| `GAAM-AGT-022` | Termination **MUST** address outstanding tasks, delegated authority, retained data, tools, obligations and evidence preservation. |

## GRAPH

| Requirement | Normative text |
|---|---|
| `GAAM-GRAPH-001` | Graph relationships used for automated decisions **MUST** be typed, scoped, attributable, time-bounded where applicable and linked to status or revocation semantics. |
| `GAAM-GRAPH-002` | A graph path **MUST** be treated as evidence for a decision, not as the decision itself. |
| `GAAM-GRAPH-003` | Each material graph assertion **MUST** identify the asserting party and authority basis. |
| `GAAM-GRAPH-004` | A graph implementation **MUST** provide integrity and provenance sufficient to detect unauthorised alteration of relied-upon assertions. |
| `GAAM-GRAPH-005` | Derived edges or computed trust values **MUST** identify their derivation method, input sources and applicable policy. |
| `GAAM-GRAPH-006` | A framework **MUST** define permitted traversal depth, relationship types, path constraints and evidence thresholds for each automated decision class. |
| `GAAM-GRAPH-007` | A relying party **MUST** apply its own policy to determine whether a discovered path is sufficient. |
| `GAAM-GRAPH-008` | A framework **MUST** define how conflicting, stale, superseded or contested graph assertions are represented and evaluated. |
| `GAAM-GRAPH-009` | Absence of a negative assertion **MUST NOT** automatically be interpreted as positive trust unless the framework explicitly justifies that inference. |

## REG

| Requirement | Normative text |
|---|---|
| `GAAM-REG-001` | Registry inclusion **MUST** have explicit semantics and **MUST NOT** be represented as general trustworthiness. |
| `GAAM-REG-002` | A registry framework **MUST** define who may create, update, suspend, revoke, correct and archive each record class. |
| `GAAM-REG-003` | Registry records used for decisions **MUST** expose sufficient status, provenance, authority and version information. |
| `GAAM-REG-004` | A registry **MUST** provide a correction and dispute path for materially incorrect or unauthorised records. |
| `GAAM-REG-005` | Federation **MUST** distinguish data replication, technical interoperability, recognition of authority and reliance upon determinations. |
| `GAAM-REG-006` | Recognition of another registry **MUST** state the accepted record classes, purposes, assurance thresholds, jurisdictional limits and withdrawal conditions. |

## OBS

| Requirement | Normative text |
|---|---|
| `GAAM-OBS-001` | Observability requirements **MUST** be proportionate and **MUST** account for privacy, confidentiality, minimisation and security. |
| `GAAM-OBS-002` | The absence of observable data **MUST NOT** be presented as evidence of compliant behaviour. |

## RISK

| Requirement | Normative text |
|---|---|
| `GAAM-RISK-001` | Risk assessment **MUST** examine authority paths, evidence paths, dependencies, graph edges, delegated capabilities and affected parties, not only roles and processes. |
| `GAAM-RISK-002` | A framework **MUST** define effect classes or thresholds that require enhanced evidence, approval, assurance, monitoring or human review. |
| `GAAM-RISK-003` | Controls relied upon to prevent high-impact effects **MUST** be testable or auditable and linked to accountable owners. |

## RED

| Requirement | Normative text |
|---|---|
| `GAAM-RED-001` | A framework **MUST** identify affected-party classes, including persons who are not members of the trust community. |
| `GAAM-RED-002` | Affected parties **SHOULD** receive notice of consequential decisions where lawful and practicable. |
| `GAAM-RED-003` | A framework **MUST** define the explanation information available for consequential decisions, including reason codes, applicable policy and review route. |
| `GAAM-RED-004` | A challenge mechanism **MUST** permit submission of corrections, contrary evidence and claims of unauthorised action. |
| `GAAM-RED-005` | Review **MUST** be performed by an actor or process with authority to confirm, modify, reverse or remedy the decision. |
| `GAAM-RED-006` | A framework **MUST** define response and resolution time expectations proportionate to the potential harm. |
| `GAAM-RED-007` | A framework **MUST** identify which remedies are available, who may order them and how compliance is verified. |
| `GAAM-RED-008` | Where an effect depends on multiple governance frameworks, the frameworks **SHOULD** define coordination, evidence sharing, jurisdiction and fallback procedures for disputes. |

## MAG

| Requirement | Normative text |
|---|---|
| `GAAM-MAG-001` | A machine-actionable package **MUST** be traceable to the authoritative human-readable framework. |
| `GAAM-MAG-002` | The package **MUST** identify its version, effective period, status and integrity mechanism. |
| `GAAM-MAG-003` | A material package change **MUST** follow the framework’s revision and transition requirements. |
| `GAAM-MAG-004` | A package **MUST NOT** silently broaden authority or reduce obligations relative to the authoritative framework. |
| `GAAM-MAG-005` | Conformance tests **SHOULD** include valid, invalid and boundary-condition examples. |

## PROF

| Requirement | Normative text |
|---|---|
| `GAAM-PROF-001` | A profile claim **MUST** identify the specification version, profile version, applicable conformance targets, exclusions and evidence location. |
| `GAAM-PROF-002` | A framework **MUST NOT** claim a profile when a mandatory category or requirement is omitted without an explicitly permitted exception. |
| `GAAM-PROF-003` | A composite profile claim **MUST** satisfy dependency closure and **MUST NOT** suppress conflicting or additional requirements without an explicit resolution rule. |
| `GAAM-PROF-004` | A partial implementation **MUST NOT** claim full profile conformance. |

## CONF

| Requirement | Normative text |
|---|---|
| `GAAM-CONF-001` | Conformance claims **MUST** be scoped to an identified target and **MUST NOT** be generalised to related entities or transactions without evidence. |
| `GAAM-CONF-002` | Framework conformance **MUST NOT** be presented as proof that every governed actor, agent, decision or transaction conforms. |
| `GAAM-CONF-003` | An agent conformance claim **MUST NOT** be presented as proof that every future action of that agent is authorised or safe. |
| `GAAM-CONF-004` | Evidence **MUST** be sufficient to reproduce or independently evaluate the conformance conclusion to the degree required by the claimed profile. |
| `GAAM-CONF-005` | Exceptions **MUST** identify the requirement, rationale, authority, duration, risk, compensating control and review date. |
| `GAAM-CONF-006` | A framework **MUST** define classification, notification, remediation, suspension and appeal procedures for non-conformance. |

## SEC

| Requirement | Normative text |
|---|---|
| `GAAM-SEC-001` | Governance-critical artifacts **MUST** be protected against unauthorised modification and rollback. |
| `GAAM-SEC-002` | Frameworks **MUST** define recovery and continuity procedures for unavailable or compromised governance services. |

## PRIV

| Requirement | Normative text |
|---|---|
| `GAAM-PRIV-001` | Evidence, receipts and observability data **MUST** be minimised to what is necessary for governance, assurance, accountability and lawful obligations. |
| `GAAM-PRIV-002` | Access to sensitive governance records **MUST** be controlled, auditable and purpose-bound. |

## RES

| Requirement | Normative text |
|---|---|
| `GAAM-RES-001` | A framework **MUST** identify critical dependencies and define safe behaviour when they are unavailable or untrustworthy. |

## ART

| Requirement | Normative text |
|---|---|
| `GAAM-ART-001` | A machine-actionable authority record **MUST** identify its authority source, issuer, subject, permitted effects, scope, effective period, status, revocation authority and accountable parties. |
| `GAAM-ART-002` | An authority record **MUST** distinguish permissions, prohibitions, obligations and constraints. |
| `GAAM-ART-003` | A system **MUST NOT** treat an authority record as operative when its status, effective period, governing context or integrity cannot be validated. |
| `GAAM-ART-004` | A delegation record **MUST** identify its parent authority, delegator, delegate, delegated scope, effective period, redelegation rule, status and propagation behaviour. |
| `GAAM-ART-005` | Effective child authority **MUST** be no broader than the intersection of valid parent authority, delegated scope, applicable policy, current context, active status, valid time and applicable constraints. |
| `GAAM-ART-006` | A delegation transition **MUST** emit or preserve a governance event sufficient to reconstruct the transition authority, time, prior state, new state and supporting evidence. |

## LIFE

| Requirement | Normative text |
|---|---|
| `GAAM-LIFE-001` | A conformant implementation **MUST** apply declared lifecycle states and transitions to governance-critical artifacts. |
| `GAAM-LIFE-002` | Lifecycle transition rules **MUST** identify the authority permitted to cause each transition and the evidence required for that transition. |
| `GAAM-LIFE-003` | An invalid, unauthorised or out-of-sequence lifecycle transition **MUST** fail without activating the requested governance state. |
| `GAAM-LIFE-004` | Suspension, revocation, expiry, supersession and termination **MUST** have explicit effects on dependent artifacts and active decisions. |
| `GAAM-LIFE-005` | Archived governance artifacts **MUST** remain reconstructable but **MUST NOT** be treated as operative unless explicitly restored through an authorised transition. |

## ASR

| Requirement | Normative text |
|---|---|
| `GAAM-ASR-001` | An assurance assertion **MUST** identify its subject, evaluated property, criteria, evaluator, method, evidence, scope, governance context, validity period, status, limitations and challenge route. |
| `GAAM-ASR-002` | Assurance labels from different domains or profiles **MUST NOT** be treated as equivalent without an explicit mapping of criteria, scope, evidence, evaluator competence, context and validity. |
| `GAAM-ASR-003` | Stale, suspended, withdrawn or contradicted assurance **MUST** trigger profile-defined safe behaviour. |

## PCOMP

| Requirement | Normative text |
|---|---|
| `GAAM-PCOMP-001` | Every profile other than the Foundation Profile **MUST** declare the Foundation Profile as a dependency. |
| `GAAM-PCOMP-002` | A profile **MUST** declare its conformance targets, normative requirement mappings, required artifacts, required evidence, required tests, permitted exclusions and dependencies. |

## OUT

| Requirement | Normative text |
|---|---|
| `GAAM-OUT-001` | A trust decision **MUST** use a declared outcome vocabulary and identify any conditions attached to the outcome. |
| `GAAM-OUT-002` | The base outcome vocabulary **MUST** support permit, deny, permit-with-conditions, restrict, suspend, require-additional-evidence, require-additional-approval, route-for-review and terminate. |
| `GAAM-OUT-003` | A decision receipt for a consequential effect **MUST** identify the decision, applicable authority, policy, evidence references, assurance references, outcome, conditions, decision time, enforcement point and accountable party. |

## SAFE

| Requirement | Normative text |
|---|---|
| `GAAM-SAFE-001` | Governance evidence and receipts **MUST** be limited to information necessary for the declared purpose and review obligations. |
| `GAAM-SAFE-002` | A high-impact system **MUST** define interruption authority, degraded operation, safe failure, recovery and post-event review. |
| `GAAM-SAFE-003` | Emergency authority **MUST** be time-bounded, purpose-bounded, attributable and subject to independent or otherwise conflict-controlled review. |

## APR

| Requirement | Normative text |
|---|---|
| `GAAM-APR-001` | A consequential effect **MUST** identify affected-party notice, explanation, challenge, review and remedy arrangements proportionate to the effect. |
| `GAAM-APR-002` | A review mechanism **MUST** have practical authority to suspend, reverse, correct or remediate an outcome. |
| `GAAM-APR-003` | Remedy completion **MUST** produce evidence linked to the original decision and effect. |

## SYS

| Requirement | Normative text |
|---|---|
| `GAAM-SYS-001` | A high-impact framework **MUST** define how individual effect records are aggregated to detect recurring, cohort-level or systemic harm. |
| `GAAM-SYS-002` | Detection of a declared systemic-harm threshold **MUST** trigger a governed intervention and preserve evidence of the response. |

## MKT

| Requirement | Normative text |
|---|---|
| `GAAM-MKT-001` | Registry inclusion, accreditation or recognition **MUST NOT** be represented as universal trustworthiness. |
| `GAAM-MKT-002` | A framework **MUST** disclose material conflicts of interest affecting registry, accreditation or assurance decisions. |
| `GAAM-MKT-003` | A high-impact recognition arrangement **MUST** address opaque exclusion, portability barriers, self-preferencing and unsupported equivalence claims. |

