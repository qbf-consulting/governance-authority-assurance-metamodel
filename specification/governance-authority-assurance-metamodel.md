---
title: "Governance, Authority and Assurance Metamodel Specification"
permalink: /specification/gaam-v0.9.0/
parent: "Normative Specification"
artifact_type: "Normative specification"
normative_status: "Normative"
---
# Governance, Authority and Assurance Metamodel Specification

{% include gaam-meta.html %}

**Version:** 0.9.0  
**Status:** Candidate Specification  
**Release date:** 16 July 2026  
**Repository:** `governance-authority-assurance-metamodel`  
**Intended audience:** Governance designers, standards developers, ecosystem architects, assurance providers, registry operators, agent-system implementers, regulators, auditors and reviewers.

---

### Document status

This document is the Candidate Specification of the Governance, Authority and Assurance Metamodel (GAAM). It establishes an independent, implementation-neutral specification for representing and governing authority, delegation, evidence, trust decisions, accountability, assurance, agentic execution and decentralised trust relationships.

Version 0.9.0 stabilises the intended normative surface for implementation, interoperability and assurance review. A conformance claim against this release MUST identify the applicable profile set, conformance target, assurance level, test-suite version, evidence, limitations and assessment independence. Candidate status does not constitute certification, universal trustworthiness or independent interoperability. Breaking normative changes remain possible only through the candidate change-control process defined by this repository.

The specification is protocol-neutral, vendor-neutral and ecosystem-neutral. It does not require any particular identifier, credential, registry, agent communication, policy, transport or cryptographic technology.

---

## 1. Introduction

Digital trust ecosystems increasingly include machine actors, distributed registries, automated policy evaluation, cross-domain recognition, delegated authority and software agents capable of producing consequential effects. A governance framework designed only as a static collection of policies and controlled documents cannot adequately govern these environments.

This specification defines a metamodel for constructing governance frameworks that govern not only participants and documents, but also the authority, evidence, decisions and effects through which trust is operationalised.

The specification is based on five propositions:

1. Trust is contextual. It is not an intrinsic property of an entity, credential, registry entry or graph path.
2. Capability does not imply authority. A system may be technically able to perform an action without being authorised to do so.
3. Delegation does not dissolve accountability. Authority may move through a chain, but responsibility must remain attributable.
4. Assurance is time-bounded and evidence-based. Certification alone cannot establish continuing fitness for every context or transaction.
5. Governance must remain effective at runtime. Consequential effects must be admitted, denied, constrained, suspended or escalated according to applicable authority, policy, evidence and risk.

A conforming governance framework therefore describes both institutional arrangements and operational governance mechanisms. It identifies who may govern, who may act, what authority they possess, how authority may be delegated, what evidence may be relied upon, how trust decisions are made, which effects may occur, how decisions are recorded, and how affected parties may challenge or remedy outcomes.

### 1.1 Purpose

The purpose of this specification is to provide a complete, implementation-independent metamodel for governance frameworks that operate across human, organisational, machine and decentralised trust environments.

### 1.2 Scope

This specification defines:

- the required structure of a governance framework;
- core concepts and relationships for governance, authority, delegation, evidence, trust decisions and effects;
- requirements for agentic-system governance;
- requirements for decentralised trust-graph governance;
- requirements for runtime governance and continuous assurance;
- controlled-document categories;
- governance framework profiles;
- conformance targets and claims;
- requirements for accountability, contestability, incident response and redress;
- requirements for machine-actionable governance artifacts.

This specification does not define:

- a cryptographic algorithm;
- a credential data model;
- a decentralised identifier method;
- a registry query protocol;
- an agent communication protocol;
- a policy language;
- a transport binding;
- a reference implementation;
- a legal agreement for any particular ecosystem.

A governance framework may reference external specifications for these matters.

### 1.3 Design goals

This specification is designed to be:

- **institutionally grounded**, by requiring legal, contractual, communal or organisational bases for authority;
- **operationally executable**, by connecting policy to machine-testable rules and runtime governance;
- **technology-neutral**, by avoiding dependencies on particular protocols or data formats;
- **composable**, by supporting profiles and extension frameworks;
- **cross-domain**, by supporting recognition among independent governance frameworks;
- **agent-ready**, by treating software agents as governed actors without treating them as accountability endpoints;
- **graph-aware**, by requiring typed, contextual and contestable relationship semantics;
- **evidence-driven**, by requiring provenance, freshness and decision reconstruction;
- **rights-preserving**, by requiring challenge, review and redress for consequential effects.

### 1.4 Normative language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY** and **OPTIONAL** are to be interpreted as described in BCP 14 when, and only when, they appear in all capitals.

### 1.5 Conformance notation

Normative requirements are assigned stable identifiers in the form `GAAM-<SECTION>-<NUMBER>`. A governance framework MAY restate a requirement in a controlled document, but it MUST preserve the requirement identifier or provide a traceable mapping.

---

## 2. Core metamodel

### 2.1 Governed entity

A **governed entity** is any person, organisation, public authority, software system, agent, device, service, registry, credential, record, policy artifact, evidence artifact or other object to which governance requirements apply.

A governed entity may be a legal person, a technical component or an informational artifact. The classification of an entity MUST NOT be used to obscure the person or organisation accountable for its operation.

**GAAM-CORE-001:** A governance framework **MUST** identify the classes of governed entities within its scope.

**GAAM-CORE-002:** Where a governed entity is a machine, software component or agent, the framework **MUST** identify one or more accountable persons or organisations and the basis of their accountability.

### 2.2 Actor

An **actor** is a governed entity capable of requesting, approving, denying, performing, supervising, recording or being affected by an action.

An actor may act in different roles in different contexts. An actor does not acquire authority merely by being identified, registered, authenticated or technically capable.

**GAAM-CORE-003:** A framework **MUST** define each governed actor role, including its responsibilities, eligibility, authority limits, obligations and lifecycle.

### 2.3 Principal

A **principal** is an actor whose interests, rights, resources or authority are represented or exercised by another actor.

A principal may be a person, organisation, public authority or, where explicitly permitted, another agent. An agent that is itself a principal does not remove the need to identify an accountable human or organisational chain.

### 2.4 Agent

An **agent** is a software actor capable of selecting or executing actions based on instructions, goals, context, policy, evidence or observed state.

Agent classes may include:

- advisory agents;
- transactional agents;
- custodial agents;
- orchestrator agents;
- supervisory agents;
- guardian agents;
- policy enforcement agents;
- infrastructure agents.

**GAAM-CORE-004:** A framework permitting agent participation **MUST** state which agent classes are permitted and which effects each class may request, recommend, approve or perform.

### 2.5 Role

A **role** is a context-specific capacity in which an actor participates.

A role may carry authority, obligations, eligibility requirements and prohibitions. Roles are not identities and SHOULD be separable from the actors that hold them.

**GAAM-CORE-005:** A role definition **MUST** specify the conditions under which the role is assigned, activated, suspended, transferred and terminated.

### 2.6 Authority

**Authority** is a recognised and bounded ability to permit, perform, approve, prohibit, delegate or constrain an effect.

Authority may arise from law, regulation, contract, governance policy, ownership, mandate, consent, community recognition or another valid source. Authority is contextual and may be limited by action, resource, subject, purpose, jurisdiction, time, value, risk, delegation depth, evidence, supervision or other conditions.

**GAAM-AUTH-001:** Every authority recognised by a framework **MUST** identify its source.

**GAAM-AUTH-002:** Authority **MUST** be bounded by sufficient scope information to determine whether a proposed effect falls within it.

**GAAM-AUTH-003:** Identification, authentication, possession of a credential, registry inclusion or technical capability **MUST NOT** be treated as sufficient proof of authority unless the framework explicitly defines and validates the authority semantics represented by that artifact or state.

### 2.7 Capability

