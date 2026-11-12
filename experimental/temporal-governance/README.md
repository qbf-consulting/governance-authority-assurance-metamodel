# Temporal governance semantic pressure cases

**Status:** experimental, informative; not a GAAM v0.9.0 conformance profile.

Run `python scripts/test_temporal_governance_alignment.py` at the repository root. The standard-library-only evaluator exercises the synthetic fixtures in [cases.json](cases.json). The existing GitHub Actions validation job runs this script.

The modeled sources, evidence-coverage watermarks and policy versions are stipulated test inputs, **not authenticated facts**. The evaluator does not prove source control, reliable clock, historical availability, legal reliance, enforcement convergence, or E2/E3 independence. The synthetic `permit` result means the *modeled qualified predicates* are satisfied. It never authorizes real actions.

Case groups: TG-01–03 temporal cutoffs and retroactivity; TG-04–07 completeness, provenance, conflicting evidence and competence; TG-08–10 multi-source composition and policy version; TG-11–14 supersession, temporal ordering and absent positive evidence; TG-15 immutable original decision receipt; TG-16–17 client observation versus recording and future effectiveness. Six independent input mutations attempt false-positive outcomes.

This is a GAAM-owned semantics test. It does not import ARPA code, implement TRQP's wire contract, validate TSMM production behavior or introduce a universal temporal schema.
