import csv,html
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
root=Path(__file__).resolve().parent.parent
out=root/'data'
pdf_out=root/'supplement'
pdf_out.mkdir(exist_ok=True)
rows=list(csv.DictReader((out/'ICAMAC2026_57_Institution_Clickable_Key.csv').open(encoding='utf-8-sig',newline='')))
city={'AE':'United Arab Emirates','SA':'Saudi Arabia','QA':'Qatar','OM':'Oman','BH':'Bahrain','KW':'Kuwait'}
base=Path('/usr/share/fonts/truetype/dejavu')
if (base/'DejaVuSans.ttf').exists() and (base/'DejaVuSans-Bold.ttf').exists():
 pdfmetrics.registerFont(TTFont('DejaVu',str(base/'DejaVuSans.ttf')))
 pdfmetrics.registerFont(TTFont('DejaVuBold',str(base/'DejaVuSans-Bold.ttf')))
else:
 # Any system can reproduce a readable appendix without redistributing a font.
 pass
FONT='DejaVu' if 'DejaVu' in pdfmetrics.getRegisteredFontNames() else 'Helvetica'
BOLD='DejaVuBold' if 'DejaVuBold' in pdfmetrics.getRegisteredFontNames() else 'Helvetica-Bold'
styles=getSampleStyleSheet();styles.add(ParagraphStyle(name='TitleCustom',fontName=BOLD,fontSize=14,leading=18,spaceAfter=14));styles.add(ParagraphStyle(name='SmallText',fontName=FONT,fontSize=8.2,leading=12,spaceAfter=8));styles.add(ParagraphStyle(name='CellSmall',fontName=FONT,fontSize=8.2,leading=11));styles.add(ParagraphStyle(name='HeadCustom',fontName=BOLD,fontSize=10.2,leading=13,spaceBefore=13,spaceAfter=7))

def footer(c,doc):
 c.setFont('Helvetica',8);c.setFillColor(colors.HexColor('#66717b'))
 c.drawString(38,25,'ICAMAC 2026 • Companion key • fixed 23 July 2026 cutoff')
 c.drawRightString(letter[0]-38,25,f'Page {doc.page}')

p=pdf_out/'ICAMAC2026_57_Institution_Clickable_Key_REGENERATED.pdf'
doc=SimpleDocTemplate(str(p),pagesize=letter,leftMargin=42,rightMargin=42,topMargin=41,bottomMargin=47,title='57-institution official locator key',author='')
story=[Paragraph('Companion audit key: 57 selected GCC institutions',styles['TitleCustom']),Paragraph('<b>Scope.</b> These are the 57 institution names, final nominal states, and retained clickable URLs transcribed directly from the six-page ICAMAC2026 submission copy. No policy or website is independently reverified by this extraction. <b>E</b> = explicit institution-level rule under the recorded gate, <b>P</b> = partial/narrow, <b>U</b> = a qualifying public rule not located under the original search protocol. A URL may be a specific instrument or merely an official context/search page (especially U cases); do not mistake the link for independent confirmation.',styles['SmallText']),Paragraph('<b>Locked counts:</b> 20 E / 12 P / 25 U. This pre-outcome oldest-four-with-ties panel is not a random sample and cannot estimate country-wide policy prevalence. Full unabridged URLs are provided in the adjacent CSV file.',styles['SmallText'])]
for state in ['AE','SA','QA','OM','BH','KW']:
 subset=[x for x in rows if x['jurisdiction']==state]
 story.append(Paragraph(f'{html.escape(city[state])} — {len(subset)} institutions',styles['HeadCustom']))
 data=[['#','Institution (submission label)','E/P/U','Retained official locator']]
 for x in subset:
  label=html.escape(x['institution_label'])
  uri=html.escape(x['evidence_or_search_url'],quote=True)
  # reportlab link markup uses double quoted escaped link
  cell=Paragraph(f'<link href="{uri}" color="#135b85"><u>Open linked locator</u></link>',styles['CellSmall'])
  data.append([str(x['row']),Paragraph(label,styles['CellSmall']),x['state'],cell])
 tab=Table(data,colWidths=[25,210,51,224],repeatRows=1,hAlign='LEFT',rowSplitRange=(1,len(data)))
 tab.setStyle(TableStyle([('FONTNAME',(0,0),(-1,0),BOLD),('FONTNAME',(0,1),(-1,-1),FONT),('FONTSIZE',(0,0),(-1,0),8),('FONTSIZE',(0,1),(-1,-1),8),('LEADING',(0,0),(-1,-1),11),('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e9eef1')),('TEXTCOLOR',(0,0),(-1,0),colors.HexColor('#1e2931')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f9fafb')]),('LINEBELOW',(0,0),(-1,0),0.65,colors.HexColor('#9faab4')),('LINEBELOW',(0,1),(-1,-1),0.2,colors.HexColor('#d9dfe5')),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5)]))
 story.append(tab)
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(p)
