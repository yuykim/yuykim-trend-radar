# yuykim-trend-radar Implementation Plan

> **For agentic workers:** Executed by my-team, wave by wave. Implement only your own task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 근거를 확인하며 현재 연구 동향과 새로운 기술 후보를 발견하는 개인용 Physical AI 레이더를 만든다.

**Architecture:** 서버는 없다. GitHub Actions에서 Python batch가 수집·분석·Gemini 요약을 수행해 SQLite(`data/radar.db`)에 이력을 저장하고, 정적 JSON을 export한다. React 정적 사이트가 이 JSON을 읽어 요약→상세와 zoom graph를 제공하며 GitHub Pages로 배포한다. 리뷰·관심 저장은 브라우저 localStorage에 둔다. 규칙 기반 순위화로 시작하고 실제 추가 발견 가치를 측정한다.

**Tech Stack:** Python, SQLite, pytest, google-genai(Gemini API); GitHub Actions, GitHub Pages; React, TypeScript, Vite, Cytoscape.js, Vitest, Playwright. 구현 시 공식 호환성을 확인해 버전과 lockfile을 고정한다.

**Spec:** [기술 트렌드 레이더 설계](../specs/2026-10-18-tech-trend-radar.md). 근거: [결론](../../research/2026-10-18-tech-trend-radar/conclusion.md), [claims](../../research/2026-10-18-tech-trend-radar/claims.md).

## Global Constraints

- 초기 도메인은 Physical AI, 사용자는 개인 1명이다.
- 주가 예측·자동매매·주문 API는 구현 범위 밖이다.
- 프로젝트·repo 이름은 `yuykim-trend-radar`이고 public repo다.
- 갱신 기준은 매일 07:00 Asia/Seoul(cron `0 22 * * *` UTC)이며 `workflow_dispatch`로 수동 갱신을 지원한다.
- 서버 프로세스는 없다. 배포물은 정적 파일뿐이다.
- 화면 디자인과 흐름은 `prototype/`을 따른다.
- LLM 요약은 Gemini API 무료 tier(Flash 계열, 모델명은 구현 시 공식 문서로 확인해 `config/llm.yml`에 고정)를 쓴다. key 이름은 `GEMINI_API_KEY`이며 로컬은 `.env`, CI는 GitHub secret에서만 읽는다. LLM이 실패·비활성이어도 원문 기반 화면은 동작해야 한다.
- 미확인 값은 null/unknown, 수집 누락은 missing으로 보존한다.
- 모든 후보와 관계는 source URL·기준 시점·검토 상태로 추적할 수 있어야 한다.
- API secret은 batch 환경변수에서만 읽고 frontend·site data·로그·fixture·commit에 포함하지 않는다.
- 초기 유료 API·hosting 결제는 하지 않는다.
- 로컬 개발·검증은 Windows PowerShell에서, 운영은 GitHub Actions(ubuntu-latest)에서 실행 가능해야 한다.

## Waves

Wave 1: Task 1 — 저장 모델·공통 계약.
Wave 2: Task 2, Task 3 — 공통 계약을 이용한 수집과 후보 분석을 각각 fixture로 개발.
Wave 3: Task 4 — 수집·분석 결과에 LLM 요약을 붙여 정적 JSON으로 export.
Wave 4: Task 5, Task 6 — Task 5가 package·의존성·공통 API 타입을 먼저 준비한 뒤 Task 6을 시작한다. 이후 확정된 API와 graph JSON을 바탕으로 담당 화면 영역을 병렬 구현한다.
Wave 5: Task 7 — 화면 통합·전향 평가·GitHub Actions/Pages 운영. 여기까지 1차 MVP.
Wave 6: Task 8 — 1차 평가 후 선택적 커뮤니티·기업·주가 확장.

같은 wave의 파일 소유권은 겹치지 않는다. 다만 Wave 4에는 Task 5→Task 6의 환경 준비 의존성이 있다. Task 5가 package·의존성·공통 API 타입 준비 완료를 알린 뒤 Task 6이 구현·검증을 시작하며, Task 6은 해당 공통 파일을 수정하지 않는다. Task 5는 graph 영역에 placeholder만 두고 Task 7에서 Task 6의 component를 연결한다. 로컬 git 저장소(main)는 이미 있다. GitHub repo 생성·push는 Task 7에서 사용자 확인 후 수행한다.

