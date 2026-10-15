---
title: Normative Boundary
permalink: /docs/future-evolution/normative-boundary/
parent: Future Evolution
grand_parent: Project & Evolution
nav_order: 3
artifact_type: Normative-boundary guidance
normative_status: Informative
---
# Normative Boundary

The future-evolution programme does not modify GAAM v0.9.0 conformance.

The following directories remain the authoritative candidate surface and are not changed by this programme commit:

```text
specification/
schemas/
profiles/
vocabularies/
conformance/
threat-model/
```

Future-evolution material therefore:

- uses `normative_status: Informative` or an equivalent experimental designation;
- cannot be cited as a GAAM v0.9.0 requirement;
- cannot be used to strengthen a v0.9.0 conformance claim;
- is excluded from canonical schema and vocabulary catalogues;
- is promoted only through the governed change and release process;
- must identify assumptions, limitations, unresolved issues, and required evidence.

The validator checks this boundary and verifies the enhancement register against controlled classifications and statuses.