A **capability** is a technical or operational ability to perform an action or produce an effect.

**GAAM-AUTH-004:** A framework **MUST** distinguish capability from authority.

**GAAM-AUTH-005:** Systems enforcing a framework **MUST NOT** admit a consequential effect solely because an actor possesses the technical means to cause it.

### 2.8 Delegation

A **delegation** is a bounded grant of authority from a delegator to a delegate.

A delegation includes, where applicable:

- delegator;
- delegate;
- originating principal;
- authority source;
- granted scope;
- purpose;
- conditions;
- obligations;
- effective period;
- acceptance;
- redelegation rights;
- supervision requirements;
- termination and revocation rules;
- accountability consequences.

**GAAM-DEL-001:** A delegation **MUST** identify the delegator, delegate, delegated authority, effective period and termination conditions.

**GAAM-DEL-002:** Redelegation **MUST** be expressly authorised.

**GAAM-DEL-003:** Each delegation hop **MUST NOT** enlarge the authority available at the parent hop unless an independently valid authority source authorises the enlargement.

**GAAM-DEL-004:** Delegated authority **MUST** remain traceable to its authority source and, where applicable, to the originating principal.

**GAAM-DEL-005:** Suspension, revocation or expiry of parent authority **MUST** affect descendant authority according to explicit propagation rules.

**GAAM-DEL-006:** Delegation **MUST NOT** extinguish the accountability of a delegator, principal, operator, provider or other party whose accountability is established by law, agreement or framework policy.

### 2.9 Permission, prohibition, obligation and constraint

A **permission** authorises an action or effect. A **prohibition** forbids it. An **obligation** requires an actor to perform an action upon a condition or event. A **constraint** limits how, when, where or under what conditions an action may occur.

**GAAM-POL-001:** A framework **MUST** define how conflicts among permissions, prohibitions, obligations and constraints are resolved.

**GAAM-POL-002:** A framework **MUST** identify the authority under which a permission, prohibition, obligation or constraint is established.

### 2.10 Policy, rule and control

A **principle** is a non-testable statement of intent or value. A **policy** is a human-auditable normative requirement or coherent set of requirements. A **rule** is a machine-testable expression of a requirement. A **control** is a safeguard intended to satisfy, enforce or provide evidence of a requirement.

**GAAM-POL-003:** Machine-actionable rules **MUST** be traceable to their normative policy source and the authority that approved that source.

**GAAM-POL-004:** A governance framework **MUST** define precedence when human-readable normative text and machine-actionable representations conflict.

**GAAM-POL-005:** Unless the framework explicitly designates a machine-actionable representation as co-normative and defines equivalence tests, the human-readable normative text **MUST** prevail.

### 2.11 Claim and assertion

A **claim** is a proposition that may be evaluated. An **assertion** is a claim made by an identified actor or artifact.

A signed, registered or credentialed assertion is not necessarily true, relevant, current or sufficient for a decision.

**GAAM-EVID-001:** A framework **MUST** define the classes of claims that may be relied upon and the evidence, provenance, status and assurance needed for each class.

### 2.12 Evidence

**Evidence** is information or an artifact used to support or challenge a claim, authority, verification result, assessment, decision or outcome.

Evidence attributes SHOULD include:

- producer or issuer;
- subject;
- creation time;
- validity interval;
- provenance;
- integrity protection;
- status and revocation source;
- confidentiality classification;
- permitted uses;
- assurance level;
- relationship to claims and decisions.

**GAAM-EVID-002:** Evidence relied upon for a consequential decision **MUST** have sufficient provenance to identify its origin and relevant transformations.

**GAAM-EVID-003:** A framework **MUST** define freshness requirements for evidence whose relevance may change over time.

**GAAM-EVID-004:** An inability to validate required evidence **MUST** result in denial, restriction, suspension or human review according to framework policy; it **MUST NOT** silently result in acceptance.

### 2.13 Verification and assessment

**Verification** is the evaluation of whether a defined condition holds. **Assessment** is a broader evaluation of whether an entity, process, artifact or system satisfies requirements, controls or a profile.

**GAAM-ASSUR-001:** A framework **MUST** distinguish verification results from broader assurance conclusions.

**GAAM-ASSUR-002:** Verification and assessment results **MUST** identify the criteria, evaluator, time, scope, limitations and evidence used.

### 2.14 Assurance

**Assurance** is a time-bounded and contextual conclusion about the confidence that may reasonably be placed in a claim, entity, process, control, decision or effect.

Assurance may be organisational, component-level, configuration-level, delegation-specific, transaction-specific, evidence-specific, continuous or outcome-specific.

**GAAM-ASSUR-003:** Assurance **MUST NOT** be represented as permanent where the underlying conditions, evidence or system state may change.

**GAAM-ASSUR-004:** A framework **MUST** define the validity, renewal, suspension, withdrawal and review conditions of each assurance conclusion it recognises.

### 2.15 Trust decision

A **trust decision** is a contextual determination made under policy about whether and under what conditions an effect should be allowed, denied, restricted, suspended, degraded or routed for review.

A trust decision SHOULD identify:

- decision-maker;
- decision context;
- proposed effect;
- relevant authority;
- applicable policy and rules;
- claims and evidence;
- verification and assessment results;
- risk and impact considerations;
- decision outcome;
- conditions and obligations;
- validity period;
- explanation or reason codes.

**GAAM-DEC-001:** A trust decision **MUST** be attributable to a decision-maker or accountable decision service.

**GAAM-DEC-002:** A trust path, credential, registry entry, reputation value or assurance mark **MUST NOT** by itself constitute a trust decision.

**GAAM-DEC-003:** A decision **MUST** be evaluated in the context of the relying party’s applicable policy, purpose and risk tolerance.

### 2.16 Effect

An **effect** is a material state change, decision consequence, transfer, disclosure, commitment, denial, approval, access, publication or other outcome governed by the framework.

Effects may be proposed, admitted, denied, restricted, suspended, reversed, remediated or contested.

**GAAM-EFF-001:** A framework **MUST** identify the consequential effect classes within its scope.

**GAAM-EFF-002:** A consequential effect **MUST NOT** be admitted unless the applicable authority, policy, evidence and runtime conditions have been evaluated to the level required by the framework.

### 2.17 Governance context

A **governance context** is the legal, institutional, contractual, technical, jurisdictional and operational environment in which authority, policy, evidence and decisions are interpreted.

**GAAM-CTX-001:** A framework **MUST** identify the governance contexts in which its requirements apply.

**GAAM-CTX-002:** Cross-context reliance **MUST** be governed by explicit recognition, mapping or conflict-resolution rules.

### 2.18 Governance event

A **governance event** is an event that changes governance-relevant state. Examples include registration, approval, delegation, acceptance, activation, invocation, denial, suspension, revocation, expiry, policy change, incident, appeal, remediation and restoration.

**GAAM-EVT-001:** A framework **MUST** define the governance events that materially affect authority, assurance, status, eligibility, policy or accountability.

**GAAM-EVT-002:** Material governance events **MUST** be attributable, time-stamped and reconstructable.

### 2.19 Accountability

**Accountability** is the obligation and capacity to explain, justify, answer for and remedy an action, decision, omission or effect.

**GAAM-ACC-001:** Every consequential effect **MUST** have at least one identifiable accountable party.

**GAAM-ACC-002:** Machine actors and agents **MUST NOT** be treated as the terminal point of accountability.

**GAAM-ACC-003:** A framework **MUST** define how accountability is allocated when multiple actors, agents, services, registries or authorities contribute to an effect.

### 2.20 Harm and remedy

**Harm** is a material adverse effect upon a person, organisation, community, market, institution or public interest. A **remedy** is an action intended to stop, reverse, correct, compensate or otherwise address harm or governance failure.

**GAAM-HARM-001:** A framework **MUST** identify material harms that may arise from governed effects, including cumulative and systemic harms where applicable.

