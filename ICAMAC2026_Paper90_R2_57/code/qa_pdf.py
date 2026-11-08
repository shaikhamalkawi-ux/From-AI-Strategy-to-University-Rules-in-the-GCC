"""Standalone R2 PDF QA: author-linked paper (8 pages), 57-link appendix (3)."""
from pathlib import Path
import json,hashlib
import fitz
root=Path(__file__).resolve().parent.parent
main=root/'manuscript/ICAMAC2026_Paper90_R2_AuthorLinked_8pages.pdf'
supp=root/'supplement/ICAMAC2026_Paper90_57_Institutions_Supplement.pdf'
url='https://github.com/shaikhamalkawi-ux/From-AI-Strategy-to-University-Rules-in-the-GCC/tree/main/ICAMAC2026_Paper90_R2_57'
with fitz.open(main) as m,fitz.open(supp) as s:
 assert len(m)==8,len(m)
 assert len(s)==3,len(s)
 assert 'From AI Strategy to University Rules in the GCC' in m[0].get_text()
 lm=[q.get('uri') for p in m for q in p.get_links() if q.get('uri')]
 ls=[q.get('uri') for p in s for q in p.get_links() if q.get('uri')]
 assert url in lm,'Author copy lacks live GitHub URL'
 assert len(ls)==57 and len(set(ls))==57,'Supplement should contain 57 unique links'
 assert '20 explicit' in '\n'.join(p.get_text() for p in m)
 report={'paper_pages':len(m),'supplement_pages':len(s),'supplement_links':len(ls),
  'repository_link_verified_in_author_copy':True,
  'paper_sha256':hashlib.sha256(main.read_bytes()).hexdigest(),
  'supplement_sha256':hashlib.sha256(supp.read_bytes()).hexdigest(),
  'status':'PASS','boundary':'visual/content/URL QA, not independent source or code validation'}
(root/'checks'/'QA_PDF_R2_AUTHOR_LINKED.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS',json.dumps(report,indent=2))
