## Advocate 1라운드

- 주장: B01은 초기 소셜 관심으로 먼저 검토할 논문을 찾는 후보 발견 경로로 우리 조건에 조건부 적용할 수 있다. 인용이 충분히 쌓이기 전 관측 가능한 신호를 활용할 실증적 출발점이 있다.
  - 근거: [S01, Abstract → Conclusions; B-S01-eysenbach.txt L5, 같은 원문 A-eysenbach-pmc.txt L110](../sources/B-S01-eysenbach.txt) "Tweets can predict highly cited articles within the first 3 days of article publication."
  - 조건 차이와 적용 논리: 원 연구는 JMIR 55편에 대한 과거 Twitter 관측이며 현재 Physical AI의 결과는 아니다. 그 차이는 예측 성능의 재현 여부에는 영향을 주지만, 초기 언급을 연구자가 검토할 후보로 제시할 근거를 없애지는 않는다. 출판 시점과 최초 관측 시점을 기록하고 실제 관련 언급을 확인하는 조건에서 적용을 지지한다. 출판 전 선행이나 기술 단위 미래 성장을 입증한 결과로 확대하지 않는다.

- 주장: A06과 같은 원 실험의 분류 결과는 초기 관심이 향후 고인용 논문을 구분한 사례가 실제 존재함을 보여준다. 따라서 소셜 신호를 보조 후보로 시험할 근거는 충분하다.
  - 근거: [S01, Abstract → Results; Results → Binary Analysis, Table 2; B-S01-eysenbach.txt L5, 같은 원문 A-eysenbach-pmc.txt L108](../sources/B-S01-eysenbach.txt) "Top-cited articles can be predicted from top-tweeted articles with 93% specificity and 75% sensitivity."
  - 조건 차이와 적용 논리: 이 결과는 55편 중 고인용 12편의 9편 검출과 비고인용 43편의 40편 제외에 해당하며, 주요 지표는 첫 7일의 tw7이다. 앞의 첫 3일 결론과 결합해 '3일 신호의 sensitivity가 75%'라고 해석하지 않는다. 우리에게 필요한 적용은 후보 검토 순서에 초기 관심을 추가하는 것이므로, 이 수치를 이식하지 않고 citation-only baseline 대비 추가 가치를 시간순 검증한다는 조건에서 긍정적 근거로 사용할 수 있다.

- 주장: 도메인과 시대 차이는 충분한 관련 사용자층이 있는 범위에서 적용 조건으로 다룰 수 있다. 우리 Physical AI 수집 대상에서 실제 논문 토론이 관측되는지 먼저 확인하고 그 범위에 한정해 적용하면 된다.
  - 근거: [S01, Discussion → Limitations of This Study; B-S01-eysenbach.txt L5, 같은 원문 A-eysenbach-pmc.txt L614](../sources/B-S01-eysenbach.txt) "The hypothesis is that the results can be replicated for other journals as long as there is a large enough Twitter user base."
  - 조건 차이와 적용 논리: 이는 저자의 재현 가설이며 Physical AI에서 입증된 사실은 아니다. 따라서 API 접근 제약 속에서도 충분한 관련 사용자와 논문 링크를 관측할 수 있는 X 범위에서 먼저 시험한다. Reddit·Threads로 넓히려면 플랫폼별로 같은 조건을 별도 검증한다. 관련 사용자층과 coverage를 확인한다는 조건은 도메인 차이를 무시하지 않으면서 후보 발견 경로로 적용할 수 있게 한다.

- 주장: 소셜 신호를 연구자의 주의 배분에 사용하는 방식은 우리 개인 연구자의 아침 확인 목적과 직접 맞는다. 계정·내용을 확인한 논문 링크를 제시하는 활용을 지지한다.
  - 근거: [S01, Discussion → Conclusions, 활용 사례; B-S01-eysenbach.txt L5, 같은 원문 A-eysenbach-pmc.txt L644](../sources/B-S01-eysenbach.txt) "Third, social media impact metrics can also be used as a filter to direct users to research articles that the public or research communities are paying attention to."
  - 근거: [S01, Discussion → Limitations of This Study, 중복 언급 처리; B-S01-eysenbach.txt L5, 같은 원문 A-eysenbach-pmc.txt L630](../sources/B-S01-eysenbach.txt) "a tweetation should be defined as an URL mentioned by a distinct unique user."
  - 조건 차이와 적용 논리: 원문은 이런 filter의 활용을 제안했으며 사용자 편익을 직접 실험한 결과는 아니다. 그럼에도 관심 논문을 빠르게 검토하려는 우리 목적은 해당 활용과 일치한다. 개인 프로젝트에서는 확보한 범위의 URL·고유 사용자 수와 원문 토론을 함께 확인하고, 반복 홍보를 검토하는 조건으로 적용할 수 있다. 기술의 우수성이나 산업적 성공을 판정하는 기능으로 확장할 필요 없이 B01 자체의 후보 발견 가치를 변론할 수 있다.