**GAAM-HARM-002:** A framework governing consequential effects **MUST** define accessible challenge, review and remedy mechanisms.

---

## 3. Relationship model

A governance framework may represent relationships as graph edges, registry records, credentials, agreements, policy records or other artifacts. Regardless of representation, each governed relationship SHOULD have a typed semantic meaning.

### 3.1 Required relationship properties

A governed relationship SHOULD identify:

- relationship type;
- source and target;
- asserting party;
- authority basis;
- scope and purpose;
- governance context;
- effective period;
- status;
- assurance level;
- provenance;
- evidence references;
- permitted reliance;
- revocation or termination mechanism;
- challenge and correction route.

**GAAM-REL-001:** A relationship used in an automated trust decision **MUST** have an unambiguous type and declared semantics.

**GAAM-REL-002:** A relationship **MUST NOT** imply broader authority or recognition than its declared scope.

### 3.2 Canonical relationship classes

A framework MAY extend the following classes:

| Relationship | Meaning |
|---|---|
| `holds` | An actor holds a role |
| `governs` | An authority governs an entity, artifact, process or framework |
| `delegates` | A delegator grants bounded authority to a delegate |
| `recognises` | An actor accepts specified determinations or status from another source for a defined purpose |
| `accredits` | An authority determines that an actor is competent to perform a defined assessment or service |
| `asserts` | An actor makes a claim |
| `supports` | Evidence supports a claim, control, assessment or decision |
| `verifies` | A verifier evaluates whether a defined condition holds |
| `assesses` | An assessor evaluates conformity or fitness against criteria |
| `permits` | Authority or policy allows an effect |
| `prohibits` | Authority or policy forbids an effect |
| `constrains` | Policy or authority limits an action or effect |
| `depends-on` | An entity, decision or service relies upon another component or source |
| `accounts-for` | A party bears accountability for an action, decision or effect |
| `revokes` | An authorised actor withdraws a previously valid relationship or status |
| `suspends` | An authorised actor temporarily disables a relationship or status |
| `supersedes` | A new artifact or state replaces an earlier one |
| `appeals` | An affected or authorised party challenges a decision or effect |
| `remedies` | An action addresses harm, error or non-conformance |

### 3.3 Relationship invariants

**GAAM-REL-003:** Recognition **MUST NOT** be treated as delegation unless the relationship explicitly grants authority.

**GAAM-REL-004:** Accreditation **MUST NOT** be treated as a guarantee of every output produced by the accredited actor.

**GAAM-REL-005:** Registry inclusion **MUST NOT** be treated as universal trustworthiness.

**GAAM-REL-006:** Revocation and suspension semantics **MUST** identify the affected relationship, effective time, authority and propagation consequences.

---

## 4. Governance framework architecture

### 4.1 Governance framework

A **governance framework** is a versioned set of human-readable and machine-actionable authorities, policies, constraints, evidence requirements, accountability relationships and operational mechanisms used to govern decisions, actions and trust relationships within or across digital ecosystems.

**GAAM-GF-001:** A conforming governance framework **MUST** include a Primary Document and an authoritative Schedule of Controlled Documents.

**GAAM-GF-002:** The Primary Document **MUST** identify the exact framework version using a persistent identifier.

**GAAM-GF-003:** The framework **MUST** publish a conformance statement identifying the profiles and conformance targets claimed.

### 4.2 Primary Document

The Primary Document is the authoritative entry point for the governance framework. It MUST contain the sections specified below or provide authoritative references to controlled documents containing the required content.

#### 4.2.1 Introduction

The Introduction SHOULD orient readers to the ecosystem, problem, governance context and intended use.

#### 4.2.2 Terminology and notation

The Primary Document MUST define normative-language conventions, glossary sources and representation conventions.

#### 4.2.3 Localisation

**GAAM-GF-004:** The framework **MUST** identify its official language or languages and SHOULD use BCP 47 language tags.

**GAAM-GF-005:** Where multiple official versions exist, the framework **MUST** define how inconsistencies are resolved.

#### 4.2.4 Purpose and scope

The framework MUST state its purpose, governed entities, affected parties, consequential effects, interactions, artifacts, jurisdictions and exclusions.

#### 4.2.5 Governance topology

The framework MUST describe whether governance is centralised, hierarchical, federated, polycentric, decentralised, peer-based or hybrid.

**GAAM-GF-006:** The framework **MUST** identify where decision rights, enforcement powers, revision powers and emergency powers reside.

#### 4.2.6 Governing authority

The framework MUST identify each governing authority, its legal or institutional identity, jurisdiction, mandate, persistent identifier, contact route and decision rights.

**GAAM-GF-007:** Where no single governing authority exists, the framework **MUST** identify the authority topology and the process by which valid governance decisions are formed.

#### 4.2.7 Administering authority

Where administration is delegated, the framework MUST identify the administering authority, delegated functions, retained powers, oversight and termination conditions.

#### 4.2.8 Authority model

The Primary Document MUST state how authority originates, is represented, delegated, verified, suspended, revoked, contested and recognised across domains.

#### 4.2.9 Trust-decision model

The Primary Document MUST describe how relying parties or decision services combine authority, policy, evidence, status, assurance, risk and context to form decisions.

#### 4.2.10 Agentic applicability declaration

**GAAM-GF-008:** Every framework **MUST** declare whether agents may participate and, if so, whether they may recommend, decide, transact, delegate, use tools, create sub-agents or produce binding effects.

#### 4.2.11 Accountability and redress model

The Primary Document MUST identify accountable parties, review routes, appeal channels, emergency contacts, remedy powers and applicable time limits.

#### 4.2.12 Governance-state publication

The framework SHOULD publish current operational state, including active version, deprecated versions, recognised extensions, active authorities, suspended participants, withdrawn accreditations, status endpoints, policy endpoints and dispute channels.

**GAAM-GF-009:** Governance state required for a runtime decision **MUST** be discoverable, authenticated and sufficiently current for the decision context.

#### 4.2.13 Objectives and principles

Objectives MUST be achievable within the framework’s authority. Principles MUST guide requirements but MUST NOT contain directly testable normative provisions.

#### 4.2.14 General requirements

General Requirements apply across the framework. They SHOULD include responsible use, regulatory compliance, conduct, cross-document consistency and governance of machine-actionable artifacts.

#### 4.2.15 Revisions

**GAAM-GF-010:** The framework **MUST** define how revisions are proposed, reviewed, approved, versioned, published, deprecated and withdrawn.

**GAAM-GF-011:** A publicly available framework **SHOULD** include a public review period for substantive revisions.

**GAAM-GF-012:** Material policy changes affecting active authority or runtime decisions **MUST** define transition and notification rules.

#### 4.2.16 Extensions and recognition

The framework MUST state whether extensions are permitted and how they are registered, activated, suspended, deactivated and communicated.

The framework SHOULD also define recognition of independent peer frameworks without requiring hierarchical extension.

#### 4.2.17 Schedule of Controlled Documents

The Schedule MUST identify each controlled document, exact version, authority, purpose, applicability, status and conformance relevance.

---

## 5. Authority topology and delegation governance

### 5.1 Authority topology patterns

A framework may use one or more patterns:

- **central authority**, where one authority possesses final decision rights;
- **hierarchical authority**, where authority is delegated through defined levels;
- **federated authority**, where independent authorities recognise defined determinations;
- **polycentric authority**, where overlapping authorities govern distinct concerns;
- **peer recognition**, where parties make local recognition decisions without a common superior;
- **decentralised authority**, where governance outcomes emerge through defined distributed procedures;
- **hybrid authority**, combining these patterns.

**GAAM-AUTH-006:** A framework **MUST** identify conflicts that may arise among authorities and the procedure for resolving or containing them.

