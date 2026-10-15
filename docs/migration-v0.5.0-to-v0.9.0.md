---
title: "Migration from GAAM v0.5.0 to v0.9.0"
permalink: /docs/migration-v0.5.0-to-v0.9.0/
parent: Implementation Guidance
artifact_type: "Migration guide"
normative_status: "Informative"
grand_parent: Implement
nav_order: 4
---
# Migration from GAAM v0.5.0 to v0.9.0

{% include gaam-meta.html %}

## Required changes

1. Bind implementations and claims to `0.9.0` and the exact profile identifiers used.
2. Replace provisional `example.org` schema identifiers with the v0.9.0 canonical namespace.
3. Revalidate profile dependencies and evidence obligations.
4. Add test-suite version, assessment independence, claim status and review/expiry metadata to conformance claims where applicable.
5. Test authority attenuation, expiry, suspension, revocation propagation, decision traceability, appeal and remedy behaviour.
6. Regenerate package manifests and checksums.

## Compatibility

The core conceptual model is retained. v0.9.0 strengthens release identity, artifact precedence, conformance evidence and behavioural assurance. A v0.5.0 structural pass is not automatically a v0.9.0 conformance result.
