# 기술 트렌드 레이더 API·데이터 소스 조사

조사 기준일: 2026-10-18 (Asia/Seoul). 먼저 같은 폴더의 `scope.md`를 읽고 평가했다. 개인 1명, 무료·저가, 매일 아침 갱신, Physical AI(Robotics, Robot Learning, VLA, World Model, JEPA)부터 시작한다. 기술 동향·신기술 조기 인지가 주목적이며 기업·주가 연결은 참고 정보다.

## 조사·판정 기준

- 공식 문서·가격표·약관·운영자 저장소를 직접 열어 확인했다. 검색에 잡힌 내용과 실제 페이지가 달랐던 경우 실제 페이지를 우선하고 차이를 기록했다. 링크는 각 행에 남겼다.
- **확인 불가**는 문서 미기재, JavaScript 화면에서 본문 추출 실패, 접근 오류, 또는 계정별 권한을 시험하지 못한 경우다. 기능이 없다는 뜻은 아니다. 인증키 발급·유료 가입·실제 인증 API 호출은 하지 않았다.
- 적합성은 작성자의 평가다. **상**: 좁은 Physical AI 도메인의 일일 수집에 직접 유용. **중**: 보조 자료이거나 접근·비용·범위 제약. **하**: 초기 예산·접근성에 맞지 않음. 기능 존재와 무료 이용 가능 여부는 별개다.
- 가격은 USD, 별도 표기된 원화는 KRW다. 월간·연간 결제를 구분했다. 호출 한도와 데이터 이용권, 저장권, 재배포권을 동일시하지 않는다. 약관상 허용을 확인하지 못했으면 비고에 명시했다.
- API 명세를 확인한 사실은 현재 서버의 정상 작동, 수집 완전성, 과거 데이터의 정확성을 보장하지 않는다. 아래 수집 방식·MVP·위험 대응은 조사 결과를 바탕으로 한 설계 제안이다.

## 1. 종목-테마·섹터 분류

### 1-1. 국내