**GAAM-AUTH-007:** Where authorities overlap, the framework **MUST** define precedence, coordination, refusal or escalation semantics.

### 5.2 Delegation lifecycle

A delegation lifecycle SHOULD include proposal, issuance, acceptance, activation, invocation, monitoring, suspension, revocation, expiry, renewal and archival.

**GAAM-DEL-007:** A delegation **MUST NOT** become active before required acceptance, registration, verification or other activation conditions are met.

**GAAM-DEL-008:** The framework **MUST** define whether delegation is transferable and whether an agent or actor may substitute another delegate.

**GAAM-DEL-009:** Material substitution of an agent, model, operator, toolchain or execution environment **MUST** trigger reassessment where it may affect authority, assurance or risk.

### 5.3 Multi-hop delegation

**GAAM-DEL-010:** A multi-hop delegation decision **MUST** validate each active hop, parent-child scope compatibility, originating-principal continuity, redelegation permission and revocation state.

**GAAM-DEL-011:** A framework **MUST** define maximum delegation depth or the policy by which depth is determined.

### 5.4 Fan-out and convergence

**GAAM-DEL-012:** Where authority is divided among multiple delegates, the framework **MUST** define whether branches are independent, cumulative, mutually exclusive or jointly controlled.

**GAAM-DEL-013:** Where delegated branches converge on one effect, the aggregate effect **MUST** be evaluated against the originating authority and applicable aggregate limits.

### 5.5 Emergency authority

A framework MAY define emergency powers for containment, suspension or intervention.

**GAAM-AUTH-008:** Emergency authority **MUST** be narrowly scoped, time-limited, attributable, reviewable and subject to post-event accountability.

---

## 6. Runtime governance

### 6.1 Runtime governance envelope

A **runtime governance envelope** is the set of governance information evaluated before and, where necessary, during an effect.

It SHOULD include:

- proposed effect;
- requesting actor;
- principal and delegation chain;
- relevant authority;
- policy and rules;
- governance context;
- evidence and freshness requirements;
- assurance status;
- risk and impact thresholds;
- revocation and suspension status;
- review and escalation route;
- obligations triggered by the outcome.

**GAAM-RUN-001:** A framework governing consequential effects **MUST** define the minimum runtime governance envelope required for each effect class.

**GAAM-RUN-002:** A runtime decision **MUST** fail safely when required authority, policy, evidence, status or context cannot be validated.

**GAAM-RUN-003:** Runtime governance **MUST** evaluate current revocation and suspension state to the freshness required by the effect’s risk.

### 6.2 Decision outcomes

Permitted outcome classes include:

- allow;
- deny;
- allow with conditions;
- restrict scope;
- degrade capability;
- suspend;
- route for human review;
- require additional evidence;
- require additional approval.

**GAAM-RUN-004:** Outcome semantics **MUST** be unambiguous to the enforcement point.

### 6.3 Decision receipt

A **decision receipt** is a record sufficient to explain and reconstruct why a consequential effect was allowed, denied, restricted, suspended or routed for review.

A receipt SHOULD identify:

- receipt identifier;
- decision time;
- decision-maker;
- effect;
- actor and principal;
- authority and delegation references;
- policy and rule versions;
- evidence and verification references;
- status checks and freshness;
- outcome and conditions;
- explanation or reason codes;
- obligations and review route;
- integrity protection.

**GAAM-RUN-005:** Each consequential effect **MUST** produce or reference a decision receipt proportionate to the effect’s risk and accountability requirements.

**GAAM-RUN-006:** A receipt **MUST NOT** expose confidential evidence beyond what is necessary for authorised audit, review or challenge.

**GAAM-RUN-007:** The framework **MUST** define retention, access, disclosure, correction and deletion rules for receipts.

### 6.4 Ongoing evaluation

Some effects are continuous rather than instantaneous.

**GAAM-RUN-008:** Where authority, risk or evidence may materially change during execution, the framework **MUST** define conditions for re-evaluation, interruption or containment.

**GAAM-RUN-009:** Runtime revocation **MUST** be capable of stopping or constraining ongoing activity where technically and legally feasible.

---

## 7. Agentic systems governance

### 7.1 Agent identity and continuity

Agent identity alone does not establish authority, capability quality or accountability.

**GAAM-AGT-001:** A framework **MUST** define the attributes needed to identify an agent for governance purposes.

**GAAM-AGT-002:** A framework **MUST** define when changes to model, instructions, memory, tools, operator, provider, execution environment or policy configuration constitute a material change of agent state or identity.

**GAAM-AGT-003:** Material changes **MUST** trigger re-registration, renewed assurance, restricted operation or another declared lifecycle response where necessary.

### 7.2 Agent principals and accountable parties

**GAAM-AGT-004:** An agent performing an effect on behalf of a principal **MUST** carry or reference verifiable authority for that effect.

**GAAM-AGT-005:** The framework **MUST** identify the principal, operator, provider, deployer and supervisor roles applicable to each agent class and allocate accountability among them.

### 7.3 Task-bound authority

**GAAM-AGT-006:** Agent authority **SHOULD** be bound to a task, purpose or effect class wherever practical.

**GAAM-AGT-007:** Tool access **SHOULD** be limited to what is necessary for the authorised task.

**GAAM-AGT-008:** An agent **MUST NOT** infer authority from mere access to accounts, credentials, data, APIs or tools.

### 7.4 Planning and policy evaluation

**GAAM-AGT-009:** An agent or supervising service **MUST** evaluate applicable governance constraints before executing a consequential plan step.

**GAAM-AGT-010:** Where an agent cannot determine whether a planned effect is authorised, it **MUST** deny, restrict or escalate rather than assume permission.

### 7.5 Redelegation and sub-agents

**GAAM-AGT-011:** An agent **MUST NOT** create a sub-agent, substitute another agent or redelegate authority unless explicitly permitted.

**GAAM-AGT-012:** A sub-agent **MUST** receive no more authority than the delegating agent is authorised to redelegate.

**GAAM-AGT-013:** The originating principal and accountable-party chain **MUST** remain discoverable across sub-agent relationships.

### 7.6 Multi-agent coordination

**GAAM-AGT-014:** A framework permitting multi-agent coordination **MUST** define how authority, task state, evidence, obligations and accountability are partitioned and reconciled.

**GAAM-AGT-015:** Coordination protocols **MUST NOT** be assumed to provide governance semantics unless those semantics are explicitly defined and validated.

**GAAM-AGT-016:** Where multiple agents contribute to one effect, the decision receipt **MUST** identify the material contributions and accountable parties.

### 7.7 Tool governance

**GAAM-AGT-017:** Tools capable of producing consequential effects **MUST** enforce or receive sufficient authority and policy context to prevent unauthorised invocation.

**GAAM-AGT-018:** Tool outputs used as evidence **MUST** carry provenance and integrity appropriate to the decision.

### 7.8 Human oversight and guardianship

Human oversight is effective only when the overseer has authority, evidence, time and practical power to intervene.

**GAAM-AGT-019:** A framework requiring human oversight **MUST** specify who performs it, when it occurs, what information is available, and what intervention powers exist.

**GAAM-AGT-020:** A guardian or supervisory agent **MUST** itself be governed by explicit authority, constraints and accountability.

### 7.9 Agent suspension and termination

**GAAM-AGT-021:** A framework **MUST** define mechanisms to suspend, isolate, contain or terminate an agent when authority, assurance or safety conditions fail.

**GAAM-AGT-022:** Termination **MUST** address outstanding tasks, delegated authority, retained data, tools, obligations and evidence preservation.

---

## 8. Decentralised trust graphs and registries

### 8.1 Trust graph

A **trust graph** is a governed set of entities, relationships and evidence that may be evaluated to support contextual trust decisions.

A trust graph is not itself a universal source of truth. Different relying parties may form different decisions from the same graph under different policies and contexts.

