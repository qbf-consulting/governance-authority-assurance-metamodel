---
title: "Changelog"
permalink: /releases/changelog/
parent: "Project Governance"
artifact_type: "Changelog"
normative_status: "Release record"
---
# Changelog

## Unreleased: temporal governance semantic alignment (informative)

- Refine GAAM-owned temporal governance roles, temporal non-amplification and evidentiary boundaries without adopting TRQP or ARPA wire models or changing the frozen v0.9.0 normative edition.
- Add cross-system GAAM–TRQP–ARPA–TSMM/TIS alignment analysis, 17 synthetic cases and six false-success probes wired into CI; explicitly retain synthetic provenance and E1-like limitations.
- Synchronize existing future-evolution concepts, documentation navigation, evidence interpretation and an evidence-gated normative disposition. Candidate distribution v0.9.5, canonical schemas, profiles, requirement IDs and published releases remain unchanged.

## [0.9.5] - 2026-11-04

### Version identity and publication
- Identify current normative **specification edition v0.9.0** independently from current **Candidate distribution/test-suite release v0.9.5**. Preserve historical v0.9.0 normative document, schema identifiers and permalink.
- Introduce backward-compatible `release.json.specificationEdition` and `PROJECT-STATUS.yaml.project.specification_edition`; retain `normativeVersion` and `candidateBaseline` as legacy Candidate **release** identifiers.
- Clarify the stable current specification index, citation and governed version-change triggers. Add failing checks for source/title-page edition, permalink, status and release mismatches.
- Preserve normative text and semantics. No E2/E3 or independent assurance claim follows from this publication correction.

### Compatibility
- Portable kit and machine-readable result release identity advance to v0.9.5 with unchanged v1 adapter semantics. Frozen v0.9.0 canonical artifact IDs, profiles, requirements and conformance meaning remain stable.

## [0.9.4] - 2026-11-04

### Fixed
- Confine portable package and manifest references to the submitted package boundary (including symlink escapes), require checksum coverage, and reject misleading integrity PASS conditions.
- Report malformed, unavailable, non-object, failed and stalled vector adapters as bounded machine-readable failures instead of unhandled execution errors.
- Reject clean-room report PASS claims with missing or mismatched requirement evidence, duplicate identifiers or uncontained evidence bytes.
- Correct outdated Candidate landing-page terminology and clarify the difference between release identity, frozen semantic baseline and post-release example revisions.

### Added
- An informative delegated-agent purchasing gateway exercise that evaluates a consequential operation through principal, authority, delegation, time, scope and policy inputs, emits a canonical-schema-shaped decision receipt, and **never executes an effect**.
- A ten-element source/evidence disposition and recorded F-102-A–E limitations for issuer/source authenticity, scenario-local policy/scope semantics, conflicting sources, receipt/effect evidence and implementation independence.
- Positive, negative and indeterminate public-CLI checks, including a false-assurance probe showing that an unauthenticated status-source label can still yield a synthetic local permit.
- A run-specific E1 gateway dossier retained in existing CI evidence artifacts: commands, exact synthetic input, expected and observed result, reason, tool versions, clock, source SHA and unverified conditions.
- Three role-based reader routes and a pinned independently authored evaluator hand-off linked to existing implementation-report/evidence-manifest and E2/E3 acceptance processes.

### Compatibility, governance and limitations
- **No changes** to frozen normative v0.9.0 specification semantics, requirement/profile identifiers, canonical schema identifiers or downstream authority rules.
- The v0.9.4 release updates **informative** portable tooling identity/result schema and maintained implementation guidance. Existing v0.9.0 artifacts remain valid, and v1 adapter request/response semantics are preserved.
- v2 raw-authority and v0.10.0 extension artifacts remain informative/experimental. Local scope comparison, policy evaluation, receipt reason codes and observation conventions are not portable normative semantics.
- The source-controlled gateway example and retained CI dossier are synthetic **E1** evidence only: neither a production authorization gateway nor proof of identity/source authenticity, reliable status freshness, effect execution, receipt signing, retention, replay protection, external E2 implementation or E3 interoperability.
- Independent participation, real newcomer usability measurements, and accepted implementation/interoperability reports remain out of scope for this maintenance release and tracked under governed processes.

