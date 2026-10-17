## Critic 1라운드

- 주장: A03의 수치를 우리 Physical AI 조기 인지 성능으로 적용할 수 없다. 평가 정답은 새 기술 자체가 아니라 등장 후 자료로 정의한 조상 topic 집합이다.
  - 근거: [S03, *Early Detection of Research Trends*, §5.3.2, A-augur.md L2533](../sources/A-augur.md#L2533) "To this end, when generating our gold standard, we consider as ancestors the top 25 topics, which mostly collaborated with the debutant topic during its initial five years of activity, and were already existing when the debutant topic emerged."
  - 근거: [S03, §5.7.1, A-augur.md L3319](../sources/A-augur.md#L3319) "for each approach, compare the clusters returned each year with the ancestors of areas that actually emerged in the following two years (see Table 5.2 at page 135) for different similarity values."
  - 조건 차이와 무효화 이유: 우리 목적은 새 기술을 조기에 알아보고 검토할 후보를 얻는 것이다. 사후에 정한 조상 집합과 비슷한 군집을 찾았다는 결과만으로 당시 사용자가 새로운 기술을 식별했거나 유용한 후보를 얻었다고 결론낼 수 없다. 미래 자료를 평가 정답에 쓰는 것 자체가 입력 누출이라는 주장은 아니다. 다만 조상 집합 매칭과 실제 후보 인지의 유효성을 별도로 검증해야 한다.

- 주장: 보고된 precision·recall은 ontology의 필터링과 의미 확장에 의존하므로, 무료 API의 논문을 모아 군집화하는 것만으로 재현된다고 볼 수 없다.
  - 근거: [S03, §5.5 Semantic filtering, A-augur.md L3020](../sources/A-augur.md#L3020) "This filter selects communities for which least 30% of their topics are found in the Computer Science Ontology."
  - 근거: [S03, §5.6 Semantic enhancement, A-augur.md L3092](../sources/A-augur.md#L3092) "This enhancement consists of merging clusters and debutant topics with their _super-areas_ ."
  - 조건 차이와 무효화 이유: 우리 수집 조건에는 2026년 VLA·JEPA 등을 일관되게 식별하는 과거 시점별 ontology의 확보가 보장돼 있지 않다. ontology coverage가 낮으면 후보가 평가 전에 제거되고, 상위 topic을 합치면 서로 다른 세부 기술도 매칭될 수 있다. 도메인별 coverage, 필터로 제외되는 후보, 의미 확장 전후 성능을 확인하지 않으면 원문의 수치는 우리 세부 기술 인지 성능을 뒷받침하지 못한다.

- 주장: 다음 1–2년의 soft debut을 맞힌다는 결과는 최초 논문보다 1–2년 앞선 탐지를 입증하지 않는다.
  - 근거: [S03, §5.3.1, A-augur.md L2497](../sources/A-augur.md#L2497) "To minimise the noise that can be caused by the spurious occurrence of the label associated with a topic in the literature, we use the concept of soft debut, in which a topic makes its debut only when it has reached at least 5 publications."
  - 근거: [S03, §5.3.1, A-augur.md L2505](../sources/A-augur.md#L2505) "After analysing the difference between the original debut (herein labelled hard debut) and the soft debut, it appears that most of the topics have their soft debut at most two years after their hard debut."
  - 조건 차이와 무효화 이유: soft debut 이전이어도 최초 논문은 이미 존재할 수 있다. 따라서 매일 아침 신기술을 먼저 알아보려는 우리 사용자에게 실질적 선행 시간이 생긴다는 결론은 성립하지 않는다. 최초 논문일·최초 수집일·5편 도달일을 구분하고, 단순한 새 키워드 알림보다 얼마나 먼저 유효 후보를 제시하는지 비교해야 한다.

## Critic 2라운드 (반박)

- advocate의 "예측 입력과 평가 정답의 시점을 분리하면 우리 조건에서도 같은 평가 질문을 시험할 수 있다"에 대한 반론
  - 재반박: [S03, §5.3.2, A-augur.md L2533](../sources/A-augur.md#L2533) "To this end, when generating our gold standard, we consider as ancestors the top 25 topics, which mostly collaborated with the debutant topic during its initial five years of activity, and were already existing when the debutant topic emerged."
  - 재반박: [S03, §5.4, 평가 similarity 설정, A-augur.md L2610](../sources/A-augur.md#L2610) "The similarity threshold _t_ cannot be defined a priori and indeed its detection will be part of the evaluation."
  - 반박 논리와 요구 조건: 입력·정답의 시간 분리는 타당하지만 그것만으로 충분하지 않다. 등장 후 5년의 정답 자료가 아직 쌓이지 않은 최신 topic은 같은 방식으로 완결 평가할 수 없고, 평가 결과를 보며 similarity threshold를 고르면 성능 선택 편향도 통제해야 한다. 성숙한 과거 사례에서 threshold·ontology를 정한 뒤 별도의 이후 기간에 고정 적용해야 한다. 최신 Physical AI 후보에 대해서는 이 평가가 아직 미완결임을 명시해야 하므로 적용 유보 입장을 유지한다.

- advocate의 "실제 과거 평가에서 유효한 군집 매칭이 보고됐으므로, 우리 조건에서도 topic 간 결합 변화를 시험할 실증 근거가 있다"에 대한 반론
  - 재반박: [S03, §5.3.1, A-augur.md L2509](../sources/A-augur.md#L2509) "Unfortunately, the number of debutant topics drastically decreases in the second part of the analysed period."
  - 재반박: [S03, 같은 문단, A-augur.md L2509](../sources/A-augur.md#L2509) "This is probably due to some missing data in our dataset."
  - 반박 논리와 요구 조건: 방법을 시험할 동기가 있다는 점은 인정한다. 그러나 저자 자신이 정답 topic 감소를 missing data의 영향으로 추정했으므로, 과거 일부 연도의 좋은 결과가 제한된 무료 API coverage에서도 유지된다는 추론은 성립하지 않는다. 우리 corpus에서 연도별 문헌·정답 coverage를 확인하고, 좁은 도메인 바깥의 조상 topic을 제외했을 때의 누락과 단순 co-occurrence baseline 대비 추가 가치를 검증해야 한다. 그 전에는 A03을 성능 근거가 아닌 검증 대상 가설로만 둘 수 있다.
