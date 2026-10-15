---
title: "Architecture Diagrams"
permalink: /diagrams/
parent: Concepts and Design
artifact_type: "Architecture diagrams"
normative_status: "Informative"
grand_parent: Understand GAAM
nav_order: 2
---
# Architecture Diagrams

{% include gaam-meta.html %}

These diagrams are informative and use Mermaid syntax.

## 1. Core decision chain

```mermaid
flowchart LR
  P[Principal] -->|delegates bounded authority| A[Agent or Actor]
  S[Authority Source] --> AU[Authority]
  AU --> D[Delegation]
  D --> A
  POL[Policy and Rules] --> TD[Trust Decision]
  E[Evidence and Status] --> TD
  A -->|requests effect| TD
  TD -->|allow, deny, restrict, suspend, review| EF[Effect]
  TD --> DR[Decision Receipt]
  EF --> AC[Accountability and Remedy]
  DR --> AC
```

## 2. Governance framework architecture

```mermaid
flowchart TD
  PD[Primary Document] --> SC[Schedule of Controlled Documents]
  PD --> AT[Authority Topology]
  PD --> TM[Trust-Decision Model]
  PD --> AR[Accountability and Redress Model]
  SC --> GOV[Governance]
  SC --> RISK[Risk, Safety and Impact]
  SC --> DEL[Authority and Delegation]
  SC --> AGT[Agent Lifecycle]
  SC --> EVID[Evidence and Provenance]
  SC --> GRAPH[Trust Graph and Registry]
  SC --> ASSUR[Assurance and Observability]
  SC --> LEGAL[Legal and Cross-Framework]
```

## 3. Multi-hop delegation

```mermaid
flowchart LR
  O[Originating Principal] -->|scope S0| D1[Delegate 1]
  D1 -->|attenuated scope S1| D2[Delegate 2]
  D2 -->|attenuated scope S2| D3[Agent]
  R[Revocation or Expiry] -.propagates.-> D1
  R -.propagates.-> D2
  R -.propagates.-> D3
```

## 4. Runtime governance

```mermaid
sequenceDiagram
  participant Requester as Actor
  participant PDP as Governance Decision Service
  participant Registry
  participant Evidence
  participant Tool as Enforcement Point
  Requester->>PDP: Proposed effect + authority context
  PDP->>Registry: Resolve authority, delegation and status
  PDP->>Evidence: Verify evidence and assurance freshness
  PDP->>PDP: Apply policy, risk and impact rules
  alt Allowed
    PDP->>Tool: Permit with constraints and obligations
    Tool-->>PDP: Execution result
  else Review required
    PDP-->>Requester: Route for accountable review
  else Denied
    PDP-->>Requester: Deny with reason code
  end
  PDP->>PDP: Produce decision receipt
```

## 5. Trust graph evaluation

```mermaid
flowchart LR
  RP[Relying Party Policy] --> TD[Contextual Trust Decision]
  N1[Authority Node] -->|recognises| N2[Registry Node]
  N2 -->|asserts status| N3[Actor Node]
  N3 -->|delegates| N4[Agent Node]
  N1 --> EV[Graph Evidence Paths]
  N2 --> EV
  N3 --> EV
  N4 --> EV
  EV --> TD
  ST[Status, Revocation and Conflicts] --> TD
```

## 6. Governance-event lifecycle

```mermaid
stateDiagram-v2
  [*] --> Proposed
  Proposed --> Issued
  Issued --> Active: acceptance/activation
  Active --> Suspended: incident or policy trigger
  Suspended --> Active: restoration
  Active --> Revoked: withdrawal
  Active --> Expired: time bound reached
  Revoked --> Archived
  Expired --> Archived
  Suspended --> Revoked
```

## 7. Continuous assurance and runtime intervention

This flow shows how operational evidence feeds assurance decisions after an effect has been permitted. It makes restriction, suspension, notification, remediation and reassessment explicit rather than treating assurance as a one-time gate.

