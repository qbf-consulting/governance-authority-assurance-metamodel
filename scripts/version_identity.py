"""Falsifiable GAAM distribution, normative edition and canonical identity contract."""
from pathlib import Path
import re

def check_identity(release, specification, current_index, status, version):
    problems=[]
    distribution=release.get("version")
    edition=release.get("specificationEdition")
    baseline=release.get("semanticBaseline")
    canonical=release.get("canonicalArtifactVersion")
    if not isinstance(edition,str) or not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+",edition):
        return ["missing or invalid specificationEdition"]
    if distribution!=version:
        problems.append("VERSION differs from Candidate release")
    if release.get("normativeVersion")!=distribution or release.get("candidateBaseline")!=distribution:
        problems.append("legacy Candidate release identity mismatch")
    if release.get("normativeChange") is False and edition!=baseline:
        problems.append("maintenance release edition differs from semantic baseline")
    if release.get("normativeChange") is False and canonical!=baseline:
        problems.append("maintenance release changes frozen canonical artifact version")
    if f"**Version:** {edition}" not in specification:
        problems.append("normative document title version differs from specificationEdition")
    if f"permalink: /specification/gaam-v{edition}/" not in specification:
        problems.append("normative document historical permalink differs from specificationEdition")
    if f"**Current specification edition:** v{edition}" not in current_index:
        problems.append("current index edition mismatch")
    if f"**Current Candidate distribution and implementation kit:** v{distribution}" not in current_index:
        problems.append("current index distribution mismatch")
    if "permalink: /specification/" not in current_index:
        problems.append("stable current index permalink missing")
    project=status.get("project",{})
    if str(project.get("specification_edition"))!=edition:
        problems.append("PROJECT-STATUS specification edition mismatch")
    if str(project.get("normative_baseline"))!=distribution:
        problems.append("PROJECT-STATUS Candidate release mismatch")
    if str(project.get("semantic_baseline"))!=baseline or str(project.get("canonical_artifact_version"))!=canonical:
        problems.append("PROJECT-STATUS semantic/canonical baseline mismatch")
    if not isinstance(release.get("schemaBase"),str) or f"/v{canonical}/schemas/" not in release["schemaBase"]:
        problems.append("schemaBase canonical namespace mismatch")
    return problems

def check_repository(root):
    import json
    import yaml
    release=json.loads((root/"release.json").read_text(encoding="utf-8"))
    spec=(root/release["normativeSpecification"]).read_text(encoding="utf-8")
    index=(root/"specification/index.md").read_text(encoding="utf-8")
    status=yaml.safe_load((root/"PROJECT-STATUS.yaml").read_text(encoding="utf-8"))
    version=(root/"VERSION").read_text(encoding="utf-8").strip()
    return check_identity(release,spec,index,status,version)

if __name__=="__main__":
    import sys
    issues=check_repository(Path(__file__).resolve().parents[1])
    for msg in issues: print("Version identity: "+msg,file=sys.stderr)
    if not issues: print("Version identity and publication: PASS")
    raise SystemExit(1 if issues else 0)