## Review Focus

1. 논문 버전/학회 재출판 중복 → 논문 수가 부풀지 않아야 한다(Task 2).
2. 소스 장애·표본 부족 → 관심 하락/0으로 표시하지 않아야 한다(Task 3·5).
3. 나중에 얻은 인용/분류 → 과거 예측에 섞이지 않아야 한다(Task 1·3).
4. seed에 없는 새 약어와 동명이의어 → 새 후보를 찾되 자동 병합하지 않아야 한다(Task 3).
5. Gemini 무료 한도 초과(429)·응답 실패 → 요약만 비고 batch·배포는 성공해야 하며, 같은 문서를 다시 요약하지 않아야 한다(Task 4).
6. zoom·레이어 변경과 시세 결측 → 선택·출처를 유지하고 잘못된 기술 edge를 만들지 않아야 한다(Task 6·8).

## 공통 계약과 파일 구조

`backend/radar/contracts.py`에 Pydantic 모델을 정의하고 JSON 필드 이름을 고정한다. ID는 문자열이며 timestamp는 timezone 포함 ISO 8601 UTC, nullable 시각은 명시적으로 null이다.

- `Document`: id, source, source_id, canonical_id, title, abstract, url, version, published_at, first_public_at, observed_at, available_at, status(preprint/accepted/retracted/unknown).
- `Observation`: entity_id, metric, value(number|null), available_at, observed_at, source, coverage_id, state(ok/missing/unknown).
- `EvidenceEdge`: id, source_id, target_id, relation, evidence_url, evidence_location, available_at, review_status(proposed/verified/rejected).
- `SourceRun`: source, started_at, finished_at, status(ok/partial/failed/disabled), coverage_id, item_count, error_code.
- `Trend`: entity_id, count_28d, share_28d, share_change, support(ok/low_support/missing), coverage_id, evidence_ids.
- `Candidate`: id, entity_id, kind(new_term/new_cluster/new_combination/rename_or_alias), first_seen_at, reasons, evidence_ids, review_status.
- `Review`: candidate_id, reviewed_at, already_known, relevant, distinct, useful, minutes_spent.
- `GraphPayload`: nodes(id,label,type), edges(EvidenceEdge), generated_at.
- `DashboardPayload`: as_of, trends, candidates, community_candidates, growth_watchlist, source_runs.
- `TopicDetail`: entity_id, label, aliases, documents, observations, evidence_edges, limitations.

동일한 계약을 frontend/src/api/types.ts 에 수동으로 반영하고, API fixture schema test로 차이를 감지한다.

파일 구조는 backend/radar/{contracts,storage,collectors,analysis,export,llm,cli}, frontend/src/{api,dashboard,detail,graph}, config, tests, scripts 로 구성한다. 각 Task의 Files에 담당 파일을 나열한다.

### Task 1: 시각·근거·리뷰 저장

**Wave:** 1 · **Depends on:** none

**Files:** Create `backend/pyproject.toml`, `backend/radar/__init__.py`, `backend/radar/contracts.py`, `backend/radar/storage.py`, `tests/test_storage.py`, `tests/fixtures/documents.json`, `config/topics.yml`, `config/sources.yml`, `config/llm.yml`, `.env.example`(`GEMINI_API_KEY=` 포함, 값 없음); Modify `.gitignore`.

**Interfaces:** Produces `Repository(db_path: str)` with `upsert_document(doc: Document) -> None`, `list_documents(cutoff: datetime) -> list[Document]`, `save_observations(items: list[Observation]) -> None`, `save_run(run: SourceRun) -> None`, `save_review(review: Review) -> None`, `list_reviews() -> list[Review]`, `save_edges(edges: list[EvidenceEdge]) -> None`, `list_edges(cutoff: datetime) -> list[EvidenceEdge]`, `list_observations(cutoff: datetime) -> list[Observation]`, `list_runs() -> list[SourceRun]`.

