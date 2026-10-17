"""Verify exact quotes using rg, validate the claim table, and inventory sources."""
from pathlib import Path
import hashlib, json, re, subprocess

ROOT=Path(__file__).resolve().parent
DOC=ROOT/'claims-A.md'
sources=[
 ('S01','A-horizon','pdf','https://arxiv.org/pdf/2202.13480'),
 ('S02','A-wang','pdf','https://arxiv.org/pdf/1707.03599'),
 ('S03','A-augur','pdf','https://arxiv.org/pdf/1912.08928'),
 ('S04','A-krenn','pdf','https://arxiv.org/pdf/2210.00881'),
 ('S05','A-growth','pdf','https://arxiv.org/pdf/2004.13159'),
 ('S06','A-eysenbach-pmc','html','https://pmc.ncbi.nlm.nih.gov/articles/PMC3278109/'),
 ('S07','A-costas-full','pdf','https://arxiv.org/pdf/1401.4321'),
 ('S08','A-penner','html','https://www.nature.com/articles/srep03052'),
 ('S09','A-lag','pdf','https://hci.stanford.edu/publications/2023/hcitransfer-chi-2023.pdf'),
]

def main():
 text=DOC.read_text(encoding='utf-8')
 claim_table=text.split('## 출처 및 판정의 범위',1)[0]
 rows=[line for line in claim_table.splitlines() if re.match(r'^\| A\d\d \|',line)]
 assert len(rows)==9, len(rows)
 results=[]; manifest=[]
 allowed={'그대로 적용','조건부 적용','적용 불가','확인 불가'}
 for i,(line,(sid,name,ext,url)) in enumerate(zip(rows,sources),1):
  cols=[s.strip() for s in line.split('|')[1:-1]]
  assert len(cols)==9,(i,len(cols))
  assert cols[0]==f'A{i:02d}'
  assert cols[7] in allowed,(i,cols[7])
  quoted=re.fullmatch('“(.*)”',cols[3])
  assert quoted,(i,cols[3])
  quote=quoted[1]
  assert len(quote.split())<=25,(i,len(quote.split()))
  original=ROOT/'sources'/f'{name}.{ext}'
  extracted=original.with_suffix('.md' if ext=='pdf' else '.txt')
  assert original.stat().st_size>10000,(sid,'empty/error original')
  if ext=='pdf': assert original.read_bytes().startswith(b'%PDF'),sid
  relative=extracted.relative_to(ROOT).as_posix()
  command=['rg','--fixed-strings','--line-number','--',quote,relative]
  proc=subprocess.run(command,cwd=ROOT,capture_output=True,encoding='utf-8')
  assert proc.returncode==0,(cols[0],proc.stderr,quote)
  matches=proc.stdout.splitlines()
  nums=[m.split(':',1)[0] for m in matches]
  result=dict(id=cols[0],source=sid,quote=quote,source_text=relative,line_numbers=nums,exit_code=proc.returncode,command=command,match_count=len(matches),quote_words=len(quote.split()))
  results.append(result)
  manifest.append(dict(source=sid,url=url,original=original.relative_to(ROOT).as_posix(),text=relative,bytes=original.stat().st_size,sha256=hashlib.sha256(original.read_bytes()).hexdigest(),text_sha256=hashlib.sha256(extracted.read_bytes()).hexdigest()))
  print(f'{cols[0]} PASS: {relative}:{",".join(nums)} exit=0 matches={len(matches)} quote_words={len(quote.split())}')
 (ROOT/'sources'/'manifest-A-selected.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
 (ROOT/'sources'/'quote-verification-A.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
 appendix=['','검증 명령: `python -X utf8 verify_claims_A.py` (작업 폴더에서 실행). 각 행의 실제 `rg` 인자와 인용문은 `sources/quote-verification-A.json`에 보존한다.','','| ID | 대조 파일 | 일치 줄 | rg exit code | 결과 |','|---|---|---|---|---|']
 for r in results:
  appendix.append(f'| {r["id"]} | `{r["source_text"]}` | {", ".join(r["line_numbers"])} | {r["exit_code"]} | PASS — 직접 인용문 전체 일치 |')
 appendix+=['','**결과: 9/9 인용문 전체 일치, 0건 누락.** 9개 원본 파일과 변환 텍스트의 SHA-256을 기록했다. 이는 인용문 존재 확인이며 실험 재현이나 Physical AI 성능 검증은 아니다.','']
 marker='<!-- QUOTE_VERIFICATION_A -->'
 assert marker in text
 DOC.write_text(text.split(marker)[0]+marker+'\n'+'\n'.join(appendix),encoding='utf-8')
 print('Table valid: 9 rows, 9 columns, allowed verdicts only. Selected primary sources: 9.')

if __name__=='__main__':main()
