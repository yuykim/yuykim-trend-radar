# Fieldnote frontend · Task 5

PowerShell에서 저장소 루트를 기준으로 실행합니다.

```powershell
npm --prefix frontend ci
npm --prefix frontend run dev
npm --prefix frontend test -- --run
npm --prefix frontend run build
frontend/node_modules/.bin/playwright test --config frontend/playwright.config.ts
```

개발 주소: http://localhost:5173/yuykim-trend-radar/

`public/data/dashboard.json`, `topics/{entity_id}.json`, `graph.json`은
명시적인 합성 UI fixture입니다. `example.org` 링크는 실제 연구 출처가 아닙니다.
재생성: `node frontend/scripts/generate-demo.mjs`.
Task 4가 같은 계약으로 export한 JSON으로 교체하면 됩니다.
교체 후 `$env:VITE_DEMO_DATA='false'`를 설정하고 build하면 DEMO 표시가 사라집니다.
실제 데이터로 교체한 뒤에만 이 설정을 사용하세요.

Vite `base`는 `/yuykim-trend-radar/`이고 데이터 요청에도 BASE_URL을 사용합니다.
`envDir: false`로 환경 파일을 로드하지 않습니다. frontend에 secret을 넣지 않습니다.

`types.ts`는 공통 계약과 Task 4의 nullable CandidateSummary를 포함합니다.
`why_new`, `difference`, `model`은 문자열, `limitations`, `source_document_ids`는
문자열 배열입니다. 모든 시각은 UTC ISO 8601 문자열이며 미확인은 null입니다.
화면 이름·동의어는 dashboard 스키마를 확장하지 않고 topic JSON에서 읽습니다.
Trend의 missing에서는 count_28d가 0이어도 표시하지 않습니다.
SourceRun의 마지막 정상 결과는 전달된 source_runs 안의 마지막 ok 기록을 찾습니다.
Task 4에서는 실패 기록과 이전 정상 기록을 함께 export해야 합니다.

리뷰·관심 저장 key는 `yuykim-trend-radar:reviews`,
`yuykim-trend-radar:watchlist`입니다. 저장이 막히거나 기존 값이 잘못되면
화면에 알리고 JSON 내보내기를 제공합니다. 새로고침 후 보존에는 localStorage가 필요합니다.

graph 탭은 placeholder입니다. Task 6은 설치된 cytoscape/@types/cytoscape와
GraphPayload를 사용하고 Task 7이 App에 연결합니다.
`.task5-ready`는 인계 신호이므로 commit하지 않습니다.

UI 검증은 설치된 Microsoft Edge를 사용합니다. 아래 명령은 테스트 전 production
preview를 자동 실행합니다. 화면 캡처 등 결과물은 `frontend/test-results/`에 저장됩니다.

```powershell
npm --prefix frontend run build
frontend/node_modules/.bin/playwright test --config frontend/playwright.config.ts
```
