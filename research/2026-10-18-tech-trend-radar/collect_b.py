from pathlib import Path
import requests, hashlib, json, concurrent.futures
from bs4 import BeautifulSoup

ROOT=Path(__file__).parent
DEST=ROOT/'sources'
DEST.mkdir(exist_ok=True)
SOURCES=[
 ('B-S01-eysenbach','https://www.jmir.org/2011/4/e123/','html'),
 ('B-S02-haustein','https://arxiv.org/pdf/1308.1838','pdf'),
 ('B-S03-bots','https://arxiv.org/pdf/1410.4139','pdf'),
 ('B-S04-x-pricing','https://docs.x.com/x-api/getting-started/pricing','html'),
 ('B-S05-reddit-2023','https://redditinc.com/news/apifacts','html'),
 ('B-S06-reddit-current','https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki','html'),
 ('B-S07-bloom','https://www.nber.org/system/files/working_papers/w28999/revisions/w28999.rev1.pdf','pdf'),
 ('B-S08-mantegna','https://arxiv.org/pdf/cond-mat/9802256','pdf'),
 ('B-S09-etf','https://www.nber.org/system/files/working_papers/w28369/w28369.pdf','pdf'),
 ('B-S10-code','https://knowledge.uchicago.edu/record/12860/files/Dissertation_Donghyun_Kang_for_submission.pdf','pdf'),
]

def fetch(entry):
 name,url,kind=entry
 r=requests.get(url,timeout=90)
 r.raise_for_status()
 if kind=='pdf' and not r.content.startswith(b'%PDF'): raise ValueError(name+' not PDF')
 p=DEST/(name+'.'+kind)
 if p.exists(): raise FileExistsError(p)
 p.write_bytes(r.content)
 if kind=='html':
  soup=BeautifulSoup(r.content,'html.parser')
  for tag in soup(['script','style','noscript']): tag.decompose()
  txt=soup.get_text(' ',strip=True)
  (DEST/(name+'.txt')).write_text(txt,encoding='utf-8')
 return dict(id=name,url=url,final_url=r.url,file=p.name,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest(),retrieved_at=r.headers.get('Date'))

if __name__=='__main__':
 results=[]
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
  jobs={pool.submit(fetch,s):s for s in SOURCES}
  for job in concurrent.futures.as_completed(jobs):
   try:
    result=job.result(); results.append(result); print(result['id'],result['bytes'],flush=True)
   except Exception as exc: print('FAILED',jobs[job][0],str(exc),flush=True)
 (DEST/'B-manifest.json').write_text(json.dumps(sorted(results,key=lambda x:x['id']),ensure_ascii=False,indent=2),encoding='utf-8')
