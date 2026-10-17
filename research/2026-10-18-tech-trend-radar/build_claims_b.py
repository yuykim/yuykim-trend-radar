from pathlib import Path
from bs4 import BeautifulSoup
import re,json,subprocess,hashlib

ROOT=Path(__file__).parent
S=ROOT/'sources'

def normalize(text):
    text=BeautifulSoup(text,'html.parser').get_text(' ')
    text=text.replace('**','').replace('_','')
    return re.sub(r'\s+',' ',text).strip()

sources={
'S01':('B-S01-eysenbach','Can Tweets Predict Citations? Metrics of Social Impact Based on Twitter and Correlation with Traditional Metrics of Scientific Impact','10.2196/jmir.2012','https://pmc.ncbi.nlm.nih.gov/articles/PMC3278109/'),
'S02':('B-S02-haustein','Tweeting biomedicine: an analysis of tweets and citations in the biomedical literature','10.1002/asi.23101; arXiv:1308.1838','https://arxiv.org/abs/1308.1838'),
'S03':('B-S03-bots','Tweets as impact indicators: Examining the implications of automated bot accounts on Twitter','arXiv:1410.4139','https://arxiv.org/abs/1410.4139'),
'S04':('B-S04-x-pricing','X API pay-per-usage pricing and credits','DOI/arXiv 해당 없음: X 공식 문서','https://docs.x.com/x-api/getting-started/pricing'),
'S05':('B-S05-reddit-2023','Key Facts to Understanding Reddit’s Recent API Updates','DOI/arXiv 해당 없음: Reddit 공식 발표','https://redditinc.com/news/apifacts'),
'S06':('B-S06-reddit-current','Reddit Data API Wiki','DOI/arXiv 해당 없음: Reddit 공식 문서','https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki'),
'S07':('B-S07-bloom','The Diffusion of Disruptive Technologies','10.3386/w28999; 2021-11 revision','https://www.nber.org/system/files/working_papers/w28999/revisions/w28999.rev1.pdf'),
'S08':('B-S08-mantegna','Hierarchical Structure in Financial Markets','arXiv:cond-mat/9802256; 10.1007/s100510050929','https://arxiv.org/abs/cond-mat/9802256'),
'S09':('B-S09-etf','Competition for Attention in the ETF Space','10.3386/w28369; 2022-01 revision','https://www.nber.org/papers/w28369'),
'S10':('B-S10-code','Papers with code or without code? Impact of GitHub repository usability on the diffusion of machine learning research','10.1016/j.ipm.2023.103477; 저자 재수록본 Ch. 3, 저장소 DOI 10.6082/uchicago.12860','https://knowledge.uchicago.edu/records/eeeh9-3vv62'),
}

rows=[]
def add(sid,section,claim,quote,experiment,difference,verdict,reason):
    rows.append(dict(id=f'B{len(rows)+1:02}',sid=sid,section=section,claim=claim,quote=quote,experiment=experiment,difference=difference,verdict=verdict,reason=reason))

add('S01','Abstract—Conclusions; Results—Binary Analysis; Table 2',
    'Q4: 초기 Twitter 언급으로 향후 고인용 논문을 식별한 결과가 있다.',
    'Tweets can predict highly cited articles within the first 3 days of article publication.',
    'JMIR 단일 저널 55편·1,573 tweets, 출판 후 초기 언급과 17~29개월 뒤 Scopus/Google Scholar 인용 비교. 고인용/고언급은 표본 내 상대 분류.',
    '의학·2009~2010년 소표본이며 Physical AI·현재 X/Reddit·신기술 단위 예측이 아니다.',
    '조건부 적용','초기 관심의 후보 발견 경로로 제한하고 계정·내용을 확인할 때만 적용한다. Physical AI의 향후 영향력에 대한 예측 성능이나 기존 논문 신호 대비 증분 가치는 별도 시간순 검증이 필요하다.')
add('S01','Abstract—Results',
    'Q4 반대 증거: 동일 연구에서도 Scopus 인용 및 순위 상관에서는 관계가 덜 명확했다.',
    'less clear for Scopus citations and rank correlations.',
    'B01과 같은 표본에서 인용 DB·상관계수 종류를 바꾸어 비교.',
    '우리는 OpenAlex 인용 및 기술 단위 집계를 사용할 예정으로 평가 기준이 다시 다르다.',
    '조건부 적용','긍정적 예측 결과는 metric에 민감하다. 우리 데이터에서 metric과 예측 기간을 먼저 고정하고 검증해야 한다.')
