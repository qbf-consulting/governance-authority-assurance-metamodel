#!/usr/bin/env python3
from pathlib import Path
import json,re,csv,hashlib,sys,urllib.parse,yaml,subprocess
from jsonschema import Draft202012Validator, FormatChecker
ROOT=Path(__file__).resolve().parents[1]
REL=json.loads((ROOT/'release.json').read_text()); VERSION=REL['version']; results=[]
def add(cid,ok,detail,kind='structural'):
 results.append({'id':cid,'kind':kind,'status':'pass' if ok else 'fail','evidence':detail})
def load(p): return json.loads(p.read_text())
# Release coherence: active artifacts only
active=[]
for base in ['README.md','index.md','VERSION','release.json','specification','profiles','schemas','vocabularies','examples','docs','mappings','matrices','threat-model']:
 p=ROOT/base
 active += [p] if p.is_file() else list(p.rglob('*'))
stale=[]
for p in active:
 if p.is_file() and p.suffix in {'.md','.json','.csv','.txt'}:
  t=p.read_text(errors='ignore')
  if re.search(r'(?<![\d.])0\.5\.0(?![\d.])|v0\.5\.0',t) and 'migration-v0.5.0' not in str(p) and p.name not in {'migration-v0.5.0-to-v0.9.0.md','README.md'}: stale.append(str(p.relative_to(ROOT)))
add('PUB-001-version-source',(ROOT/'VERSION').read_text().strip()==VERSION,f'authoritative version={VERSION}','publication')
add('PUB-002-active-version-coherence',not stale,'no stale active v0.5.0 references' if not stale else ', '.join(stale),'publication')
spec=(ROOT/REL['normativeSpecification']).read_text()
add('PUB-003-specification-identity',f'**Version:** {VERSION}' in spec and '**Status:** Candidate Specification' in spec,'normative specification identifies candidate release','publication')
# Publication hygiene: repository source files, published landing pages and sidebar entries

def front_matter(path):
 text=path.read_text(errors='ignore')
 if not text.startswith('---\n'): return {},False
 end=text.find('\n---\n',4)
 if end<0: return {},False
 data={}
 for line in text[4:end].splitlines():
  if ':' in line:
   k,v=line.split(':',1); data[k.strip()]=v.strip().strip('"').strip("'")
 return data,True
cfg=(ROOT/'_config.yml').read_text()
example_dirs=sorted(d for d in (ROOT/'examples').iterdir() if d.is_dir())
excluded_readmes=[f'examples/{d.name}/README.md' for d in example_dirs]+['examples/README.md']
missing_exclusions=[x for x in excluded_readmes if f'  - {x}' not in cfg]
add('PUB-HYG-README-EXCLUDE',not missing_exclusions,'all implementation-pattern README files excluded from Jekyll publication' if not missing_exclusions else 'missing exclusions: '+', '.join(missing_exclusions),'publication')
landing_errors=[]; support_errors=[]
for d in example_dirs:
 idx=d/'index.md'; readme=d/'README.md'
 if not idx.exists(): landing_errors.append(f'{d.name}: index.md missing'); continue
 fm,valid=front_matter(idx)
 if not valid or fm.get('parent')!='Implementation Patterns' or fm.get('permalink')!=f'/examples/{d.name}/': landing_errors.append(f'{d.name}: invalid landing-page front matter')
 rfm,rvalid=front_matter(readme) if readme.exists() else ({},False)
 if not rvalid or rfm.get('published')!='false' or rfm.get('nav_exclude')!='true': landing_errors.append(f'{d.name}: README publication boundary missing')
 for md in d.glob('*.md'):
  if md.name in {'README.md','index.md'}: continue
  sfm,svalid=front_matter(md)
  if not svalid or sfm.get('nav_exclude')!='true': support_errors.append(str(md.relative_to(ROOT)))
add('PUB-HYG-LANDINGS',not landing_errors,f'{len(example_dirs)} canonical pattern landing pages use clean directory URLs' if not landing_errors else '; '.join(landing_errors),'publication')
add('PUB-HYG-SUPPORT-NAV',not support_errors,'all supporting pattern pages excluded from primary navigation' if not support_errors else ', '.join(support_errors),'publication')
cfm,cvalid=front_matter(ROOT/'CHANGELOG.md')
add('PUB-HYG-CHANGELOG',cvalid and cfm.get('title')=='Changelog' and cfm.get('permalink')=='/releases/changelog/','changelog begins with valid canonical front matter' if cvalid else 'changelog front matter malformed','publication')
# Information architecture: grouped documentation, promoted workflow, and appendices
ia_groups={
 'Orientation':['docs/guided-learning.md','docs/documentation-architecture.md'],
 'Concepts and Design':['docs/architecture-overview.md','diagrams/architecture-diagrams.md','docs/design-principles.md','docs/design-rationale.md'],
 'Implementation Guidance':['docs/implementation-guide.md','docs/lifecycle-model.md','docs/control-document-schedule.md','docs/migration-v0.5.0-to-v0.9.0.md','docs/reviewer-guide.md'],
 'Assurance and Governance Tracking':['docs/conformance-guide.md','docs/candidate-readiness.md','docs/open-questions.md','docs/candidate-stability-policy.md','governance/README.md'],
}
ia_errors=[]
for order,(group,pages) in enumerate(ia_groups.items(),1):
 group_file=ROOT/'docs'/({'Orientation':'orientation.md','Concepts and Design':'concepts-and-design.md','Implementation Guidance':'implementation-guidance.md','Assurance and Governance Tracking':'assurance-and-governance-tracking.md'}[group])
 gfm,gvalid=front_matter(group_file) if group_file.exists() else ({},False)
 if not gvalid or gfm.get('parent')!='Documentation' or gfm.get('has_children')!='true' or gfm.get('nav_order')!=str(order): ia_errors.append(f'{group}: invalid group index')
 for page in pages:
  fm,valid=front_matter(ROOT/page)
  if not valid or fm.get('parent')!=group or fm.get('grand_parent')!='Documentation': ia_errors.append(f'{page}: invalid Documentation grouping')
add('PUB-IA-DOCUMENTATION',not ia_errors,'Documentation is grouped into four validated reader routes' if not ia_errors else '; '.join(ia_errors),'publication')
appendix_expected={'docs/glossary.md':'1','vocabularies/index.md':'2','matrices/index.md':'3','mappings/index.md':'4','docs/faq.md':'5','docs/style-guide.md':'6','docs/github-pages-publication.md':'7'}
appendix_errors=[]
afm,avalid=front_matter(ROOT/'appendices/index.md') if (ROOT/'appendices/index.md').exists() else ({},False)
if not avalid or afm.get('title')!='Appendices' or afm.get('has_children')!='true' or afm.get('nav_order')!='11': appendix_errors.append('appendices/index.md invalid')
for page,order in appendix_expected.items():
 fm,valid=front_matter(ROOT/page)
 if not valid or fm.get('parent')!='Appendices' or fm.get('nav_order')!=order: appendix_errors.append(f'{page}: invalid Appendix placement')
for folder,parent in [('matrices','Matrices'),('mappings','Mappings and Source Crosswalks')]:
 for md in (ROOT/folder).glob('*.md'):
  if md.name=='index.md': continue
  fm,valid=front_matter(md)
  if not valid or fm.get('parent')!=parent or fm.get('grand_parent')!='Appendices': appendix_errors.append(f'{md.relative_to(ROOT)}: invalid nested Appendix placement')
add('PUB-IA-APPENDICES',not appendix_errors,'Appendices consolidates reference material without changing URLs' if not appendix_errors else '; '.join(appendix_errors),'publication')
ifm,ivalid=front_matter(ROOT/'implementation-reports/README.md')
implementation_report_errors=[]
if not ivalid or ifm.get('parent') or ifm.get('grand_parent') or ifm.get('nav_order')!='5' or ifm.get('has_children')!='true': implementation_report_errors.append('implementation-reports/README.md not promoted cleanly')
for md in (ROOT/'implementation-reports').glob('*.md'):
 if md.name=='README.md': continue
 fm,valid=front_matter(md)
 if not valid or fm.get('parent')!='Implementation Reports': implementation_report_errors.append(f'{md.relative_to(ROOT)}: invalid report parent')