- [ ] `test_cutoff_excludes_late_features` 작성: available_at이 cutoff 다음 날인 논문·Observation·edge는 조회 결과가 0건, cutoff 당일이면 1건이어야 한다. available_at이 null인 항목은 과거 평가에서 제외한다.
- [ ] `python -m pytest tests/test_storage.py -q` 를 실행해 미구현으로 인한 실패를 확인한다.
- [ ] 공통 계약·SQLite migration·transaction을 구현한다. 리뷰가 완료된 fixture 30건을 만들고 synthetic/retrospective 여부를 명시한다. config에 seed, 동의어, 미검증 venue, 예산·후보 수 상한을 등록한다.
- [ ] 동일한 canonical_id의 버전을 보존하고 중복 없는 문헌 집계가 가능하도록 한다. 리뷰와 원문 근거의 이력을 보존한다.
- [ ] 같은 명령으로 PASS를 확인한다. .env/.db/log/cache가 git 대상에서 제외되는지 확인하고 secret이 없는 파일만 명시해 로컬 commit한다.

### Task 2: 논문 수집과 coverage

**Wave:** 2 · **Depends on:** 1

**Files:** Create `backend/radar/collectors/{__init__,base,arxiv,openreview,openalex,normalize}.py`, `tests/test_collectors.py`, `tests/fixtures/{arxiv,openreview,openalex}.json`, `config/venue-coverage.yml`.

**Interfaces:** Consumes Task 1 contracts. Produces `collect(source: str, since: datetime, cutoff: datetime) -> tuple[list[Document], SourceRun]`, `canonicalize(documents: list[Document]) -> list[Document]`.

- [ ] `test_preprint_and_venue_version_count_once` 는 arXiv 버전과 학회 버전을 canonical_id로 1건으로 집계하고 각 버전의 공개일을 보존하는지 assert한다. `test_partial_fetch_not_empty_success` 는 중간 페이지 실패가 partial로 기록되며 빈 성공으로 처리되지 않는지 assert한다.
- [ ] `python -m pytest tests/test_collectors.py -q` 로 미구현으로 인한 실패를 확인한다.
- [ ] arXiv의 넓은 cs.RO/인접 범위 수집과 seed 검색을 구분한다. 공통 limiter는 3초당 1회·동시 연결 1개로 제한한다. OpenReview의 venue/API 버전은 manifest에 명시하고 OpenAlex 무료 예산을 초과하기 전에 중단한다. 페이지 실패·429는 횟수가 제한된 재시도와 checkpoint로 처리한다.
- [ ] 인증 없는 공개 데이터 또는 기존에 허용된 key로 각 source에 소량 GET을 수행하고, 일시·건수·사용 필드만 기록한다. key가 설정되지 않았다면 disabled로 종료하고 가상의 성공을 기록하지 않는다.
- [ ] fixture 검증 PASS를 확인하고 실제 연결 성공과 미검증 상태를 구분해 기록한 뒤 담당 파일만 commit한다.

### Task 3: 현재 트렌드와 알려지지 않은 후보

**Wave:** 2 · **Depends on:** 1

**Files:** Create `backend/radar/analysis/{__init__,trends,discovery,evaluation}.py`, `tests/test_trends.py`, `tests/test_discovery.py`, `tests/test_evaluation.py`.

**Interfaces:** Produces `compute_trends(documents: list[Document], observations: list[Observation], cutoff: datetime) -> list[Trend]`, `discover(documents: list[Document], known_aliases: dict[str,list[str]], cutoff: datetime) -> list[Candidate]`, `evaluate(candidates: list[Candidate], baseline: list[Candidate], reviews: list[Review]) -> dict`.