add('S02','Abstract; Methods—Analysis; Table 1; Conclusion',
    'Q4 반대 증거: 대규모 생의학 표본에서 tweets와 인용의 상관은 낮아 동일한 영향력 지표로 볼 수 없다.',
    'correlations between tweets and citations are low',
    '2010~2012년 PubMed∩WoS 1,431,576건, Altmetric.com tweets. 기간 편향을 줄인 주 분석은 2011년 논문, WoS 인용과 Spearman 상관.',
    '현재 Physical AI의 분야별 표본이 아니며 Reddit·Threads는 평가하지 않았다.',
    '조건부 적용','소셜 관심과 학술 인용을 별도 표시할 근거다. 낮은 상관 자체가 추가 예측력이나 예측력 부재를 증명하지는 않는다.')
add('S03','Conclusion and Future Directions; Table 1',
    'Q4 반대 증거: 식별한 자동 계정만으로도 분석 대상 arXiv tweets의 최소 9%를 차지했다.',
    'at least amount to 9% of tweets',
    '2012년 arXiv 제출물 중 WoS 저널에 출판된 논문의 tweets; 계정 분석은 51개 arXiv 관련 계정. 모든 Twitter 계정에 대한 비율이 아니다.',
    '현대 Physical AI·X/Reddit의 bot 비율 및 악의적 조작 비율은 측정하지 않았다.',
    '조건부 적용','자동 배포가 관심도 집계를 부풀릴 수 있다는 위험에 적용한다. 9%를 현재 데이터의 보정 계수로 사용해서는 안 된다.')
add('S03','Results and Discussion—Figure 2; Table 1',
    'Q4/Q6: 당시 일반 bot 탐지기는 논문 자동 배포 계정의 상당수를 bot으로 판별하지 못했다.',
    'Only three accounts were considered more likely to be bots than humans.',
    '51개 arXiv 관련 계정에 Truthy Bot or Not? 점수를 적용; bot 확률이 인간보다 높은 계정은 3개.',
    '2014년 탐지기 결과이므로 현재 bot 탐지기의 정확도로 이전할 수 없다.',
    '조건부 적용','계정 유형·원문과의 중복·실제 논의 여부를 확인하는 보완 절차가 필요하다는 근거다. 현행 탐지기의 정확도는 별도로 측정해야 한다.')
add('S04','How it works; Credit consumption details—Read operations',
    'Q4 수집 제약: 현재 X API는 사용량 기반 유료 모델이며 일반 Post 읽기는 자원당 $0.005로 명시된다.',
    'The X API uses pay-per-usage pricing. / Posts: Read $0.005 per resource',
    '실험 아님. 2026-10-18 조회 공식 문서; read는 반환 자원당 과금, 월 Post 읽기 상한 300만. 계정·endpoint별 차이 존재.',
    '개인 프로젝트이며 고가 유료 데이터 없음. 본인 데이터의 Owned Reads와 외부 기술 게시물 검색은 다르다.',
    '그대로 적용','X를 무료 상시 수집원으로 전제할 수 없다. 현재 가격표만 확인했으며 2023년 당시 요금의 증거로 소급하지 않는다.')
add('S05','Key dates for our API Terms and Services',
    'Q4 수집 제약: Reddit은 2023-07-01부터 높은 사용량을 요구하는 제삼자 앱에 1,000 API calls당 $0.24 요금을 발표했다.',
    'the rate for third-party apps that require higher usage limits is $0.24 per 1K API calls.',
    '실험 아님. 2023년 공식 발표. 무료 한도는 당시 OAuth client id당 100 QPM, 비인증 10 QPM으로 안내.',
    '역사적 도입 정책이며 현재 개인 앱의 승인·유료 계약 조건을 확정하지 않는다.',
    '조건부 적용','2023년 변경 이력에만 적용한다. 현재 접근 가능성은 B08의 최신 문서와 실제 앱의 자격을 함께 확인해야 한다.')
