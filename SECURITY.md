---
title: "Security Policy"
permalink: /governance/security/
parent: "Project Governance"
artifact_type: "Security policy"
normative_status: "Normative process"
---
# Security Policy

{% include gaam-meta.html %}

## Supported versions

Security and normative-safety fixes are applied to current `main` and the latest supported release identified by repository status/release metadata. Older releases should be treated as unsupported unless a maintainer explicitly states otherwise.

## Scope

Security reports may concern repository automation, published schemas, examples, or specification defects that could predictably enable unsafe authority, delegation, evidence, registry or agent behaviour.

## Reporting

Do not publish exploit details or sensitive ecosystem information in a public issue. Use GitHub private vulnerability reporting when enabled. Otherwise contact the repository owner privately and include:

- affected version, file or requirement;
- impact and plausible exploitation path;
- whether implementations or evidence may already be exposed;
- suggested mitigation; and
- disclosure constraints.

## Specification vulnerabilities

A normative ambiguity may be treated as a security issue when reasonable conforming implementations could admit unauthorised effects, lose accountability, suppress revocation or misrepresent assurance. Remediation must identify affected normative/evidence artifacts and must not silently preserve an assurance claim that depended on defective semantics.