**GAAM-GRAPH-001:** Graph relationships used for automated decisions **MUST** be typed, scoped, attributable, time-bounded where applicable and linked to status or revocation semantics.

**GAAM-GRAPH-002:** A graph path **MUST** be treated as evidence for a decision, not as the decision itself.

### 8.2 Node classes

A framework SHOULD identify permitted node classes, which may include:

- persons;
- organisations;
- public authorities;
- agents;
- registries;
- governance frameworks;
- roles;
- credentials;
- policies;
- evidence artifacts;
- assurance services;
- effects;
- decisions.

### 8.3 Edge classes

A framework MUST define the semantics of edge classes it relies upon. Identity, authority, delegation, recognition, accreditation, assurance, accountability, dependency, prohibition, suspension and revocation MUST remain distinguishable.

### 8.4 Graph provenance and integrity

**GAAM-GRAPH-003:** Each material graph assertion **MUST** identify the asserting party and authority basis.

**GAAM-GRAPH-004:** A graph implementation **MUST** provide integrity and provenance sufficient to detect unauthorised alteration of relied-upon assertions.

**GAAM-GRAPH-005:** Derived edges or computed trust values **MUST** identify their derivation method, input sources and applicable policy.

### 8.5 Graph traversal

**GAAM-GRAPH-006:** A framework **MUST** define permitted traversal depth, relationship types, path constraints and evidence thresholds for each automated decision class.

**GAAM-GRAPH-007:** A relying party **MUST** apply its own policy to determine whether a discovered path is sufficient.

### 8.6 Conflicting claims

**GAAM-GRAPH-008:** A framework **MUST** define how conflicting, stale, superseded or contested graph assertions are represented and evaluated.

**GAAM-GRAPH-009:** Absence of a negative assertion **MUST NOT** automatically be interpreted as positive trust unless the framework explicitly justifies that inference.

### 8.7 Registry governance

A **registry** is a governed service or dataset that records and makes discoverable specified entities, relationships, status or authority assertions.

**GAAM-REG-001:** Registry inclusion **MUST** have explicit semantics and **MUST NOT** be represented as general trustworthiness.

**GAAM-REG-002:** A registry framework **MUST** define who may create, update, suspend, revoke, correct and archive each record class.

**GAAM-REG-003:** Registry records used for decisions **MUST** expose sufficient status, provenance, authority and version information.

**GAAM-REG-004:** A registry **MUST** provide a correction and dispute path for materially incorrect or unauthorised records.

### 8.8 Registry federation and recognition

**GAAM-REG-005:** Federation **MUST** distinguish data replication, technical interoperability, recognition of authority and reliance upon determinations.

**GAAM-REG-006:** Recognition of another registry **MUST** state the accepted record classes, purposes, assurance thresholds, jurisdictional limits and withdrawal conditions.

### 8.9 Graph security

A framework SHOULD address:

- sybil attacks;
- graph poisoning;
- reputation manipulation;
- false recognition;
- authority laundering;
- selective revocation suppression;
- stale caches;
- inference attacks;
- concentration and registry capture;
- denial of correction.

---

## 9. Assurance and observability

### 9.1 Assurance forms

A framework MAY recognise:

- organisational assurance;
- service assurance;
- component assurance;
- configuration assurance;
- delegation assurance;
- transaction assurance;
- evidence assurance;
- continuous assurance;
- outcome assurance.

**GAAM-ASSUR-005:** The framework **MUST** define what each assurance form establishes and what it does not establish.

### 9.2 Assurance providers

The framework SHOULD define assessors, auditors, accreditors, certifiers, monitoring services and assurance consumers where applicable.

**GAAM-ASSUR-006:** Assurance providers **MUST** disclose material conflicts of interest and the basis of their competence and authority.

**GAAM-ASSUR-007:** Assurance results **MUST** be challengeable and correctable when materially wrong.

### 9.3 Continuous assurance

Continuous assurance uses current or event-driven evidence to determine whether relevant conditions remain satisfied.

**GAAM-ASSUR-008:** A Continuous Assurance Profile framework **MUST** define monitored controls, evidence sources, sampling or event frequency, thresholds, drift conditions, escalation and suspension actions.

**GAAM-ASSUR-009:** A continuous assurance service **MUST** identify data gaps, blind spots and periods during which assurance could not be maintained.

### 9.4 Observability

Observability may include logs, metrics, traces, status signals, policy decisions, evidence events and incident indicators.

**GAAM-OBS-001:** Observability requirements **MUST** be proportionate and **MUST** account for privacy, confidentiality, minimisation and security.

**GAAM-OBS-002:** The absence of observable data **MUST NOT** be presented as evidence of compliant behaviour.

### 9.5 Trust marks

**GAAM-ASSUR-010:** A trust mark **MUST** identify or resolve to its issuer, scope, criteria, validity, status and limitations.

**GAAM-ASSUR-011:** A trust mark **MUST NOT** imply broader assurance than the underlying assessment supports.

---

## 10. Risk, safety, harm and impact

### 10.1 Risk model

A framework MUST maintain a risk model covering threats to purpose, objectives, rights, operations, market integrity and public interest.

Risk analysis SHOULD consider:

- affected actors and non-participants;
- severity, likelihood and reversibility;
- concentration and systemic dependencies;
- delegation amplification;
- authority laundering;
- confused-deputy behaviour;
- multi-agent collusion;
- tool misuse;
- memory or instruction contamination;
- stale trust evidence;
- cascading revocation failure;
- accountability fragmentation;
- denial of redress.

**GAAM-RISK-001:** Risk assessment **MUST** examine authority paths, evidence paths, dependencies, graph edges, delegated capabilities and affected parties, not only roles and processes.

### 10.2 Impact thresholds

**GAAM-RISK-002:** A framework **MUST** define effect classes or thresholds that require enhanced evidence, approval, assurance, monitoring or human review.

### 10.3 Cumulative and systemic harm

**GAAM-HARM-003:** A framework **MUST** consider harms arising cumulatively across repeated low-level decisions where such harms are reasonably foreseeable.

**GAAM-HARM-004:** A framework **SHOULD** identify concentration, lock-in, exclusion, manipulation and market-power risks created by trust infrastructure.

### 10.4 Safety controls

Safety controls MAY include capability restriction, sandboxing, dual control, rate limits, value limits, geographic restrictions, mandatory review, reversible execution and emergency suspension.

**GAAM-RISK-003:** Controls relied upon to prevent high-impact effects **MUST** be testable or auditable and linked to accountable owners.

---

## 11. Accountability, contestability and redress

### 11.1 Affected parties

An **affected party** is a person or organisation whose rights, interests, opportunities, resources or status may be materially affected by a governed decision or effect.

**GAAM-RED-001:** A framework **MUST** identify affected-party classes, including persons who are not members of the trust community.

### 11.2 Notice and explanation

**GAAM-RED-002:** Affected parties **SHOULD** receive notice of consequential decisions where lawful and practicable.

**GAAM-RED-003:** A framework **MUST** define the explanation information available for consequential decisions, including reason codes, applicable policy and review route.

### 11.3 Challenge and review

**GAAM-RED-004:** A challenge mechanism **MUST** permit submission of corrections, contrary evidence and claims of unauthorised action.

**GAAM-RED-005:** Review **MUST** be performed by an actor or process with authority to confirm, modify, reverse or remedy the decision.

**GAAM-RED-006:** A framework **MUST** define response and resolution time expectations proportionate to the potential harm.

### 11.4 Remedy

Remedies may include correction, reversal, restoration, deletion, explanation, re-performance, compensation, restitution, apology, sanction, policy change or systemic remediation.

**GAAM-RED-007:** A framework **MUST** identify which remedies are available, who may order them and how compliance is verified.

### 11.5 Cross-framework disputes