add('S06','Rate Limits',
    'Q4 수집 제약: Reddit 현재 무료 접근 자격이 있는 OAuth client의 한도는 100 QPM이며 비인증 트래픽은 차단된다.',
    '100 queries per minute (QPM) per OAuth client id / Traffic not using OAuth or login credentials will be blocked',
    '실험 아님. 공식 Wiki 조회 2026-10-18; 무료 접근 자격자 대상, QPM은 10분 창 평균. HTML은 Reddit 공식 help-center API 응답의 article.body.',
    '신규 개인 앱이 무료 접근 자격·승인을 이미 얻었다는 정보는 scope.md에 없다.',
    '조건부 적용','무료 접근 자격과 OAuth 인증이 확보될 때 적용한다. 2023년 비인증 10 QPM을 현재도 사용할 수 있다고 해석하면 안 된다.')
add('S07','Abstract; §2 Data Construction; Data Appendix §1.2 Patents',
    'Q5/Q6: 특허·채용 공고·earnings calls의 text-based exposure measure로 기술의 기업 확산을 추적한 실증 사례가 있다.',
    'We identify novel technologies using textual analysis of patents, job postings, and earnings calls.',
    '2021-11판, 미국 29개 disruptive technologies. USPTO 1976~2016년 특허, 2002~2019년 earnings calls, 채용 공고. 특허 assignee를 Compustat 기업에 연결.',
    '우리는 무료 논문/API 중심; EIKON·Burning Glass·Compustat 대규모 자료가 없고 Physical AI의 신흥 기술을 매일 본다.',
    '조건부 적용','출처·날짜·관계 유형을 보존한 특허/기업 기술 언급 연결의 방법론적 근거다. 동일 규모 재현이나 논문 저자 소속만으로 실제 도입을 판정하는 근거는 아니다.')
add('S07','Data Appendix §2.5 Grouping bigrams into technologies',
    'Q5 반대 증거: 기술 표현을 자동으로 묶는 절차에는 약 10~20% false positive가 보고되었다.',
    'a false positive rate of about 10-20%.',
    '검색 결과 및 earnings calls·특허·Wikipedia embedding 기반 자동 bigram grouping. 최종 기술 분류에는 수동 검토를 사용.',
    '우리 World Model·VLA·JEPA 용어의 자동 연결 정확도를 직접 측정한 결과가 아니다.',
    '조건부 적용','소수 기술로 시작하는 우리 조건에서는 용어·기업 연결의 수동 검토 필요성을 뒷받침한다. 10~20%를 우리 시스템 예상 오류율로 옮기지는 않는다.')
add('S07','§2.2 Use of technical bigrams in earnings calls',
    'Q5/Q6 반대 증거: 이 연구의 기술 선택을 그대로 실시간 조기 탐지 성능의 증거로 사용할 수 없다.',
    'peak year',
    '전체 표본에서 peak year 빈도가 2002년 대비 최소 10배인 bigram을 선택하고 특허 인용 threshold를 사용한 사후 분류.',
    '우리는 매일 당시까지 공개된 정보만으로 새 기술을 인지해야 한다.',
    '적용 불가','미래를 포함하는 표본 전체의 peak와 누적 인용을 사용하는 절차이므로 그대로는 실시간 탐지 검증이 아니다. 이는 연구 방법과 우리 시점 조건을 비교한 판단이며 저자의 실패 보고가 아니다.')
add('S08','Abstract; 본문 Fig. 1–3 (번호 없는 본문)',
    'Q5: 일별 주가 수익률 상관으로 만든 MST/clustering이 경제적으로 의미 있는 기업 분류를 드러낼 수 있다.',
    'a meaningful economic taxonomy.',
    '1989-07~1995-10, DJIA 및 전체 기간 S&P500 잔류 443종목. 일별 log 수익률 상관→거리→minimum spanning tree, Forbes 산업 분류와 비교.',
    '과거 미국 대형주·긴 관측창이며 현대 Physical AI 관련 기업·매일 바뀌는 좁은 집합이 아니다.',
    '조건부 적용','관측창·표본·거래일 정렬을 명시하는 참고 관계망으로 적용할 수 있다. 기술 채택이나 미래 수익률의 증거로 해석하지 않는다.')