## [0.9.3] - 2026-11-03

### Fixed

- Repair CLI vector filtering, pilot probes, pytest execution and excluded GitHub Pages links; enforce regression and publication checks.
- Generate validation evidence and package artifacts on each checked-out commit instead of relying on stale committed PASS reports; enforce a clean CI tree.

### Added

- Requirement-level reference audit that distinguishes fixture names from substantive assurance; conservative review findings register covering all 29 adversarial findings.
- Optional five-case v2 raw-authority evaluation with explicit UTC time, failure reasons and always-deny falsification; preserve v1 compatibility.
- Informative, opt-in experimental schema fields and tests, historical ID resolver mapping, bounded adoption configurations and protocol reference boundaries.

### Assurance limitations

- Frozen v0.9.0 semantics and schema identifiers unchanged; experimental v0.10.0 representations are not normative.
- Checksum-only packages do not establish authenticity. Independent conformance, complete scope/time semantics, cryptographic receipts and consequential-effect normative floor remain unresolved.

## [0.9.2] - 2026-09-22

### Added

- Promote the EUDI Wallet ARF v3.0.0 and GLEIF vLEI EGF v4.0 reviews into coordinated implementation-validation cases using ecosystem crosswalk schema v1.1.
- Add five behavioural vectors derived from those cases for effect-specific authority scope, upstream delegation invalidation, fail-closed unknown authority state, assurance freshness and attributable decision accountability.
- Add explicit source-finding provenance to each new vector and map every vector into requirement assurance traceability.

### Changed

- Advance the maintenance distribution, portable conformance-kit contract and test-suite identity from v0.9.1 to v0.9.2.
- Designate v0.9.2 as the current normative Candidate and implementation baseline while preserving the frozen v0.9.0 semantic/canonical artifact lineage, requirement identifiers, profile identifiers and conformance semantics.
- Keep framework-readiness mappings separate from implementation evidence and GAAM L0-L4 conformance claims.

### Documentation

- Record explicit-authority and distributed-authority benchmark roles for the vLEI and EUDI validation cases.
- Make authority sources, governed actors/relationships/effects, enforcement, revocation, assurance mechanisms, positive/negative semantics and limitations explicit in the common crosswalk contract.

## [0.9.1] - 2026-08-20

### Added

- Portable external-package and conformance-claim validation with a language-neutral adapter protocol.
- Informative conformance-kit manifest, result schema, reference adapter and Foundation starter package.
- Delegation-cycle, decision-receipt integrity, decision replay and lifecycle-event replay vectors.
- Local and scheduled remote canonical-schema byte verification.

### Changed

- Separate the v0.9.1 distribution and test-suite identity from the frozen v0.9.0 normative baseline and canonical schema namespace.
- Make release ZIP construction scope-controlled and byte-reproducible through `SOURCE_DATE_EPOCH`.
- Generate v0.9.1 package and validation evidence without changing v0.9.0 normative semantics or identifiers.

### Documentation

- Add a reusable, machine-readable ecosystem readiness crosswalk method and validated informative mappings for EUDI Wallet ARF v3.0.0 and GLEIF vLEI EGF v4.0.
- Add comparative implementation takeaways covering authority/reliance boundaries, assurance composition, unknown state, dependency-aware revocation, correction versus remedy, and test generation. These artifacts do not change GAAM v0.9.0 normative requirements or conformance semantics.

- Added a validator-controlled Future Evolution programme with expansion principles, concept classification, a normative boundary, a four-commit delivery roadmap, fifteen candidate concept pages, and a 25-entry machine-readable enhancement register. GAAM v0.9.0 normative requirements, schemas, profiles, vocabularies, conformance semantics, and threat-model content remain unchanged.
- Reorganised site navigation with four grouped Documentation routes, a top-level Implementation Reports workflow, and an Appendices section for glossary, vocabularies, matrices, mappings, FAQ, style guidance, and publication documentation. Existing file paths and permalinks remain unchanged.

## Unreleased: assurance-ready composed patterns