add('PUB-IA-REPORTS',not implementation_report_errors,'Implementation Reports is a top-level workflow with intact children' if not implementation_report_errors else '; '.join(implementation_report_errors),'publication')
top_orders={'docs/index.md':'3','profiles/index.md':'4','implementation-reports/README.md':'5','schemas/index.md':'6','threat-model/README.md':'7','examples/index.md':'8','conformance/index.md':'9','decisions/index.md':'10','appendices/index.md':'11','releases/index.md':'12','GOVERNANCE.md':'13'}
order_errors=[]
for page,order in top_orders.items():
 fm,valid=front_matter(ROOT/page)
 if not valid or fm.get('nav_order')!=order: order_errors.append(f'{page}: expected nav_order {order}')
add('PUB-IA-TOP-ORDER',not order_errors,'top-level workflow order is deterministic' if not order_errors else '; '.join(order_errors),'publication')
# Future-evolution programme: informative research boundary and controlled register
future_root=ROOT/'docs/future-evolution'
future_required={
 'index.md','expansion-principles.md','concept-classification.md','normative-boundary.md','delivery-roadmap.md','concepts/index.md',
 'concepts/standing-qualification-and-recognition.md','concepts/framework-composition.md','concepts/institutional-succession.md',
 'concepts/authority-scope-composition.md','concepts/obligation-lifecycle.md','concepts/temporal-governance.md',
 'concepts/evidence-predicates.md','concepts/uncertainty-and-confidence.md','concepts/organisational-authority-chains.md',
 'concepts/agent-and-composite-action-governance.md','concepts/assurance-composition-and-dependency.md',
 'concepts/continuity-caching-and-revocation.md','concepts/privacy-inference-and-observability.md',
 'concepts/affected-parties-and-remedy.md','concepts/jurisdiction-market-and-systemic-governance.md'
}
future_missing=sorted(x for x in future_required if not (future_root/x).exists())
future_errors=[]
ffm,fvalid=front_matter(future_root/'index.md') if (future_root/'index.md').exists() else ({},False)
if not fvalid or ffm.get('parent')!='Documentation' or ffm.get('nav_order')!='5' or ffm.get('has_children')!='true' or ffm.get('normative_status')!='Informative': future_errors.append('future-evolution index has invalid publication boundary')
for md in sorted((future_root/'concepts').glob('*.md')) if (future_root/'concepts').exists() else []:
 if md.name=='index.md': continue
 fm,valid=front_matter(md)
 if not valid or fm.get('nav_exclude')!='true' or fm.get('normative_status')!='Informative': future_errors.append(f'{md.relative_to(ROOT)}: candidate concept publication boundary invalid')
add('PUB-FUTURE-EVOLUTION',not future_missing and not future_errors,'future-evolution programme published as informative research' if not future_missing and not future_errors else '; '.join(future_missing+future_errors),'publication')
future_register_path=ROOT/'governance/future-enhancement-register.json'
future_register_errors=[]
valid_future_gaps={'already-covered','guidance-gap','pattern-gap','schema-gap','vocabulary-gap','profile-gap','normative-semantics-gap','test-gap','evidence-gap'}
valid_future_layers={'informative-concept','draft-profile','experimental-schema','experimental-fields','experimental-vocabulary','implementation-pattern','implementation-guidance','behavioural-test','core-candidate'}
valid_future_statuses={'candidate','prototype-available','under-evaluation','closed'}
valid_promotion={'not-assessed','retain-as-guidance','retain-as-pattern','retain-as-experimental','promote-to-profile','promote-to-core','promote-to-normative-schema','defer','reject'}
try:
 fr=load(future_register_path)
 if fr.get('gaamVersion')!=VERSION or fr.get('normativeStatus')!='informative' or fr.get('status')!='active-research': future_register_errors.append('register identity or normative boundary invalid')
 entries=fr.get('entries',[]); feids=[x.get('id') for x in entries]
 if len(entries)!=25 or len(feids)!=len(set(feids)): future_register_errors.append('register must contain 25 unique candidate enhancements')
 for e in entries:
  if e.get('status') not in valid_future_statuses: future_register_errors.append(f"{e.get('id')}: invalid status")
  if e.get('gapClassification') not in valid_future_gaps: future_register_errors.append(f"{e.get('id')}: invalid gap classification")
  layers=set(e.get('candidateDeliveryLayer',[]))
  if not layers or not layers<=valid_future_layers: future_register_errors.append(f"{e.get('id')}: invalid delivery layer")
  if e.get('promotionStatus') not in valid_promotion: future_register_errors.append(f"{e.get('id')}: invalid promotion status")
  if not e.get('implementationEvidenceRequired'): future_register_errors.append(f"{e.get('id')}: evidence threshold missing")
  baddeps=[x for x in e.get('dependencies',[]) if x not in feids]
  if baddeps: future_register_errors.append(f"{e.get('id')}: unknown dependencies {baddeps}")
except Exception as e: future_register_errors.append(str(e))
add('GOV-FUTURE-REGISTER',not future_register_errors,'25 future enhancements classified with controlled delivery and promotion states' if not future_register_errors else '; '.join(future_register_errors[:10]),'governance')
# Draft profiles and experimental artefacts must remain outside v0.9.0 conformance
research_errors=[]
draft_root=ROOT/'profiles-draft'; exp_root=ROOT/'experimental'
expected_drafts={'governed-ecosystem-operations','organisational-authority','institutional-continuity','privacy-and-inference-governance','cross-jurisdiction-governance','market-and-infrastructure-governance','advanced-agent-orchestration'}
actual_drafts={d.name for d in draft_root.iterdir() if d.is_dir()} if draft_root.exists() else set()
if actual_drafts!=expected_drafts: research_errors.append(f'draft profile set differs: {sorted(actual_drafts)}')
for slug in sorted(expected_drafts):
 p=draft_root/slug/'profile-candidate.json'
 if not p.exists(): research_errors.append(f'{slug}: profile-candidate.json missing'); continue
 try:
  o=load(p)
  if o.get('gaamVersion')!=VERSION or o.get('status')!='research-draft' or o.get('normativeStatus')!='informative-non-conformant' or o.get('conformanceClaimPermitted') is not False: research_errors.append(f'{slug}: invalid research boundary')
 except Exception as e: research_errors.append(f'{slug}: {e}')
add('GOV-FUTURE-DRAFT-PROFILES',not research_errors,f'{len(expected_drafts)} draft profiles are explicitly non-conformant' if not research_errors else '; '.join(research_errors[:10]),'governance')
experimental_errors=[]
try:
 ec=load(exp_root/'catalog.json'); entries=ec.get('schemas',[])
 if ec.get('gaamVersion')!=VERSION or ec.get('normativeStatus')!='non-normative': experimental_errors.append('catalog boundary invalid')
 for e in entries:
  sp=exp_root/e['schema']; xp=exp_root/e['example']
  if not sp.exists() or not xp.exists(): experimental_errors.append(f"{e.get('id')}: missing schema/example"); continue
  s=load(sp); x=load(xp)
  try: Draft202012Validator.check_schema(s)
  except Exception as err: experimental_errors.append(f"{e.get('id')}: invalid schema {err}"); continue
  if '/experimental/0.9.0-research/' not in s.get('$id',''): experimental_errors.append(f"{e.get('id')}: identifier outside experimental namespace")
  if x.get('status')!='experimental' or x.get('normativeStatus')!='non-normative': experimental_errors.append(f"{e.get('id')}: example boundary invalid")
  errs=list(Draft202012Validator(s,format_checker=FormatChecker()).iter_errors(x))
  if errs: experimental_errors.append(f"{e.get('id')}: example invalid {errs[0].message}")
 canonical_ids={load(p).get('$id') for p in (ROOT/'schemas').glob('*.schema.json')}
 exp_ids={load(exp_root/e['schema']).get('$id') for e in entries}
 if canonical_ids & exp_ids: experimental_errors.append('experimental and canonical schema identifiers overlap')
except Exception as e: experimental_errors.append(str(e))
add('SCH-EXPERIMENTAL',not experimental_errors,f'{len(entries) if not experimental_errors else 0} experimental schemas and examples validated outside the canonical surface' if not experimental_errors else '; '.join(experimental_errors[:10]),'schema')
# Canonical directories must not import experimental identifiers
leaks=[]
for base_dir in ['specification','schemas','profiles','vocabularies','conformance','threat-model']:
 for p in (ROOT/base_dir).rglob('*'):
  if p.is_file() and 'experimental/0.9.0-research' in p.read_text(errors='ignore'): leaks.append(str(p.relative_to(ROOT)))
