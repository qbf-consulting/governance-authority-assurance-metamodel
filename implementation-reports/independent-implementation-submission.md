# Independent Implementation Evidence Submission

## Purpose

This guide defines the evidence intake path for independent implementations that want to contribute admissible GAAM E2 implementation evidence.

It supports GitHub issue #20 and does not lower the independence, provenance, or acceptance requirements already enforced by the repository.

## Eligibility

A submission intended to contribute to independent-implementation evidence MUST:

- be non-synthetic;
- identify the implementation and source revision;
- disclose relationships with GAAM maintainers and other participating organisations;
- declare the assessor's independence classification;
- identify the GAAM semantic baseline and profiles evaluated;
- provide requirement-level results;
- provide a machine-readable evidence manifest;
- preserve the referenced evidence bytes;
- contain no failed or indeterminate result or open exception inside the claimed boundary if it is intended to satisfy the readiness criterion.

Maintainer-authored fixtures, repository-owned clean-room exercises and illustrative reports remain useful adoption evidence but do not satisfy independent E2 evidence.

## Minimum execution path

1. **Select scope.** Start with the Foundation Profile. A second submission should additionally exercise at least one composed profile.
2. **Record implementation provenance.** Identify repository/source revision, runtime/build information and relevant deployment assumptions.
3. **Run portable validation.**
   - validate the implementation package;
   - validate the conformance claim;
   - run applicable behavioural vectors through the implementation adapter.
4. **Evaluate requirements.** Record requirement-level outcomes using the implementation-report contract.
5. **Assemble evidence.** Produce an evidence manifest with stable evidence IDs, paths, media types and SHA-256 digests.
6. **Disclose independence.** Record assessor identity, organisation, relationships, conflicts and independence classification.
7. **Submit.** Add the machine-readable report under `implementation-reports/reports/` through a pull request, with its evidence manifest and referenced evidence where repository retention is appropriate.
8. **Governed acceptance.** Maintainers review structural validity, evidence completeness, independence disclosure, exceptions and claim boundaries. Acceptance requires an attributable decision record.

## Required files

At minimum:

```text
implementation-reports/reports/<report-id>.json
<evidence-manifest path declared by the report>
<referenced evidence artifacts>
```

The report MUST validate against:

- `implementation-reports/implementation-report.schema.json`
- `implementation-reports/evidence-manifest.schema.json`
- `implementation-reports/conformance-result.schema.json`

## Evidence needed to satisfy #20

The repository can close #20 only when all of the following are true:

- at least two qualifying independent reports are accepted;
- both disclose relationships;
- at least one covers `gaam:profile:foundation:0.9.0`;
- at least one covers Foundation plus at least one additional profile;
- referenced evidence bytes validate against their manifests;
- no contributing report has a failed/indeterminate result or open exception inconsistent with the claimed boundary.

## Review and falsification

A structurally valid report is not automatically accepted.

The evidence is inadmissible for the independent-implementation claim if independence is not disclosed, evidence cannot be reproduced, the report relies on synthetic repository fixtures as its substantive implementation, or unresolved results are collapsed into success.

Any material semantic divergence or defect discovered during implementation enters the governed finding/change lifecycle independently of whether the implementation report is accepted.