- Expanded the delegated agent purchasing, cross-registry recognition and high-impact multi-agent service examples into assurance-ready implementation patterns.
- Added pattern manifests, differentiated architecture and authority documentation, lifecycle, evidence, review, remedy, privacy, security and affected-party analysis.
- Added valid and invalid authority, delegation, decision-receipt, governance-event and remedy fixtures.
- Added a shared pattern catalogue, maturity model, template, validation guide and composed-pattern comparison.
- Preserved normative GAAM requirements, schemas, profiles, vocabularies, threat-model content and conformance semantics.

{% include gaam-meta.html %}

All notable changes will be documented here. The project uses Semantic Versioning adapted for an evolving specification.

## Unreleased

### Governance

- Add evidence-gated research-to-normative promotion governance with machine-readable candidate and decision contracts, fourteen promotion gates, proportional evidence thresholds, and explicit separation between research dispositions and normative approval.
- Add machine-readable implementation-report, evidence-manifest and conformance-result contracts with controlled report lifecycle, provenance, independence, claim-boundary and acceptance controls.
- Generate candidate readiness from candidate issues, governed reviews and accepted implementation evidence; expose explicit blocking gates and closure predicates in both JSON and the GitHub Pages dashboard.
- Validate positive and negative implementation-report fixtures, evidence-reference integrity and freshness of the generated readiness view.
- Add `PROJECT-STATUS.yaml` as GAAM's repository-local status and authority declaration for portfolio consumption.
- Freeze a content-addressed candidate review baseline and add machine-verifiable review/finding contracts, controlled review vocabulary, evidence directories and a joint disposition register.
- Strengthen validation so reviewer independence, decision authority, evidence references, blocker state and evidence-backed finding closure are checked without changing the v0.9.0 normative surface.

### Fixed

- Separate repository README files from GitHub Pages landing pages for all implementation patterns.
- Publish each pattern at a clean directory URL through `index.md`.
- Exclude supporting pattern pages from primary sidebar navigation while retaining direct-link and search access.
- Add publication-hygiene validation for front matter, duplicate landing pages and unexpected navigable pattern-support pages.

- Enable Just the Docs' Mermaid support (`mermaid: version: "11.16.0"` in `_config.yml`). Disabled by default when the theme is consumed as a gem, so the ```` ```mermaid ```` fenced diagrams in `diagrams/architecture-diagrams.md` were rendering as plain code blocks instead of diagrams.

- Add empty `_includes/head_custom.html`, `header_custom.html`, `footer_custom.html` and `nav_footer_custom.html` stubs. Just the Docs' own bundled templates include these unconditionally and the gem does not ship default versions of them, so the Jekyll build failed with "could not locate the included file" until the site provided them.

- Remove duplicate body-level H1 headings from page-layout documents and establish front matter as the authoritative title source.
- Refactor the GAAM page header and artifact metadata to prevent overlapping or floating titles across responsive layouts.
- Declare `kramdown-parser-gfm` explicitly so strict Jekyll builds do not depend on transitive gem resolution.
- Bring the homepage (`index.md`) and mappings landing page (`mappings/index.md`) under the shared `layout: page` template; both previously used `layout: default` and rendered without the site stylesheet, status banner, breadcrumbs and artifact metadata.
- Replace the implicit, silent `gaam-page`-marker skip in `scripts/validate_pages.py` with an explicit, empty exemption list, so any future page using `layout: default` fails the structural-contract check instead of being skipped unnoticed.
- Add a local `_layouts/default.html` override so the theme's own site-title banner no longer renders as a second `h1` on every page alongside GAAM's page-specific title; every page now has exactly one `h1`, matching the page-title contract the site already claimed. (Superseded below: the site no longer uses `jekyll-theme-minimal` or this override.)
- Add `scripts/publish_versioned_schemas.py`, run in both CI workflows after the Jekyll build, to mirror `schemas/*.json` into the versioned path (`_site/<version>/schemas/`) declared by every schema's `$id`. Previously no build step published anything at that path, so every canonical schema identifier pointed at a URL that did not exist on the live site.

### Changed