**GAAM-RED-008:** Where an effect depends on multiple governance frameworks, the frameworks **SHOULD** define coordination, evidence sharing, jurisdiction and fallback procedures for disputes.

---

## 12. Controlled documents

Each controlled-document category MAY contain one or more documents. Applicability depends on the framework profiles claimed. A framework MUST explain the omission of any category required by an applicable profile.

### 12.1 Glossary

The Glossary SHOULD define all ambiguous terms and SHOULD distinguish normative definitions from explanatory notes.

### 12.2 Governance and institutional requirements

This category MUST define constituting authority, governing bodies, decision rights, operating rules, conflicts of interest, enforcement, sanctions, revision governance and dispute authority.

### 12.3 Risk, safety and impact requirements

This category MUST define risk methodology, threat and harm taxonomy, risk ownership, controls, residual risk, monitoring and treatment.

### 12.4 Authority and delegation requirements

Required for the Delegated Authority and Agentic Systems Profiles. It MUST define authority sources, scope, delegation records, lineage, redelegation, acceptance, revocation, propagation and accountability.

### 12.5 Agent lifecycle and operational control

Required for the Agentic Systems Profile. It MUST define registration, activation, configuration, material change, tool access, memory governance, monitoring, suspension, compromise response and retirement.

### 12.6 Business and market-integrity requirements

This category SHOULD define value exchanges, incentives, sustainability, conflicts of interest, liability allocation, anti-competitive recognition, assurance shopping, registry capture and market manipulation.

### 12.7 Technical interoperability requirements

This category MUST identify external technical specifications, profiles, discovery methods, status mechanisms, test suites and interoperability requirements without redefining protocol details.

### 12.8 Information trust requirements

This category MUST address information security, availability, processing integrity, confidentiality and privacy. It SHOULD address data minimisation, retention, purpose limitation and provenance.

### 12.9 Evidence, provenance and traceability requirements

Required for Machine-Actionable, Agentic, Trust Graph, Continuous Assurance and High-Impact Profiles. It MUST define evidence classes, provenance, integrity, freshness, retention, disclosure and decision reconstruction.

### 12.10 Trust graph and recognition requirements

Required for the Decentralised Trust Graph Profile. It MUST define node and edge semantics, path evaluation, provenance, conflicts, negative assertions, derived values, recognition and graph security.

### 12.11 Registry and discovery requirements

Required where registries are authoritative or relied upon. It MUST define record authority, lifecycle, discovery, status, correction, federation, history and operator obligations.

### 12.12 Trust assurance and certification requirements

This category SHOULD define assessment schemes, assessors, accreditors, certifiers, trust marks, evidence and appeals.

### 12.13 Continuous assurance and observability requirements

Required for the Continuous Assurance Profile. It MUST define monitoring sources, controls, freshness, thresholds, drift, incident signals, suspension and gaps.

### 12.14 Human oversight and intervention requirements

Required where human oversight is a control. It MUST define actors, timing, evidence, authority, intervention power, workload, conflicts and review quality.

### 12.15 Inclusion, equitability and accessibility requirements

This category MUST address access, usability, accommodation, language, digital exclusion and impacts upon vulnerable or marginalised groups.

### 12.16 Incident response, dispute and redress requirements

Required for Agentic, Trust Graph, Continuous Assurance and High-Impact Profiles. It MUST define reporting, triage, containment, preservation, investigation, notification, correction, appeal, remedy and restoration.

### 12.17 Legal agreements

This category MUST identify governed parties, applicable law, obligations, liability, enforcement, dispute resolution and relationship to the framework.

### 12.18 Cross-framework interoperability and conflict requirements

Required where external frameworks are recognised. It MUST define recognition scope, policy mapping, assurance equivalence, conflicts, refusal, withdrawal and dispute coordination.

### 12.19 Machine-actionable governance artifacts

Required for the Machine-Actionable Governance Profile. It MUST define governance packages, schemas, policy artifacts, status endpoints, validation, integrity, versioning and normative precedence.

---

## 13. Machine-actionable governance package

A **machine-actionable governance package** is a versioned and integrity-protected set of artifacts that allows software to discover and evaluate applicable governance state.

A package SHOULD include:

- framework identifier and version;
- profile claims;
- governing authority assertions;
- authority topology;
- role and effect definitions;
- policy and rule identifiers;
- delegation and evidence schemas;
- status and revocation endpoints;
- registry and discovery endpoints;
- assurance profiles;
- dispute and review endpoints;
- conformance tests;
- integrity metadata.

**GAAM-MAG-001:** A machine-actionable package **MUST** be traceable to the authoritative human-readable framework.

**GAAM-MAG-002:** The package **MUST** identify its version, effective period, status and integrity mechanism.

**GAAM-MAG-003:** A material package change **MUST** follow the framework’s revision and transition requirements.

**GAAM-MAG-004:** A package **MUST NOT** silently broaden authority or reduce obligations relative to the authoritative framework.

**GAAM-MAG-005:** Conformance tests **SHOULD** include valid, invalid and boundary-condition examples.

---

## 14. Profiles

Profiles are composable packages of requirements. A framework may claim one or more profiles.

### 14.1 Foundation Profile

The Foundation Profile requires:

- Primary Document;
- governing and administering authority model;
- purpose, scope, objectives and principles;
- general requirements;
- Schedule of Controlled Documents;
- governance, risk, technical, information trust, accessibility and legal categories;
- framework-level conformance statement.

### 14.2 Machine-Actionable Governance Profile

Adds:

- machine-actionable governance package;
- policy-to-rule traceability;
- schemas and validation;
- governance-state publication;
- conformance tests;
- version and precedence controls.

### 14.3 Delegated Authority Profile

Adds:

- authority and delegation controlled document;
- delegation lineage;
- attenuation;
- redelegation rules;
- revocation propagation;
- accountable-party mapping;
- delegation conformance evidence.

### 14.4 Agentic Systems Profile

Adds:

- agent applicability declaration;
- agent lifecycle controlled document;
- agent authority and task binding;
- tool governance;
- multi-agent coordination;
- decision receipts;
- suspension and containment;
- human oversight where applicable.

### 14.5 Decentralised Trust Graph Profile

Adds:

- node and edge semantics;
- relationship provenance;
- traversal policy;
- conflict and negative assertion handling;
- registry and recognition governance;
- graph security;
- trust-decision separation.

### 14.6 Continuous Assurance Profile

Adds:

- continuous assurance controlled document;
- observability sources;
- freshness and drift rules;
- gap reporting;
- event-driven reassessment;
- automatic suspension or escalation.

### 14.7 High-Impact Systems Profile

Adds:

- enhanced risk and impact assessment;
- affected-party analysis;
- stricter authority and evidence thresholds;
- mandatory decision receipts;
- effective human review or equivalent accountable control;
- incident and redress requirements;
- systemic harm monitoring.

**GAAM-PROF-001:** A profile claim **MUST** identify the specification version, profile version, applicable conformance targets, exclusions and evidence location.

**GAAM-PROF-002:** A framework **MUST NOT** claim a profile when a mandatory category or requirement is omitted without an explicitly permitted exception.

---

## 15. Conformance

### 15.1 Conformance targets

This specification defines the following targets:

- governance framework;
- controlled document;
- governed organisation;
- authority record;
- delegation record;
- agent;
- registry;
- trust graph;
- trust decision;
- transaction or effect;
- evidence package;
- decision receipt;
- assurance service;
- machine-actionable governance package.

### 15.2 Conformance claim

A conformance claim MUST identify:

- claimant;
- target;
- specification version;
- profiles;
- applicable requirements;
- assessment method;
- evidence;
- evaluator;
- date and validity;
- limitations;
- status and withdrawal mechanism.

**GAAM-CONF-001:** Conformance claims **MUST** be scoped to an identified target and **MUST NOT** be generalised to related entities or transactions without evidence.

