# Public repository baseline

This record captures controls reviewed under issue #9. It is repository assurance evidence, not external certification.

| Control | State | Evidence | Residual risk |
|---|---|---|---|
| Purpose/maturity/authority/adoption | PASS | `README.md`, `PROJECT-STATUS.yaml`, `GOVERNANCE.md`, `AI_USAGE.md` | None identified. |
| Licensing/attribution/release | PASS | `LICENSE`, `NOTICE.md`, `ATTRIBUTIONS.md`, `CHANGELOG.md` | Publication remains maintainer judgment. |
| Security reporting/supported versions | PASS | `SECURITY.md` | Hosted private-reporting enablement remains platform evidence. |
| Contribution/community/support | PASS | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SUPPORT.md`, issue/PR templates | None identified. |
| Dependency updates | PASS | `.github/dependabot.yml` | Hosted Dependabot enablement remains platform evidence. |
| Default-branch governance | PASS | active `protect-main` observed 2026-09-05: PRs, resolved conversations, linear history, deletion/non-fast-forward protection, strict required `validate`, no bypass actors | Required check name must remain synchronized with CI. |
| Normative/evidence validation | PASS | repository workflows, schemas/examples/docs validation | Workflow green does not override normative judgment. |
| Authority boundary | PASS | `GOVERNANCE.md`, model/docs | GAAM defines its metamodel; implementations and external standards retain their own authority. |

## Completion boundary

The applicable baseline is complete when the remediation PR merges with the required `validate` check green. Hosted GitHub security-feature enablement is not inferred from repository files.
