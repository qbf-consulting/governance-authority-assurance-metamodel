#!/usr/bin/env python3
"""Generate GAAM candidate-readiness state from authoritative repository evidence."""
from pathlib import Path
import json,sys

ROOT=Path(__file__).resolve().parents[1]
VERSION=(ROOT/'VERSION').read_text().strip()

def load(path):
    return json.loads((ROOT/path).read_text())

def refs_for_review(name):
    path=f'governance/reviews/{name}.json'
    obj=load(path)
    refs=[path]
    refs.extend(obj.get('evidence',[]))
    return obj, refs

issues=load('governance/candidate-issues.json')
issue_by_id={x['id']:x for x in issues.get('issues',[])}
reports=[]
reports_dir=ROOT/'implementation-reports/reports'
if reports_dir.exists():
    for p in sorted(reports_dir.glob('*.json')):
        reports.append((p,json.loads(p.read_text())))

accepted=[(p,o) for p,o in reports if o.get('reportStatus')=='accepted' and not o.get('synthetic',False)]
accepted_ids=[o.get('reportId') for _,o in accepted]
independent=[(p,o) for p,o in accepted if o.get('independence',{}).get('classification')=='independent' and o.get('independence',{}).get('relationshipsDisclosed') is True]
def qualifies(o):
    result_states={x.get('status') for x in o.get('results',[])}
    exception_states={x.get('status') for x in o.get('exceptions',[])}
    return bool(o.get('results')) and not (result_states & {'fail','indeterminate'}) and not (exception_states & {'open'})
qualifying_independent=[(p,o) for p,o in independent if qualifies(o)]
foundation='gaam:profile:foundation:0.9.0'
foundation_covered=any(foundation in o.get('profiles',[]) for _,o in qualifying_independent)
composed_covered=any(any(x!=foundation for x in o.get('profiles',[])) for _,o in qualifying_independent)

privacy, privacy_refs=refs_for_review('privacy-review')
security, security_refs=refs_for_review('security-review')
affected, affected_refs=refs_for_review('affected-party-review')
interop, interop_refs=refs_for_review('interoperability-review')
implementation, impl_refs=refs_for_review('implementation-evidence')


def issue_state(issue_id):
    x=issue_by_id[issue_id]
    return x.get('status')=='closed', [f'governance/candidate-issues.json#{issue_id}']

def review_complete(obj):
    return obj.get('status')=='complete' and obj.get('attestation',{}).get('status')=='attested' and not obj.get('blockingFindings',[])

def gate(gid,title,state,closure,evidence=None,source_issues=None,blocking=True):
    return {'id':gid,'title':title,'state':state,'blocking':blocking,'evidence':evidence or [],'closurePredicate':closure,'sourceIssues':source_issues or []}

cr1_closed,_=issue_state('GAAM-CR-001')
cr2_closed,_=issue_state('GAAM-CR-002')
cr3_closed,_=issue_state('GAAM-CR-003')
cr4_closed,_=issue_state('GAAM-CR-004')
cr5_closed,_=issue_state('GAAM-CR-005')

report_evidence=[str(p.relative_to(ROOT)) for p,_ in accepted]
gates=[]
gates.append(gate('independent-implementations','Two independent implementations',
    'satisfied' if len(qualifying_independent)>=2 else ('in-progress' if len(qualifying_independent)>0 else 'not-satisfied'),
    'At least two non-synthetic accepted implementation reports declare independent assessment with disclosed relationships and contain no failed or indeterminate result or open exception.',
    report_evidence,['GAAM-CR-001']))
gates.append(gate('foundation-implementation','Foundation implementation coverage',
    'satisfied' if foundation_covered else 'not-satisfied',
    'At least one accepted independent implementation report includes the Foundation Profile.',report_evidence,['GAAM-CR-001']))
gates.append(gate('composed-profile-implementation','Composed-profile implementation coverage',
    'satisfied' if composed_covered else 'not-satisfied',
    'At least one accepted independent implementation report covers Foundation plus at least one additional GAAM profile.',report_evidence,['GAAM-CR-001']))

gates.append(gate('requirement-testability','Requirement testability disposition','satisfied',
    'The normative requirement index and requirement-test coverage matrix remain validator-clean.',
    ['matrices/normative-requirements-index.csv','matrices/requirement-test-coverage.csv']))
gates.append(gate('canonical-identifiers','Canonical identifier publication',
    'satisfied' if cr3_closed else 'in-progress',
    'GAAM-CR-003 is closed with resolvable versioned identifiers, checksum verification and historical-retention evidence.',
    ['governance/candidate-issues.json'],['GAAM-CR-003']))

gates.append(gate('privacy-review','Privacy review',
    'satisfied' if review_complete(privacy) else ('in-progress' if privacy.get('status')=='in-progress' else 'not-satisfied'),
    'The privacy review is complete, attested, and has no unresolved blocking findings.',privacy_refs,['GAAM-CR-004']))
gates.append(gate('security-review','Security review',
    'satisfied' if review_complete(security) else ('in-progress' if security.get('status')=='in-progress' else 'not-satisfied'),
    'The security review is complete, attested, and has no unresolved blocking findings or unresolved critical security issue.',security_refs,['GAAM-CR-005']))
gates.append(gate('affected-party-review','Affected-party review',
    'satisfied' if review_complete(affected) else ('in-progress' if affected.get('status')=='in-progress' else 'not-satisfied'),
    'The affected-party review is complete, attested, and has no unresolved blocking findings.',affected_refs,['GAAM-CR-004']))
