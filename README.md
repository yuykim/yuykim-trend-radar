# yuykim-trend-radar

Physical AI 문헌의 연구 관심·신규 후보·원문 근거를 살펴보는 개인용 정적 사이트입니다.
후보는 규칙 기반 제안이며 미래 기술 성공이나 주가를 예측하지 않습니다.

## 로컬 실행 (Windows PowerShell)

Python 3.13, Node 22.12 이상, Git을 사용합니다.

```powershell
python -m pip install -r backend/requirements.lock -e ./backend 'pytest>=8,<9'
npm ci --prefix frontend
python -m radar.cli run --out frontend/public/data
npm --prefix frontend run dev
```

개발 URL은 `/yuykim-trend-radar/`입니다. Gemini는 선택 사항입니다.
`GEMINI_API_KEY`는 프로세스 환경변수로만 읽습니다. 로컬 `.env`를 사용한다면
자신의 환경 로더로 환경변수에 주입하세요. CLI와 Vite는 `.env`를 자동으로 읽지 않습니다.
키·`.env`를 출력하거나 Git에 추가하지 마세요. 키 미설정·429·네트워크 실패에도 원문 기반 실행은 성공합니다.

```powershell
python -m radar.cli run --as-of 2026-10-18T22:00:00Z --out frontend/public/data
python -m pytest -q
npm --prefix frontend test -- --run
npm --prefix frontend run build
npm --prefix frontend run test:e2e
```

E2E는 Windows의 설치된 Edge를 사용합니다. CI는 Playwright Chromium을 설치합니다.
`tests/e2e/data`는 합성 E2E fixture이며 실제 export와 독립적입니다.

## 수집·데이터 보존

매일 07:00 Asia/Seoul(22:00 UTC)에 실행합니다. 수동 재실행도 같은 일일 22:00 UTC
경계와 56일 publication window를 사용하여 완료된 페이지를 재사용합니다.
partial/failed window는 DB에 남겨 다음날 runner에서도 먼저 이어받습니다.
이전 window 복구가 끝나면 다음 실행부터 최신 경계로 진행하며, 하루 이상 오래된 window는
완료됐어도 현재 coverage snapshot으로 사용하지 않습니다.
최초 56일 bootstrap 완료 후에는 마지막 완료 경계에서 하루를 겹치는 증분 수집으로
전환합니다. 이전 28일 분모는 DB에 보존된 동일 coverage 문헌과 합쳐 계산합니다.
이 증분 상태는 현재 고정된 source 범위에 대한 것입니다. 범위·분류 설정을 바꿀 때는
새 `--db`와 새 `RADAR_COLLECTOR_STATE` 경로로 bootstrap하여 서로 다른 코퍼스를 섞지 마세요.
실제 관측 시각을 소급하지 않으므로 기본 dashboard 기준 시각은 수집 완료 시각입니다.
명시적 `--as-of`는 해당 시각 이후에 새로 관측한 자료를 제외합니다.

arXiv broad 수집만 켜져 있습니다. OpenReview는 venue 미확정, OpenAlex는 설정상
disabled입니다. disabled는 정상적인 선택 상태이며 수집 성공으로 계산하지 않습니다.
수집 실패/partial도 SourceRun으로 남기고 export를 계속합니다.
arXiv 전체 페이지 수집 성공 시에만 같은 coverage의 topic/`__all__` count snapshot을
저장합니다. 실패 시 missing이며 0%나 하락으로 해석하지 않습니다. 기존 Task 3 계약상
정확히 28일 차이인 동일 coverage snapshot만 비중 차이를 계산하므로 초기에는 null일 수 있습니다.

첫 실제 문서가 생기기 전에는 기존 `frontend/public/data` 합성 예시를 유지합니다.
`run-status.json`의 DEMO 상태와 최근 수집 결과를 화면에 별도 표시합니다.
첫 실제 문서부터 전체 JSON을 실제 export로 교체하며, 이후 장애 때도 실제 이력을 표시합니다.
CLI가 생성하는 상태가 DEMO 표시를 결정하므로 운영 build flag를 수동으로 바꿀 필요가 없습니다.
임의의 새 출력 경로에는 보존할 예시가 없으므로 정상적인 빈 payload를 만듭니다.