add('GOV-FUTURE-NO-NORMATIVE-IMPORT',not leaks,'canonical v0.9.0 artifacts do not import experimental identifiers' if not leaks else ', '.join(leaks),'governance')

# Future evolution must not be represented as current conformance material
future_boundary_errors=[]
for pth in [ROOT/'docs/future-evolution', ROOT/'governance/future-enhancement-register.json']:
 if not pth.exists(): future_boundary_errors.append(str(pth.relative_to(ROOT))+' missing')
for pth in (future_root.rglob('*') if future_root.exists() else []):
 if pth.is_file() and pth.suffix in {'.md','.json'}:
  txt=pth.read_text(errors='ignore')
  if 'normative_status: Normative' in txt or 'normativeStatus": "normative"' in txt: future_boundary_errors.append(f'{pth.relative_to(ROOT)} claims normative status')
add('GOV-FUTURE-BOUNDARY',not future_boundary_errors,'future-evolution assets cannot be mistaken for GAAM v0.9.0 conformance material' if not future_boundary_errors else '; '.join(future_boundary_errors),'governance')
# Future-evolution readiness assessment
readiness_root=ROOT/'governance/reviews/evidence/future-evolution'
readiness_errors=[]
required_readiness={'README.md','capability-matrix.csv','capability-matrix.md','implementation-findings.json','interoperability-findings.json','normative-impact-analysis.md','promotion-candidates.json','reviewer-attestation.json'}
missing=sorted(x for x in required_readiness if not (readiness_root/x).exists())
if missing: readiness_errors.append('missing: '+', '.join(missing))
try:
 rr=load(ROOT/'governance/future-enhancement-register.json')
 if any(e.get('promotionStatus')=='not-assessed' for e in rr.get('entries',[])): readiness_errors.append('unassessed enhancement remains')
 matrix=list(csv.DictReader((readiness_root/'capability-matrix.csv').open()))
 if len(matrix)!=25 or {r.get('enhancement_id') for r in matrix}!={e.get('id') for e in rr.get('entries',[])}: readiness_errors.append('capability matrix does not cover register')
 pf=load(readiness_root/'promotion-candidates.json')
 if pf.get('corePromotions') or pf.get('normativeSchemaPromotions'): readiness_errors.append('assessment must not directly promote core or canonical schemas')
 att=load(readiness_root/'reviewer-attestation.json')
 if att.get('independence')!='not-independent': readiness_errors.append('maintainer assessment must not claim independence')
 for name in ['implementation-findings.json','interoperability-findings.json']:
  obj=load(readiness_root/name)
  if len(obj.get('findings',[]))!=25 or obj.get('normativeStatus')!='informative': readiness_errors.append(name+' boundary or coverage invalid')
except Exception as e: readiness_errors.append(str(e))
add('GOV-FUTURE-READINESS',not readiness_errors,'25 candidates assessed with explicit non-normative dispositions and independent-review boundary' if not readiness_errors else '; '.join(readiness_errors[:10]),'governance')
# Requirements
ids=re.findall(r'\*\*(GAAM-[A-Z]+-\d{3}):\*\*',spec)
idx=list(csv.DictReader((ROOT/'matrices/normative-requirements-index.csv').open())); idxids=[r['requirement_id'] for r in idx]
add('REQ-001-unique',len(ids)==len(set(ids)),f'{len(ids)} identifiers','normative')
add('REQ-002-index-exact',ids==idxids,f'{len(idxids)} indexed requirements','normative')
add('REQ-003-normative-language',all(any(k in r['requirement'] for k in ['MUST','SHALL','SHOULD','MAY']) for r in idx),f'{len(idx)} indexed statements classified','normative')
# Informative ecosystem readiness crosswalks
crosswalk_errors=[]
crosswalk_files=sorted((ROOT/'mappings').glob('*-gaam-crosswalk.json'))
try:
 crosswalk_schema=load(ROOT/'mappings/ecosystem-crosswalk.schema.json')
 Draft202012Validator.check_schema(crosswalk_schema)
 validator=Draft202012Validator(crosswalk_schema,format_checker=FormatChecker())
 seen_finding_ids=set()
 for p in crosswalk_files:
  obj=load(p)
  errs=list(validator.iter_errors(obj))
  if errs: crosswalk_errors.append(f'{p.name}: {errs[0].message}'); continue
  for f in obj.get('findings',[]):
   if f['id'] in seen_finding_ids: crosswalk_errors.append(f"duplicate finding id {f['id']}")
   seen_finding_ids.add(f['id'])
   missing_req=[x for x in f['gaamRequirements'] if x not in set(ids)]
   if missing_req: crosswalk_errors.append(f"{f['id']}: unknown GAAM requirements {missing_req}")
except Exception as e: crosswalk_errors.append(str(e))
add('MAP-ECOSYSTEM-CROSSWALKS',not crosswalk_errors,f'{len(crosswalk_files)} informative ecosystem crosswalks validated against mapping schema and normative requirement identifiers' if not crosswalk_errors else '; '.join(crosswalk_errors[:10]),'mapping')
# Schemas
schemas={p.stem.replace('.schema',''):load(p) for p in (ROOT/'schemas').glob('*.schema.json')}
base=REL['schemaBase']; ids_seen=[]
for name,obj in schemas.items():
 try: Draft202012Validator.check_schema(obj); ok=True; detail='valid Draft 2020-12 schema'
 except Exception as e: ok=False; detail=str(e)
 add('SCH-'+name,ok,detail,'schema'); ids_seen.append(obj.get('$id'))
add('SCH-IDS',len(ids_seen)==len(set(ids_seen)) and all(x.startswith(base) for x in ids_seen),f'{len(ids_seen)} unique canonical identifiers','schema')
cat=load(ROOT/'schemas/catalog.json'); add('SCH-CATALOG',len(cat['schemas'])==len(schemas) and {x['id'] for x in cat['schemas']}==set(ids_seen),'catalog covers all schemas','schema')
# Vocabularies
for p in sorted((ROOT/'vocabularies').glob('*.json')):
 o=load(p); vals=o.get('values',o.get('terms',[])); normalized=[json.dumps(x,sort_keys=True) for x in vals]
 add('VOC-'+p.stem,o.get('version')==VERSION and o.get('status')=='candidate' and o.get('extensionPolicy') in {'closed','controlled-extensible','profile-extensible','implementation-defined'} and len(normalized)==len(set(normalized)),f'{len(vals)} governed values','vocabulary')
# Profiles
pids=set(ids); manifests={}
for p in sorted((ROOT/'profiles/manifests').glob('*.json')):
 o=load(p); manifests[o['id']]=o
 errs=list(Draft202012Validator(schemas['profile-manifest'],format_checker=FormatChecker()).iter_errors(o)); missing=[x for x in o['requirements'] if x not in pids]
 depok=(p.stem=='foundation' and not o['dependencies']) or (p.stem!='foundation' and f'gaam:profile:foundation:{VERSION}' in o['dependencies'])
 doc=ROOT/'profiles'/(p.stem+'-profile.md'); doceq=doc.exists() and f'**Version:** {VERSION}' in doc.read_text()
 add('PRO-'+p.stem,not errs and not missing and depok and doceq,f'{len(o["requirements"])} requirements; dependencies={depok}; document={doceq}','profile')
