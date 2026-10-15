---
title: "Reviewer Guide"
permalink: /docs/reviewer-guide/
parent: Implementation Guidance
artifact_type: "Review guide"
normative_status: "Informative"
grand_parent: Implement
nav_order: 5
---
# Reviewer Guide

{% include gaam-meta.html %}

## Review priorities

Reviewers should focus first on architecture rather than wording:

1. Are authority, delegation and accountability correctly separated?
2. Can the metamodel govern multi-hop agent execution without protocol assumptions?
3. Are trust-graph relationships sufficiently typed and contestable?
4. Can an implementation determine what must happen when evidence or status is missing?
5. Are conformance targets testable and proportionate?
6. Are affected-party and redress requirements operational rather than aspirational?

## Comment format

A high-value review comment should identify the section or requirement, describe the failure scenario, explain the consequence and propose either revised text or a decision question.

## Release-blocking findings

The following should be treated as release-blocking for later stable milestones:

- authority amplification through valid-looking delegation;
- loss of originating-principal or accountable-party traceability;
- silent acceptance when required evidence cannot be verified;
- graph semantics that allow automated reliance on untyped relationships;
- assurance claims without scope or validity;
- consequential agent actions without interruption or redress paths.
