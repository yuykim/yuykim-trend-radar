from collect_b import DEST
import requests, hashlib,json
from bs4 import BeautifulSoup
targets={
'B-S01-eysenbach': ['https://pmc.ncbi.nlm.nih.gov/articles/PMC3278109/','https://www.jmir.org/2011/4/e123'],
'B-S06-reddit-current':['https://support.reddithelp.com/api/v2/help_center/en-us/articles/16160319875092.json','https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki?output=1'],
'B-S10-code':['https://knowledge.uchicago.edu/records/eeeh9-3vv62/files/Dissertation_Donghyun_Kang_for_submission.pdf?download=1']}
manifest=json.loads((DEST/'B-manifest.json').read_text(encoding='utf-8'))
for name,urls in targets.items():
 if any(x['id']==name and x['bytes']>1000 for x in manifest): continue
 for url in urls:
  try:
   r=requests.get(url,timeout=90,headers={'User-Agent':'Mozilla/5.0'});r.raise_for_status()
   if len(r.content)<1000: raise ValueError('empty')
   kind='pdf' if r.content.startswith(b'%PDF') else 'html'
   body=r.content
   if url.endswith('.json'): body=r.json()['article']['body'].encode('utf-8')
   p=DEST/(name+'.'+kind);p.write_bytes(body)
   if kind=='html':
    soup=BeautifulSoup(body,'html.parser')
    for t in soup(['script','style','noscript']):t.decompose()
    (DEST/(name+'.txt')).write_text(soup.get_text(' ',strip=True),encoding='utf-8')
   manifest=[x for x in manifest if x['id']!=name]
   manifest.append(dict(id=name,url=url,final_url=r.url,file=p.name,bytes=len(body),sha256=hashlib.sha256(body).hexdigest(),retrieved_at=r.headers.get('Date')))
   print('OK',name,len(body),flush=True);break
  except Exception as exc:print('FAILED',name,str(exc),flush=True)
(DEST/'B-manifest.json').write_text(json.dumps(sorted(manifest,key=lambda x:x['id']),ensure_ascii=False,indent=2),encoding='utf-8')