- [ ] `test_share_denominator_same_coverage` 는 동일한 coverage 내 대상 2건/전체 10건일 때 share_28d=0.2, coverage 변경 시 share_change=null인지 assert한다. `test_missing_is_not_decline` 은 source 누락 시 missing, 4건일 때 low_support인지 assert한다.
- [ ] `test_unknown_term_is_candidate_not_alias` 는 seed 밖에서 반복되는 full-name/약어 쌍을 new_term 후보로 만들고, 같은 약어의 다른 의미를 자동 병합하지 않는지 assert한다. `test_future_feature_ignored` 는 cutoff 이후 관측을 추가해도 순위가 바뀌지 않는지 assert한다.
- [ ] `python -m pytest tests/test_trends.py tests/test_discovery.py tests/test_evaluation.py -q` 로 미구현으로 인한 실패를 확인한다.
- [ ] 최근 28일과 직전 28일의 share·건수를 산출하고, 신규 용어와 공기 쌍의 증가를 초기 후보로 근거 문서와 함께 제시한다. 미할당 문서의 가벼운 TF-IDF 유사도 cluster도 후보에 포함하되 신기술로 확정하지 않는다. 작은 표본은 제거하지 않고 경고한다. 임계값 3/5/10의 민감도를 비교한다.
- [ ] `test_unmatched_baseline_has_no_invented_lead` 는 baseline에서 발견되지 않은 후보의 lead_days=null, additional_discovery=true인지 assert한다. precision@5·중복률·공통 후보의 lead 중앙값·검토 시간을 계산한다.
- [ ] 모든 테스트의 PASS와 예측 확률이 출력되지 않는 것을 확인하고 commit한다.

### Task 4: LLM 요약과 정적 JSON export

**Wave:** 3 · **Depends on:** 2, 3

**Files:** Create `backend/radar/llm.py`, `backend/radar/export.py`, `tests/test_llm.py`, `tests/test_export.py`, `tests/fixtures/site-data/{dashboard,graph}.json`, `tests/fixtures/site-data/topics/sample.json`.

**Interfaces:** Consumes Repository·collect·compute_trends·discover. Produces `summarize(candidate: Candidate, documents: list[Document], client: LLMClient | None) -> CandidateSummary | None` (CandidateSummary: why_new, difference, limitations, model, generated_at, source_document_ids), `export_site(repo: Repository, out_dir: str, as_of: datetime) -> None` → `out_dir/dashboard.json`(DashboardPayload), `out_dir/topics/{entity_id}.json`(TopicDetail), `out_dir/graph.json`(GraphPayload). Candidate·TopicDetail에 `summary: CandidateSummary | null` 필드를 추가한다(contracts.py 수정은 이 Task가 담당).

- [ ] `test_llm_disabled_returns_none` 는 `GEMINI_API_KEY` 미설정 시 None, `test_llm_429_does_not_fail_run` 은 fake client가 429를 던져도 None과 경고만 남는지, `test_summary_cached_by_document_set` 은 같은 candidate·문서 집합이면 두 번째 호출에서 client가 호출되지 않는지, `test_summary_only_cites_given_documents` 는 source_document_ids가 입력 문서의 부분집합인지 assert한다.
- [ ] `test_export_evidence_and_stale_source` 는 후보 evidence_ids의 문헌이 topic JSON에 있고 failed source의 마지막 성공 시각이 dashboard에 남는지, `test_export_contains_no_secret` 은 export 결과 전체에 env 값 문자열이 없는지, `test_empty_graph_is_valid` 는 빈 nodes/edges 배열이 출력되는지 assert한다.
- [ ] `python -m pytest tests/test_llm.py tests/test_export.py -q` 로 실패를 확인한다.
- [ ] Gemini 호출은 실행당 상한(`config/llm.yml`의 `max_calls_per_run`, 기본 30)과 요청 간 간격을 두고, 입력은 제목·abstract·URL만 보낸다. 요약은 SQLite에 캐시하고 model·generated_at을 보존해 화면에 "LLM 생성, 원문 확인 필요"를 표시할 수 있게 한다.
- [ ] PASS를 확인하고 commit한다.

### Task 5: 요약 A와 상세 B

**Wave:** 4 · **Depends on:** 4

**Files:** Create `frontend/package.json`, `frontend/index.html`, `frontend/vite.config.ts`, `frontend/tsconfig.json`, `frontend/src/{main,App}.tsx`, `frontend/src/styles.css`, `frontend/src/api/{types,client}.ts`, `frontend/src/dashboard/Dashboard.tsx`, `frontend/src/detail/TopicDetail.tsx`, `frontend/src/dashboard/Dashboard.test.tsx`, `frontend/src/detail/TopicDetail.test.tsx`. lockfile은 이 Task에서만 담당한다.