add('S08','본문 Fig. 3 이후 해석 및 결론 (번호 없는 본문)',
    'Q5 반대 증거: co-movement에는 기업별·기업군별 경제 요인이 반영되므로 이를 곧바로 공통 기술 관계로 해석할 수 없다.',
    'economic factors which are specific to the considered group',
    '동일 주가 표본에서 금광 기업군 등 특정 경제 요인과 전체 시장 공통 요인을 해석. 기술 연결 정답과의 검증은 아님.',
    '우리 graph에는 논문·특허 근거의 기술 연결도 함께 들어간다.',
    '그대로 적용','주가 상관 edge와 기술 근거 edge를 구별해야 한다는 해석에 적용한다. 이 논문이 Physical AI 연결망의 유용성이나 사용자 편익을 직접 검증한 것은 아니다.')
add('S09','Abstract; Fig. 2 Performance of ETFs Around Launch',
    'Q5 반대 증거: specialized ETF는 출시 후 첫 5년간 약 30%의 누적 risk-adjusted 저성과를 보였다.',
    'over their first five years, specialized ETFs lose about 30% in risk-adjusted terms.',
    '2000~2019년 출시 주변 성과, calendar-time portfolios·가치 가중 및 Fama–French–Carhart 4-factor alpha. specialized는 sector/industry와 thematic을 포함.',
    '순수 Physical AI ETF만의 결과도, 모든 시기·국가의 테마 투자 결과도 아니다. 우리 목적은 기술 탐색이며 투자 판단은 부차적.',
    '조건부 적용','인기 있는 기술 테마가 투자 초과성과를 보장하지 않는다는 반대 증거다. 30%를 우리 관심 기업의 예상 손실이나 기술 전망으로 사용하지 않는다.')
add('S09','Abstract; Introduction',
    'Q5: ETF 저성과의 해석은 높은 수수료만이 아니라 출시 당시 기초 주식의 과대평가와 연결된다.',
    'overvaluation of the underlying stocks',
    'B14와 같은 연구; 수수료·hedging demand 설명을 검토한 뒤 출시 시점 과대평가와 attention 경쟁으로 해석.',
    '개별 기업·오늘의 Physical AI 밸류에이션을 측정하지 않았다.',
    '조건부 적용','소셜 관심·기술 성장과 투자 매력도를 동일시하지 않을 근거다. 실제 매매 판단이나 오늘의 과대평가 판정은 이 결과로 도출할 수 없다.')
add('S10','저자 재수록 Ch. 3 Abstract; Analysis I—Impact of First Repository on Paper Citation Rate',
    'Q6: 첫 GitHub repository 공개 뒤 ML 논문의 월별 인용률이 약 20% 높아지는 추정 결과가 있다.',
    'papers enjoy approximately 20% advantages in monthly citation rates',
    'PwC 2014-11~2022-05 표본 20,000편 중 GitHub 연결 19,109편·39,782 repositories. MAG 인용, nearest-neighbor matching 및 paper/age fixed effects Poisson 모형.',
    '관측 연구·일반 ML 표본이며 Physical AI 기술의 미래 성공이나 GitHub stars 증가율을 검증한 것은 아니다.',
    '조건부 적용','코드 링크·최초 공개일을 추가할 근거로 사용한다. 약 20%는 이 표본의 추정치이며 개별 논문 예측값이나 공개의 보장된 인과효과로 쓰지 않는다.')
add('S10','저자 재수록 Ch. 3 Abstract; Analysis II; Discussion and Conclusion',
    'Q6 반대 증거: ML framework의 인기도도 인용률과 연결되어 코드 기반 관심을 기술 우수성으로만 해석하기 어렵다.',
    'could influence the monthly citation rate for papers.',
    '첫 repository에서 사용하는 framework의 월별 PwC implementation share와 인용을 분석; 주 변화는 TensorFlow↔PyTorch.',
    'GitHub stars 인기도나 Physical AI 실사용·산업 확산 측정과는 다르다.',
    '조건부 적용','framework 접근성과 생태계 인기를 기술 성능과 구별할 때 적용한다. 인용·코드 공개 한 지표로 기술적 우수성을 단정하지 않는다.')