**GAAM-CONF-002:** Framework conformance **MUST NOT** be presented as proof that every governed actor, agent, decision or transaction conforms.

**GAAM-CONF-003:** An agent conformance claim **MUST NOT** be presented as proof that every future action of that agent is authorised or safe.

### 15.3 Evidence of conformance

Evidence may include document review, automated tests, assessment reports, operational records, decision receipts, status records, monitoring results and challenge outcomes.

**GAAM-CONF-004:** Evidence **MUST** be sufficient to reproduce or independently evaluate the conformance conclusion to the degree required by the claimed profile.

### 15.4 Exceptions and compensating controls

A framework MAY permit exceptions where an equivalent or stronger outcome is achieved.

**GAAM-CONF-005:** Exceptions **MUST** identify the requirement, rationale, authority, duration, risk, compensating control and review date.

### 15.5 Non-conformance

**GAAM-CONF-006:** A framework **MUST** define classification, notification, remediation, suspension and appeal procedures for non-conformance.

---

## 16. Security, privacy and resilience considerations

Governance infrastructure is itself a target for compromise and capture. Frameworks SHOULD address:

- key and credential compromise;
- unauthorised policy changes;
- registry poisoning;
- status suppression;
- decision-service manipulation;
- provenance forgery;
- assurance fraud;
- insider threats;
- denial of review;
- dependency compromise;
- model or agent substitution;
- concentration risk;
- cross-framework policy conflict.

**GAAM-SEC-001:** Governance-critical artifacts **MUST** be protected against unauthorised modification and rollback.

**GAAM-SEC-002:** Frameworks **MUST** define recovery and continuity procedures for unavailable or compromised governance services.

**GAAM-PRIV-001:** Evidence, receipts and observability data **MUST** be minimised to what is necessary for governance, assurance, accountability and lawful obligations.

**GAAM-PRIV-002:** Access to sensitive governance records **MUST** be controlled, auditable and purpose-bound.

**GAAM-RES-001:** A framework **MUST** identify critical dependencies and define safe behaviour when they are unavailable or untrustworthy.

---

## 17. Illustrative examples

### 17.1 Delegated purchasing agent

A person delegates authority to a purchasing agent to acquire office equipment up to a defined value, from approved vendors, before a deadline. The agent has technical capability to use a payment tool, but the runtime decision service verifies the task-bound delegation, vendor status, aggregate spend, evidence freshness and prohibition against redelegation. A decision receipt records the authority chain, policy version, evidence and payment effect.

The example demonstrates that account access is not authority; the transaction is admitted only after contextual evaluation.

### 17.2 Cross-border professional registry

A relying organisation discovers a professional through a foreign registry. The local framework recognises only specified registration classes, for a defined purpose, subject to current status and assurance. The registry path supports the local decision but does not determine it. A conflicting suspension notice routes the request for review.

### 17.3 Multi-agent benefit application

An intake agent gathers information, an evidence agent validates documents, and an eligibility agent recommends an outcome. None has unilateral authority to issue a benefit. A decision service applies policy, records each agent’s contribution and routes high-impact denials for accountable review. The affected person receives notice and a correction route.

### 17.4 Continuous assurance failure

A certified service loses access to required monitoring data. The continuous assurance service reports an assurance gap rather than silently preserving a green status. High-risk effects are suspended while low-risk effects are restricted according to policy.

---

## 18. Implementation guidance

This section is informative.

Framework authors should begin with effects and accountability rather than documents. A useful sequence is:

1. Identify consequential effects.
2. Identify affected parties and harms.
3. Identify legitimate authority sources.
4. Define roles, delegations and accountability.
5. Define the evidence and assurance needed before each effect.
6. Define runtime decisions, enforcement and receipts.
7. Define lifecycle, incident and redress procedures.
8. Package these requirements into controlled documents and profiles.

Implementations should avoid representing trust as a single scalar score. Where scores are used, the derivation, context, limitations and decision policy should remain visible.

---

## Annex A. Consolidated glossary

**Accountability:** Obligation and capacity to explain, justify, answer for and remedy an action, decision, omission or effect.

**Actor:** Governed entity capable of requesting, approving, denying, performing, supervising, recording or being affected by an action.

**Affected party:** Person or organisation whose rights, interests, opportunities, resources or status may be materially affected.

**Agent:** Software actor capable of selecting or executing actions based on instructions, goals, context, policy, evidence or observed state.

**Assessment:** Evaluation of whether an entity, process, artifact or system satisfies requirements, controls or a profile.

**Assurance:** Time-bounded and contextual conclusion about the confidence that may reasonably be placed in a claim, entity, process, control, decision or effect.

**Authority:** Recognised and bounded ability to permit, perform, approve, prohibit, delegate or constrain an effect.

**Capability:** Technical or operational ability to perform an action or produce an effect.

**Claim:** Proposition that may be evaluated.

**Constraint:** Limitation upon how, when, where or under what conditions an action may occur.

**Control:** Safeguard intended to satisfy, enforce or provide evidence of a requirement.

**Decision receipt:** Record sufficient to explain and reconstruct why a consequential effect was allowed, denied, restricted, suspended or routed for review.

**Delegation:** Bounded grant of authority from a delegator to a delegate.

**Effect:** Material state change, decision consequence, transfer, disclosure, commitment, denial, approval, access, publication or other governed outcome.

**Evidence:** Information or artifact used to support or challenge a claim, authority, verification result, assessment, decision or outcome.

**Governance context:** Legal, institutional, contractual, technical, jurisdictional and operational environment in which authority, policy, evidence and decisions are interpreted.

**Governance event:** Event that changes governance-relevant state.

**Governance framework:** Versioned set of human-readable and machine-actionable authorities, policies, constraints, evidence requirements, accountability relationships and operational mechanisms.

**Governed entity:** Any person, organisation, authority, system, agent, service, registry, artifact or other object to which governance requirements apply.

**Harm:** Material adverse effect upon a person, organisation, community, market, institution or public interest.

**Machine-actionable governance package:** Versioned, integrity-protected set of artifacts enabling software to discover and evaluate applicable governance state.

**Obligation:** Required action triggered by a condition or event.

**Permission:** Authorisation for an action or effect.

**Policy:** Human-auditable normative requirement or coherent set of requirements.

**Principal:** Actor whose interests, rights, resources or authority are represented or exercised by another actor.

**Profile:** Composable package of requirements, controls, evidence expectations, tests and permitted effects.

**Prohibition:** Rule or policy forbidding an action or effect.

**Registry:** Governed service or dataset recording and making discoverable specified entities, relationships, status or authority assertions.

**Relationship:** Typed and contextual connection between governed entities or artifacts.

**Remedy:** Action intended to stop, reverse, correct, compensate or otherwise address harm or governance failure.

**Role:** Context-specific capacity in which an actor participates.

**Rule:** Machine-testable expression of a requirement.

**Runtime governance envelope:** Governance information evaluated before and, where necessary, during an effect.

**Trust decision:** Contextual determination under policy about whether and under what conditions an effect should occur.

**Trust graph:** Governed set of entities, relationships and evidence evaluated to support contextual trust decisions.

**Verification:** Evaluation of whether a defined condition holds.

---

## Annex B. Core invariants

1. Capability does not imply authority.
2. Identity does not imply permission.
3. Registry inclusion does not imply universal trustworthiness.
4. A graph path is evidence for a decision, not the decision itself.
5. Delegation must remain bounded and traceable.
6. Redelegation must be explicit.
7. Delegation does not dissolve accountability.
8. Assurance is contextual and time-bounded.
9. Required evidence must have provenance and sufficient freshness.
10. Consequential effects require attributable decisions and proportionate receipts.
11. Machine actors are not terminal accountability points.
12. Governance changes affecting active authority require controlled transition.
13. Failure to validate required governance state must fail safely.
14. Review must have the authority and practical capacity to change outcomes.
15. Machine-actionable governance must not silently diverge from normative governance.

