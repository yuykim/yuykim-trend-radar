## Critic 1라운드

- 주장: B01의 첫 3일 예측 결과는 우리 Physical AI의 향후 고인용 논문 식별 근거로 직접 적용할 수 없다. 원 연구도 다른 저널 재현을 미완료 과제로 남겼다.
  - 근거: [S01, *Can Tweets Predict Citations?*, Discussion → Limitations of This Study, A-eysenbach-pmc.txt L614; 같은 원문 B-S01-eysenbach.txt L5](../sources/A-eysenbach-pmc.txt#L614) "The results presented here should be confirmed with tweets about other journals, as well as with future JMIR articles, and our group is currently conducting comparative analyses with other datasets."
  - 근거: [S01, 같은 절, A-eysenbach-pmc.txt L619; B-S01-eysenbach.txt L5](../sources/A-eysenbach-pmc.txt#L619) "Journals that do not send out alerts for each article may have very different tweetation characteristics (eg, more late-stage tweetations)."
  - 조건 차이와 무효화 이유: 2009–2010년 JMIR 55편의 출판 직후 관측과, API 접근이 제한된 현재 X·Reddit·Threads의 Physical AI 논문 수집은 관측 모집단과 배포 방식이 다르다. 관련 사용자가 존재해도 우리가 첫 3일 언급을 충분히 수집한다는 보장은 없다. 최초 출판·preprint 공개·최초 수집 시점과 수집 누락을 구분하고 플랫폼별로 재현하기 전에는 선행성이나 예측력을 주장할 수 없다.

- 주장: 같은 실험과 더 큰 원 연구 모두에서 metric에 따른 차이가 있으므로, B01을 OpenAlex 인용이나 기술 단위 성장으로 확대할 수 없다.
  - 근거: [S01, Abstract → Results, B-S01-eysenbach.txt L5; B02와 같은 원문](../sources/B-S01-eysenbach.txt#L5) "less clear for Scopus citations and rank correlations."
  - 근거: [S02, *Tweeting biomedicine*, Abstract, B-S02-haustein.md L31; B03 원문](../sources/B-S02-haustein.md#L31) "The results show that tweeting behavior varies between journals and specialties and correlations between tweets and citations are low, implying that impact metrics based on tweets are different from those based on citations."
  - 조건 차이와 무효화 이유: S01의 긍정 결과는 같은 표본에서도 인용 DB·상관계수에 민감하며, S02는 2010–2012년 생의학 약 140만 문헌을 다룬다. 두 연구 모두 현재 Physical AI의 OpenAlex 인용·topic 성장에 대한 실험은 아니다. S02의 낮은 상관이 예측력 부재나 증분 예측력 존재를 증명하지는 않지만, S01의 긍정 사례 하나를 일반적 영향력 예측으로 옮길 근거도 주지 않는다. 예측 단위·인용 DB·기간을 고정한 별도 평가가 필요하다.

- 주장: 고유 사용자 수를 세는 것만으로 소셜 관심 신호를 신뢰할 수 없다. 원 연구의 반복 계정 처리와 별개로 자동 배포 계정의 비선택적 언급을 통제해야 한다.
  - 근거: [S01, Discussion → Limitations of This Study, A-eysenbach-pmc.txt L630; B-S01-eysenbach.txt L5](../sources/A-eysenbach-pmc.txt#L630) "Thus, multiple tweets sent by the same user about the same article would have been counted multiple times."
  - 근거: [S03, *Tweets as impact indicators*, Methods and Results, B-S03-bots.md L81; B04 원문](../sources/B-S03-bots.md#L81) "While categories 1) and 2) can be classified as completely automated and non-selective (except for an initial selection of the platform or topic) and thus qualify as Twitter bots, accounts classified in category 3) can be identified as human and selective."
  - 조건 차이와 무효화 이유: S03의 범위는 2012년 arXiv/WoS 문헌과 식별한 관련 계정이다. 현재 bot 비율을 추정하는 근거로 쓰지 않는다. 다만 여러 고유 자동 계정이 같은 새 논문을 배포하면 고유 사용자 기준을 통과해도 인간의 관심과 구분되지 않는다는 반례가 성립한다. 우리 arXiv 논문 후보에서 자동 배포·저자 홍보·독립 연구자의 논평을 구분하지 않으면 빠른 배포량이 연구자의 검토 우선순위로 잘못 변환될 수 있다.

## Critic 2라운드 (반박)

- advocate의 "계정·내용을 확인한 논문 링크를 제시하는 활용" 및 "URL·고유 사용자 수와 원문 토론을 함께 확인"하면 적용할 수 있다는 논거에 대한 반론
  - 재반박: [S01, Discussion → Limitations of This Study, A-eysenbach-pmc.txt L623; B-S01-eysenbach.txt L5](../sources/A-eysenbach-pmc.txt#L623) "The current report does not include a systematic qualitative analysis of tweet contents."
  - 재반박: [S03, Methods and Results, B-S03-bots.md L81](../sources/B-S03-bots.md#L81) "While categories 1) and 2) can be classified as completely automated and non-selective (except for an initial selection of the platform or topic) and thus qualify as Twitter bots, accounts classified in category 3) can be identified as human and selective."
  - 반박 논리와 요구 조건: 관심 링크를 수동 검토하는 활용 제안 자체는 가능하지만, S01의 예측 실험은 그러한 내용 검증 절차의 성능을 평가하지 않았다. 자동 계정도 서로 다른 고유 사용자이므로 중복 제거는 관심의 독립성을 보장하지 않는다. bot을 모두 악의적 조작으로 볼 필요도 없다. 자동 배포와 선택적 인간 언급을 분리한 뒤, 개인 사용자가 감당할 검토 수 안에서 관련 논문 발견률·놓친 논문·검토 시간을 비교해야 한다. 그 전에는 검증된 후보 발견 가치로 인정할 수 없다.

- advocate의 "93% specificity와 75% sensitivity ... 보조 후보로 시험할 근거는 충분하다"에 대한 반론
  - 재반박: [S01, Abstract → Results, A-eysenbach-pmc.txt L108; B-S01-eysenbach.txt L5; A06과 같은 실험](../sources/A-eysenbach-pmc.txt#L108) "Top-cited articles can be predicted from top-tweeted articles with 93% specificity and 75% sensitivity."
  - 재반박: [S01, Discussion → twimpact factor 설명, B-S01-eysenbach.txt L5; A-eysenbach-pmc.txt L524–526](../sources/B-S01-eysenbach.txt#L5) "An even shorter period of time (3 days), tw3, was already sufficient in the sample to discriminate between highly cited and less cited articles, but I suggest a standard n of 7, which has the advantage that it always includes a weekend; thus, journal articles published toward the end of the week are less penalized for the weekend effect."
  - 반박 논리와 요구 조건: advocate가 3일 결론과 주로 tw7에 따른 분류 수치를 구분한 점은 인정한다. 그러나 A06과 B01은 같은 표본의 결과이므로 독립적인 재현 증거 두 개로 셀 수 없다. 고인용 12편 중 9편을 찾았다는 결과는 현재 인용·논문 신호만 사용하는 baseline보다 소셜을 추가하면 더 잘 찾는다는 비교도 아니다. 원문은 3일에도 구분됐다는 표본 내 결과와 7일 표준 제안을 함께 제시한다. 우리 첫 3일 신호의 수집 coverage를 검증하고, 동일한 공개 시점의 논문 신호 baseline과 소셜 추가 모델을 분리된 이후 기간에서 비교해야 B01의 예측적 적용을 인정할 수 있다.
