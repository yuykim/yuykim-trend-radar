# Tech Trend Radar Implementation Plan

> **For agentic workers:** Executed by my-team, wave by wave. Implement only your own task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 근거를 확인하며 현재 연구 동향과 새로운 기술 후보를 발견하는 개인용 Physical AI 레이더를 만든다.

**Architecture:** Python 수집기가 시간·출처 이력을 SQLite에 저장하고 FastAPI가 근거·후보·graph를 제공한다. React 화면은 요약→상세와 zoom graph를 제공한다. 규칙 기반 순위화로 시작하고 실제 추가 발견 가치를 측정한다.

**Tech Stack:** Python, FastAPI, SQLite, pytest; React, TypeScript, Vite, Cytoscape.js, Vitest, Playwright. 구현 시 공식 호환성을 확인해 버전과 lockfile을 고정한다.

**Spec:** [기술 트렌드 레이더 설계](../specs/2026-10-18-tech-trend-radar.md). 근거: [결론](../../research/2026-10-18-tech-trend-radar/conclusion.md), [claims](../../research/2026-10-18-tech-trend-radar/claims.md).

## Global Constraints

- 초기 도메인은 Physical AI, 사용자는 개인 1명이다.
- 주가 예측·자동매매·주문 API는 구현 범위 밖이다.
- 갱신 기준은 매일 07:00 Asia/Seoul이다.
- 미확인 값은 null/unknown, 수집 누락은 missing으로 보존한다.
- 모든 후보와 관계는 source URL·기준 시점·검토 상태로 추적할 수 있어야 한다.
- API secret은 backend 환경변수에서만 읽고 frontend·로그·fixture에 포함하지 않는다.
- 초기 유료 API·hosting 결제는 하지 않는다.
- 개발·검증은 Windows PowerShell에서 실행 가능해야 한다.

## Waves

Wave 1: Task 1 — 저장 모델·공통 계약.
Wave 2: Task 2, Task 3 — 공통 계약을 이용한 수집과 후보 분석을 각각 fixture로 개발.
Wave 3: Task 4 — 수집·분석 결과를 API로 제공.
Wave 4: Task 5, Task 6 — Task 5가 package·의존성·공통 API 타입을 먼저 준비한 뒤 Task 6을 시작한다. 이후 확정된 API와 graph JSON을 바탕으로 담당 화면 영역을 병렬 구현한다.
Wave 5: Task 7 — 화면 통합·전향 평가·Windows 운영. 여기까지 1차 MVP.
Wave 6: Task 8 — 1차 평가 후 선택적 커뮤니티·기업·주가 확장.

같은 wave의 파일 소유권은 겹치지 않는다. 다만 Wave 4에는 Task 5→Task 6의 환경 준비 의존성이 있다. Task 5가 package·의존성·공통 API 타입 준비 완료를 알린 뒤 Task 6이 구현·검증을 시작하며, Task 6은 해당 공통 파일을 수정하지 않는다. Task 5는 graph 영역에 placeholder만 두고 Task 7에서 Task 6의 component를 연결한다. git 저장소가 없으므로 Task 1에서 로컬 git 초기화·기존 .gitignore 검토 후 시작하며 원격 생성·push는 포함하지 않는다.

## Review Focus

1. 논문 버전/학회 재출판 중복 → 논문 수가 부풀지 않아야 한다(Task 2).
2. 소스 장애·표본 부족 → 관심 하락/0으로 표시하지 않아야 한다(Task 3·5).
3. 나중에 얻은 인용/분류 → 과거 예측에 섞이지 않아야 한다(Task 1·3).
4. seed에 없는 새 약어와 동명이의어 → 새 후보를 찾되 자동 병합하지 않아야 한다(Task 3).
5. zoom·레이어 변경과 시세 결측 → 선택·출처를 유지하고 잘못된 기술 edge를 만들지 않아야 한다(Task 6·8).

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

파일 구조는 backend/radar/{contracts,storage,collectors,analysis,api,cli}, frontend/src/{api,dashboard,detail,graph}, config, tests, scripts 로 구성한다. 각 Task의 Files에 담당 파일을 나열한다.

