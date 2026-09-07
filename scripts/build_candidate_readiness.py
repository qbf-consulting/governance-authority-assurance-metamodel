#!/usr/bin/env python3
"""Generate GAAM specification readiness and external evidence maturity independently."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]
RELEASE=json.loads((ROOT/'release.json').read_text()); VERSION=RELEASE.get('normativeVersion',RELEASE['version'])
def load(path): return json.loads((ROOT/path).read_text())
def refs_for_review(name):
    path=f'governance/reviews/{name}.json'; obj=load(path); return obj,[path]+obj.get('evidence',[])
issues=load('governance/candidate-issues.json'); issue_by_id={x['id']:x for x in issues.get('issues',[])}
classification={x['id']:x for x in load('governance/v1-gate-classification.json')['gates']}
reports=[]; reports_dir=ROOT/'implementation-reports/reports'
if reports_dir.exists():
    for p in sorted(reports_dir.glob('*.json')): reports.append((p,json.loads(p.read_text())))
accepted=[(p,o) for p,o in reports if o.get('reportStatus')=='accepted' and not o.get('synthetic',False)]
accepted_ids=[o.get('reportId') for _,o in accepted]
independent=[(p,o) for p,o in accepted if o.get('independence',{}).get('classification')=='independent' and o.get('independence',{}).get('relationshipsDisclosed') is True]
def qualifies(o):
    rs={x.get('status') for x in o.get('results',[])}; es={x.get('status') for x in o.get('exceptions',[])}
    return bool(o.get('results')) and not (rs & {'fail','indeterminate'}) and not (es & {'open'})
qualifying=[(p,o) for p,o in independent if qualifies(o)]
foundation='gaam:profile:foundation:0.9.0'
foundation_covered=any(foundation in o.get('profiles',[]) for _,o in qualifying)
composed_covered=any(foundation in o.get('profiles',[]) and any(x!=foundation for x in o.get('profiles',[])) for _,o in qualifying)
privacy,privacy_refs=refs_for_review('privacy-review'); security,security_refs=refs_for_review('security-review'); affected,affected_refs=refs_for_review('affected-party-review'); interop,interop_refs=refs_for_review('interoperability-review'); implementation,impl_refs=refs_for_review('implementation-evidence')
def review_complete(o): return o.get('status')=='complete' and o.get('attestation',{}).get('status')=='attested' and not o.get('blockingFindings',[])
def gate(gid,title,state,closure,evidence=None,source=None):
    c=classification[gid]
    return {'id':gid,'title':title,'state':state,'controlBoundary':c['control'],'blocksSpecificationStable':c['blocksSpecificationStable'],'evidenceLevel':c['evidenceLevel'],'proves':c['proves'],'evidence':evidence or [],'closurePredicate':closure,'sourceIssues':source or []}
report_evidence=[str(p.relative_to(ROOT)) for p,_ in accepted]
gates=[
 gate('independent-implementations','Two independent implementations','satisfied' if len(qualifying)>=2 else ('in-progress' if qualifying else 'not-satisfied'),'At least two admissible independent implementation reports.',report_evidence,['GAAM-CR-001']),
 gate('foundation-implementation','Foundation implementation coverage','satisfied' if foundation_covered else 'not-satisfied','At least one admissible independent report covers Foundation.',report_evidence,['GAAM-CR-001']),
 gate('composed-profile-implementation','Composed-profile implementation coverage','satisfied' if composed_covered else 'not-satisfied','At least one admissible independent report covers Foundation plus another profile.',report_evidence,['GAAM-CR-001']),
 gate('requirement-testability','Requirement testability disposition','satisfied','Normative requirement index and test coverage remain validator-clean.',['matrices/normative-requirements-index.csv','matrices/requirement-test-coverage.csv']),
 gate('canonical-identifiers','Canonical identifier publication','satisfied' if issue_by_id['GAAM-CR-003']['status']=='closed' else 'not-satisfied','Canonical identifiers remain publication-bound and historically retrievable.',['governance/candidate-issues.json'],['GAAM-CR-003']),
 gate('privacy-review','Independent privacy review','satisfied' if review_complete(privacy) else ('in-progress' if privacy.get('status')=='in-progress' else 'not-satisfied'),'Independent privacy review is complete and attested.',privacy_refs,['GAAM-CR-004']),
 gate('security-review','Independent security review','satisfied' if review_complete(security) else ('in-progress' if security.get('status')=='in-progress' else 'not-satisfied'),'Independent security review is complete and attested.',security_refs,['GAAM-CR-005']),
 gate('affected-party-review','Independent affected-party review','satisfied' if review_complete(affected) else ('in-progress' if affected.get('status')=='in-progress' else 'not-satisfied'),'Independent affected-party review is complete and attested.',affected_refs,['GAAM-CR-004']),
 gate('cross-implementation-interoperability','Cross-implementation interoperability','satisfied' if review_complete(interop) and issue_by_id['GAAM-CR-002']['status']=='closed' else ('in-progress' if interop.get('status')=='in-progress' else 'not-satisfied'),'Admissible cross-validator evidence from independent implementations exists.',interop_refs,['GAAM-CR-002']),
 gate('governed-ecosystem-applicability','Governed ecosystem applicability','in-progress','Independent applicability evidence exists for the declared ecosystem boundary.',impl_refs),
]
# Stable remains fail-closed on any repository-controlled candidate issue explicitly marked blockingV1.
open_repo_blockers=[x for x in issues.get('issues',[]) if x.get('blockingV1') and x.get('status')!='closed']
gates.append(gate('candidate-issue-disposition','Repository-controlled candidate issue disposition','satisfied' if not open_repo_blockers else 'not-satisfied','Every repository-controlled candidate issue marked blockingV1 is closed with required evidence.',['governance/candidate-issues.json'],[x['id'] for x in open_repo_blockers]))
# A known blocking finding is a specification blocker even when independent attestation is not required for Stable.
known_findings=[]
for name,obj in [('privacy',privacy),('security',security),('affected-party',affected)]:
    for finding in obj.get('blockingFindings',[]): known_findings.append({'review':name,'finding':finding})
spec_blocking=[g['id'] for g in gates if g['blocksSpecificationStable'] and g['state']!='satisfied']
if known_findings: spec_blocking.append('known-material-findings')
# Evidence levels are monotonic and claim-bounded. E2 requires admissible independent evidence; E3 additionally requires interop.
e2_impl=len(qualifying)>=2 and foundation_covered and composed_covered
e2_reviews=all(review_complete(x) for x in [privacy,security,affected])
e2=e2_impl and e2_reviews
e3=e2 and review_complete(interop) and issue_by_id['GAAM-CR-002']['status']=='closed'
evidence_level='E3' if e3 else ('E2' if e2 else 'E1')
out={'gaamVersion':VERSION,'maturityModel':'governance/maturity-model.json','gateClassification':'governance/v1-gate-classification.json','specification':{'eligibleForStableDecision':not spec_blocking,'blockingGates':spec_blocking,'knownBlockingFindings':known_findings},'evidence':{'level':evidence_level,'acceptedImplementationReports':accepted_ids,'independentImplementationEvidenceSatisfied':e2_impl,'independentReviewEvidenceSatisfied':e2_reviews,'crossImplementationEvidenceSatisfied':e3},'gates':gates}
json_text=json.dumps(out,indent=2)+'\n'
label={'satisfied':'Complete','in-progress':'In progress','not-satisfied':'Not started'}
lines=['---','title: "Maturity and Evidence Dashboard"','permalink: /governance/candidate-readiness/','parent: Assurance and Governance Tracking','artifact_type: "Generated governance view"','normative_status: "Informative"','grand_parent: Documentation','nav_order: 2','---','# Maturity and Evidence Dashboard','','{% include gaam-meta.html %}','','> **Generated view.** Do not edit by hand. Run `python scripts/build_candidate_readiness.py`.','','GAAM tracks **specification maturity** separately from **external evidence maturity**. Missing evidence controlled exclusively by independent actors does not become a veto over specification development; it remains an explicit unproven evidence claim. External evidence can still falsify assumptions and trigger governed reassessment.','','## Current decision state','',f'**Eligible for a Stable specification release decision:** **{"YES" if out["specification"]["eligibleForStableDecision"] else "NO"}**  ',f'**Specification blockers:** {len(spec_blocking)}  ',f'**External evidence maturity:** **{evidence_level}**  ',f'**Accepted independent implementation reports:** {len(accepted_ids)}','','A Stable/E1 state asserts specification stability and repository validation only. It does **not** assert independent implementation, independent assurance, interoperability, operational fitness, certification, or deployment validation.','','## Gate classification','','| Gate | State | Control boundary | Blocks Stable | Evidence level | Proposition |','|---|---|---|---:|---|---|']
for g in gates: lines.append(f'| {g["title"]} | {label[g["state"]]} | {g["controlBoundary"]} | {"Yes" if g["blocksSpecificationStable"] else "No"} | {g["evidenceLevel"]} | {g["proves"].replace("|","/")} |')
lines += ['','## Specification blockers','']
if spec_blocking:
    for x in spec_blocking: lines.append(f'- `{x}`')
else: lines.append('No repository-controlled Stable blocker is currently open.')
lines += ['','## Evidence boundary','','Synthetic, self-assessed, maintainer-authored and repository-owned fixtures never satisfy independent E2/E3 claims. Independent implementation and review evidence advances E2; cross-implementation evidence advances E3. Missing external evidence leaves those claims unproven rather than making the specification unstable.','','## Reassessment rule','','If external implementation, review or interoperability evidence exposes a material ambiguity, security/privacy defect, semantic divergence or invalid normative assumption, that finding enters the governed change lifecycle and may invalidate Stable readiness until disposition and reassessment complete.']
md_text='\n'.join(lines)+'\n'
if '--check' in sys.argv:
    stale=[]
    for p,text in [('governance/candidate-readiness.json',json_text),('docs/candidate-readiness.md',md_text)]:
        if not (ROOT/p).exists() or (ROOT/p).read_text()!=text: stale.append(p)
    if stale: print('stale generated maturity state: '+', '.join(stale),file=sys.stderr); sys.exit(1)
else:
    (ROOT/'governance/candidate-readiness.json').write_text(json_text); (ROOT/'docs/candidate-readiness.md').write_text(md_text)
print(json.dumps({'eligibleForStableDecision':out['specification']['eligibleForStableDecision'],'blockingGates':len(spec_blocking),'evidenceLevel':evidence_level},indent=2))