---


## 18. Feature-complete governance artifacts

### 18.1 Canonical authority records

**GAAM-ART-001:** A machine-actionable authority record **MUST** identify its authority source, issuer, subject, permitted effects, scope, effective period, status, revocation authority and accountable parties.

**GAAM-ART-002:** An authority record **MUST** distinguish permissions, prohibitions, obligations and constraints.

**GAAM-ART-003:** A system **MUST NOT** treat an authority record as operative when its status, effective period, governing context or integrity cannot be validated.

### 18.2 Canonical delegation records

**GAAM-ART-004:** A delegation record **MUST** identify its parent authority, delegator, delegate, delegated scope, effective period, redelegation rule, status and propagation behaviour.

**GAAM-ART-005:** Effective child authority **MUST** be no broader than the intersection of valid parent authority, delegated scope, applicable policy, current context, active status, valid time and applicable constraints.

**GAAM-ART-006:** A delegation transition **MUST** emit or preserve a governance event sufficient to reconstruct the transition authority, time, prior state, new state and supporting evidence.

### 18.3 Governance artifact lifecycles

**GAAM-LIFE-001:** A conformant implementation **MUST** apply declared lifecycle states and transitions to governance-critical artifacts.

**GAAM-LIFE-002:** Lifecycle transition rules **MUST** identify the authority permitted to cause each transition and the evidence required for that transition.

**GAAM-LIFE-003:** An invalid, unauthorised or out-of-sequence lifecycle transition **MUST** fail without activating the requested governance state.

**GAAM-LIFE-004:** Suspension, revocation, expiry, supersession and termination **MUST** have explicit effects on dependent artifacts and active decisions.

**GAAM-LIFE-005:** Archived governance artifacts **MUST** remain reconstructable but **MUST NOT** be treated as operative unless explicitly restored through an authorised transition.

### 18.4 Assurance expressions

**GAAM-ASR-001:** An assurance assertion **MUST** identify its subject, evaluated property, criteria, evaluator, method, evidence, scope, governance context, validity period, status, limitations and challenge route.

**GAAM-ASR-002:** Assurance labels from different domains or profiles **MUST NOT** be treated as equivalent without an explicit mapping of criteria, scope, evidence, evaluator competence, context and validity.

**GAAM-ASR-003:** Stale, suspended, withdrawn or contradicted assurance **MUST** trigger profile-defined safe behaviour.

### 18.5 Profile composition

**GAAM-PCOMP-001:** Every profile other than the Foundation Profile **MUST** declare the Foundation Profile as a dependency.

**GAAM-PCOMP-002:** A profile **MUST** declare its conformance targets, normative requirement mappings, required artifacts, required evidence, required tests, permitted exclusions and dependencies.

**GAAM-PROF-003:** A composite profile claim **MUST** satisfy dependency closure and **MUST NOT** suppress conflicting or additional requirements without an explicit resolution rule.

**GAAM-PROF-004:** A partial implementation **MUST NOT** claim full profile conformance.

### 18.6 Decision outcomes and receipts

**GAAM-OUT-001:** A trust decision **MUST** use a declared outcome vocabulary and identify any conditions attached to the outcome.

**GAAM-OUT-002:** The base outcome vocabulary **MUST** support permit, deny, permit-with-conditions, restrict, suspend, require-additional-evidence, require-additional-approval, route-for-review and terminate.

**GAAM-OUT-003:** A decision receipt for a consequential effect **MUST** identify the decision, applicable authority, policy, evidence references, assurance references, outcome, conditions, decision time, enforcement point and accountable party.

**GAAM-DEC-004:** A receipt **MUST** minimise disclosed information while preserving sufficient provenance for review and reconstruction.

### 18.7 Privacy, safety and affected-party protections

**GAAM-SAFE-001:** Governance evidence and receipts **MUST** be limited to information necessary for the declared purpose and review obligations.

**GAAM-SAFE-002:** A high-impact system **MUST** define interruption authority, degraded operation, safe failure, recovery and post-event review.

**GAAM-SAFE-003:** Emergency authority **MUST** be time-bounded, purpose-bounded, attributable and subject to independent or otherwise conflict-controlled review.

**GAAM-APR-001:** A consequential effect **MUST** identify affected-party notice, explanation, challenge, review and remedy arrangements proportionate to the effect.

**GAAM-APR-002:** A review mechanism **MUST** have practical authority to suspend, reverse, correct or remediate an outcome.

**GAAM-APR-003:** Remedy completion **MUST** produce evidence linked to the original decision and effect.

**GAAM-SYS-001:** A high-impact framework **MUST** define how individual effect records are aggregated to detect recurring, cohort-level or systemic harm.

**GAAM-SYS-002:** Detection of a declared systemic-harm threshold **MUST** trigger a governed intervention and preserve evidence of the response.

### 18.8 Market integrity and recognition

**GAAM-MKT-001:** Registry inclusion, accreditation or recognition **MUST NOT** be represented as universal trustworthiness.

**GAAM-MKT-002:** A framework **MUST** disclose material conflicts of interest affecting registry, accreditation or assurance decisions.

**GAAM-MKT-003:** A high-impact recognition arrangement **MUST** address opaque exclusion, portability barriers, self-preferencing and unsupported equivalence claims.


## Annex B.1. Normative artifact precedence and candidate invariants

When GAAM artifacts conflict, the normative specification governs substantive meaning; normative JSON Schemas govern machine-readable structure; controlled vocabularies govern enumerated terms; profile manifests govern declared profile composition; and conformance tests provide evidence without redefining the specification. An implementation MUST disclose any unresolved conflict rather than selecting the least restrictive interpretation.

The following candidate invariants apply across profiles where the relevant capability is present:

1. Authority MUST originate from an identifiable authority source and MUST remain within its declared scope and effective period.
2. Delegation MUST NOT enlarge authority, bypass a prohibition, exceed redelegation permission or obscure the originating principal.
3. Suspension, expiry and revocation MUST be evaluated before an effect is authorised and MUST propagate to dependent authority where the governing policy requires it.
4. A trust decision MUST identify the authority, policy, evidence and assurance state used to reach the outcome.
5. A consequential effect MUST be traceable to a decision receipt and an accountable party.
6. High-impact operation MUST provide an appeal path, remedy path and affected-party evidence appropriate to the claimed profile.
7. A conformance claim MUST NOT represent structural validation as behavioural assurance or self-assessment as independent assessment.
8. A governance package MUST be rejected when required artifacts, integrity evidence or profile dependencies are absent or inconsistent.

## Annex C. Resolved architectural decisions for v0.9.0

The v0.9.0 Candidate Specification adopts the following decisions:

1. GAAM remains a standalone, protocol-independent metamodel.
2. Persistent identifiers may use any verifiable identifier method satisfying profile requirements; DIDs are not mandatory.
3. Decision receipts are mandatory for consequential effects and profile-defined boundary events.
4. Assurance expressions are contextual and are not universal trust scores.
5. Machine-readable artifacts are normative for structure where explicitly designated; human-readable normative text governs substantive meaning.
6. High-impact status is profile and context defined rather than jurisdictionally universal.
7. Emergency authority requires conflict-controlled post-event review.
8. Minimum authority and delegation fields are defined by the canonical schemas.
9. Agent identity continuity depends upon declared changes to model, operator, memory, tools, policy and execution environment.
10. Graph ontology extensions are permitted when their semantics, provenance and compatibility are declared.

## Annex D. Architectural provenance and compatibility posture

GAAM is an independent metamodel. Informative mappings may assist adoption from other governance models, but they do not create specification lineage, normative incorporation, semantic equivalence or dependency. Conformance claims apply only to the GAAM version and profiles explicitly identified by the claimant.