gates.append(gate('cross-implementation-interoperability','Cross-implementation interoperability',
    'satisfied' if review_complete(interop) and cr2_closed else ('in-progress' if interop.get('status')=='in-progress' else 'not-satisfied'),
    'The interoperability review is complete and GAAM-CR-002 is closed with cross-validator evidence from independent implementations.',interop_refs,['GAAM-CR-002']))

eco_att=ROOT/'governance/reviews/evidence/implementation/ecosystems/reviewer-attestation.json'
eco_independent=False
if eco_att.exists():
    att=json.loads(eco_att.read_text())
    eco_independent=att.get('independence')=='independent' and att.get('status') in {'complete','attested','accepted'}
gates.append(gate('governed-ecosystem-applicability','Governed ecosystem applicability',
    'satisfied' if eco_independent else 'in-progress',
    'The governed ecosystem capability assessment receives independent attestation and candidate enhancement dispositions are reviewed.',
    impl_refs,[],False))

open_candidate=[x for x in issues.get('issues',[]) if x.get('blockingV1') and x.get('status')!='closed']
gates.append(gate('candidate-issue-disposition','Breaking candidate issue disposition',
    'satisfied' if not open_candidate else 'not-satisfied',
    'Every candidate issue with blockingV1=true is closed with its required evidence.',
    ['governance/candidate-issues.json'],[x['id'] for x in open_candidate]))

blocking=[g['id'] for g in gates if g['blocking'] and g['state']!='satisfied']
out={
    'gaamVersion':VERSION,
    'generatedFrom':[
        'governance/candidate-issues.json',
        'governance/reviews/privacy-review.json',
        'governance/reviews/security-review.json',
        'governance/reviews/affected-party-review.json',
        'governance/reviews/interoperability-review.json',
        'governance/reviews/implementation-evidence.json',
        'implementation-reports/reports/*.json',
        'matrices/normative-requirements-index.csv',
        'matrices/requirement-test-coverage.csv'
    ],
    'eligibleForV1Decision':not blocking,
    'acceptedImplementationReports':accepted_ids,
    'blockingGates':blocking,
    'gates':gates
}
json_text=json.dumps(out,indent=2)+'\n'

state_label={'satisfied':'Complete','in-progress':'In progress','not-satisfied':'Not started','blocked':'Blocked'}
lines=[
'---',
'title: "Candidate Readiness Dashboard"',
'permalink: /governance/candidate-readiness/',
'parent: Assurance and Governance Tracking',
'artifact_type: "Generated governance view"',
'normative_status: "Informative"',
'grand_parent: Documentation',
'nav_order: 2',
'---',
'# Candidate Readiness Dashboard','',
'{% include gaam-meta.html %}','',
'> **Generated view.** Do not edit the gate table by hand. Run `python scripts/build_candidate_readiness.py` after changing candidate issues, review registers, or implementation reports.','',
'This dashboard exposes the evidence currently available for progression from GAAM v0.9.0 to v1.0.0. Its authoritative machine-readable state is [`governance/candidate-readiness.json`](../governance/candidate-readiness.json).','',
'## Current decision state','',
f'**Eligible for a v1.0.0 release decision:** **{"YES" if out["eligibleForV1Decision"] else "NO"}**  ',
f'**Blocking gates:** {len(blocking)}  ',
f'**Accepted implementation reports:** {len(accepted_ids)}','',
'## Candidate gates','',
'| Gate | State | Blocking | Closure predicate |',
'|---|---|---:|---|'
]
for g in gates:
    lines.append(f'| {g["title"]} | {state_label[g["state"]]} | {"Yes" if g["blocking"] else "No"} | {g["closurePredicate"].replace("|","/")} |')
lines += ['','## Current blockers','']
if blocking:
    for bid in blocking:
        g=next(x for x in gates if x['id']==bid)
        issues=', '.join(g.get('sourceIssues',[])) or 'No candidate issue ID'
        lines.append(f'- `{bid}` — {g["title"]}. Source issue(s): {issues}.')
else:
    lines.append('No blocking gate is currently open.')
lines += ['','## Evidence acceptance boundary','',
'Only non-synthetic implementation reports with `reportStatus: accepted` are candidate-readiness inputs. An accepted report contributes to the independent-implementation gate only when it declares `independence.classification: independent` and `relationshipsDisclosed: true`. Schema-valid examples and fixtures never satisfy candidate exit criteria.','',
'## Decision rule','',
'A v1.0.0 release decision is eligible only when every blocking gate in `governance/candidate-readiness.json` is `satisfied`. Eligibility permits a governed release decision; it does not itself approve or publish v1.0.0.','',
'## How to submit evidence','',
'Use the repository issue forms and the [Implementation Reports](../implementation-reports/) workflow. Machine-readable reports must validate against `implementation-reports/implementation-report.schema.json`, reference a valid evidence manifest, disclose assessment independence, and remain within their stated claim boundary.'
]
md_text='\n'.join(lines)+'\n'
if '--check' in sys.argv:
    stale=[]
    if not (ROOT/'governance/candidate-readiness.json').exists() or (ROOT/'governance/candidate-readiness.json').read_text()!=json_text:
        stale.append('governance/candidate-readiness.json')
    if not (ROOT/'docs/candidate-readiness.md').exists() or (ROOT/'docs/candidate-readiness.md').read_text()!=md_text:
        stale.append('docs/candidate-readiness.md')
    if stale:
        print('stale generated candidate readiness: '+', '.join(stale),file=sys.stderr)
        sys.exit(1)
else:
    (ROOT/'governance/candidate-readiness.json').write_text(json_text)
    (ROOT/'docs/candidate-readiness.md').write_text(md_text)
print(json.dumps({'eligibleForV1Decision':out['eligibleForV1Decision'],'blockingGates':len(blocking),'acceptedImplementationReports':len(accepted_ids)},indent=2))