all_profile_ids=set(manifests)
missingdeps=[d for o in manifests.values() for d in o['dependencies'] if d not in all_profile_ids]
add('PRO-DEPENDENCIES',not missingdeps,'all profile dependencies resolve' if not missingdeps else str(missingdeps),'profile')
# Pattern architecture, fixtures and claims
pattern_schema_path=ROOT/'examples/pattern-manifest.schema.json'
pattern_schema=load(pattern_schema_path) if pattern_schema_path.exists() else None
pattern_catalog_path=ROOT/'examples/catalog.json'
pattern_catalog=load(pattern_catalog_path) if pattern_catalog_path.exists() else {'patterns':[]}
catalog_paths={x.get('path') for x in pattern_catalog.get('patterns',[])}
pattern_ids=[]
fixture_type_map={'authority':'authority','delegation':'delegation','decision-receipt':'decision-receipt','governance-event':'governance-event','remedy':'remedy'}
for d in sorted((ROOT/'examples').iterdir()):
 if not d.is_dir(): continue
 required={'README.md','pattern.json','conformance-claim.json'}
 missing=sorted(x for x in required if not (d/x).exists())
 add('PAT-'+d.name+'-CONTRACT',not missing,'required files present' if not missing else 'missing '+', '.join(missing),'pattern')
 manifest=None
 if (d/'pattern.json').exists() and pattern_schema:
  try:
   manifest=load(d/'pattern.json'); errs=list(Draft202012Validator(pattern_schema).iter_errors(manifest))
   add('PAT-'+d.name+'-MANIFEST',not errs,'manifest conforms' if not errs else str(errs[0]),'pattern')
  except Exception as e: add('PAT-'+d.name+'-MANIFEST',False,str(e),'pattern')
 elif (d/'pattern.json').exists(): add('PAT-'+d.name+'-MANIFEST',False,'pattern manifest schema missing','pattern')
 else: add('PAT-'+d.name+'-MANIFEST',False,'pattern manifest missing','pattern')
 if manifest:
  pattern_ids.append(manifest.get('id'))
  bad_profiles=[x for x in manifest.get('profiles',[]) if x not in all_profile_ids]
  bad_reqs=[x for x in manifest.get('requirements',[]) if x not in pids]
  refs=manifest.get('artifacts',[])+manifest.get('supportingExamples',[])
  missing_refs=[x for x in refs if not (d/x).exists()]
  missing_beh=[x for x in manifest.get('behaviouralVectors',[]) if not (ROOT/'tests/behavioural'/f'{x}.json').exists()]
  add('PAT-'+d.name+'-REFERENCES',not bad_profiles and not bad_reqs and not missing_refs and not missing_beh,'profile, requirement, artifact and behavioural references resolve' if not (bad_profiles or bad_reqs or missing_refs or missing_beh) else f'profiles={bad_profiles}; requirements={bad_reqs}; artifacts={missing_refs}; behavioural={missing_beh}','pattern')
  scenarios=bool(manifest.get('positiveScenarios')) and bool(manifest.get('negativeScenarios'))
  maturity=manifest.get('maturity'); maturity_ok=maturity!='assurance-ready' or (scenarios and bool(manifest.get('requirements')) and bool(manifest.get('behaviouralVectors')) and bool(manifest.get('limitations')))
  add('PAT-'+d.name+'-MATURITY',maturity_ok,f'{maturity} claim supported' if maturity_ok else f'{maturity} claim lacks required evidence','pattern')
  add('PAT-'+d.name+'-CATALOG',d.name in catalog_paths,'catalogue entry present' if d.name in catalog_paths else 'catalogue entry missing','pattern')
  declared={x.get('path'):x for x in manifest.get('schemaFixtures',[])}
 else: declared={}
 for p in sorted(list(d.glob('*.valid.json'))+list(d.glob('*.invalid.json'))):
  expected=p.name.endswith('.valid.json')
  try: o=load(p); typ=o.get('type'); key=fixture_type_map.get(typ); errs=list(Draft202012Validator(schemas[key],format_checker=FormatChecker()).iter_errors(o)) if key else [Exception('unknown type')]
  except Exception as e: typ=None; key=None; errs=[e]
  ok=(not errs) if expected else bool(errs)
  decl=declared.get(p.name); declaration_ok=bool(decl) and decl.get('type')==typ and decl.get('expectedValid')==expected
  add('FIX-'+d.name+'-'+p.stem,ok and declaration_ok,('accepted' if expected else 'rejected')+' as expected; manifest declaration matched' if ok and declaration_ok else f'validation={ok}; declaration={declaration_ok}; error={errs[0] if errs else "none"}','fixture')
 if (d/'conformance-claim.json').exists():
  try:
   claim=load(d/'conformance-claim.json'); errs=list(Draft202012Validator(schemas['conformance-claim'],format_checker=FormatChecker()).iter_errors(claim)); evid=bool(claim.get('evidence')); independent=(claim.get('level')!='L4' or claim.get('assessmentIndependence')=='independent')
   add('CLM-'+d.name,not errs and evid and independent and bool(claim.get('limitations')),'schema, evidence, limitations and independence rules satisfied' if not errs else str(errs[0]),'conformance')
  except Exception as e: add('CLM-'+d.name,False,str(e),'conformance')
 else: add('CLM-'+d.name,False,'conformance claim missing','conformance')
add('PAT-IDS',len(pattern_ids)==len(set(pattern_ids)),f'{len(pattern_ids)} unique pattern identifiers','pattern')
add('PAT-CATALOG-COVERAGE',catalog_paths=={d.name for d in (ROOT/'examples').iterdir() if d.is_dir()},f'{len(catalog_paths)} pattern directories catalogued' if catalog_paths=={d.name for d in (ROOT/'examples').iterdir() if d.is_dir()} else 'catalogue and directory set differ','pattern')
# Future-evolution patterns must remain research-only and linked to the enhancement register
future_pattern_errors=[]
expected_future_patterns={'agent-state-change-control', 'assurance-composition', 'downstream-remedy-propagation', 'cross-jurisdiction-policy-conflict', 'degraded-trust-service-operation', 'inferred-evidence-governance', 'post-decision-obligation-lifecycle', 'institutional-authority-succession', 'revocation-propagation-boundaries'}
register=load(ROOT/'governance/future-enhancement-register.json')
register_assets={a for e in register.get('entries',[]) for a in e.get('researchAssets',[])}
for slug in sorted(expected_future_patterns):
 d=ROOT/'examples'/slug
 try:
  m=load(d/'pattern.json')
  if m.get('status')!='draft' or m.get('maturity')!='behavioural' or not m.get('id','').endswith(':0.9.0-research'): future_pattern_errors.append(slug+': invalid research identity')
  if 'No independent implementation or interoperability evidence is asserted.' not in m.get('limitations',[]): future_pattern_errors.append(slug+': limitation missing')
  if f'examples/{slug}/' not in register_assets: future_pattern_errors.append(slug+': enhancement register link missing')
 except Exception as err: future_pattern_errors.append(slug+': '+str(err))
add('PAT-FUTURE-EVOLUTION',not future_pattern_errors,f'{len(expected_future_patterns)} future-evolution patterns are behavioural, traceable and non-normative' if not future_pattern_errors else '; '.join(future_pattern_errors),'pattern')

# Behavioural vectors
def behaviour(o):
 x=o['input']; i=o['id']
 if i.startswith('authority-'):
  valid=x.get('status')=='active' and x.get('withinScope') and x.get('withinTime') and x.get('sourceValid')
 elif i.startswith('delegation-'):
  valid=(x.get('delegationPermitted') and set(x.get('childEffects',[]))<=set(x.get('parentEffects',[]))
         and x.get('depth',0)<=x.get('maxDepth',0) and x.get('parentActive',True)
         and x.get('childWithinParentTime',True))
 elif i.startswith('decision-'):
  valid=(all([x.get('authorityId'),x.get('policyId'),x.get('evidenceIds'),x.get('assuranceIds'),x.get('accountableParty')])
         and x.get('evidenceFresh',True) and x.get('policyCurrent',True))
 elif i.startswith('assurance-'):
  ranks={'self':1,'reviewed':2,'independent':3}
  valid=(x.get('evidencePresent') and x.get('withinValidity')
         and ranks.get(x.get('independence'),0)>=ranks.get(x.get('requiredIndependence'),0))
 elif i.startswith('high-impact-'):
  valid=((not x.get('highImpact')) or all([x.get('appealPath'),x.get('remedyPath'),x.get('affectedPartyAnalysis')]))
  valid=valid and x.get('noticeProvided',True) and x.get('reviewIndependent',True)
 elif i.startswith('lifecycle-event-order-'):
  seq=[e.get('sequence') for e in x.get('events',[])]
  valid=bool(seq) and seq==sorted(seq) and len(seq)==len(set(seq)) and x['events'][0].get('type')=='issued'
 elif i.startswith('runtime-'):
  valid=(x.get('stateFresh') and x.get('authorityStatusKnown')) or (x.get('failurePolicy')=='fail-closed' and not x.get('effectAdmitted'))
 elif i.startswith('profile-composition-'):
  selected=set(x.get('selectedProfiles',[])); deps=x.get('dependencies',{})
  valid=all(set(deps.get(profile,[]))<=selected for profile in selected)
 elif any(i.startswith(prefix) for prefix in ('future-','institutional-succession-','jurisdiction-conflict-','agent-state-change-','obligation-fulfilled-','remedy-propagation-','inferred-evidence-','degraded-operation-','assurance-composition-','revocation-propagation-')):
  valid=all([x.get('researchPattern'),x.get('currentAuthorityValid'),x.get('evidenceTraceable'),x.get('candidateSemanticsExplicit'),x.get('failSafe'),x.get('reviewPath')])
 else: valid=False
 return bool(valid)