add('S10','저자 재수록 Ch. 3 Discussion and Conclusion—Limitations',
    'Q6 반대 증거: PwC 표본 기반 추정 효과의 크기는 데이터 출처에 따라 달라질 수 있다.',
    'estimated effect sizes may vary',
    '저자 자체 한계 진술; PwC-indexed ML papers와 GitHub에 분석 범위를 제한. 여기서 인용한 것은 다른 논문 결과가 아닌 본 연구의 일반화 한계.',
    '우리는 OpenReview/OpenAlex/arXiv 수집이고 새 분야·코드 미공개 논문도 포함한다.',
    '조건부 적용','우리 수집원에서 코드 공개의 추가 탐색 가치를 다시 검증해야 한다. PwC의 과거 연구 데이터 사용이 현재 PwC 서비스/API의 가용성을 입증하지 않는다.')

def main():
    # PDF는 먼저 pdf-to-md 스킬로 변환했다. 검색용 정규화는 줄바꿈/서식만 제거한다.
    for sid,(stem,*_) in sources.items():
        original=S/(stem+('.md' if (S/(stem+'.pdf')).exists() else '.txt'))
        (S/(stem+'.search.txt')).write_text(normalize(original.read_text(encoding='utf-8')),encoding='utf-8')
    checks=[]
    for r in rows:
        stem=sources[r['sid']][0]; search=S/(stem+'.search.txt')
        # slash는 여러 독립된 원문 발췌를 구분한다. 문장으로 이어 붙이지 않는다.
        for quote in r['quote'].split(' / '):
            out=subprocess.run(['rg','-n','-F','-o','--',quote,str(search)],capture_output=True,text=True,encoding='utf-8')
            checks.append({'id':r['id'],'file':search.name,'quote':quote,'status':'PASS' if out.returncode==0 else 'FAIL','match':out.stdout.strip()})
    failures=[x for x in checks if x['status']=='FAIL']
    if failures: print(json.dumps(failures,ensure_ascii=False,indent=2));raise SystemExit(1)
    header='''# Q4~Q6 1차 자료 claim 검증 B

기준: [scope.md](scope.md)의 개인 1명·Physical AI·무료 API 중심·매일 아침 탐색 조건. 조사일: 2026-10-18. 연구 7건과 공식 API 정책 자료 3건, 총 10건을 사용했다. 관측 연구의 인용 예측과 기술의 미래 성공, 기업의 실제 채택, 투자 성과는 서로 다른 결과변수다.

직접 인용문은 영어 원문 그대로이며 짧은 연속 발췌도 포함한다. ` / `는 서로 떨어진 발췌를 구분하며 원문에 없는 연결 문장을 만들지 않는다. 모든 자료는 sources/에 저장한 신뢰할 수 없는 외부 데이터로 취급했고 실행하지 않았다. PDF는 로컬 텍스트 변환만 수행했다. 정규화 검색본은 HTML/Markdown 서식과 줄바꿈만 제거했으며 수치·철자·문구는 바꾸지 않았다.

| ID | 주장 | 출처 | 직접 인용문 | 1차/2차 | 실험 조건 | 우리 조건과의 차이 | 판정 | 판정 근거 |
|---|---|---|---|---|---|---|---|---|
'''
    lines=[]
    for r in rows:
        stem,title,doi,url=sources[r['sid']]
        local=stem+('.pdf' if (S/(stem+'.pdf')).exists() else '.html')
        source=f'[{title}]({url}); {doi}; {r["section"]}; [{r["sid"]}](sources/{local})'
        vals=[r['id'],r['claim'],source,'“'+r['quote']+'”','1차（정책 자료는 발행 주체의 직접 명세）' if r['sid'] in ['S04','S05','S06'] else '1차',r['experiment'],r['difference'],r['verdict'],r['reason']]
        lines.append('| '+' | '.join(x.replace('|','\\|') for x in vals)+' |')
    tail='''

## 확인 범위와 제외한 주장

- Reddit/Threads 언급의 향후 인용 예측, GitHub stars 자체의 증분 예측력, 산업 저자 **비중**의 예측력은 이번 10건에서 직접 확인하지 못했다. 직접 인용할 실증 결과가 없어 claim 표에 넣지 않았고, 이 조사 기준 **확인 불가**다. 기업 저자 소속은 연구 생산 관계를 뜻할 수 있지만 채택·매출·특허 소유의 증거로 승격하지 않는다.
- Kogan et al.의 labor exposure 연구는 검색 단계에서 확인했지만 최종 10건 corpus에는 포함하지 않았다. 다른 논문이 요약한 해당 결과를 재인용하지 않았으며 그 결과의 우리 조건 적용은 **확인 불가**다. Q5의 text-based exposure 및 특허-기업 연결은 직접 읽은 Bloom et al. 원문으로 한정했다.
- X의 현재 사용량 과금은 공식 문서에서 확인했다. 2023년 최초 유료화 시점·당시 tier별 금액은 이번 저장 원문만으로 확정하지 않아 claim으로 채택하지 않았다. Reddit은 2023년 발표와 현재 Wiki를 별도 보존했다.
- 소셜의 인용 대비 시간적 선행은 B01의 출판 직후 신호에 한정한다. 출판 전 선행, 기술 단위 조기 탐지, 현재 인용·저자 신호 대비 out-of-sample 증분 예측력은 이 결과로 확인되지 않는다. 코드 공개 연구의 repository 생성일도 실제 코드 최초 공개일·재현 성공일과 동일하다고 보장되지 않는다.
- 코드 공개·framework 사용·특허 연결은 추가 메타데이터 후보로 뒷받침되지만, 우리 대시보드나 graph view가 사용자 편익을 높인다는 직접 실험은 아니다. 기술 간 관계와 기업 관계의 출처·관계 유형·날짜를 분리하는 제안은 위 조건 비교에서 도출한 설계 판단이다.
- 2차 결과를 그대로 채택한 행은 없다. S10은 저자 학위논문 Chapter 3의 원 논문 재수록본으로 확인했다. PwC 편향에 대한 외부 연구의 요약은 별도 empirical claim으로 사용하지 않았다.

## 저장 자료와 재현 정보

원문 URL·최종 URL·다운로드 시점 응답 헤더·SHA-256·파일 크기: [B-manifest.json](sources/B-manifest.json). 다운로드 코드와 검증 코드는 외부 자료와 분리한 로컬 작성 파일이다. S06은 공식 help-center API의 article.body HTML을 저장했으며 전체 웹페이지 HTML을 저장한 것과 구별한다. S01은 JMIR 다운로드의 빈 응답을 사용하지 않고 PMC 원문으로 교체했다. S10은 이전된 공식 대학 저장소의 PDF다.

소셜 신호 일반화에 대한 찬성·비판 2라운드 및 독립 판정: [B01-social.md](debate/B01-social.md). B01의 최종 조건은 후보 발견 경로로 한정하며 Physical AI 미래 영향력의 검증된 예측기로 인정하지 않는다.

## 인용문 grep 대조 결과

명령: `rg -n -F -o -- <직접 인용문> sources/<원문 stem>.search.txt`. 원문을 먼저 로컬에 저장하고 PDF→Markdown 변환 후, 서식·공백만 정규화한 검색본에서 전체 발췌 문자열을 고정 문자열로 대조했다. 아래 결과는 최종 실행의 실제 반환값이다. 정규화 검색본은 원문이 아니라 대조 편의를 위한 파생 파일이며 원문 PDF/HTML은 별도 보존한다.

| ID | 대조 파일 | 결과 |
|---|---|---|
'''
    for r in rows:
        matched=[x for x in checks if x['id']==r['id']]
        tail+=f'| {r["id"]} | [검색본](sources/{matched[0]["file"]}) | PASS {len(matched)}/{len(matched)}; rg exit 0 |\n'
    tail+=f'\n합계: **{len(rows)}개 claim, {len(checks)}개 연속 발췌 전부 PASS, 불일치 0개**. 대조 로그: [B-quote-check.json](sources/B-quote-check.json). `grep` 일치는 인용문 존재만 확인하며 연구 설계의 타당성이나 Physical AI 예측 성능을 보증하지 않는다.\n'
    (ROOT/'claims-B.md').write_text(header+'\n'.join(lines)+tail,encoding='utf-8')
    (S/'B-quote-check.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'WROTE claims-B.md: {len(rows)} claims; {len(checks)} exact excerpts PASS; 10 primary sources')

if __name__=='__main__':main()
