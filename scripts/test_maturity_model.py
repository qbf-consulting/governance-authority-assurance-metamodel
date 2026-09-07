#!/usr/bin/env python3
"""Regression tests for GAAM dual-axis maturity invariants."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def check(ok,msg):
    if not ok: errors.append(msg)
model=json.loads((ROOT/'governance/maturity-model.json').read_text())
classes={x['id']:x for x in json.loads((ROOT/'governance/v1-gate-classification.json').read_text())['gates']}
issues={x['id']:x for x in json.loads((ROOT/'governance/candidate-issues.json').read_text())['issues']}
state=json.loads((ROOT/'governance/candidate-readiness.json').read_text())
# Falsification 1: external absence cannot become a Stable veto.
for gid in ['independent-implementations','foundation-implementation','composed-profile-implementation','cross-implementation-interoperability']:
    check(classes[gid]['control']=='external',f'{gid}: expected external control')
    check(classes[gid]['blocksSpecificationStable'] is False,f'{gid}: external evidence incorrectly blocks Stable')
# Falsification 2: external absence cannot elevate evidence maturity.
if not state['evidence']['independentImplementationEvidenceSatisfied']:
    check(state['evidence']['level'] not in {'E2','E3','E4'},'missing independent implementation evidence elevated evidence maturity')
if not state['evidence']['crossImplementationEvidenceSatisfied']:
    check(state['evidence']['level'] not in {'E3','E4'},'missing interoperability evidence elevated E3/E4')
# Falsification 3: repository-controlled gates remain fail-closed.
for gid in ['requirement-testability','canonical-identifiers','candidate-issue-disposition']:
    check(classes[gid]['blocksSpecificationStable'] is True,f'{gid}: repository-controlled Stable gate was weakened')
# Falsification 4: open external candidate issues cannot masquerade as repository blockers.
for iid in ['GAAM-CR-001','GAAM-CR-002']:
    check(issues[iid]['status']=='open',f'{iid}: test assumes external evidence remains open')
    check(issues[iid]['blockingV1'] is False,f'{iid}: external evidence still encoded as v1 veto')
# Falsification 5: self/synthetic evidence cannot satisfy independence by policy.
check('Synthetic, self-assessed' in model['evidenceMaturity']['nonSubstitution'],'non-substitution rule missing')
# Falsification 6: external evidence remains a reassessment input.
check('MUST enter' in model['reassessmentRule'],'external falsification/reassessment rule missing')
# Falsification 7: known blocking findings are independently represented as Stable blockers.
known=state['specification'].get('knownBlockingFindings',[])
if known: check('known-material-findings' in state['specification']['blockingGates'],'known material findings do not block Stable')
if errors:
    print('Maturity model regression tests failed:')
    for e in errors: print('- '+e)
    sys.exit(1)
print('Maturity model regression tests passed: external evidence cannot veto Stable or inflate assurance claims')