for p in sorted((ROOT/'tests/behavioural').glob('*.json')):
 o=load(p); actual=behaviour(o); add('BEH-'+o['id'],actual==o['expectedValid'],f'expected={o["expectedValid"]}; actual={actual}','behavioural')
# Requirement-level assurance traceability
trace=list(csv.DictReader((ROOT/'matrices/requirement-assurance-traceability.csv').open()))
trace_ids=[r['requirement_id'] for r in trace]
valid_dispositions={'behavioural-testable','structural-testable','observable','reviewable','procedural','mixed'}
evidence_catalogue=load(ROOT/'implementation-reports/evidence-catalogue.json')
evidence_ids={x['id'] for x in evidence_catalogue['entries']}
behaviour_ids={p.stem for p in (ROOT/'tests/behavioural').glob('*.json')}
known_test_ids=behaviour_ids|{'claim-level-evidence','package-integrity'}
trace_errors=[]
if trace_ids!=idxids: trace_errors.append('traceability rows do not exactly match normative requirement index order')
for row in trace:
 if row['testability'] not in valid_dispositions: trace_errors.append(f"{row['requirement_id']}: invalid testability disposition")
 refs={x for x in row['evidence_catalogue_ids'].split(';') if x}
 if not refs or not refs<=evidence_ids: trace_errors.append(f"{row['requirement_id']}: unknown or missing evidence reference")
 tests={x for x in row['test_ids'].split(';') if x}
 if not tests<=known_test_ids: trace_errors.append(f"{row['requirement_id']}: unknown test identifiers {sorted(tests-known_test_ids)}")
add('TRC-REQUIREMENTS',not trace_errors,f'{len(trace)} requirements have testability and evidence dispositions' if not trace_errors else '; '.join(trace_errors[:10]),'traceability')
referenced_tests={x for row in trace for x in row['test_ids'].split(';') if x}
orphan_behaviour=sorted(behaviour_ids-referenced_tests)
add('TRC-TEST-ORPHANS',not orphan_behaviour,f'{len(behaviour_ids)} behavioural tests referenced by requirement traceability' if not orphan_behaviour else ', '.join(orphan_behaviour),'traceability')

# Threat traceability
tr=load(ROOT/'threat-model/threat-register.json'); test_ids={r['id'].replace('BEH-','') for r in results if r['kind']=='behavioural'}|{'claim-level-evidence','package-integrity'}
unmapped=[t['id'] for t in tr['threats'] if not t.get('requirements') or not t.get('tests') or any(x not in test_ids for x in t['tests'])]
add('THR-TRACE',not unmapped,f'{len(tr["threats"])} threats mapped to requirements and tests' if not unmapped else str(unmapped),'threat')
# Publication source contract
heading_errors=[]
for p in ROOT.rglob('*.md'):
 if any(part in {'.git', 'packages', 'node_modules', '_site', 'vendor'} for part in p.parts): continue
 text=p.read_text(errors='ignore')
 match=re.match(r'^---\n(.*?)\n---\n(.*)$',text,re.S)
 if not match: continue
 layout_match=re.search(r'^layout:\s*(\S+)\s*$',match.group(1),re.M)
 if layout_match and layout_match.group(1) not in ('page', 'default'): continue
 title_match=re.search(r'^title:\s*["\']?(.*?)["\']?\s*$',match.group(1),re.M)
 body=match.group(2)
 h1s=re.findall(r'^#\s+(.+)$',body,re.M)
 if len(h1s) != 1:
  heading_errors.append(f'{p.relative_to(ROOT)} contains {len(h1s)} body H1 headings; expected exactly one')
 elif title_match and h1s[0].strip() != title_match.group(1).strip():
  heading_errors.append(f'{p.relative_to(ROOT)} H1 does not match front-matter title')
add('DOC-PAGE-TITLE-CONTRACT',not heading_errors,'all rendered Markdown pages declare exactly one H1 matching front matter' if not heading_errors else '; '.join(heading_errors[:10]),'documentation')
# CTWG glossary alignment contract
glossary_text=(ROOT/'docs/glossary.md').read_text()
glossary_terms=re.findall(r'^\*\*(.+?)\*\*\s+—\s+.+$',glossary_text,re.M)
alignment=load(ROOT/'mappings/ctwg-v1.4.1-glossary-alignment.json')
aligned_terms=[x.get('gaamTerm') for x in alignment.get('terms',[])]
valid_statuses={'adopted','extended','local'}
alignment_errors=[]
if len(aligned_terms)!=len(set(aligned_terms)): alignment_errors.append('duplicate GAAM terms in alignment register')
missing=sorted(set(glossary_terms)-set(aligned_terms)); extra=sorted(set(aligned_terms)-set(glossary_terms))
if missing: alignment_errors.append('missing terms: '+', '.join(missing))
if extra: alignment_errors.append('unknown terms: '+', '.join(extra))
invalid=[x.get('gaamTerm') for x in alignment.get('terms',[]) if x.get('status') not in valid_statuses]
if invalid: alignment_errors.append('invalid statuses: '+', '.join(invalid))
add('DOC-CTWG-GLOSSARY-ALIGNMENT',not alignment_errors,f'{len(glossary_terms)} glossary terms covered by CTWG alignment register' if not alignment_errors else '; '.join(alignment_errors),'documentation')
# Local links
bad=[]
for p in ROOT.rglob('*.md'):
 if any(part in {'.git', 'packages', 'node_modules', '_site', 'vendor'} for part in p.parts): continue
 for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',p.read_text(errors='ignore')):
  if target.startswith(('http:','https:','mailto:','#')): continue
  clean=urllib.parse.unquote(target.split('#')[0]);
  if clean and not (p.parent/clean).resolve().exists(): bad.append(f'{p.relative_to(ROOT)} -> {target}')
add('DOC-LOCAL-LINKS',not bad,'all local links resolve' if not bad else '; '.join(bad[:10]),'documentation')
add('DOC-TSMM-CANONICAL','https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model' in (ROOT/'mappings/tsmm-v0.22.0-adoption-crosswalk.md').read_text(),'canonical TSMM repository link present','provenance')
add('CI-WORKFLOW',(ROOT/'.github/workflows/validate.yml').exists(),'validation workflow present','automation')
# Candidate governance and v1 readiness controls
# Repository-local status is authoritative for member-owned operational declarations.
status_errors=[]
try:
 project_status=yaml.safe_load((ROOT/'PROJECT-STATUS.yaml').read_text())
 allowed_status={
  'maturity':{'exploratory','working-draft','implementation-draft','candidate','pilot-ready','stable','maintenance','historical'},
  'lifecycle':{'active','maintenance','superseded','archived'},
  'operational_status':{'active-development','active-validation','pilot-use','stable-maintenance','upstream-tracking','dormant','superseded'},
  'specification_status':{'not-applicable','working-draft','community-draft','candidate-specification','stable-specification'},
 }
 if project_status.get('schema_version')!='1.0': status_errors.append('schema_version must be 1.0')
 pr=project_status.get('project',{})
 if pr.get('name')!='governance-authority-assurance-metamodel': status_errors.append('project name mismatch')
 for field,values in allowed_status.items():
  if pr.get(field) not in values: status_errors.append(f'{field}: invalid value {pr.get(field)}')
 if pr.get('maturity')!='candidate' or pr.get('operational_status')!='active-validation' or pr.get('specification_status')!='candidate-specification': status_errors.append('candidate declaration does not match release state')
 if not pr.get('intended_use') or not pr.get('not_asserted'): status_errors.append('intended_use and not_asserted must be non-empty')
 auth=project_status.get('authority',{})
 if not auth.get('normative_scope') or not auth.get('delegation') or not auth.get('revocation_or_supersession'): status_errors.append('authority contract incomplete')
 evidence=project_status.get('evidence',{})
 if not evidence.get('validation_commands') or not evidence.get('known_limitations'): status_errors.append('evidence contract incomplete')
 for out_path in evidence.get('evidence_outputs',[]):
  # Generated validation output may not exist until this run completes; all other declared outputs must exist.
  if out_path!='validation/validation-report.json' and not (ROOT/out_path).exists(): status_errors.append(f'missing declared evidence output {out_path}')