- Migrate the GitHub Pages site from `jekyll-theme-minimal` to [Just the Docs](https://just-the-docs.com). Retires the hand-built `_layouts/page.html`, `_layouts/default.html`, `_includes/status-banner.html`, `_includes/artifact-meta.html` and `assets/css/gaam.css` in favour of the theme's own layout, nested sidebar navigation, breadcrumbs, built-in search and `_sass/custom/custom.scss` extension point. Adds `_includes/gaam-meta.html`, a small include for the artifact-type/normative-status/version disclosure the theme has no equivalent for. All 65+ content pages gain `parent`/`nav_order`/`has_children` front matter driving the new sidebar; five files that previously had no front matter at all (`README.md`, `NOTICE.md`, `CODE_OF_CONDUCT.md`, `docs/open-questions.md`, `implementation-reports/TEMPLATE.md`) now do. `README.md` is excluded from the Jekyll build and remains a GitHub-rendered document only, since `index.md` is the site's actual homepage. `scripts/validate_pages.py` is rewritten to check theme-independent invariants (required pages render, exactly one `h1` per page, a stylesheet loads, a search index is published) rather than the retired theme's specific region markup.

- Upgrade supported first-party GitHub Actions to Node 24-compatible major releases.
- Add source and rendered-publication checks for the one-H1 rule, publication-region ordering and stylesheet availability.

### Documentation

- Add machine-readable candidate issue and review registers, governed GitHub issue and pull-request templates, and a v1.0.0 readiness dashboard without changing the normative specification surface.
- Add requirement-level assurance traceability, testability dispositions, and expanded negative and boundary fixtures for existing GAAM v0.9.0 obligations.
- Add an informative implementation and evidence readiness toolkit covering profile selection, self-assessment, evidence organisation, quality, retention and report preparation. Include a machine-readable evidence catalogue and an explicitly non-conformant illustrative report without changing normative requirements, schemas, profiles or conformance semantics.
- Align the GitHub Pages publication surface with the compact `jekyll-theme-minimal` scheme, explicit landing-page navigation and the supported Pages build action.
- Replace theme-dependent header navigation with content-led entry points for the specification, implementation guidance, profiles, schemas, vocabularies, conformance and releases.
- Replace oblique references to an external governance metamodel with explicit attribution to the ToIP Governance Metamodel Specification v1.0 and Companion Guide v1.0.
- Reframe the TSMM crosswalk as a GAAM source-adoption and architectural-differentiation record.
- Remove residual language implying that GAAM is a successor "v2" of the ToIP specification.
- Add repository-level source attribution and a GitHub Pages landing page for mappings.

## [0.9.0] - 2026-07-16

### Added

- Feature-complete normative requirements for canonical artifacts, lifecycle, assurance, profiles, decisions, safety, remedy, systemic harm and market integrity.
- Eight exhaustive profile manifests, canonical JSON Schemas and controlled vocabularies.
- Three end-to-end implementation patterns with positive and negative fixtures.
- Executable validation, generated evidence, threat model, ADRs and GitHub workflows.
- Full GitHub Pages navigation and `AI_USAGE.md` disclosure.
- Candidate stability and artifact-precedence governance.
- Canonical schema catalogue, behavioural vectors, threat register and traceability matrices.
- Modular validation evidence, CI workflow and reproducible v0.9.0 governance package.

### Changed

- Replaced open markers with v0.9.0 decision dispositions.
- Reframed unexplained predecessor-version language as independent architectural provenance.
- Expanded conformance, implementation and lifecycle guidance.
- Corrected the normative specification identity from v0.1.0 to v0.9.0.
- Updated active profiles, manifests, schemas, vocabularies, examples and claims to v0.9.0.
- Corrected TSMM references to the canonical repository.
- Operationalised L0–L4 conformance evidence and independence boundaries.

### Documentation

- Published canonical schemas and controlled vocabularies through GitHub Pages.
- Added stable permalinks, shared layouts, status metadata and full documentation navigation.
- Added human-readable schema, vocabulary and traceability catalogues.
- Added production-equivalent strict Jekyll build and rendered-site validation.
- Added least-privilege GitHub Pages deployment workflow.

## [0.1.0] - 2026-07-15

### Added

- Initial public draft of the Governance, Authority and Assurance Metamodel.
- Core concepts for authority, delegation, evidence, assurance, trust decisions, effects and accountability.
- Normative governance for agentic systems, runtime evaluation, registries and decentralised trust graphs.
- Composable conformance profiles.
- Requirements, relationship and conformance matrices.
- Implementation, conformance and reviewer guidance.
- Initial examples and architecture diagrams.
- Repository governance, contribution, security and release hygiene.
