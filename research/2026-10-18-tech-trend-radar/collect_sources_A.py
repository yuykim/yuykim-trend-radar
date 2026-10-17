"""Download inert research documents; never execute downloaded content."""
from pathlib import Path
import hashlib, json, re, requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent
DEST = ROOT / 'sources'
DEST.mkdir(exist_ok=True)
SOURCES = [
 ('A-krenn', 'https://arxiv.org/pdf/2210.00881', 'pdf'),
 ('A-augur', 'https://oro.open.ac.uk/54345/1/JCDL2018_v49ANG.pdf', 'pdf'),
 ('A-growth', 'https://arxiv.org/pdf/2004.13159', 'pdf'),
 ('A-small', 'https://www.sciencedirect.com/science/article/pii/S0048733314000298', 'html'),
 ('A-eysenbach', 'https://www.jmir.org/2011/4/e123/', 'html'),
 ('A-costas', 'https://arxiv.org/abs/1401.4321', 'html'),
 ('A-penner', 'https://www.nature.com/articles/srep03052', 'html'),
 ('A-hype', 'https://doi.org/10.1016/j.techfore.2016.04.005', 'html'),
 ('A-lag', 'https://hci.stanford.edu/publications/2023/hcitransfer-chi-2023.pdf', 'pdf'),
]

if __name__ == '__main__':
 records=[]
 for name,url,kind in SOURCES:
  try:
   r=requests.get(url,timeout=40)
   r.raise_for_status()
   data=r.content
   if kind=='pdf' and not data.startswith(b'%PDF'): raise ValueError('Not a PDF')
   path=DEST/f'{name}.{kind}'
   path.write_bytes(data)
   if kind=='html':
    soup=BeautifulSoup(data,'html.parser')
    for tag in soup(['script','style','noscript']): tag.decompose()
    txt='\n'.join(re.sub(r'\s+',' ',s).strip() for s in soup.stripped_strings)
    path.with_suffix('.txt').write_text(txt,encoding='utf-8')
   records.append(dict(name=name,url=url,final_url=r.url,file=path.name,bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
   print(name,len(data),r.url,flush=True)
  except Exception as e:
   records.append(dict(name=name,url=url,error=str(e)))
   print(name,'ERROR',str(e),flush=True)
 (DEST/'manifest-A-initial.json').write_text(json.dumps(records,indent=2,ensure_ascii=False),encoding='utf-8')