except Exception as e: status_errors.append(str(e))
add('GOV-PROJECT-STATUS',not status_errors,'repository-local candidate status, authority and evidence contract valid' if not status_errors else '; '.join(status_errors),'governance')

# The baseline is content-addressed. A Git commit may be absent when the reviewed input is an archive.
baseline_errors=[]
try:
 baseline=load(ROOT/'governance/reviews/review-baseline.json')
 if baseline.get('gaamVersion')!=VERSION or baseline.get('status')!='frozen': baseline_errors.append('version/status mismatch')
 ns=baseline.get('normativeSurface',{}); surface_paths=ns.get('paths',[])
 if surface_paths!=['specification','schemas','profiles','vocabularies','conformance','threat-model']: baseline_errors.append('normative surface path set mismatch')
 digest_lines=[]; count=0
 for base_dir in surface_paths:
  for fp in sorted((ROOT/base_dir).rglob('*')):
   if fp.is_file():
    count+=1; digest_lines.append(f'{fp.relative_to(ROOT)} {hashlib.sha256(fp.read_bytes()).hexdigest()}')
 current_digest=hashlib.sha256(('\n'.join(digest_lines)).encode()).hexdigest()
 if ns.get('fileCount')!=count: baseline_errors.append(f'normative surface file count changed: expected {ns.get("fileCount")}, found {count}')
 if ns.get('sha256')!=current_digest: baseline_errors.append('normative surface digest no longer matches frozen review baseline')
 src=baseline.get('sourceIdentity',{})
 if src.get('type') not in {'normative-surface-sha256','git-commit'} or not (src.get('sha256') or src.get('gitCommit')): baseline_errors.append('source identity is not content-addressed')
except Exception as e: baseline_errors.append(str(e))
add('GOV-REVIEW-BASELINE',not baseline_errors,'candidate review baseline is frozen and normative surface digest matches' if not baseline_errors else '; '.join(baseline_errors),'governance')

register=load(ROOT/'governance/candidate-issues.json')
review_files={p.stem:load(p) for p in sorted((ROOT/'governance/reviews').glob('*.json'))}
classes={'editorial','clarification','compatible-extension','breaking-normative-change','security-correction'}
statuses={'open','in-progress','closed','withdrawn'}; severities={'critical','high','medium','low','informational'}
gov_errors=[]; issue_ids=[]
for issue in register.get('issues',[]):
 issue_ids.append(issue.get('id'))
 if issue.get('status') not in statuses: gov_errors.append(f"{issue.get('id')}: invalid status")
 if issue.get('severity') not in severities: gov_errors.append(f"{issue.get('id')}: invalid severity")
 if issue.get('changeClass') not in classes: gov_errors.append(f"{issue.get('id')}: invalid change class")
 if not issue.get('decisionAuthority') or not issue.get('requiredEvidence') or not issue.get('disposition'): gov_errors.append(f"{issue.get('id')}: incomplete governance fields")
 badreq=[x for x in issue.get('affectedRequirements',[]) if x not in pids]
 badpro=[x for x in issue.get('affectedProfiles',[]) if x not in all_profile_ids]
 if badreq: gov_errors.append(f"{issue.get('id')}: unknown requirements {badreq}")
 if badpro: gov_errors.append(f"{issue.get('id')}: unknown profiles {badpro}")
add('GOV-CANDIDATE-REGISTER',not gov_errors,f'{len(issue_ids)} candidate issues have valid authority, scope, evidence and disposition fields' if not gov_errors else '; '.join(gov_errors[:10]),'governance')
add('GOV-CANDIDATE-IDS',len(issue_ids)==len(set(issue_ids)) and all(re.fullmatch(r'GAAM-CR-\d{3}',x or '') for x in issue_ids),f'{len(issue_ids)} unique candidate issue identifiers','governance')
required_reviews={'privacy-review','security-review','affected-party-review','interoperability-review','implementation-evidence'}
review_errors=[]; finding_ids=[]
try:
 review_schema=load(ROOT/'governance/reviews/review-register.schema.json'); Draft202012Validator.check_schema(review_schema)
 finding_schema=load(ROOT/'governance/reviews/finding.schema.json'); Draft202012Validator.check_schema(finding_schema)
 review_validator=Draft202012Validator(review_schema,format_checker=FormatChecker())
 finding_validator=Draft202012Validator(finding_schema,format_checker=FormatChecker())
except Exception as e:
 review_errors.append('review schema invalid: '+str(e)); review_validator=None; finding_validator=None
for name in required_reviews:
 obj=review_files.get(name)
 if not obj: review_errors.append(f'missing {name}'); continue
 if review_validator:
  errs=list(review_validator.iter_errors(obj))
  if errs: review_errors.append(f'{name}: schema: {errs[0].message}')
 if obj.get('gaamVersion')!=VERSION: review_errors.append(f'{name}: version mismatch')
 reviewer=obj.get('reviewer',{})
 if obj.get('status')=='complete':
  if reviewer.get('independence')=='unassigned': review_errors.append(f'{name}: complete review has unassigned independence')
  if obj.get('attestation',{}).get('status')!='attested' or not obj.get('completedAt'): review_errors.append(f'{name}: complete review lacks attestation/completion time')
  if obj.get('blockingFindings'): review_errors.append(f'{name}: complete review retains blocking findings')
 for finding in obj.get('findings',[]):
  if finding_validator:
   errs=list(finding_validator.iter_errors(finding))
   if errs: review_errors.append(f'{name}/{finding.get("id","unknown")}: {errs[0].message}'); continue
  finding_ids.append(finding.get('id'))
  badreq=[x for x in finding.get('affectedRequirements',[]) if x not in pids]
  badpro=[x for x in finding.get('affectedProfiles',[]) if x not in all_profile_ids]
  if badreq: review_errors.append(f'{finding.get("id")}: unknown requirements {badreq}')
  if badpro: review_errors.append(f'{finding.get("id")}: unknown profiles {badpro}')
  for ref in finding.get('evidence',[])+finding.get('closureEvidence',[]):
   if ref.startswith(('http://','https://')): continue
   if not (ROOT/ref).exists(): review_errors.append(f'{finding.get("id")}: missing evidence {ref}')
  if finding.get('status')=='closed' and not finding.get('closureEvidence'): review_errors.append(f'{finding.get("id")}: closed without closure evidence')
  if finding.get('status')=='deferred' and (not finding.get('owner') or not finding.get('targetDate')): review_errors.append(f'{finding.get("id")}: deferred without owner/target date')
  if finding.get('status')=='accepted-risk' and not finding.get('decisionAuthority'): review_errors.append(f'{finding.get("id")}: risk accepted without authority')
 # Register evidence references must resolve, except governed external URLs.
 for ref in obj.get('evidence',[]):
  if ref.startswith(('http://','https://')): continue
  if not (ROOT/ref).exists(): review_errors.append(f'{name}: missing evidence {ref}')
 # blockingFindings must point at findings in this register.
 local_ids={f.get('id') for f in obj.get('findings',[])}
 if any(x not in local_ids for x in obj.get('blockingFindings',[])): review_errors.append(f'{name}: blockingFindings contains unknown IDs')
add('GOV-REVIEW-REGISTERS',not review_errors,f'{len(required_reviews)} review registers conform with attributable authority, evidence and closure controls' if not review_errors else '; '.join(review_errors[:12]),'governance')
add('GOV-REVIEW-FINDING-IDS',len(finding_ids)==len(set(finding_ids)),f'{len(finding_ids)} review finding identifiers are unique','governance')

# Joint disposition is intentionally empty until cross-review findings exist, but its authority and closure rule are explicit.
joint_errors=[]
try:
 joint=load(ROOT/'governance/reviews/joint-disposition-register.json')
 if joint.get('gaamVersion')!=VERSION or joint.get('baseline')!='governance/reviews/review-baseline.json': joint_errors.append('version/baseline mismatch')
 if not joint.get('decisionAuthority') or not joint.get('closureRule'): joint_errors.append('authority or closure rule missing')
 for entry in joint.get('entries',[]):
  if not entry.get('id') or not entry.get('disposition') or not entry.get('verificationEvidence'): joint_errors.append(f"{entry.get('id','unknown')}: incomplete disposition")