**Interfaces:** Consumes Task 4의 site data JSON 계약. `client.ts`는 `import.meta.env.BASE_URL + "data/..."`를 fetch한다. 리뷰·관심은 localStorage key `yuykim-trend-radar:reviews`, `yuykim-trend-radar:watchlist`에 저장하고 JSON export 버튼을 제공한다. Produces `App`, graph 탭 placeholder, `TopicDetail({id: string})`.

- [ ] `shows_missing_and_low_support` 는 missing을 0%로 표시하지 않는지, `opens_topic_evidence` 는 카드 선택→문헌 링크→기준 시각을 확인한다. `labels_preprint_and_unverified_summary` 는 동료심사와 본문 확인 상태의 혼동을 방지한다.
- [ ] `npm --prefix frontend test -- --run` 으로 미구현으로 인한 실패를 확인한다.
- [ ] prototype/의 시각 디자인을 옮겨 4개 영역의 요약·상세·리뷰 입력을 구현한다. LLM 요약은 출처 문서 링크와 "LLM 생성" 표시를 함께 보여준다. source 장애, 초기 데이터 부족, 빈 상태를 표시한다. 미래 성공률 수치 대신 성장 후보의 feature와 불확실성을 나열한다. LLM이 설정되지 않아도 원문과 규칙 설명이 표시되어야 한다.
- [ ] 같은 테스트와 `npm --prefix frontend run build`(Vite `base: '/yuykim-trend-radar/'`) 의 PASS를 확인하고 package/lock을 포함해 commit한다.

### Task 6: 기술·기업 graph

**Wave:** 4 · **Depends on:** 4 및 Task 5의 package·의존성·공통 API 타입 준비

**Files:** Create `frontend/src/graph/{GraphView.tsx,graphModel.ts,graphModel.test.ts,GraphView.test.tsx}`.

**Interfaces:** Consumes GraphPayload. Produces `GraphView({data: GraphPayload, onSelect: (id:string)=>void})`, `visibleGraph(data: GraphPayload, zoom: number, layers: string[]) -> GraphPayload`.

- [ ] `test_zoom_reveals_companies` 는 zoom=1.19에서 기업이 숨겨지고 1.2에서 표시되는지 assert한다. `test_layer_switch_preserves_selected_node` 는 숨겨진 노드의 선택을 detail에서 유지하는지, `test_correlation_never_becomes_technology_edge` 는 관계의 타입을 assert한다.
- [ ] Task 5의 package 준비 후 `npm --prefix frontend test -- --run src/graph` 로 미구현으로 인한 실패를 확인한다. 필요한 의존성은 Task 5에서 사전 등록한 Cytoscape.js를 사용하고 package는 편집하지 않는다.
- [ ] graph의 zoom·범례·관계 filter·근거 패널을 구현한다. 가시 노드 최대 500개 제한과 필터 적용 상태를 표시하고, 생략된 edge를 존재하지 않는 관계로 해석하지 않도록 한다. 빈 상태와 고립 노드 표시도 구현한다.
- [ ] graph 테스트 PASS를 확인하고 담당 파일만 commit한다.

### Task 7: 통합·일일 운영·가치 검증

**Wave:** 5 · **Depends on:** 5, 6

**Files:** Create `backend/radar/cli.py`, `.github/workflows/daily.yml`, `tests/test_daily_run.py`, `tests/e2e/radar.spec.ts`, `config/evaluation.yml`, `README.md`; Modify `frontend/src/App.tsx`, `frontend/package.json`.

**Interfaces:** Consumes 모든 선행 계약. Produces `python -m radar.cli run --as-of ISO8601 --out frontend/public/data`(collect→analyze→summarize→export), `python -m radar.cli evaluate --protocol config/evaluation.yml`.