### Task 1: 시각·근거·리뷰 저장

**Wave:** 1 · **Depends on:** none

**Files:** Create `backend/pyproject.toml`, `backend/radar/__init__.py`, `backend/radar/contracts.py`, `backend/radar/storage.py`, `tests/test_storage.py`, `tests/fixtures/documents.json`, `config/topics.yml`, `config/sources.yml`, `.env.example`; Modify `.gitignore`.

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

### Task 4: 근거를 추적할 수 있는 API

**Wave:** 3 · **Depends on:** 2, 3

**Files:** Create `backend/radar/api/{__init__,app,queries}.py`, `tests/test_api.py`, `tests/fixtures/api/{dashboard,topic,graph}.json`.

**Interfaces:** Consumes Repository·collect·compute_trends·discover. Produces `GET /api/dashboard -> DashboardPayload`, `GET /api/topics/{id} -> TopicDetail`, `GET /api/graph?as_of=... -> GraphPayload`, `POST /api/reviews(Review) -> Review`, `POST /api/candidates/link` body `{url: str}` → `{status: proposed, url: str}`.

- [ ] `test_dashboard_evidence_and_stale_source` 는 후보에서 evidence_ids의 문헌을 추적할 수 있고 failed source에 마지막 성공 시각이 남는지 assert한다. `test_review_persists` 와 `test_graph_relation_provenance` 를 작성한다.
- [ ] `python -m pytest tests/test_api.py -q` 로 미구현으로 인한 실패를 확인한다.
- [ ] local-only API를 구현한다. 수동 URL 추가는 후보 등록까지만 수행하고 server에서 임의 URL을 fetch하지 않는다. unknown ID는 404, 빈 그래프는 200과 빈 배열을 반환한다. 시작 시 거래 인증이나 외부 쓰기를 실행하지 않는다.
- [ ] API schema와 fixture를 저장하고 PASS를 확인한 뒤 commit한다.

### Task 5: 요약 A와 상세 B

**Wave:** 4 · **Depends on:** 4

**Files:** Create `frontend/package.json`, `frontend/index.html`, `frontend/vite.config.ts`, `frontend/tsconfig.json`, `frontend/src/{main,App}.tsx`, `frontend/src/styles.css`, `frontend/src/api/{types,client}.ts`, `frontend/src/dashboard/Dashboard.tsx`, `frontend/src/detail/TopicDetail.tsx`, `frontend/src/dashboard/Dashboard.test.tsx`, `frontend/src/detail/TopicDetail.test.tsx`. lockfile은 이 Task에서만 담당한다.

**Interfaces:** Consumes API contracts. Produces `App`, graph 탭 placeholder, `TopicDetail({id: string})`.

- [ ] `shows_missing_and_low_support` 는 missing을 0%로 표시하지 않는지, `opens_topic_evidence` 는 카드 선택→문헌 링크→기준 시각을 확인한다. `labels_preprint_and_unverified_summary` 는 동료심사와 본문 확인 상태의 혼동을 방지한다.
- [ ] `npm --prefix frontend test -- --run` 으로 미구현으로 인한 실패를 확인한다.
- [ ] 4개 영역의 요약·상세·리뷰 입력을 구현한다. source 장애, 초기 데이터 부족, 빈 상태를 표시한다. 미래 성공률 수치 대신 성장 후보의 feature와 불확실성을 나열한다. LLM이 설정되지 않아도 원문과 규칙 설명이 표시되어야 한다.
- [ ] 같은 테스트와 `npm --prefix frontend run build` 의 PASS를 확인하고 package/lock을 포함해 commit한다.

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

**Files:** Create `backend/radar/cli.py`, `scripts/register-daily-task.ps1`, `tests/test_daily_run.py`, `tests/e2e/radar.spec.ts`, `config/evaluation.yml`, `README.md`; Modify `frontend/src/App.tsx`, `frontend/package.json`.

**Interfaces:** Consumes 모든 선행 계약. Produces `python -m radar.cli collect --as-of ISO8601`, `python -m radar.cli evaluate --protocol config/evaluation.yml`.

