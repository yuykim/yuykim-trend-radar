from pathlib import Path
import json,hashlib,requests,re
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parent/'sources'
items=[
 ('A-augur','https://arxiv.org/pdf/1912.08928','pdf'),
 ('A-wang','https://arxiv.org/pdf/1707.03599','pdf'),
 ('A-horizon','https://arxiv.org/pdf/2202.13480','pdf'),
 ('A-eysenbach-pmc','https://pmc.ncbi.nlm.nih.gov/articles/PMC3278109/','html'),
 ('A-costas-full','https://arxiv.org/pdf/1401.4321','pdf'),
]
log=[]
for name,url,ext in items:
 try:
  r=requests.get(url,timeout=40);r.raise_for_status()
  if not r.content:raise ValueError('Empty response')
  p=root/f'{name}.{ext}';p.write_bytes(r.content)
  if ext=='html':
   s=BeautifulSoup(r.content,'html.parser')
   for t in s(['script','style','noscript']):t.decompose()
   p.with_suffix('.txt').write_text('\n'.join(re.sub(r'\s+',' ',x).strip() for x in s.stripped_strings),encoding='utf-8')
  log.append(dict(name=name,url=url,final_url=r.url,file=p.name,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest()))
  print(name,len(r.content),flush=True)
 except Exception as e: print(name,str(e),flush=True)
(root/'manifest-A-more.json').write_text(json.dumps(log,indent=2),encoding='utf-8')