except Exception as e: joint_errors.append(str(e))
add('GOV-JOINT-DISPOSITION',not joint_errors,'joint disposition authority and closure rule are explicit' if not joint_errors else '; '.join(joint_errors),'governance')
# Governed ecosystem applicability evidence
eco_dir=ROOT/'governance/reviews/evidence/implementation/ecosystems'
eco_required={'README.md','governed-ecosystem-capability-matrix.csv','governed-ecosystem-capability-matrix.md','governed-ecosystem-enhancement-register.json','governed-ecosystem-normative-impact-analysis.md','reference-ecosystem-comparison.md','reviewer-attestation.json'}
eco_missing=sorted(x for x in eco_required if not (eco_dir/x).exists())
add('GOV-ECO-EVIDENCE',not eco_missing,'governed ecosystem evidence package complete' if not eco_missing else 'missing '+', '.join(eco_missing),'governance')
eco_errors=[]
if not eco_missing:
 try:
  with (eco_dir/'governed-ecosystem-capability-matrix.csv').open(newline='') as f:
   eco_rows=list(csv.DictReader(f))
  valid_gaps={'already-covered','guidance-gap','pattern-gap','schema-gap','vocabulary-gap','profile-gap','normative-semantics-gap','test-gap','evidence-gap'}
  valid_disps={'no-change','documentation-clarification','implementation-guidance','new-informative-pattern','new-behavioural-test','schema-extension-proposal','vocabulary-extension-proposal','profile-proposal','normative-requirement-proposal','defer-pending-implementation'}
  for row in eco_rows:
   if row.get('gap_classification') not in valid_gaps: eco_errors.append(f"{row.get('ecosystem_capability')}: invalid gap classification")
   if row.get('proposed_disposition') not in valid_disps: eco_errors.append(f"{row.get('ecosystem_capability')}: invalid disposition")
   bad=[x for x in row.get('gaam_requirements','').split(';') if x and x not in pids]
   if bad: eco_errors.append(f"{row.get('ecosystem_capability')}: unknown requirements {bad}")
  reg=load(eco_dir/'governed-ecosystem-enhancement-register.json')
  if len(reg.get('entries',[]))!=len(eco_rows): eco_errors.append('enhancement register and capability matrix differ in size')
  if reg.get('gaamVersion')!=VERSION: eco_errors.append('enhancement register version mismatch')
  att=load(eco_dir/'reviewer-attestation.json')
  if att.get('independence')!='not-independent': eco_errors.append('maintainer-prepared assessment must not claim independence')
 except Exception as e: eco_errors.append(str(e))
add('GOV-ECO-DISPOSITION',not eco_errors,f'{len(eco_rows) if not eco_errors else 0} ecosystem capabilities classified with controlled dispositions' if not eco_errors else '; '.join(eco_errors[:10]),'governance')
templates=['change-proposal.yml','implementation-report.yml','review-finding.yml']
missing_templates=[x for x in templates if not (ROOT/'.github/ISSUE_TEMPLATE'/x).exists()]
add('GOV-CONTRIBUTION-CONTROLS',not missing_templates and (ROOT/'.github/pull_request_template.md').exists(),'candidate issue forms and pull-request governance template present' if not missing_templates else str(missing_templates),'governance')
open_blockers=[x['id'] for x in register.get('issues',[]) if x.get('blockingV1') and x.get('status')!='closed']
add('GOV-V1-READINESS-STATE',True,f'{len(open_blockers)} explicitly recorded open v1 blockers: {", ".join(open_blockers)}','governance')
# Portable implementation evidence and evidence-driven candidate readiness
implementation_evidence_errors=[]
try:
 report_schema=load(ROOT/'implementation-reports/implementation-report.schema.json'); Draft202012Validator.check_schema(report_schema)
 evidence_manifest_schema=load(ROOT/'implementation-reports/evidence-manifest.schema.json'); Draft202012Validator.check_schema(evidence_manifest_schema)
 conformance_result_schema=load(ROOT/'implementation-reports/conformance-result.schema.json'); Draft202012Validator.check_schema(conformance_result_schema)
 report_validator=Draft202012Validator(report_schema,format_checker=FormatChecker())
 evidence_manifest_validator=Draft202012Validator(evidence_manifest_schema,format_checker=FormatChecker())
 result_validator=Draft202012Validator(conformance_result_schema,format_checker=FormatChecker())
except Exception as e:
 implementation_evidence_errors.append('schema error: '+str(e)); report_validator=evidence_manifest_validator=result_validator=None

# Example and future submitted reports must be structurally valid. Only reports/ can contribute to readiness.
report_paths=[]
example_report=ROOT/'implementation-reports/examples/illustrative-report.json'
if example_report.exists(): report_paths.append(example_report)
reports_dir=ROOT/'implementation-reports/reports'
if reports_dir.exists(): report_paths += sorted(reports_dir.glob('*.json'))
seen_report_ids=[]
for rp in report_paths:
 try:
  report=load(rp)
  if report_validator:
   errs=list(report_validator.iter_errors(report))
   if errs: implementation_evidence_errors.append(f'{rp.relative_to(ROOT)}: schema: {errs[0].message}'); continue
  rid=report.get('reportId'); seen_report_ids.append(rid)
  badreq=[x for x in report.get('requirementsEvaluated',[]) if x not in pids]
  badpro=[x for x in report.get('profiles',[]) if x not in all_profile_ids]
  if badreq: implementation_evidence_errors.append(f'{rid}: unknown requirements {badreq}')
  if badpro: implementation_evidence_errors.append(f'{rid}: unknown profiles {badpro}')
  result_ids=[]
  for result in report.get('results',[]):
   if result_validator:
    errs=list(result_validator.iter_errors(result))
    if errs: implementation_evidence_errors.append(f'{rid}/{result.get("resultId","unknown")}: {errs[0].message}')
   result_ids.append(result.get('resultId'))
   if result.get('requirementId') not in report.get('requirementsEvaluated',[]): implementation_evidence_errors.append(f'{rid}: result requirement not declared in requirementsEvaluated')
   if result.get('requirementId') not in pids: implementation_evidence_errors.append(f'{rid}: result references unknown requirement {result.get("requirementId")}')
  if len(result_ids)!=len(set(result_ids)): implementation_evidence_errors.append(f'{rid}: duplicate result IDs')
  for exc in report.get('exceptions',[]):
   bad=[x for x in exc.get('affectedRequirements',[]) if x not in pids]
   if bad: implementation_evidence_errors.append(f'{rid}/{exc.get("id")}: unknown exception requirements {bad}')
  mp=ROOT/report.get('evidenceManifest','')
  if not mp.exists(): implementation_evidence_errors.append(f'{rid}: evidence manifest missing')
  else:
   manifest=json.loads(mp.read_text())
   if evidence_manifest_validator:
    errs=list(evidence_manifest_validator.iter_errors(manifest))
    if errs: implementation_evidence_errors.append(f'{rid}: evidence manifest schema: {errs[0].message}')
   if manifest.get('reportId')!=rid: implementation_evidence_errors.append(f'{rid}: evidence manifest reportId mismatch')
   evidence_ids=[]
   for art in manifest.get('artifacts',[]):
    evidence_ids.append(art.get('evidenceId'))
    ap=ROOT/art.get('path','')
    if not ap.exists(): implementation_evidence_errors.append(f'{rid}/{art.get("evidenceId")}: evidence artifact missing')
    elif hashlib.sha256(ap.read_bytes()).hexdigest()!=art.get('sha256'): implementation_evidence_errors.append(f'{rid}/{art.get("evidenceId")}: evidence digest mismatch')
   if len(evidence_ids)!=len(set(evidence_ids)): implementation_evidence_errors.append(f'{rid}: duplicate evidence IDs')
   referenced={x for result in report.get('results',[]) for x in result.get('evidenceIds',[])}
   missing=sorted(referenced-set(evidence_ids))
   if missing: implementation_evidence_errors.append(f'{rid}: result evidence IDs missing from manifest {missing}')
  if report.get('evidenceLevel')=='L4' and report.get('independence',{}).get('classification')!='independent': implementation_evidence_errors.append(f'{rid}: L4 requires independent assessment')
  if report.get('reportStatus')=='accepted':
   if report.get('synthetic'): implementation_evidence_errors.append(f'{rid}: synthetic report cannot be accepted')
   review=report.get('review',{})
   if not review.get('acceptedBy') or not review.get('acceptedAt') or not review.get('decisionEvidence'): implementation_evidence_errors.append(f'{rid}: accepted report lacks attributable acceptance decision')
   elif not (ROOT/review.get('decisionEvidence')).exists(): implementation_evidence_errors.append(f'{rid}: acceptance decision evidence missing')
 except Exception as e: implementation_evidence_errors.append(f'{rp.relative_to(ROOT)}: {e}')