- [ ] `test_resume_partial_run`, `test_as_of_is_0700_seoul`(22:00 UTC 실행이 다음날 07:00 KST as_of를 갖는지), `test_run_succeeds_without_llm` 을 작성한다. E2E는 요약→상세→graph→근거→리뷰→새로고침 후 localStorage 유지를 확인한다.
- [ ] `python -m pytest tests/test_daily_run.py -q` 와 E2E 명령으로 실패를 확인한다.
- [ ] graph 통합과 CLI를 구현한다. `daily.yml`은 `schedule: cron '0 22 * * *'`, `workflow_dispatch`, `concurrency`(중복 실행 방지)를 갖고 test → `radar.cli run` → `data/radar.db` commit(bot) → frontend build → `actions/deploy-pages` 순으로 수행한다. secret은 `secrets.GEMINI_API_KEY`로만 주입하고 로그에 출력하지 않는다.
- [ ] config/evaluation.yml에 4주, 후보 하루 최대 5건, baseline, spec의 Go 기준 5개 항목을 고정한다. 전향 평가 시작일, score를 가린 리뷰, sample 부족 시 inconclusive를 기록한다.
- [ ] 전체 pytest, frontend unit, build, Playwright E2E를 로컬에서 실행한다. 사용자 확인 후 `gh repo create yuykim-trend-radar --public`, push, Pages(source: GitHub Actions) 활성화, `GEMINI_API_KEY` secret 등록을 수행하고 README에 절차를 적는다. push 전 `.env`가 tracked되지 않았는지 확인하고, `workflow_dispatch` 1회 실행으로 배포 URL을 확인한다.

### Task 8: 평가 후 선택적 확장

**Wave:** 6 · **Depends on:** 7 및 1차 평가 판단

**Files:** Create `backend/radar/collectors/{hn,bluesky,toss}.py`, `backend/radar/analysis/{community,companies,correlation}.py`, `tests/test_enrichment.py`, `config/company-seeds.yml`; Modify `backend/radar/export.py`, `frontend/src/detail/TopicDetail.tsx`.

**Interfaces:** Produces `community_candidates(documents: list[Document]) -> list[Candidate]`, `company_edges(documents: list[Document]) -> list[EvidenceEdge]`, `correlate(returns_by_security: dict[str,list[Observation]], window: int=120, min_overlap: int=60) -> list[EvidenceEdge]`.

- [ ] API 권한·비용·데이터 저장 조건을 소량 read-only 연결로 확인한다. 미확인 connector는 disabled로 둔다. HN/Bluesky는 관련 비율과 추가 후보 수, Reddit/Threads는 자격·권한을 먼저 확인한다.
- [ ] `test_reposts_do_not_count_as_independent`, `test_affiliation_not_adoption`, `test_correlation_requires_60_aligned_returns` 를 작성한다. 조정 방식이 unknown이거나 서로 다른 통화·시장을 정렬하지 않고 비교한 경우 edge가 생성되지 않는지 assert한다.
- [ ] `python -m pytest tests/test_enrichment.py -q` 로 미구현으로 인한 실패를 확인한다.
- [ ] 원본 게시물·자동 배포·독립적인 논의를 구분하고 기업 관계는 수동 확인한 seed에서 확장한다. 토스의 sector/candle 조회만 구현한다. 토스 API는 허용 IP 등록이 필요해 GitHub Actions의 유동 IP에서는 동작하지 않으므로 로컬 수동 실행 전용으로 두고 결과만 commit한다. 계산은 120거래일/최소 60일·수정종가의 일간 수익률로 계산한다. 기업 ID와 증권 ID의 혼동을 방지한다.
- [ ] 테스트·관련 frontend 테스트·build를 실행한다. 추가 가치가 없는 source를 제외하는 판단도 기록하고 commit한다. 주문 기능은 추가하지 않는다.

## 계획 자기점검

- A→B, graph, 알려지지 않은 기술 탐색, 시간순 평가, 기업·주가의 보조적 역할을 각 Task에 연결했다.
- 현재 관심도·신규 후보·미래 성장 target을 구분하고 미래 예측 성능은 구현 완료 조건에 포함하지 않았다.
- 같은 wave의 담당 파일은 겹치지 않는다. 다만 Wave 4의 Task 6은 실행 환경 준비를 위해 Task 5의 package 생성을 기다려야 하므로 완전히 독립적이지 않다. graph 계약은 Task 4에서 고정된다.
- Go 기준은 사용자 가치를 위한 제안 임계값이며 논문에서 얻은 실증값이 아니다. 4주가 끝나기 전에 성공을 선언하지 않는다.
- 서버·Windows Task Scheduler를 제거하고 GitHub Actions/Pages로 대체했다. LLM 실패는 batch 실패로 이어지지 않는다(Task 4·7).
