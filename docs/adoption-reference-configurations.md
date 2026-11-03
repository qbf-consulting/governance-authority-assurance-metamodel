---
title: "Informative Adoption Reference Configurations"
artifact_type: "Informative implementation guidance"
normative_status: "Informative"
parent: Implement
nav_order: 8
---
# Informative Adoption Reference Configurations

These examples size the initial evaluation for three adopters. **They are not new normative GAAM profiles.** Derive actual obligations from governed profile manifests and their dependencies. A structurally valid artifact does not show that runtime authority exists.

| Configuration | Starting point | Minimum evidence to inspect | Not established by a passing example |
|---|---|---|---|
| Agent gateway / enforcement point | Requested effect, actor, policy, authority, scope and decision point | Authority/delegation artifacts, receipt, status observation, negative cases and enforcement logs | Authority origin, scope attenuation across opaque dimensions, current revocation, external effect handling |
| Registry operator | Governing publisher, status lifecycle and source of authority | Registry change events, revocation rules, publication provenance and historical retention policy | Independent recognition, relying-party authorization or authentic source by URI alone |
| Framework author | Defined effect classes, selected conformance profiles and remedy paths | Effect classification, applicable manifests, documented exemptions and accountable review | Complete operational conformance or independent L4 assessment |

Start from `conformance-kit/starter/`. Run `python scripts/gaam.py validate-package conformance-kit/starter`, then `python scripts/gaam.py validate-claim conformance-kit/starter/artifacts/conformance-claim.json`. Exercise the explicitly experimental v2 adapter using `python scripts/gaam.py run-vectors --suite v2 python conformance-kit/reference_adapter.py`. A real adopter must substitute an independently implemented evaluator, preserve time and reason semantics, and provide actual enforcement evidence rather than interpreting reference adapter PASS as independent verification.

## Illustrative protocol relationships

**OAuth Token Exchange, RFC 8693.** The `subject_token` and optional `actor_token` can inform modeling of a principal and acting party; `resource`, `audience`, and `scope` bound the requested target and permissions. An exchange does not itself establish a GAAM delegation acceptance, ensure current authority at execution, or automatically propagate future revocation.

**OAuth Rich Authorization Requests, RFC 9396.** `authorization_details` objects have a required `type` whose field semantics belong to the corresponding API. `actions`, `locations`, `identifier`, and `privileges` may inform typed GAAM scope constraints, but only governed comparison semantics can establish attenuation. A requested authorization is not a grant.

**MCP tool-call enforcement.** Discovery and listing of tools are capability information; they do not authorize an actor to invoke a consequential `tools/call`. A gateway must bind authenticated caller, tool, effect, policy, resource and current authority to the actual execution decision. OAuth validation at the transport boundary and effect-specific authorization remain distinct.

Sources: https://www.rfc-editor.org/rfc/rfc8693.html ; https://www.rfc-editor.org/rfc/rfc9396.html ; https://modelcontextprotocol.io/specification/ .

These are **informative mappings only**, not implemented integration adapters or claims of conformance to any version of those protocols. Further mapping work should be driven by observed implementer failures, not speculative feature coverage.
