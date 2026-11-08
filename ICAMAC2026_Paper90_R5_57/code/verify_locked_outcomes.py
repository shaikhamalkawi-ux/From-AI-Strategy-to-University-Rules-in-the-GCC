"""Arithmetic-only verification of source-transcribed locked GCC results.
DOES NOT constitute independent source recovery, coding, or human verification.
"""
from pathlib import Path
from collections import Counter,defaultdict
import csv,math,hashlib,json
ROOT=Path(__file__).resolve().parent.parent
matrix=list(csv.DictReader((ROOT/'data/ICAMAC2026_6_Jurisdiction_Layer_Matrix.csv').open(encoding='utf-8')))
inst=list(csv.DictReader((ROOT/'data/ICAMAC2026_57_Institution_Clickable_Key.csv').open(encoding='utf-8-sig')))
assert len(matrix)==6
assert len(inst)==57
assert len(set((x['jurisdiction'],x['institution_label']) for x in inst))==57
assert all(x[k] in {'E','P','U'} for x in matrix for k in ['L1','L2','L3','L4'])
assert Counter(x['state'] for x in inst)==Counter({'E':20,'P':12,'U':25})
assert Counter(x['jurisdiction'] for x in inst)==Counter({'AE':13,'SA':11,'QA':10,'OM':8,'BH':7,'KW':8})
by_j={j:Counter(x['state'] for x in inst if x['jurisdiction']==j) for j in ['AE','SA','QA','OM','BH','KW']}
assert by_j=={
 'AE':Counter({'E':5,'P':3,'U':5}),
 'SA':Counter({'E':3,'P':4,'U':4}),
 'QA':Counter({'E':2,'P':2,'U':6}),
 'OM':Counter({'E':2,'P':1,'U':5}),
 'BH':Counter({'E':6,'P':0,'U':1}),
 'KW':Counter({'E':2,'P':2,'U':4})
}
assert all(c['E']>=2 and c['P']+c['U']>=1 for c in by_j.values())
D=sum(x['L4']=='E' and x['L3']!='E' for x in matrix)
assert D==5
assert sum(x['L3']=='E' for x in matrix)==1
assert sum(x['L4']=='E' for x in matrix)==6
assert {k:Counter(x[k] for x in matrix) for k in ['L1','L2','L3','L4']}=={
'L1':Counter({'E':4,'P':2}),
'L2':Counter({'E':5,'P':1}),
'L3':Counter({'E':1,'P':2,'U':3}),
'L4':Counter({'E':6})}
envelopes={k:[sum(x[k]=='E' for x in matrix)/6,(sum(x[k]=='E' for x in matrix)+sum(x[k]=='P' for x in matrix))/6] for k in ['L1','L2','L3','L4']}
assert math.isclose(envelopes['L4'][0]-envelopes['L3'][1],.5)
assert all(sum(x['L4']=='E' and x['L3']!='E' for x in matrix if x!=rm)>=4 for rm in matrix)
broad=[dict(x) for x in matrix]; next(x for x in broad if x['Jurisdiction']=='UAE')['L3']='E'
assert sum(x['L4']=='E' and x['L3']!='E' for x in broad)==4
pre=[dict(x) for x in matrix]; next(x for x in pre if x['Jurisdiction']=='Oman')['L4']='P'
assert sum(x['L4']=='E' and x['L3']!='E' for x in pre)==4
print('PASS | locked matrix 6/6, panel 57/57, counts 20/12/25, D=5, OBEF broader D=4, pre-SQU D=4, fuzzy min gap=.500, leave-one-jurisdiction-out >=4')