```mermaid
flowchart LR
  OBS[Operational Observations] --> COL[Evidence Collection]
  COL --> EVA[Assurance Evaluation]
  EVA --> DEC{Assurance remains sufficient?}
  DEC -- Yes --> CONT[Continue with current constraints]
  DEC -- Degraded --> REST[Restrict or increase oversight]
  DEC -- Failed --> SUSP[Suspend governed capability]
  REST --> REC[Emit governance event and decision receipt]
  SUSP --> REC
  REC --> NOTIFY[Notify accountable and affected parties]
  NOTIFY --> REVIEW[Review, remediation and reassessment]
  REVIEW --> EVA
```

**Evidence produced:** observations, assurance evaluations, governance events, decision receipts, notifications and reassessment outcomes.

## 8. Delegation fan-out, convergence and revocation impact

This flow extends the linear delegation model to show independent grants converging on one operational agent and the dependency analysis required when one grant is revoked.

```mermaid
flowchart TD
  P[Originating Principal] -->|Delegation A| D1[Delegate A]
  P -->|Delegation B| D2[Delegate B]
  D1 -->|Attenuated grant| AG[Operational Agent]
  D2 -->|Independent approval or constraint| AG
  AG --> SUB[Sub-agent or Tool]
  REV[Revocation of Delegation A] --> IMP[Dependency Resolution]
  IMP --> D1
  IMP --> AG
  IMP --> SUB
  D2 --> REEVAL[Re-evaluate remaining authority]
  IMP --> REEVAL
  REEVAL --> OUT{Sufficient authority remains?}
  OUT -- Yes --> LIMIT[Continue under reduced scope]
  OUT -- No --> STOP[Suspend or terminate effect]
```

**Evidence produced:** delegation graph, dependency-resolution record, recomputed authority scope and enforcement outcome.

## 9. Contestability, review and remedy lifecycle

This flow places affected-party notice, challenge, evidence resolution, accountable review, correction and remedy inside the governance architecture.

```mermaid
flowchart TD
  EFFECT[Governed Effect] --> NOTICE[Notice and Explanation]
  NOTICE --> PARTY[Affected Party]
  PARTY -->|Accepts| CLOSE[Close with retained evidence]
  PARTY -->|Challenges| CASE[Open Review Case]
  CASE --> RECORD[Resolve decision receipt, authority and evidence]
  RECORD --> REVIEW[Accountable or Independent Review]
  REVIEW --> RESULT{Review outcome}
  RESULT -- Upheld --> EXPLAIN[Confirm decision and reasons]
  RESULT -- Corrected --> CORRECT[Correct record or decision]
  RESULT -- Harm established --> REMEDY[Provide remedy or redress]
  CORRECT --> UPDATE[Emit superseding governance event]
  REMEDY --> UPDATE
  UPDATE --> LEARN[Update controls, policy or assurance]
```

**Evidence produced:** notice, review case, linked decision record, review finding, correction or remedy record and superseding governance event.

## 10. Profile composition and conformance evidence

This flow explains profile dependency closure and the path from a declared conformance target to a bounded, evidence-backed claim.

```mermaid
flowchart TD
  F[Foundation Profile] --> MAG[Machine-Actionable Governance]
  F --> DA[Delegated Authority]
  MAG --> RG[Runtime Governance]
  DA --> AS[Agentic Systems]
  RG --> AS
  AS --> HI[High-Impact Systems]
  RG --> CA[Continuous Assurance]
  CA --> HI
  TARGET[Declared Conformance Target] --> SELECT[Select applicable profiles]
  SELECT --> REQ[Resolve cumulative requirements]
  REQ --> TEST[Execute required tests]
  TEST --> EVID[Assemble conformance evidence]
  EVID --> CLAIM[Issue bounded conformance claim]
```

**Evidence produced:** selected-profile set, resolved requirement set, test results, evidence manifest and bounded conformance claim.
