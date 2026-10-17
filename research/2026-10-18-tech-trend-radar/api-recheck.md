# 인계 후 핵심 API 재확인

확인일: 2026-10-18. 기존 [52개 항목 조사](api-survey.md)를 보존하고, 초기 구현에 영향을 주는 공식 문서를 다시 열었다. 아래는 문서 확인 결과이며 인증 API 호출 성공이나 계정 권한 검증 결과가 아니다.

| 소스 | 다시 확인한 내용 | 구현 결정 |
|---|---|---|
| [arXiv](https://info.arxiv.org/help/api/tou.html) | legacy API는 전체 클라이언트를 합해 3초당 1회, 동시 연결 1개. 서지 메타데이터 CC0와 논문 본문 권리는 구별됨 | 최초 발견 채널. 공통 rate limiter를 사용하고 PDF 전체를 무조건 재배포하지 않음 |
| [OpenReview](https://docs.openreview.net/getting-started/using-the-api) | 계정 필요, 사이트와 동일한 접근권한. API 1과 2가 공존하며 JSON 형식 차이 | 공개 venue를 등록·시험한 뒤 사용. 탑티어 학회 전체가 이 서비스에 있다는 전제 금지 |
| [OpenAlex 인증](https://help.openalex.org/api/authentication/), [가격](https://help.openalex.org/access/pricing/) | 무료 key는 하루 $1 사용 예산, cursor 첫 페이지 이후 key 필요. 일반 무료 key는 초당 30회지만 일부 검색은 별도 제한 | 인용·기관·topic 보강. 무료 예산 안에서 중단하며 선불 충전은 초기 구현에 포함하지 않음 |
| [Hacker News](https://github.com/HackerNews/API) | 공식 item/story API 제공 | 커뮤니티 후보 채널. Physical AI recall과 추가 발견 가치를 먼저 측정 |
| [Bluesky 검색 reference](https://docs.bsky.app/docs/api/app-bsky-feed-search-posts) | 이번 재접속은 endpoints.bsky.app으로 이동하고 본문이 추출되지 않음 | 기존 조사만으로 정상 작동 확정 금지. 실제 소규모 공개 GET·검색 coverage 검증을 connector 진입 조건으로 둠 |
| [X](https://docs.x.com/x-api/getting-started/pricing) | 공식 가격 문서 재접속 | 초기 상시 수집 제외. 실제 필요성과 비용을 확인한 뒤 선택적으로 추가 |
| [Reddit](https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki) | 공식 Data API Wiki 재접속 | 무료 자격·OAuth 권한을 실제 확인하기 전 필수 경로로 두지 않음 |
| [토스증권 OpenAPI JSON](https://openapi.tossinvest.com/openapi-docs/latest/openapi.json) | 공개 JSON 명세 재접속. 기존 조사에 sector·candle 기능 기록 | 기업·주가는 후속 단계. 현재 키 권한·IP·저장 범위는 미검증이며 이번에 .env를 읽거나 주문 API를 호출하지 않음 |

HN/Bluesky는 접근 가능한 후보이지 Physical AI의 대표 표본으로 검증된 채널이 아니다. 소셜을 추가하는 단계에서 수집 가능한 양과 실제 관련 게시물 비율을 측정한다. Threads는 이번 재확인 범위에 포함하지 않았으며 기존 조사상의 미확인 권한 조건을 유지한다.
