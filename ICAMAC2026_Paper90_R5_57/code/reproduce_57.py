#!/usr/bin/env python3
"""Regenerate counts/sensitivity from locked 57-case labels, not source-classification validation."""
from pathlib import Path
import csv, json
from collections import Counter
P = Path(__file__).resolve().parent.parent
read=lambda p: list(csv.DictReader((P/'data'/p).open(encoding='utf-8-sig',newline='')))
ins=read('ICAMAC2026_57_Institution_Clickable_Key.csv')
chain=read('ICAMAC2026_6_Jurisdiction_Layer_Matrix.csv')
assert len(ins)==57 and len(chain)==6
assert [r['Jurisdiction'] for r in chain]==['UAE','Saudi Arabia','Qatar','Oman','Bahrain','Kuwait']
assert len({(r['jurisdiction'],r['institution_label']) for r in ins})==57
assert [r['row'] for r in ins]==list(map(str,range(1,58)))
assert {r['state'] for r in ins}<={'E','P','U'}
assert all({r[k] for r in chain}<={'E','P','U'} for k in ('L1','L2','L3','L4'))
counts=Counter(r['state'] for r in ins)
assert counts=={'E':20,'P':12,'U':25},counts
country={c:Counter(r['state'] for r in ins if r['jurisdiction']==c) for c in ['AE','SA','QA','OM','BH','KW']}
expected={'AE':(5,3,5),'SA':(3,4,4),'QA':(2,2,6),'OM':(2,1,5),'BH':(6,0,1),'KW':(2,2,4)}
assert {c:tuple(country[c][s] for s in 'EPU') for c in country}==expected
l3=sum(r['L3']=='E' for r in chain)
l4=sum(r['L4']=='E' for r in chain)
D=sum(r['L4']=='E' and r['L3']!='E' for r in chain)
assert (l3,l4,D)==(1,6,5)
envelopes={k:{'lower':sum(r[k]=='E' for r in chain)/6,
               'upper':sum(r[k] in ('E','P') for r in chain)/6} for k in ('L1','L2','L3','L4')}
assert envelopes['L4']['lower']-envelopes['L3']['upper']==0.5
l3_broad=[dict(r) for r in chain]
next(r for r in l3_broad if r['Jurisdiction']=='UAE')['L3']='E'
assert sum(r['L4']=='E' and r['L3']!='E' for r in l3_broad)==4
# Algebraic indicator perturbation bound -- CONDITIONAL not empirical error rate.
conditional={str(k):max(0,D-k) for k in range(7)}
out={'source_cutoff':'2026-07-23','panel_N':len(ins),'panel_counts':dict(counts),
     'jurisdiction_counts':{c:dict(country[c]) for c in country},
     'l3_explicit':l3,'l4_explicit':l4,'l4_explicit_l3_not':D,
     'fuzzy_representation_envelopes':envelopes,'broad_uae_D':4,
     'conditional_min_gap_by_changed_indicator_count':conditional,
     'validation_boundary':'Arithmetic only; no source recall, coder agreement, or implementation validation.'}
(P/'checks'/'REPRODUCED_57_COUNTS.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('PASS: 57 cases; E/P/U=20/12/25; L3E=1/6; L4E=6/6; D=5/6; fuzzy min=.500.')
