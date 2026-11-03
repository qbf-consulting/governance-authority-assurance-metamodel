# GAAM npm development-dependency security disposition (2026-11-03)

**Scope:** `package-lock.json`, npm development dependencies used by `scripts/validate_mermaid.mjs` in GitHub Actions. This is a **toolchain remediation**, not a normative GAAM change, runtime authorization control, assessment, or independent security certification.

## Dependency path and reachability

`mermaid@11.16.1` is a direct development dependency of GAAM. Its dependency manifest includes `dompurify@^3.3.3` and `katex@^0.16.45`. GAAM's Node-based validator creates a jsdom document and calls `mermaid.parse` on documentation Mermaid blocks; CI installs this npm tree with `npm ci`. The current Jekyll Pages publication uses a separate rendering path; a vulnerable **dev** dependency does not prove that the affected JavaScript is served to browsers, but it is installed and used by CI. Published-site dependency reachability requires its own assessment and is **not inferred** from dev-only metadata.

## Advisory disposition

| Alert | Package | Observed before fix | Fixed dependency | Disposition |
| --- | --- | --- | --- | --- |
| #15, incomplete IN_PLACE fix / GHSA-mrv2-3pqr-j5jr | DOMPurify | 3.4.13 | 3.4.17 | Pin transitively with npm override; verify lock and CI |
| #12, node-removing afterSanitize hooks / GHSA-p98j-92pf-mc4p | DOMPurify | 3.4.13 | 3.4.17 | Included in same corrected version |
| #16, SMIL attribute guard on XHTML media type | DOMPurify | 3.4.13 | 3.4.17 | Included in same corrected version |
| #14, IN_PLACE force-removed rawtext root | DOMPurify | 3.4.13 | 3.4.17 | Included in same corrected version |
| #13, prototype pollution influences KaTeX trust / GHSA-238p-pmpm-9mq7 | KaTeX | 0.16.47 | 0.18.2 | Targeted npm override, **outside Mermaid's declared semver range**; require full diagram and Pages validation |

### Compatibility decision

Do not casually upgrade Mermaid 11 to 12 merely to force a fix into the dependency tree: that could introduce unrelated diagram or publication regressions. Instead hold Mermaid at 11.16.1 and pin **both** patched libraries using npm overrides and SRI-validated lockfile packages. KaTeX 0.18.2 is outside Mermaid's published `^0.16.45` range, so a green install alone cannot establish compatibility. Parse the repository's actual diagram corpus with the existing validator and require rendered-page and conformance checks to remain green. This is tested compatibility for the **GAAM diagram corpus**, not a general upstream support guarantee. A later compatible upstream Mermaid release should replace the override through a separate evaluated upgrade.

The committed lock entries were sourced using matching npm resolved URLs and SHA-512 SRI digests published in independently indexed lockfile examples; `npm ci` rechecks them against the downloaded packages. No lockfile integrity hashes are invented. `scripts/check_npm_security.py` detects version/override drift and duplicate vulnerable nested entries.

## Verification commands

```bash
python scripts/check_npm_security.py
npm ci
npm ls mermaid dompurify katex
npm run validate:mermaid
python scripts/validate.py
bundle exec jekyll build --strict_front_matter --trace
python scripts/validate_pages.py
```

CI also runs canonical publication and reproducible archive checks. These commands are evidence of repository-owned reproducibility, not an independent assessment of all possible Mermaid/KaTeX input patterns. Actual security dashboard closure can lag after merge and must be checked separately.

## Maintenance and residual risk

Dependabot weekly npm updates are enabled so subsequent updates can be reviewed instead of silently accumulating stale transitive packages. Fixed-version overrides are intentionally narrow and should be revisited when Mermaid supports patched KaTeX within its declared range. A full browser-side exploitation test is outside this CI maintenance tranche; no undocumented assumption of impossibility of XSS or prototype pollution is asserted. The existing `dompurify@3.4.16` PR is insufficient and should be superseded once this replacement is green and merged.

**Normative and release boundary:** no changed GAAM candidate semantics, canonical schemas, profile IDs, conformance levels, assurance classification, or release version. GitHub Actions should publish docs from validated main without cutting a new candidate release solely for this security-tooling update.
