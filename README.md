# Governance, Authority and Assurance Metamodel

[![Version](https://img.shields.io/badge/version-0.9.0-blue.svg)](VERSION)
[![Status](https://img.shields.io/badge/status-candidate%20specification-purple.svg)](releases/v0.9.0.md)
[![Validation](https://github.com/sankarshanmukhopadhyay/governance-authority-assurance-metamodel/actions/workflows/validate.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/governance-authority-assurance-metamodel/actions/workflows/validate.yml)

GAAM specifies how digital and agentic systems represent and enforce **authority, delegation, revocation, evidence, assurance, trust decisions, effects, accountability, appeal and remedy**. It treats governance as an executable system property rather than a document-only control layer.

Version **0.9.0** is the **Candidate Specification**. Its normative surface, eight composable profiles, canonical schemas, governed vocabularies, behavioural test vectors, threat traceability and reproducible governance package are available for implementation and external review. Candidate status does not constitute certification or independent interoperability.

Repository-owned maturity, lifecycle, authority boundaries, validation commands and known limitations are declared in [`PROJECT-STATUS.yaml`](PROJECT-STATUS.yaml). This declaration is the status source consumed by portfolio governance and does not expand GAAM's normative scope.

## Start here

- [Normative specification](specification/governance-authority-assurance-metamodel.md)
- [Architecture overview](docs/architecture-overview.md)
- [Implementation guide](docs/implementation-guide.md)
- [Conformance and assurance guide](docs/conformance-guide.md)
- [Profiles](profiles/index.md)
- [Schemas](schemas/index.md)
- [Threat model](threat-model/README.md)
- [Candidate stability policy](docs/candidate-stability-policy.md)
- [Candidate readiness dashboard](docs/candidate-readiness.md) — generated from review and implementation evidence
- [Implementation reports](implementation-reports/README.md) — human and machine-readable evidence workflow
- [Migration from v0.5.0](docs/migration-v0.5.0-to-v0.9.0.md)
- [v0.9.0 release notes](releases/v0.9.0.md)

## Validate

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

The validator produces `validation/validation-report.json`, `VALIDATION_REPORT.md`, requirement coverage, threat traceability and package checksums. A passing run means the repository satisfies its publication, structural and included behavioural checks. It does not create an L4 independent-assessment claim.

## Release progression

| Version | Status |
|---|---|
| v0.1.0 | Initial Public Draft |
| v0.5.0 | Feature Complete Draft |
| **v0.9.0** | **Candidate Specification** |
| v1.0.0 | Stable Initial Release, subject to candidate exit criteria |

## Source relationship

GAAM is an independent specification. The [Trust Systems Meta-Model](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model) informed selected semantic analysis, documented in the [TSMM adoption crosswalk](mappings/tsmm-v0.22.0-adoption-crosswalk.md), without creating a normative dependency.

## License

See [LICENSE](LICENSE), [NOTICE](NOTICE.md) and [ATTRIBUTIONS](ATTRIBUTIONS.md).

### Evidence-gated evolution

Future-evolution research remains outside v0.9.0 conformance. Any later research-to-normative transition is governed through machine-readable promotion candidates, fourteen evidence gates and separately attributable promotion decisions under `governance/promotion/`.
