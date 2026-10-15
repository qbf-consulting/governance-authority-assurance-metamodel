---
title: "Design Rationale"
permalink: /docs/design-rationale/
parent: Concepts and Design
artifact_type: "Design rationale"
normative_status: "Informative"
grand_parent: Understand GAAM
nav_order: 4
---
# Design Rationale

{% include gaam-meta.html %}

## Why authority is first-class

Many digital systems authenticate actors without proving that those actors possess authority for the proposed effect. GAAM separates identity, capability and authority so implementations can prevent technically possible but unauthorised actions.

## Why effects are first-class

Governance is consequential only when it changes what a system permits, denies, constrains or escalates. Modelling effects connects abstract policy to operational outcomes and enables transaction-level conformance.

## Why delegation is a graph

Modern authority frequently passes through organisations, employees, platforms, agents, tools and sub-agents. A single delegation token cannot explain the complete chain. GAAM therefore requires lineage, scope attenuation, parent-state propagation and originating-principal continuity.

## Why trust is a decision

Treating trust as an entity property encourages overbroad reliance. GAAM models a trust decision as a contextual evaluation performed by, or attributable to, a relying party under applicable policy and risk tolerance.

## Why assurance expires

System configuration, evidence, software dependencies and operating conditions change. Assurance is consequently represented as a bounded conclusion with scope, validity, limitations, renewal and withdrawal conditions.

## Why agents are not accountability endpoints

An agent may plan and execute actions, but it does not remove the institutional relationships that enabled its deployment. GAAM requires accountable human or organisational chains and governs principal, operator, provider, deployer and supervisor roles.

## Why graph traversal is governed

A graph path may reveal that several actors recognise or delegate to one another, but path existence alone does not establish fitness for a purpose. Traversal depth, relationship semantics, provenance, status and relying-party policy determine whether a path is relevant evidence.

## Why receipts matter

Periodic audit cannot reconstruct every consequential runtime decision. Decision receipts provide proportionate records of authority, policy, evidence, outcome and accountable parties while allowing confidentiality-preserving disclosure.