SQLite `data/radar.db`에는 문헌·관측·요약 cache·일일 평가 snapshot을 저장합니다.
`RADAR_COLLECTOR_STATE=data/collector-state.db`는 페이지 checkpoint와 일일 예산 ledger입니다.
CI는 두 DB 및 공개 JSON을 bot commit하여 다음 runner에 복구합니다. DB에는 공개 메타데이터만
보관하며, 브라우저 리뷰는 localStorage와 사용자의 JSON export에 남습니다.
ID 변환은 Task 4 export를 그대로 사용하고 `correlation`/`stock_correlation`을 변환하지 않습니다.

## 전향 평가

`config/evaluation.yml`은 4주·하루 최대 5건·동일 코퍼스 날짜순 seed baseline,
broad feed 비교와 다섯 Go 기준을 고정합니다. `prospective_start`는 아직 null입니다.
실제 평가 전에 UTC 시작 시각을 지정·commit하세요. 합성 검증을 효용 성과로 계산하지 않습니다.

```powershell
python -m radar.cli evaluate --protocol config/evaluation.yml --review-out data/blind-review.json
python -m radar.cli evaluate --protocol config/evaluation.yml --reviews my-reviews.json
```

매일 최초 노출 snapshot을 고정하며 재실행은 평가 이력을 바꾸지 않습니다.
blind packet은 출처 문서 ID와 무작위 순서의 opaque review ID만 포함하고 점수·순위·arm을 숨깁니다.
문헌은 DB에서 확인하고 리뷰 JSON 배열에 `candidate_id`로 review ID를 사용합니다.
나머지 필드는 `reviewed_at`, `already_known`, `relevant`, `distinct`, `useful`, `minutes_spent`입니다.
브라우저 JSON export(`reviews` 배열 포함)도 입력할 수 있습니다.
baseline 리뷰는 blind packet으로 별도 수행해야 합니다. 표본이나 라벨 부족은 inconclusive입니다.
공통 후보만 발견 시차를 계산하며 baseline 미발견은 추가 발견으로 남깁니다.
공통 후보는 정확히 같은 entity ID로만 대응시킵니다. seed/broad 피드와 시스템 후보의
identity가 다르면 자동 대응하지 않으므로 발견 시차는 null로 남을 수 있습니다.
Go 판단에는 28일 모두 primary arm별 5개 후보와 완전한 리뷰가 필요합니다.

## GitHub 활성화 (사용자 확인 후 lead가 수행)

이 작업에서는 repo 생성·push·secret 등록·Pages 활성화를 수행하지 않았습니다.
사용자 확인 후 아래 절차를 진행하세요.

1. `.env`가 tracked되지 않았는지 `git ls-files -- .env`로 확인합니다(출력이 없어야 함).
2. `gh repo create yuykim-trend-radar --public --source . --remote origin`을 실행합니다.
3. `git push -u origin main`을 실행합니다.
4. GitHub Settings → Actions → General에서 workflow의 읽기·쓰기 권한을 허용합니다.
5. Settings → Secrets and variables → Actions에서 `GEMINI_API_KEY` secret을 직접 입력합니다.
   키는 명령행 인수나 로그에 넣지 않습니다. 요약을 끄려면 secret을 생략합니다.
6. Settings → Pages → Source를 **GitHub Actions**로 설정합니다.
7. Actions → Daily radar → Run workflow를 1회 실행하고 테스트·수집·배포 결과를 확인합니다.

배포 예정 URL: `https://<GitHub 사용자명>.github.io/yuykim-trend-radar/`.
실제 배포와 Ubuntu lockfile 호환성은 workflow 실행 후 확인해야 합니다.
workflow는 중복 실행을 직렬화하고 test → batch → DB/JSON commit → build → Pages 배포 순입니다.
저장 단계는 뒤 단계 실패에도 실행되어 이미 완료된 수집 checkpoint를 잃지 않습니다.