- [ ] `test_duplicate_run_locked`, `test_resume_partial_run`, `test_timezone_0700_seoul` 을 작성한다. E2E는 요약→상세→graph→근거→리뷰→새로고침 후 저장 유지 여부를 확인한다.
- [ ] `python -m pytest tests/test_daily_run.py -q` 와 E2E 명령으로 미구현으로 인한 실패를 확인한다.
- [ ] graph 통합과 CLI, 07:00 KST Task Scheduler 등록 script를 구현한다. script는 생성만 하고 사용자가 터미널에서 명시적으로 실행하도록 절차를 작성한다. 중복 실행 lock·실패 log·수동 재실행을 제공한다.
- [ ] config/evaluation.yml에 4주, 후보 하루 최대 5건, baseline, spec의 Go 기준 5개 항목을 고정한다. 전향 평가 시작일, score를 가린 리뷰, sample 부족 시 inconclusive를 기록한다. 데이터 누락 시 비교 대상 날짜 제외를 명시한다.
- [ ] 전체 backend pytest, frontend unit, build, Playwright E2E를 실행한다. 실제 key가 설정되지 않은 source와 향후 90일 평가 미완료를 README에 명시한다. 구현 완료와 유용성 입증을 각각 보고하고 commit한다.

### Task 8: 평가 후 선택적 확장

**Wave:** 6 · **Depends on:** 7 및 1차 평가 판단

**Files:** Create `backend/radar/collectors/{hn,bluesky,toss}.py`, `backend/radar/analysis/{community,companies,correlation}.py`, `tests/test_enrichment.py`, `config/company-seeds.yml`; Modify `backend/radar/api/queries.py`, `frontend/src/detail/TopicDetail.tsx`.

**Interfaces:** Produces `community_candidates(documents: list[Document]) -> list[Candidate]`, `company_edges(documents: list[Document]) -> list[EvidenceEdge]`, `correlate(returns_by_security: dict[str,list[Observation]], window: int=120, min_overlap: int=60) -> list[EvidenceEdge]`.

- [ ] API 권한·비용·데이터 저장 조건을 소량 read-only 연결로 확인한다. 미확인 connector는 disabled로 둔다. HN/Bluesky는 관련 비율과 추가 후보 수, Reddit/Threads는 자격·권한을 먼저 확인한다.
- [ ] `test_reposts_do_not_count_as_independent`, `test_affiliation_not_adoption`, `test_correlation_requires_60_aligned_returns` 를 작성한다. 조정 방식이 unknown이거나 서로 다른 통화·시장을 정렬하지 않고 비교한 경우 edge가 생성되지 않는지 assert한다.
- [ ] `python -m pytest tests/test_enrichment.py -q` 로 미구현으로 인한 실패를 확인한다.
- [ ] 원본 게시물·자동 배포·독립적인 논의를 구분하고 기업 관계는 수동 확인한 seed에서 확장한다. 토스의 sector/candle 조회만 구현하고, 120거래일/최소 60일·수정종가의 일간 수익률로 계산한다. 기업 ID와 증권 ID의 혼동을 방지한다.
- [ ] 테스트·관련 frontend 테스트·build를 실행한다. 추가 가치가 없는 source를 제외하는 판단도 기록하고 commit한다. 주문 기능은 추가하지 않는다.

## 계획 자기점검

- A→B, graph, 알려지지 않은 기술 탐색, 시간순 평가, 기업·주가의 보조적 역할을 각 Task에 연결했다.
- 현재 관심도·신규 후보·미래 성장 target을 구분하고 미래 예측 성능은 구현 완료 조건에 포함하지 않았다.
- 같은 wave의 담당 파일은 겹치지 않는다. 다만 Wave 4의 Task 6은 실행 환경 준비를 위해 Task 5의 package 생성을 기다려야 하므로 완전히 독립적이지 않다. graph 계약은 Task 4에서 고정된다.
- Go 기준은 사용자 가치를 위한 제안 임계값이며 논문에서 얻은 실증값이 아니다. 4주가 끝나기 전에 성공을 선언하지 않는다.
- 이번 요청의 작업 범위는 조사·계획 작성까지다. 앱 구현·스케줄 등록·유료 계약은 수행하지 않았다.
