from pathlib import Path
import argparse,fitz,re,csv,collections,json
ap=argparse.ArgumentParser(description='Extract the 57 retained clickable links from the original six-page conference PDF (not included in public GitHub).')
ap.add_argument('original_pdf',help='Path to the author-provided submitted six-page PDF with clickable table')
ap.add_argument('--output-dir',default=str(Path(__file__).resolve().parent.parent/'data'))
args=ap.parse_args()
src=Path(args.original_pdf)
out=Path(args.output_dir);out.mkdir(parents=True,exist_ok=True)
p=fitz.open(src)[-1]
lines=[]
for b in p.get_text('dict')['blocks']:
    if b['type']!=0:continue
    for l in b['lines']:
        x,y=l['bbox'][:2]
        if 182<=y<=385 and x>=340:
            s=''.join(t['text'] for t in l['spans']).strip()
            if re.match(r'^(AE|SA|QA|OM|BH|KW): ',s):
                lines.append((round(y,1),round(x,1),s))
links=[a for a in p.get_links() if a.get('uri') and a['from'].y0>180 and a['from'].y0<390 and a['from'].x0>340]
rows=[]
for k,(y,x,s) in enumerate(lines):
    opts=[a for a in links if abs(a['from'].y0-(y-.85))<1.8 and abs(a['from'].x0-(x-1))<3.5]
    if len(opts)!=1:
        print('MATCH_ERROR',k,s,y,x,[(round(a['from'].x0,1),round(a['from'].y0,1)) for a in links if abs(a['from'].y0-y)<2])
        continue
    state=re.search(r'\[([EPU])\]',s)
    rows.append({'row':k+1,'jurisdiction':s[:2],'institution_label':re.sub(r'^\w{2}:\s*','',re.sub(r'\s*\[[EPU]\]$','',s)), 'state':state.group(1) if state else '?','evidence_or_search_url':opts[0]['uri'],'link_type':'Retained cited instrument or official context/search page; not independently reverified in this revision'})
assert len(rows)==57,len(rows)
assert collections.Counter(x['state'] for x in rows)=={'E':20,'P':12,'U':25}
assert collections.Counter(x['jurisdiction'] for x in rows)=={'AE':13,'SA':11,'QA':10,'OM':8,'BH':7,'KW':8}
with (out/'ICAMAC2026_57_Institution_Clickable_Key.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
(out/'ICAMAC2026_57_Link_Audit.json').write_text(json.dumps({'source_pdf':src.name,'row_count':57,'state_counts':dict(collections.Counter(x['state'] for x in rows)),'jurisdiction_counts':dict(collections.Counter(x['jurisdiction'] for x in rows))},indent=2),encoding='utf-8')
print('ROWS',len(rows))
for x in rows[:5]:print(x['institution_label'],x['state'],x['evidence_or_search_url'][:70])