## Advocate 2라운드 (반박)

- critic의 "관련 사용자가 존재해도 우리가 첫 3일 언급을 충분히 수집한다는 보장은 없다"에 대한 반론
  - 재반박: [S01, Discussion → Limitations of This Study; A-eysenbach-pmc.txt L614](../sources/A-eysenbach-pmc.txt) "The results presented here should be confirmed with tweets about other journals, as well as with future JMIR articles, and our group is currently conducting comparative analyses with other datasets."
  - 인정하되 조건 좁힘: 재현과 수집 coverage가 확인되지 않았다는 반론은 타당하다. 따라서 현재 Physical AI에서 첫 3일 예측 성능이나 보편적 선행성을 인정하자는 주장은 하지 않는다. 원 연구는 다른 저널에서의 확인을 요구하면서도 관측된 결과 자체를 부정하지 않으므로, 이를 보조 신호의 검증 출발점으로 삼는 입장은 유지한다. preprint 공개일·정식 출판일·최초 수집일과 수집 중단을 구분하고, 정한 초기 window를 관측할 수 있는 플랫폼·기간에 한정해 적용한다. 늦게 수집된 논문에서 언급이 없다는 사실을 무관심으로 계산하지 않는다.

- critic의 "B01을 OpenAlex 인용이나 기술 단위 성장으로 확대할 수 없다"에 대한 반론
  - 재반박: [S01, Discussion → Conclusions, 활용 사례; A-eysenbach-pmc.txt L644](../sources/A-eysenbach-pmc.txt) "Third, social media impact metrics can also be used as a filter to direct users to research articles that the public or research communities are paying attention to."
  - 인정하되 조건 좁힘: 인용 DB·metric에 따른 차이와 낮은 상관은 인정하며, JMIR 결과를 OpenAlex 인용이나 Physical AI 기술 성장의 예측 성능으로 옮기지 않는다. 그러나 소셜 신호와 인용이 다른 정보를 측정한다는 지적은 위와 같은 관심 논문 filter의 적용을 배제하지 않는다. 이 인용은 활용 제안이지 사용자 효용 실험은 아니므로, 후보 발견 경로로 시험하는 조건부 찬성만 유지한다. 동일 공개 시점의 논문 신호 baseline 대비 관련 논문 발견률·검토 시간을 비교하고, 영향력 예측을 주장하려면 고정한 인용 DB·기간의 별도 시간순 평가를 요구한다. A06은 B01과 같은 표본이므로 독립적인 재현 근거로 중복 계산하지 않는다.

- critic의 "고유 사용자 수를 세는 것만으로 소셜 관심 신호를 신뢰할 수 없다"에 대한 반론
  - 재반박: [B측 S03, Tweets as impact indicators, Methods and Results, 계정 분류; B-S03-bots.md L81](../sources/B-S03-bots.md) "While categories 1) and 2) can be classified as completely automated and non-selective (except for an initial selection of the platform or topic) and thus qualify as Twitter bots, accounts classified in category 3) can be identified as human and selective."
  - 재반박: [S01, Discussion → Limitations of This Study; A-eysenbach-pmc.txt L623](../sources/A-eysenbach-pmc.txt) "The current report does not include a systematic qualitative analysis of tweet contents."
  - 인정하되 조건 좁힘: 고유 사용자로 중복을 제거해도 자동 배포 계정이 남는다는 반례를 인정한다. 반면 계정 분류 원문은 선택적 인간 언급과 비선택적 자동 배포를 구분하므로, 소셜 신호 전체를 포기하기보다 구분해 시험할 근거를 제공한다. 자동 배포·저자 홍보·독립 연구자의 선택적 언급을 분리하고 판단이 어려운 계정은 따로 표시하는 조건으로 좁힌다. 이 보정 절차의 효과가 S01에서 입증됐다고 주장하지 않으며, 보정 전후 후보 관련성과 검토 부담을 비교해 유효한 범위에서만 적용한다. 따라서 원시 언급 수의 신뢰성 주장은 줄이되, 검토 가능한 소셜 후보 경로로서의 적용 찬성은 유지한다.