| 이름 | 제공 데이터 | 무료 한도/가격 | 인증 | 우리 용도 적합성(상/중/하) | 공식 문서 URL | 비고(제약, ToS 상 저장/재배포 제한) |
| --- | --- | --- | --- | --- | --- | --- |
| KRX 정보데이터시스템(Data Marketplace) | 시장 통계 UI. 종목별 업종 분류·ETF 구성종목 다운로드의 구체적인 현행 메뉴/필드: 확인 불가 | 웹·데이터 상품별 가격: 확인 불가 | 메뉴별 인증: 확인 불가 | 중 | [정보데이터시스템](https://data.krx.co.kr/), [OPEN API 서비스 소개](https://openapi.krx.co.kr/contents/OPP/INFO/OPPINFO001.jsp) | 첫 화면의 본문 추출 실패. 웹 다운로드와 공식 OPEN API를 구분해야 한다. UI 내부 요청을 공개 API로 간주하지 않는다. 이 경로의 자동수집·저장·재배포 허용: 확인 불가 |
| KRX OPEN API | 공식 목록에서 주식·지수·증권상품의 일별 통계 확인. 기술 테마 분류/기업별 업종 필드/ETF holdings 전용 API: 확인 불가 | 키당 10,000회/일. 확인한 소개·약관에 명시적 요금표 없음 → 무료 여부/가격 확인 불가 | 회원가입·API 인증키 신청, 이용기간 1년·연장 | 중 | [서비스 목록](https://openapi.krx.co.kr/contents/OPP/INFO/service/OPPINFO004.cmd), [이용약관](https://openapi.krx.co.kr/contents/OPP/INFO/OPPINFO002.jsp) | 비상업적 이용만 허용, 제3자 제공 금지, 화면에 한국거래소 통계정보 사용 명시. 계약 종료 후 이용 불가. 과거 조회 가능과 무제한 영구 보관권은 다름 |
| 금융위원회 기업기본정보(공공데이터포털) | 기업개요의 업종·주요 사업, 법인등록번호, 계열회사·연결대상 종속기업. 기술 테마 라벨 API: 확인 불가 | 무료, 개발계정 신청 가능 트래픽 10,000; 일일 한도 초과 오류 명시. 운영 증설 신청 가능 | 활용신청 후 serviceKey | 상 | [기업기본정보 V2](https://www.data.go.kr/data/15043184/openapi.do) | 포털에 이용허락범위 제한 없음. 설명상 기준일 다음 영업일 13시 이후 갱신. 법인과 종목 연결을 별도로 해야 함. 주식시세 API의 제한을 이 데이터에 그대로 적용하지 않음 |
| DART OpenAPI 기업개황·고유번호 | `company.json`의 `induty_code`, 회사명·종목코드·법인등록번호. `corpCode.xml`의 corp_code↔stock_code | 호출 상한 오류 설명에 일반적으로 20,000건 이상, 키별 다를 수 있음. 해당 명세에 가격·정확한 초기화 주기 미기재 → 확인 불가 | 40자리 crtfc_key | 상 | [기업개황](https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS001&apiId=2019002), [고유번호](https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS001&apiId=2019018), [약관](https://opendart.fss.or.kr/intro/terms.do) | 업종코드를 Physical AI 테마로 변환하는 규칙은 직접 만들어야 함. 기술 테마 전용 조회 확인 불가. 원문·첨부물의 무제한 저장/재배포 허용 확인 불가 |
| 한국투자증권 KIS Developers | 국내업종 현재·일자별·기간별 지수, 구분별 전체시세; 해외 업종별코드·시세. 기술 테마 그룹/구성종목 전용 기능 확인 불가 | 공식 API 목록에서 이용료·현행 TPS 확인 불가 | 계좌 개설·ID 연결·Open API 신청 → App Key/App Secret 발급·REST 접근토큰 | 중 | [공식 API 서비스 목록](https://apiportal.koreainvestment.com/apiservice), [공식 신청·인증 가이드](https://github.com/koreainvestment/open-trading-api) | 업종 지수 조회가 회사별 산업/테마 라벨 전체 제공을 뜻하지 않음. 테마와 업종 구분 필요. 제3자 표시·저장·재배포 조건 확인 불가 |
| 키움 REST API | `ka90001` 테마그룹별요청, `ka90002` 테마구성종목요청. `ka10106` 인포스탁 테마코드·`ka10107` 테마상세 종목리스트, 업종 API도 목록에 존재 | 실전 테마·인포스탁 이용료와 현행 TPS: 확인 불가. 무료 모의투자 안내를 실전 테마 무료 근거로 사용하지 않음 | OAuth Client Credentials, appkey·secretkey → token | 상 | [공식 API 가이드](https://openapi.kiwoom.com/m/guide/apiguide?dummyVal=0), [모의투자 안내](https://openapi.kiwoom.com/intro/mockInvestInfo?dummyVal=0) | 국내 테마 후보 수집에 직접적. TR 존재까지 확인, 테마별 실제 목록·모의 지원·인포스탁 계약 조건 확인 불가. 테마 원자료 저장/재배포 허용 확인 불가 |
| 토스증권 Open API Sector | 자체 산업 분류 3계층, 한 종목의 복수 섹터 소속. `/api/v1/sectors`, `/{sectorId}/stocks`, `/{sectorId}/etfs`, 상세·랭킹 | 가이드 표 SECTOR 최대 5회/초, 응답 헤더가 현재 한도. API 이용료·무료 월간 한도 확인 불가 | 토스 계좌·WTS 클라이언트 등록, OAuth Client Credentials, 허용 IP | 상 | [공식 가이드](https://developers.tossinvest.com/), [공식 OpenAPI JSON v1.2.24](https://openapi.tossinvest.com/openapi-docs/latest/openapi.json), [서비스 안내](https://home.tossinvest.com/ko/open-api) | JSON으로 기능 직접 확인. GICS와 다른 자체 산업 분류. 관련 ETF 목록은 ETF 구성종목 목록이 아님. VLA/JEPA 섹터 존재·섹터별 국내/미국 완전성·저장/재배포 허용 확인 불가 |

### 1-2. 해외 및 ETF holdings

| 이름 | 제공 데이터 | 무료 한도/가격 | 인증 | 우리 용도 적합성(상/중/하) | 공식 문서 URL | 비고(제약, ToS 상 저장/재배포 제한) |
| --- | --- | --- | --- | --- | --- | --- |
| GICS(MSCI/S&P DJI) | Sector → Industry Group → Industry → Sub-Industry, 주된 사업 기준 회사별 분류 | 체계 설명은 공개. 회사별 전체 분류 데이터의 무료 API·라이선스 가격 확인 불가 | 데이터 계약·전달 방식 확인 불가 | 중 | [MSCI GICS 공식 설명](https://www.msci.com/indexes/index-resources/gics) | 한 회사에 각 계층의 단일 분류. VLA/World Model 같은 기술 테마와 일치하지 않음. 공개 분류 정의를 회사별 전체 데이터의 저장/재배포 허용 근거로 사용할 수 없음 |
| Financial Modeling Prep(FMP) | company profile의 industry, sector/industry 목록·screener. `/stable/etf/holdings` 구성종목·비중, ETF sector/country weightings | Basic 무료 250회/일. Starter 월 $19(연간 결제), 표의 월간 정가 $29. ETF holdings의 무료 권한 및 최소 유료 티어 확인 불가 | API key, 헤더 또는 apikey 파라미터 | 중 | [API 문서](https://site.financialmodelingprep.com/developer/docs), [가격표](https://site.financialmodelingprep.com/developer/docs/pricing) | 글로벌 기능 명시, 국내 개별 종목·필드 완전성 확인 불가. Personal/Commercial 요금 구분. 원자료 영구 저장·재배포 허용 확인 불가 |
| Polygon / Massive | Massive 공식 ticker overview의 `sic_code`, `sic_description`, 회사 설명·CIK·FIGI. 기술 테마·ETF holdings 전용 API 확인 불가 | Stocks Basic $0, 5회/분. Starter $29/월 | API key | 중 | [Ticker overview](https://massive.com/docs/rest/stocks/tickers/ticker-overview), [가격표](https://massive.com/pricing) | 이 조사에서는 Massive 현행 문서 기준. SIC를 GICS로 기록하면 안 됨. 미국 주식 중심. ETF 자체 시세와 holdings는 별개. 개인용 요금의 저장·재배포 범위 확인 불가 |
| Alpha Vantage | `OVERVIEW` 기업 정보; `ETF_PROFILE` ETF 지표·holdings·자산/섹터 배분 | 일반 무료 25회/일. 검증된 오픈소스·교육 프로젝트 무제한 제공 안내 있으나 승인 대상 여부 확인 불가. ETF_PROFILE의 계정별 권한 미시험 | apikey | 중 | [공식 API 문서](https://www.alphavantage.co/documentation/), [무료 한도](https://www.alphavantage.co/support/) | 문서에 ETF holdings 기능 확인. BOTZ/ROBO 개별 지원 확인 불가. 저장·재배포 범위 확인 불가 |
| EODHD Fundamentals | Sector·Industry 및 GicSector/GicGroup/GicIndustry/GicSubIndustry. ETF_Data에 Holdings·Top_10_Holdings·Sector_Weights | 무료 20 API calls/일, 20요청/분. Fundamentals $59.99/월. fundamentals 요청은 10 calls 차감; 무료에서 모든 fundamentals 사용 가능 여부 확인 불가 | api_token | 중 | [Fundamentals 명세](https://eodhd.com/financial-apis/stock-etfs-fundamental-data-feeds), [가격표](https://eodhd.com/pricing) | 공급자 GICS 필드가 MSCI 직접 라이선스나 재배포권까지 보장하지 않음. 개인/상업용 구분, 구체 저장·재배포 허용 확인 불가 |
| Finnhub | 공식 Python SDK에서 company_profile2·etfs_holdings, 글로벌 fundamentals·ETF holdings 제공 확인. 세부 업종 응답 스키마 확인 불가 | 공식 가격표 본문 추출 실패 → 무료 한도·현재 유료 가격 확인 불가. 과거의 60회/분 주장을 현행 수치로 사용하지 않음 | API key, 공식 문서는 token 또는 X-Finnhub-Token 안내 | 중 | [공식 SDK](https://github.com/Finnhub-Stock-API/finnhub-python), [API](https://finnhub.io/docs/api), [가격표](https://finnhub.io/pricing), [인증 설명](https://www.finnhub.io/docs/api/country) | SDK에 기능이 있어도 무료 entitlement를 뜻하지 않음. ETF holdings·한국시장 권한·저장/재배포 범위 확인 불가 |
| yfinance(비공식 Yahoo 접근) | Ticker.info·Sector/Industry API, funds_data.top_holdings 등 | 라이브러리 무료. Yahoo가 보장한 무료 호출 한도/가용성 확인 불가 | 일반 공개 조회에 별도 사용자 API key 절차 없음 | 중 | [프로젝트 문서](https://ranaroussi.github.io/yfinance/), [API reference](https://ranaroussi.github.io/yfinance/reference/index.html) | Yahoo의 공식 API 상품이 아님. 프로젝트가 연구·교육 및 Yahoo 데이터 개인 이용을 명시. `top_holdings`를 전체 holdings로 취급하지 않음. 데이터 저장/재배포 권한은 Yahoo 약관에 따름 |
| Global X BOTZ 운용사 공개 holdings | holdings 날짜, 기업명·ticker·SEDOL·비중, Full CSV 다운로드 표시 | 웹 열람에 가격 표시 없음. 공식 자동수집 API·호출 한도 확인 불가 | 공개 페이지 무인증 | 상 | [BOTZ 공식 상품·holdings](https://www.globalxetfs.com/funds/botz) | 2026-10-16 기준 표시 확인. 테마 후보군 초기화에 유용. 공개 다운로드가 자동수집·재배포 허가를 뜻하지 않음; 저장·재배포 약관 확인 불가 |
| ROBO Global Robotics & Automation Index ETF | holdings 날짜, 기업명·ticker·FIGI·주식수·시장가치·비중, CSV 다운로드 표시 | 웹 열람에 가격 표시 없음. 공식 자동수집 API·호출 한도 확인 불가 | 공개 페이지 무인증 | 상 | [ROBO 공식 상품·holdings](https://www.roboglobaletfs.com/robo) | 페이지에 2026-10-15 기준 표시. 비상장 연구기업 포함 보장 없음. 저장·자동수집·재배포 약관 확인 불가 |

### ETF로 테마-기업을 연결하는 방법 — 설계 제안

1. BOTZ·ROBO를 각각 하나의 **운용사 정의 테마 후보군**으로 등록한다. 상품 설명과 holdings 기준일·수집일·원본 URL을 함께 기록한다. 전체 CSV 다운로드를 먼저 소규모로 검토한다.
2. holdings의 ticker와 거래소·ISIN/SEDOL/FIGI 등 확인 가능한 식별자로 회사와 증권을 구분한다. `6954 JP` 같은 운용사 ticker를 미국 ticker로 해석하지 않는다. 식별자가 없거나 불일치하면 확인 불가로 남긴다.
3. 기업 연결에는 `ETF 편입`이라는 근거 유형을 붙인다. 편입 비중을 그 기업의 기술 역량·기술 매출 비중·연구 영향력으로 해석하지 않는다. VLA·JEPA·World Model 연결에는 논문 소속·공시·특허라는 별도 증거가 필요하다.
4. 같은 기업이 여러 ETF에 포함돼도 회사 노드는 하나로 통합하고 편입 관계·비중·기준일은 별개로 보관한다. 과거 편입 구성 조회/보관 권한을 확인하지 못한 ETF는 현재 스냅샷을 과거 시점에 소급하지 않는다.
5. 저장·자동수집 권한이 확인되기 전에는 원문 링크와 수동 검토를 우선한다. API로 전환하면 FMP/Alpha Vantage/EODHD의 해당 ETF 지원과 holdings entitlement를 실제 키로 검증한다.

## 2. 주가·시계열

분류 데이터와 시세의 상품 권한은 별개다. 일일 참고 화면에는 일봉이 우선이며 실시간 데이터는 필수가 아니다.

| 이름 | 제공 데이터 | 무료 한도/가격 | 인증 | 우리 용도 적합성(상/중/하) | 공식 문서 URL | 비고(제약, ToS 상 저장/재배포 제한) |
| --- | --- | --- | --- | --- | --- | --- |
| KRX OPEN API | 국내 유가증권·코스닥·코넥스 일별 매매, 지수·ETF/ETN 시세. 목록에 2010년 이후 제공 안내. 해외 개별주식 미확인 | 10,000회/일/키. 가격 확인 불가 | API 인증키 | 중 | [서비스 목록](https://openapi.krx.co.kr/contents/OPP/INFO/service/OPPINFO004.cmd), [약관](https://openapi.krx.co.kr/contents/OPP/INFO/OPPINFO002.jsp) | 비상업적 이용·제3자 제공 금지·계약 종료 후 이용 불가. 수정주가/배당 반영의 상세 확인 불가 |
| 금융위원회 주식시세정보 | 국내 주식·수익증권·신주인수권 시가·고가·저가·종가·거래량. 해외 주식 제공 확인 불가 | 무료, 개발계정 10,000, 운영 증설 신청 가능 | 활용신청·serviceKey | 중 | [주식시세정보](https://www.data.go.kr/data/15094808/openapi.do) | 설명을 우선: **다음 영업일 13시 이후** 갱신. 메타데이터의 실시간 표기와 충돌. 공공누리 4유형(출처·비상업·변경금지), 제3자 무단 제공/재배포 금지. 아침에 전일 종가가 없을 수 있음 |
| 한국투자증권 | 국내 기간별시세·분봉, 해외 기간별시세·분봉·환율. 해외 업종별 시세도 목록에 존재 | 현재 무료 한도·이용료·실전/모의 TPS 확인 불가 | 계좌·ID 연결·API 신청 후 App Key/App Secret·REST 접근토큰 | 중 | [공식 API 목록](https://apiportal.koreainvestment.com/apiservice), [공식 인증 가이드](https://github.com/koreainvestment/open-trading-api) | 개별 해외 거래소·지연시간·최장 과거 조회 범위·수정주가·저장/재배포 조건 확인 불가 |
| 키움 REST API | 국내 일·주·월·년봉(ka10081/82/83/94), 업종 일봉(ka20006). 공식 목록에 미국주식 시세·차트 카테고리 존재 | 실전 시세 요금·현재 TPS 확인 불가. 모의투자 무료, 미국 모의 시세 무료 실시간 명시 | OAuth token | 중 | [API 가이드](https://openapi.kiwoom.com/m/guide/apiguide?dummyVal=0), [모의투자 범위](https://openapi.kiwoom.com/intro/mockInvestInfo?dummyVal=0) | 미국 모의 NYSE/NASDAQ/AMEX 한정. 실전 해외 범위·시계열 길이·저장/재배포 허용 확인 불가. 구형 Windows OCX와 현행 REST를 혼동하지 않음 |
| 토스증권 Open API | 국내·미국 현재가·OHLCV, `/api/v1/candles`에 1m/1d, count 최대 200, before/nextBefore 페이지네이션, adjusted 기본 true | 가이드 표 MARKET_DATA 최대 15회/초, CHART 20회/초; 실제 응답 헤더 우선. 이용료·월간 무료 한도 확인 불가 | OAuth Client Credentials·허용 IP | 상 | [공식 JSON 명세](https://openapi.tossinvest.com/openapi-docs/latest/openapi.json), [가이드](https://developers.tossinvest.com/) | 소수 관심종목의 일봉에 우선 검토. 전체 과거 보존기간·수정주가의 배당 처리 방식·저장/재배포 허용 확인 불가 |
| FMP | 글로벌 quote·historical chart/EOD. 한국 개별 종목 커버리지 확인 불가 | Basic 무료 250회/일, 가격표에 5년 EOD. Starter $19/월(연간 결제), 300회/분 | API key | 중 | [문서](https://site.financialmodelingprep.com/developer/docs), [가격표](https://site.financialmodelingprep.com/developer/docs/pricing) | Basic의 종목별 허용·각 endpoint 권한 확인 불가. 데이터 표시·저장·재배포 허용 확인 불가 |
| Massive | 미국 전체 주식 ticker, Basic EOD·분봉 집계·2년 이력. 한국 주식 제공 확인 불가 | Basic $0, 5회/분; Starter $29/월 | API key | 상 | [가격·포함 데이터](https://massive.com/pricing) | 일일 미국 소수 종목 참고용. 무료 실시간으로 해석하지 않음. 개인용 요금이며 재배포/영구 저장 허용 확인 불가 |
| Alpha Vantage | 글로벌 일봉·기타 주기, 미국·영국·캐나다·독일·인도·중국 예시. 한국 커버리지 확인 불가 | 무료 일반 25회/일. 미국 실시간·15분 지연 및 DAILY_ADJUSTED는 premium. 유료 현행 가격 확인 불가 | apikey | 중 | [문서](https://www.alphavantage.co/documentation/), [한도](https://www.alphavantage.co/support/) | compact/full·수정주가의 유료 구분 필요. 25회/일을 25종목 이상 전체 데이터 무료로 해석하지 않음. 저장/재배포 허용 확인 불가 |
| EODHD | All-World EOD, intraday 상품. 공식 한국 종목 페이지에서 `.KO`, OperatingMIC XKRX 확인 | 무료 20 calls/일·20요청/분. EOD $19.99/월, EOD+Intraday $29.99/월. EOD 1 call, intraday 5 calls | api_token | 중 | [가격표](https://eodhd.com/pricing), [한국 종목 예시](https://eodhd.com/financial-summary/007810.KO) | 무료 계정의 한국시장 이용권·시계열 길이 확인 불가. 환율·분할·배당 조정 선택 필요. 저장/재배포 허용 확인 불가 |
| Finnhub | 공식 SDK의 stock_candles·quote, 글로벌 시장 데이터 기능 | 가격표 추출 실패, 현행 무료 candles 권한·한도·유료 가격 확인 불가 | API key | 중 | [공식 SDK](https://github.com/Finnhub-Stock-API/finnhub-python), [가격표](https://finnhub.io/pricing) | quote 무료 여부를 candles 무료 근거로 사용할 수 없음. 국내 커버리지·저장/재배포 허용 확인 불가 |
| yfinance | history·download 시계열; Yahoo 심볼에 의존한 시장별 조회 | 라이브러리 무료, 보장된 요청량 없음 | 일반 조회 사용자 API key 불필요 | 중 | [프로젝트 문서](https://ranaroussi.github.io/yfinance/), [API reference](https://ranaroussi.github.io/yfinance/reference/index.html) | 한국시장 개별 종목의 현행 가용성·완전성 확인 불가. 개인 연구용 대안, 429·스키마 변경 위험. Yahoo 공식 제공 계약으로 볼 수 없으며 저장/재배포 권리 별도 |
| DART / 금융위 기업기본정보 / GICS | 기업·공시·분류 자료. 확인한 명세에 OHLCV 제공 없음 | 주가 조회에는 해당 없음 | 각 서비스 기준 | 하 | [DART 기업개황](https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS001&apiId=2019002), [기업기본정보](https://www.data.go.kr/data/15043184/openapi.do), [GICS](https://www.msci.com/indexes/index-resources/gics) | 분류 소스를 시세 소스로 간주하지 않음 |

## 3. 기술·연구 정보

| 이름 | 제공 데이터 | 무료 한도/가격 | 인증 | 우리 용도 적합성(상/중/하) | 공식 문서 URL | 비고(제약, ToS 상 저장/재배포 제한) |
| --- | --- | --- | --- | --- | --- | --- |
| OpenAlex | works·인용·authorships·institutions·topics. Concepts는 deprecated, Topics 사용 권고. works에 날짜·topic·기관 필터 및 집계 | 무료 key $1/일, list/filter $0.10/1,000호출, search $1/1,000호출. 무키 10회/초·무료 key 30회/초, per_page 최대 100. 초과분 prepaid | 가벼운 무인증 가능, cursor 첫 페이지 이후는 무료 API key 필요 | 상 | [API](https://help.openalex.org/api/), [인증·한도](https://help.openalex.org/api/authentication/), [가격](https://help.openalex.org/access/pricing/), [작업별 비용](https://help.openalex.org/access/example-costs/), [폐기 예정 기능](https://help.openalex.org/api/deprecations/) | 메타데이터 CC0. 논문 원문 저작권과 별개. 예전 100,000회/일·mailto polite pool 전제를 쓰지 않음. 최신 인증 문서를 과거 안내보다 우선 |
| Semantic Scholar Academic Graph | 논문·저자·인용·venue·SPECTER2 embedding, 추천 논문, datasets | 공개 API 기본 이용 가능. 무인증 전체 사용자 공유 1,000 RPS, 개인 key 초기 1 RPS. 별도 유료 가격 확인 불가 | 일부 무인증, 일부 key 필요; key 사용 권고 | 상 | [공식 API 소개](https://webflow.semanticscholar.org/product/api), [Graph reference](https://api.semanticscholar.org/api-docs/graph), [API license](https://webflow.semanticscholar.org/product/api/license) | 공유 1,000 RPS는 사용자별 보장량이 아님. 출처 표시, 데이터별 CC BY-NC·ODC-BY 등 및 제3자 원문 라이선스 적용. 하나의 개방 라이선스로 일괄 처리 금지 |
| arXiv API | Atom XML, title/abstract/author/category/날짜 검색·정렬·페이지네이션. Physical AI 초기 논문 발견 | legacy API는 **3초당 최대 1요청·동시 연결 1개**. 일반 사용의 별도 이용료 확인 불가 | 공개 API key 요구 없음 | 상 | [API manual](https://info.arxiv.org/help/api/user-manual.html), [API ToU](https://info.arxiv.org/help/api/tou.html) | 서지 메타데이터 저장·변환·공유 허용 명시. 원문은 개인·연구 사용과 논문별 라이선스 구분. PDF를 API처럼 대량 재배포하지 않음 |
| OpenReview API 2 / legacy API 1 | 학회 submissions·notes·리뷰·결정 등 접근권한 있는 데이터. API 1은 일부 과거 학회에 남아 있고 단계적 폐기 | 사용법 문서에 구체 무료 quota·TPS·가격 미기재 → 확인 불가 | 현행 문서상 OpenReview 계정, 사이트와 같은 자격증명·권한 | 상 | [Using the API](https://docs.openreview.net/getting-started/using-the-api) | API 1/2의 JSON 차이. 비공개 리뷰·익명 저자 소속은 접근 불가할 수 있음. 학회별 공개 범위·저장/재배포 조건 확인 불가 |
| Papers with Code: 기존 사이트·데이터 | 기존 `paperswithcode.com`을 열면 Hugging Face Trending Papers로 redirect. 기존 운영자 저장소에 논문-코드·평가 데이터 export 안내 | 공개 저장소 데이터; 작동하는 현행 legacy API·quota·가격 확인 불가 | 공개 페이지·저장소 무인증 | 하 | [기존 주소](https://paperswithcode.com/), [현재 도착 페이지](https://huggingface.co/papers/trending), [운영자 데이터 저장소](https://github.com/paperswithcode/paperswithcode-data) | 기존 사이트의 독립 제공 중단/이동은 redirect로 확인. **정확한 종료일·전체 benchmark/API 이관 완료 여부 확인 불가**. export의 현재 다운로드 성공·갱신 여부도 미시험. 저장소 데이터 CC-BY-SA |
| Hugging Face Hub API | 모델·데이터셋·Spaces 목록, downloads·likes·tags·갱신일. 공식 HfApi `list_models`·`list_datasets`에 `sort=trending_score` 확인 | Hub API 익명 500/5분/IP, Free 1,000/5분. 공식 표는 September 2025 기준이라고 표시하며 익명/무료 한도 변경 가능 명시 | 공개 조회 무인증 가능, HF_TOKEN 권장·gated/private는 권한 필요 | 상 | [Hub API](https://huggingface.co/docs/hub/api), [HfApi reference](https://huggingface.co/docs/huggingface_hub/package_reference/hf_api), [한도](https://huggingface.co/docs/hub/rate-limits) | 원시 trending 점수의 계산식·과거 이력 보장 확인 불가. 모델/데이터셋 파일은 각 저장소 라이선스·gating 적용, 메타데이터 접근과 재배포 권리는 구분 |
| GitHub REST API | repository 검색, stars·topics·생성/갱신 시각, stargazers. 검색 정렬로 인기 repo 후보 확보 | 무인증 일반 60회/시간, 인증 일반 5,000회/시간. 검색 인증 30회/분·무인증 10회/분, query당 최대 1,000결과 | 공개 일부 무인증, PAT/GitHub App 사용 가능 | 상 | [Search API](https://docs.github.com/en/rest/search/search), [Rate limits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api) | 공식 Trending 순위 API는 확인 불가. stars 정렬을 Trending과 동일시하지 않고 일일 star 스냅샷 차이를 자체 지표로 사용. 코드 재배포는 repo별 라이선스; API 메타데이터 보관 세부 ToS 확인 불가 |
| PatentsView PatentSearch API | 미국 특허·assignee·CPC 등 검색·필터 | 기존 key 45회/분, 기본 100·최대 1,000레코드/응답. **신규 key 발급 일시 중단** 명시. 별도 이용료 확인 불가 | X-Api-Key | 하 | [공식 운영자 API reference](https://github.com/PatentsView/PatentSearch-API/blob/main/docs/docs/Search%20API/SearchAPIReference.md) | 신규 개인 프로젝트가 즉시 key 발급 가능하다고 전제하지 않음. 기존 구 API와 구분. 원자료 보관·재배포 라이선스의 상세 확인 불가 |
| Google Patents / Google Patents Public Datasets | 국제 특허 검색과 BigQuery 공개 데이터. Google 공식 글에 서지·분류·assignee 및 데이터 결합 설명 | BigQuery 공개 데이터 쿼리 첫 1 TB/월 무료(공식 페이지 표기), 이후 쿼리 과금; 별도 저장·내보내기 비용 가능. 웹 검색용 공식 REST API 확인 불가 | BigQuery 프로젝트·IAM/인증. 웹 검색과 별개 | 중 | [Google Patents Public Datasets 공식 설명](https://cloud.google.com/blog/topics/public-datasets/google-patents-public-datasets-connecting-public-paid-and-private-patent-data), [BigQuery public data](https://docs.cloud.google.com/bigquery/public-data) | 테이블별 최신 갱신일·한국 데이터 완전성·데이터별 재배포 라이선스 확인 불가. 웹 검색 결과 스크래핑을 공식 API로 표현하지 않음. 쿼리 스캔 비용 제어 필요 |
| KIPRIS Plus | 국내 특허·실용 공개/등록 공보, 출원인 법인, 권리자 변경 이력 등 상품. Open API 개발 가이드 제공 | **월 1,000회 무료**, 매월 초기화. 유료 기본 일 5,320원/연 1,941,800원(VAT 포함). 2개 이하 상품 50%, 개인 등 추가 50% 할인 안내 | 상품 신청·Open API 인증키; 상품별 권한 | 중 | [공식 수수료](https://plus.kipris.or.kr/portal/use/paymentMmg.do?menuNo=200026), [공식 FAQ](https://plus.kipris.or.kr/portal/bbs/Faq_info.do?buttonIndex=&pageIndex=2), [개발 가이드 안내](https://plus.kipris.or.kr/portal/bbs/view.do?bbsId=B0000001&menuNo=210149&nttId=1060&pageIndex=1) | 월 1,000회를 일 한도로 혼동하지 않음. 무료 소진 시 자동결제 없음. 개별 API의 출원인 필드·페이지 크기·저장/재배포 조건 확인 불가. 개인 할인 실청구액은 신청 시 확인 필요 |
| Crunchbase REST API | 기업·인물·투자유치·관계, 검색·entity lookup | Sales를 통한 provisioned API key 필요. 공개 무료 quota·현재 가격 확인 불가. Enterprise 200회/분·동시 3요청 | X-cb-user-key 권고 | 하 | [공식 시작 문서](https://data.crunchbase.com/docs/welcome-to-crunchbase-data), [인증·한도·약관 안내](https://data.crunchbase.com/docs/using-the-api) | 승인·계약 필드만 접근. 기본적으로 제3자 데이터 배포 금지, 별도 계약 예외. 내부 연구에 유용하나 초기 필수 의존성으로 부적합 |
| Google Trends 공식 API alpha | 최근 약 5년, 일·주·월·연, 국가/하위 지역, 요청 간 일관된 스케일의 검색 관심도 | **제한된 alpha 신청**, 일반 공개 전환·가격·quota 확인 불가 | alpha 승인 필요, 실제 인증 방식 확인 불가 | 중 | [현행 공식 alpha 문서](https://developers.google.com/search/apis/trends), [공식 발표](https://developers.google.com/search/blog/2025/07/trends-api) | 절대 검색 건수가 아님. 승인 대기 없이 MVP에서 쓸 수 있다고 전제하지 않음. API 데이터 저장/재배포 세부 조건 확인 불가 |
| Google Trends 웹 / pytrends(비공식) | 공식 웹의 Explore·Trending now·다운로드/내보내기; pytrends는 비공식 자동 접근 | 웹 사용·수동 CSV 경로. 공식 자동수집 quota 없음. pytrends의 보장된 무료 quota 확인 불가 | 웹 기능별 로그인 조건 확인 불가 | 중 | [공식 웹](https://trends.google.com/trends/), [공식 데이터 FAQ](https://support.google.com/trends/answer/4365533?hl=en), [pytrends 프로젝트](https://github.com/GeneralMills/pytrends) | pytrends는 Google 공식 API가 아니며 저장소가 archived 상태. 상대값·표본·낮은 검색량의 0값 주의. 자동수집·장기 저장·재배포 허용 확인 불가 |

### Physical AI 수집 필터 — 설계 제안

- arXiv는 `cs.RO`와 제목·초록의 `robot learning`, `vision-language-action`, `world model`, `JEPA` 등을 조합한다. VLA 같은 약어만 사용하지 않고 정식 명칭도 검색한다. 키워드의 현재 공식 topic ID는 조회하지 않았으므로 **확인 불가**다.
- OpenAlex는 Topics와 검색어를 결합한다. 공식 문서상 `/works?filter=topics.id:T...`를 사용할 수 있고, 기업 소속 논문은 `authorships.institutions.type:company`로 제한할 수 있다. `from_publication_date` 등 날짜 조건을 사용하되 개별 query는 구현 전 실제 API 응답으로 검증한다. [Topics](https://help.openalex.org/data/topics/), [기관 type](https://help.openalex.org/data/institution-types/), [Works](https://help.openalex.org/data/works/)
- OpenReview는 관심 학회별 venue·invitation·공개 submission을 지정한다. 실제 ICLR/CoRL/RSS 등 venue ID·review 공개 시점은 이 조사에서 확인하지 않았으므로 고정값을 만들지 않는다.
- Hugging Face는 모델·데이터셋을 따로 수집하고 `trending_score`, likes, downloads의 관측일별 스냅샷을 구분한다. GitHub의 star 증가와 서로 다른 모집단의 지표라는 점을 표시한다.

## 4. 커뮤니티

| 이름 | 제공 데이터 | 무료 한도/가격 | 인증 | 우리 용도 적합성(상/중/하) | 공식 문서 URL | 비고(제약, ToS 상 저장/재배포 제한) |
| --- | --- | --- | --- | --- | --- | --- |
| Reddit Data API | 공개 게시글·댓글 등, OAuth 클라이언트 기반 접근 | 무료 자격이 있는 클라이언트는 **100 queries/분/client ID**, 현재 10분 평균. 유료·상업용 현행 단가 확인 불가 | 등록 OAuth token·고유 User-Agent, 이용 신청/정책 준수 | 중 | [현행 Data API Wiki](https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki) | 개인·비상업이라고 자동 승인되는 것은 아님. 삭제된 게시글/댓글 내용·계정 식별정보 제거 필수. 48시간 이내 정기 삭제는 **권고**이며 모든 데이터의 일률적 법정 TTL로 표현하지 않음. 원문 장기 축적이 필요한 설계와 충돌 가능 |
| X API | 게시글 검색·조회, 사용자·반응·counts 등 | 현행 문서 **구독 없이 pay-per-use**. Post read $0.005/건, User read $0.010/건; 종량제 Post read 300만/월 상한. Enterprise 별도, 가격 확인 불가 | 개발자 계정·선불 credits, endpoint별 token | 하 | [공식 가격·credits](https://docs.x.com/x-api/getting-started/pricing) | 과거 Free/Basic/Pro 월정액을 현행 티어로 제시하지 않음. 일반 검색 Post 100건/일×30일은 $15/월의 단순 계산이며 user 조회 등 추가 비용 제외. 무료 인센티브는 상시 무료 quota와 다름. 저장·삭제동기화·재배포 정책 상세 확인 불가 |
| Threads API | **키워드 검색 가능**: 공식 Meta Postman `GET /keyword_search`, q·search_type=TOP 확인; RECENT의 현행 지원 확인 불가 | 현행 무료 quota·가격·검색 호출 수 제한 확인 불가 | Meta 앱·사용자 권한 승인. 검색 요청의 OAuth scope/심사 상세는 접근한 현재 문서에서 확인 불가 | 중 | [현재 공식 검색 요청 문서](https://www.postman.com/meta/threads/request/34203612-b3b2c12a-7ce6-4d86-a3c6-6d31e3b66ea1), [공식 workspace](https://www.postman.com/meta/threads/overview), [개발자 검색 문서](https://developers.facebook.com/docs/threads/keyword-search/) | Meta 개발자 페이지는 429/추출 실패, 공식 Postman으로 기능 직접 확인. 예전 짧은 Postman URL은 현재 Request not found라 대체 URL 사용. 현재 검색 권한명·기간/완전성·저장/재배포 허용 확인 불가 |
| Hacker News Firebase API | item·comment·user, top/new/best/ask/show/job stories, updates | 공식 문서 현재 rate limit 없음. 별도 가격 표시 없음 | 공개 v0 읽기 무인증 | 상 | [공식 HN API](https://github.com/HackerNews/API) | 공식 API의 전문 키워드 검색 확인 불가. 목록→본문을 받아 Physical AI 자체 필터. 삭제/dead 반영. API 문서 라이선스와 게시글 재배포권은 별개, 원문 저장/재배포 상세 조건 확인 불가 |
| Bluesky API | 공개 posts·likes·social graph. 공식 API reference에 `app.bsky.feed.searchPosts` 존재 | public AppView의 구체 숫자 quota·가격 확인 불가. 공식 문서는 generous rate-limits 및 제한 시 문의 안내 | 공개 조회는 `public.api.bsky.app` 무인증; 사용자별 동작은 인증·PDS 경유 | 상 | [공식 HTTP API reference](https://docs.bsky.app/docs/api/app-bsky-feed-get-author-feed), [Hosts/Auth](https://bsky.network/docs/api-directory/), [Rate limits](https://bsky.network/docs/rate-limits/) | PDS의 한도를 public AppView 한도로 옮겨 적지 않음. 전체 검색 결과·과거 기간 완전성 확인 불가. 삭제·계정 변경 반영 필요. 무제한 원문 저장·재배포 권한 확인 불가 |

## 5. 기업-기술 연결

| 이름 | 제공 데이터 | 무료 한도/가격 | 인증 | 우리 용도 적합성(상/중/하) | 공식 문서 URL | 비고(제약, ToS 상 저장/재배포 제한) |
| --- | --- | --- | --- | --- | --- | --- |
| OpenAlex institutions의 company type | 기관 type `company`, works authorships의 기관, ROR 기반 유형·기관 연결 | §3 OpenAlex와 동일한 예산, 추가 독립 무료 quota 아님 | 무료 API key 권장 | 상 | [기관 type 정의·필터](https://help.openalex.org/data/institution-types/), [기관 객체](https://help.openalex.org/data/institutions/) | `/institutions?filter=type:company`, `/works?filter=authorships.institutions.type:company`. 소속은 논문 발표 시점의 관계로 해석. 상장사 ticker·모회사 자동 매핑은 제공 보장 없음. 메타데이터 CC0와 논문 원문 권리는 구분 |
| 특허 assignee: PatentsView | 미국 특허의 assignee 연결 후보 | 기존 key 45회/분, 신규 key 발급 일시 중단 | X-Api-Key | 하 | [공식 API reference](https://github.com/PatentsView/PatentSearch-API/blob/main/docs/docs/Search%20API/SearchAPIReference.md) | assignee와 연구 수행기업·현재 최종 권리자·상장 모회사는 동일하지 않을 수 있음. 현재 소유권 이전 이력을 모두 반영하는지 확인 불가. 저장/재배포 조건 확인 불가 |
| 특허 assignee/applicant: Google Patents BigQuery | 특허 서지·분류·assignee 중심 기술-기업 후보 | 공개 쿼리 첫 월 1 TB 무료 범위, 이후 과금 | Google Cloud 인증·프로젝트 | 중 | [공식 데이터 설명](https://cloud.google.com/blog/topics/public-datasets/google-patents-public-datasets-connecting-public-paid-and-private-patent-data), [쿼리 접근·비용](https://docs.cloud.google.com/bigquery/public-data) | 영문/현지명·자회사·동명이인 정규화 필요. 키워드 일치를 기술 보유 사실로 확정하지 않음. 테이블별 현행 저장/재배포 조건 확인 불가 |
| KIPRIS Plus 국내 특허·권리자 | 출원인 법인·공개/등록 공보·권리자 변경 이력 상품 | 월 1,000회 무료, 유료 요금·할인은 §3 참고 | 상품별 Open API 인증키 | 중 | [상품·수수료](https://plus.kipris.or.kr/portal/use/paymentMmg.do?menuNo=200026), [개발 가이드](https://plus.kipris.or.kr/portal/bbs/view.do?bbsId=B0000001&menuNo=210149&nttId=1060&pageIndex=1) | 발명자·출원인·등록 권리자를 구분. 특허 종류별 상세 schema·법인번호 매핑과 재배포 권한은 확인 불가 |
| SEC EDGAR: submissions API + Archives의 10-K | submissions JSON의 filing 목록에서 10-K 식별 후 원문 HTML/text를 Archives에서 수집. companyfacts는 재무 XBRL이며 10-K 사업 설명 전문이 아님 | API key 불필요, 사용자 전체 **10요청/초 이하**. 별도 사용료 표기 없음 | 무인증, 식별 가능한 자동화 요청·User-Agent | 상 | [공식 API 설명](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [Developer Resources·Fair Access](https://www.sec.gov/about/developer-resources) | 제출 이력→원문은 2단계. CIK·accession·filing date·보고기간을 보관하고 Business/R&D 등에서 근거 문장 추출. 기업의 기술 언급은 실사용·성과와 구분. 공시 첨부물의 제3자 저작물까지 일괄 재배포 허용된다고 단정하지 않음 |
| DART 사업보고서 원문 | `document.xml`로 접수번호 기반 공시 원문 ZIP. 사업보고서의 사업 내용·연구개발 등에서 기술 근거 추출 | 명세 일반 요청 제한 20,000건 이상에서 오류 가능·키별 상이. 정확한 무료 quota·가격 확인 불가 | crtfc_key·rcept_no | 상 | [원문 API](https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS001&apiId=2019003), [공시 목록](https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS001&apiId=2019001), [약관](https://opendart.fss.or.kr/intro/terms.do) | 목록에서 사업보고서·정정공시를 찾고 원문 파싱. 재무 API만으로 사업 설명 전문 확보 불가. corp_code↔종목코드 연결 필요. 장기 원문 저장·재배포 세부 허용 확인 불가 |

### 연결 근거를 저장하는 최소 구조 — 설계 제안

`technology_id`, `company_id`, `evidence_type`(논문 소속/특허 출원인/공시 언급/ETF 편입), `source_id`, `source_url`, `published_at`, `observed_at`, `valid_from`, `valid_to`, `confidence`, `license_status`를 구분한다. 회사·증권·연구기관은 같은 노드로 합치지 않고, 확인된 법인 관계를 통해 연결한다. 저장이 허용된 근거만 보관하고, 허용이 불명확한 원문은 URL 중심으로 관리한다.

## 확인 불가·추가 확인이 필요한 항목

- KRX UI의 업종/holdings 자동수집 인터페이스, OPEN API 이용료, 기업별 업종/테마 제공 여부는 확인 불가다. 확인한 공식 서비스 목록은 일별 통계 중심이다.
- 한국투자증권의 현행 무료 한도·이용료, 키움의 실전 테마 가격·TPS, 토스의 API 요금·저장/재배포 조건은 확인 불가다. 일반 거래 수수료를 데이터 API 이용료로 대체하지 않았다.
- Finnhub 동적 가격표와 세부 API 페이지의 본문은 추출하지 못했다. 공식 SDK로 기능은 확인했지만 무료 60회/분·candles/holdings 무료라는 주장은 검증하지 못해 채택하지 않았다.
- Threads 검색 기능은 현재 공식 Postman 문서로 확인했다. 과거 검색 결과에는 `threads_keyword_search` scope가 있으나 현재 직접 연 페이지에서 상세를 확보하지 못했으므로 현행 권한명·심사/한도는 확인 불가로 남겼다.
- Papers with Code의 redirect는 직접 확인했지만 종료 날짜·데이터 전체 이관·과거 API 운영 여부는 확인 불가다. legacy export는 최신성이나 다운로드 성공을 검증하지 않았다.
- 대부분의 금융·커뮤니티 데이터는 기능 문서만으로 장기 보관/재배포 권한을 확정할 수 없었다. 개인 이용 가능성을 공개 대시보드·공유 데이터셋의 허용으로 확대하지 않았다.

## 위험 요소

- **접근·과금 변경:** X는 현재 종량제, OpenAlex는 일일 달러 예산, Google Trends는 제한 alpha, PatentsView는 신규 key 발급 중단이다. 월 예산 제한·요청량 기록·429 재시도·소스 비활성화 기능을 둔다.
- **저장·재배포 제약:** KRX·금융위 주식시세는 제3자 제공 제한이 명시돼 있다. Reddit 삭제 동기화, S2 데이터별 라이선스, Yahoo 개인 이용 조건도 각각 반영한다. 약관 미확인 원문을 공통 영구 저장소에 무조건 누적하지 않는다.
- **갱신 지연과 사후 정보:** 금융위 시세는 다음 영업일 오후 제공이라 아침 전일 확인에 불리하다. 논문 인용·특허 공개·공시·ETF 리밸런싱도 관측 지연이 다르다. 발표일·기준일·수집일을 따로 저장하고 최신 데이터를 과거 시점에 소급하지 않는다.
- **표본·인기 지표 편향:** ETF는 운용사 편입 기준, GitHub/Hugging Face/소셜은 플랫폼 이용자·홍보 활동의 영향을 받는다. 소셜 언급·stars·downloads를 연구 성능이나 미래 기술 가치로 확정하지 않는다.
- **식별·분류 오류:** GICS/SIC/토스 섹터/키움 테마는 서로 다른 분류다. 기업·연구소·자회사·상장증권의 이름 일치만으로 연결하지 않는다. 로봇·World Model 같은 다의어는 수동 검토 표본으로 정밀도를 확인한다.
- **시계열 왜곡:** 통화·시간대·거래일·분할·배당·수정주가 정의·상장폐지·현재 ETF 편입종목 사용에 따라 co-movement가 달라진다. 조정 방식이 확인되지 않은 가격을 섞지 않는다. 이 프로젝트는 주가 예측을 평가 목표로 삼지 않는다.

## MVP 추천 조합

1. **논문:** arXiv + OpenReview를 일일 발견 채널로, OpenAlex Topics·인용·기관을 보강 채널로 사용한다. Semantic Scholar는 누락 보강에 선택적으로 추가한다.
2. **코드·모델:** GitHub API의 star 일일 변화 + Hugging Face 모델/데이터셋의 trending_score·likes·downloads를 추적한다.
3. **커뮤니티:** HN + Bluesky로 시작하고, Reddit·Threads는 접근권한과 보관 조건 확인 후 추가한다. X는 초기 필수 구성에서 제외한다.
4. **기업 연결:** OpenAlex company institutions + SEC 10-K/DART 사업보고서 + BOTZ/ROBO 공식 holdings를 근거 유형별로 연결한다. 특허는 KIPRIS 무료 범위부터 선택적으로 검토한다.
5. **주가·예산:** 토스 국내·미국 일봉을 계정·요금·저장 조건 확인 후 우선 사용하고, 미국 대안은 Massive Basic을 검토한다. 논문·코드 수집은 무료 범위를 우선하며 시세 조건 확인 전에는 기술 레이더만 운영한다.