if len(seen_report_ids)!=len(set(seen_report_ids)): implementation_evidence_errors.append('duplicate implementation report IDs')
add('ASSURANCE-IMPLEMENTATION-REPORTS',not implementation_evidence_errors,f'{len(report_paths)} implementation report artifacts conform with provenance, evidence and acceptance controls' if not implementation_evidence_errors else '; '.join(implementation_evidence_errors[:12]),'assurance')

# Fixture contract proves positive and negative validation behaviour.
fixture_errors=[]
try:
 valid_fixture=load(ROOT/'implementation-reports/fixtures/valid-independent-report.json')
 if list(report_validator.iter_errors(valid_fixture)): fixture_errors.append('valid-independent-report rejected')
 for name in ['invalid-missing-source-revision.json','invalid-unknown-profile.json','invalid-independence-claim.json','invalid-missing-evidence.json']:
  obj=load(ROOT/'implementation-reports/fixtures'/name)
  if not list(report_validator.iter_errors(obj)): fixture_errors.append(f'{name} unexpectedly accepted')
except Exception as e: fixture_errors.append(str(e))
add('ASSURANCE-IMPLEMENTATION-FIXTURES',not fixture_errors,'implementation-report schema accepts the positive fixture and rejects four controlled negative fixtures' if not fixture_errors else '; '.join(fixture_errors),'assurance')

# Candidate readiness is generated, schema-valid and current with its authoritative inputs.
readiness_errors=[]
try:
 readiness_schema=load(ROOT/'governance/candidate-readiness.schema.json'); Draft202012Validator.check_schema(readiness_schema)
 readiness=load(ROOT/'governance/candidate-readiness.json')
 errs=list(Draft202012Validator(readiness_schema).iter_errors(readiness))
 if errs: readiness_errors.append('schema: '+errs[0].message)
 cp=subprocess.run([sys.executable,str(ROOT/'scripts/build_candidate_readiness.py'),'--check'],cwd=ROOT,capture_output=True,text=True)
 if cp.returncode!=0: readiness_errors.append((cp.stderr or cp.stdout).strip())
 if readiness.get('eligibleForV1Decision') != (len(readiness.get('blockingGates',[]))==0): readiness_errors.append('eligibility inconsistent with blocking gates')
 gate_ids=[x.get('id') for x in readiness.get('gates',[])]
 if len(gate_ids)!=len(set(gate_ids)): readiness_errors.append('duplicate readiness gate IDs')
except Exception as e: readiness_errors.append(str(e))
add('GOV-CANDIDATE-READINESS',not readiness_errors,'candidate readiness is schema-valid, generated from authoritative evidence and current' if not readiness_errors else '; '.join(readiness_errors[:8]),'governance')

# Package manifest + integrity
pkg=ROOT/'packages'/f'gaam-v{VERSION}'; pkg.mkdir(parents=True,exist_ok=True)
artifact_paths=['PROJECT-STATUS.yaml',REL['normativeSpecification'],'release.json','schemas/catalog.json','threat-model/threat-register.json','matrices/normative-requirements-index.csv','matrices/requirement-test-coverage.csv','matrices/requirement-assurance-traceability.csv','matrices/threat-control-test-matrix.csv','governance/candidate-issues.json']
artifact_paths += [str(p.relative_to(ROOT)) for b in ['schemas','vocabularies','profiles/manifests','tests/behavioural'] for p in sorted((ROOT/b).glob('*.json'))]
artifact_paths += [str(p.relative_to(ROOT)) for p in sorted((ROOT/'governance/reviews').rglob('*')) if p.is_file() and p.name not in {'.gitkeep'}]
artifact_paths += [str(p.relative_to(ROOT)) for p in sorted((ROOT/'examples').rglob('*')) if p.is_file() and p.name not in {'.gitkeep'}]
artifact_paths += [str(p.relative_to(ROOT)) for p in sorted((ROOT/'docs/future-evolution').rglob('*')) if p.is_file() and p.name not in {'.gitkeep'}]
artifact_paths += ['governance/future-enhancement-register.json','governance/candidate-readiness.json','governance/candidate-readiness.schema.json']
artifact_paths += [str(p.relative_to(ROOT)) for p in sorted((ROOT/'implementation-reports').glob('*.schema.json'))]
artifact_paths += [str(p.relative_to(ROOT)) for p in sorted((ROOT/'implementation-reports/examples').iterdir()) if p.is_file() and p.suffix in {'.json','.txt'}]
artifact_paths += [str(p.relative_to(ROOT)) for p in sorted((ROOT/'implementation-reports/reports').glob('*.json'))]
# Include locally retained evidence referenced by implementation reports so packaged report evidence remains reconstructable.
for rp in report_paths:
 try:
  ro=load(rp); mp=ROOT/ro.get('evidenceManifest','')
  if mp.exists():
   artifact_paths.append(str(mp.relative_to(ROOT)))
   mo=load(mp)
   for art in mo.get('artifacts',[]):
    ap=ROOT/art.get('path','')
    if ap.exists(): artifact_paths.append(str(ap.relative_to(ROOT)))
 except Exception:
  pass
artifact_paths += [str(p.relative_to(ROOT)) for b in ['profiles-draft','experimental'] for p in sorted((ROOT/b).rglob('*')) if p.is_file() and p.name not in {'.gitkeep'}]
manifest={'id':f'urn:gaam:package:{VERSION}','type':'gaam-governance-package','gaamVersion':VERSION,'status':'active','profiles':sorted(manifests),'artifacts':[{'id':Path(x).stem,'path':x,'mediaType':'application/json' if x.endswith('.json') else 'application/yaml' if x.endswith(('.yaml','.yml')) else 'text/markdown' if x.endswith('.md') else 'text/csv'} for x in artifact_paths if not x.startswith(('schemas/','vocabularies/'))], 'schemas':[p.name for p in sorted((ROOT/'schemas').glob('*.schema.json'))], 'vocabularies':[p.name for p in sorted((ROOT/'vocabularies').glob('*.json'))], 'integrity':{'algorithm':'sha-256','manifest':'checksums.json'}}
(pkg/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
perrs=list(Draft202012Validator(schemas['gaam-package']).iter_errors(manifest)); add('PKG-MANIFEST',not perrs,'package manifest conforms','package')
checks=[]
for x in sorted(set(artifact_paths+[f'packages/gaam-v{VERSION}/manifest.json'])):
 p=ROOT/x
 if p.exists(): checks.append({'path':x,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(pkg/'checksums.json').write_text(json.dumps({'algorithm':'sha-256','scope':'declared source artifacts excluding this checksum file','files':checks},indent=2)+'\n')
verified=all(hashlib.sha256((ROOT/x['path']).read_bytes()).hexdigest()==x['sha256'] for x in checks)
add('PKG-INTEGRITY',verified,f'{len(checks)} checksums verified','package')
# Reports
out=ROOT/'validation'; out.mkdir(exist_ok=True)
summary={'gaamVersion':VERSION,'testSuiteVersion':VERSION,'status':'pass' if all(r['status']=='pass' for r in results) else 'fail','checks':len(results),'passed':sum(r['status']=='pass' for r in results),'failed':sum(r['status']=='fail' for r in results),'results':results}
(out/'validation-report.json').write_text(json.dumps(summary,indent=2)+'\n')
md=['---','title: GAAM v0.9.0 Validation Report','permalink: /validation-report/','nav_exclude: true','artifact_type: Validation evidence','normative_status: Repository generated','---','# GAAM v0.9.0 Validation Report','','{% include gaam-meta.html %}','',f'**Status:** {summary["status"].upper()}  ',f'**Checks:** {summary["checks"]}  ',f'**Passed:** {summary["passed"]}  ',f'**Failed:** {summary["failed"]}  ','','This report evidences repository publication, structural and included behavioural checks. It is not an independent L4 assessment.','','| ID | Kind | Status | Evidence |','|---|---|---|---|']
md += [f'| `{r["id"]}` | {r["kind"]} | {r["status"].upper()} | {r["evidence"].replace("|","/")} |' for r in results]
(ROOT/'VALIDATION_REPORT.md').write_text('\n'.join(md)+'\n')
print(json.dumps({k:summary[k] for k in ['status','checks','passed','failed']},indent=2)); sys.exit(0 if summary['status']=='pass' else 1)
