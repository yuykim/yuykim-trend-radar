## Advocate 1라운드

- 주장: A03은 Physical AI에서 emerging topic의 조상 topic 군집을 조기에 발견하는 방법 후보로 조건부 적용할 수 있다. 실제 과거 평가에서 유효한 군집 매칭이 보고됐으므로, 우리 조건에서도 topic 간 결합 변화를 시험할 실증 근거가 있다.
  - 근거: [S03, §5.7.1, Fig. 5.25 해석; A-augur.md L3321](../sources/A-augur.md) "Given this value, precision stays high (0.6-0.71) for the years from 1999 to 2005, while recall is in the range 0.43 to 0.63."
  - 조건 차이와 적용 논리: 이 수치는 similarity threshold 0.2와 1999–2005년 평가에 한정된다. 과거 CS 전체와 현재 Physical AI의 차이는 수치의 이식에는 영향을 주지만, 우리 논문 집합에서 같은 종류의 군집 신호를 검증할 근거를 없애지는 않는다. 무료 API로 확보한 문헌에 일관된 topic 식별과 충분한 과거 관측이 가능하다는 조건에서 적용을 지지한다. 수치는 우리 시스템의 예상 정확도로 사용하지 않는다.

- 주장: 이 방법의 예측 대상과 평가 window는 우리 목적 중 신기술의 조기 후보 인지와 맞는다. 새 이름을 맞히는 기능 대신, 앞으로 주목할 topic 조합을 보여주는 기능으로 적용할 수 있다.
  - 근거: [S03, §5.7.1, 평가 절차; A-augur.md L3319](../sources/A-augur.md) "for each approach, compare the clusters returned each year with the ancestors of areas that actually emerged in the following two years (see Table 5.2 at page 135) for different similarity values."
  - 조건 차이와 적용 논리: 원문의 1–2년은 다음 두 해에 등장한 topic과의 매칭 window다. 매일 아침 확인하는 우리 화면에서도 과거 기간을 누적한 군집 후보를 갱신해 보여줄 수 있으므로, 화면 확인 주기가 연 단위 평가와 다르다는 사실은 이 활용을 무효화하지 않는다. 일 단위 조기 탐지 성능은 별도 검증하되, 개인 연구자의 검토 후보를 제공한다는 적용 범위는 유지된다.

- 주장: soft debut을 명시하면 단발성 용어 출현과 여러 논문에서 확인되는 topic 형성을 구분할 수 있어, 우리 조기 인지 목적에도 적용 가능한 평가 기준이 된다.
  - 근거: [S03, §5.3.1 Debutant topics; A-augur.md L2497](../sources/A-augur.md) "To minimise the noise that can be caused by the spurious occurrence of the label associated with a topic in the literature, we use the concept of soft debut, in which a topic makes its debut only when it has reached at least 5 publications."
  - 조건 차이와 적용 논리: Physical AI의 preprint·학회 논문 비중이 다르더라도, 소수의 우연한 용어 사용을 topic 형성과 구별할 필요는 동일하다. 5편을 우선 명시적 평가 기준으로 삼고 중복 논문을 제거하며 기준 민감도를 확인하는 조건에서 적용을 지지한다. 따라서 A03의 선행성을 최초 논문보다 1–2년 앞섰다는 의미로 확대하지 않는다.

- 주장: 등장 후 자료를 사용하는 조상 topic 정답 구축은 회고적 평가에 활용할 수 있다. 예측 입력과 평가 정답의 시점을 분리하면 우리 조건에서도 같은 평가 질문을 시험할 수 있다.
  - 근거: [S03, §5.3.2 Extraction of related topics; A-augur.md L2533](../sources/A-augur.md) "To this end, when generating our gold standard, we consider as ancestors the top 25 topics, which mostly collaborated with the debutant topic during its initial five years of activity, and were already existing when the debutant topic emerged."
  - 조건 차이와 적용 논리: 원문의 정답은 등장 후 첫 5년의 관계를 이용한다. 이를 사후 평가 정답에만 사용하고, 군집 생성에는 당시 이용 가능했던 문헌·ontology만 사용하도록 고정하면 미래 정보가 예측 입력으로 들어가는 일을 막을 수 있다. 이 구분은 적용 조건이며 원 연구의 누출 부재를 입증했다는 뜻은 아니다. 따라서 충분히 성숙한 과거 Physical AI 사례로 backtest를 구성하는 조건에서 A03의 활용을 지지한다.

## Advocate 2라운드 (반박)

- critic의 "조상 집합 매칭과 실제 후보 인지의 유효성을 별도로 검증해야 한다"에 대한 반론
  - 재반박: [S03, §5.7.4, 매칭되지 않은 군집 해석; A-augur.md L3462](../sources/A-augur.md) "Nonetheless, this collaboration can still be meaningful and relevant for the stakeholders."
  - 인정하되 조건 좁힘: 조상 집합 매칭이 사용자 편익의 실증은 아니라는 지적은 인정한다. 다만 해당 문맥에서 저자는 새 topic으로 이어지지 않은 결합도 이해관계자에게 의미 있을 수 있다고 설명한다. 이는 효용을 입증한 결과가 아니라, 조상 군집을 검토 후보로 제시하는 적용 논리의 근거다. 따라서 '검증된 신기술 식별기'라는 적용은 유보하되, 관련 논문과 결합 변화를 보여주는 후보 생성 방법으로 시험한다는 찬성 입장은 유지한다. 성숙한 과거 사례의 군집 매칭 평가와 사용자의 후보 관련성 평가를 분리해야 한다.

- critic의 "ontology의 필터링과 의미 확장에 의존하므로, 무료 API의 논문을 모아 군집화하는 것만으로 재현된다고 볼 수 없다"에 대한 반론
  - 재반박: [S03, §5.5 Semantic filtering; A-augur.md L3020](../sources/A-augur.md) "This filter selects communities for which least 30% of their topics are found in the Computer Science Ontology."
  - 재반박: [S03, §5.7.1, Fig. 5.25 해석; A-augur.md L3321](../sources/A-augur.md) "Given this value, precision stays high (0.6-0.71) for the years from 1999 to 2005, while recall is in the range 0.43 to 0.63."
  - 인정하되 조건 좁힘: 이 의존성은 보고된 수치를 단순 군집화로 이식하는 주장을 막지만, ontology를 포함한 AUGUR 절차를 검증 후보로 삼을 근거까지 없애지는 않는다. 당시 이용 가능했던 ontology를 확보할 수 있는 과거 기간에 한정하고, Physical AI 세부 topic의 coverage, 필터로 제거된 후보, 의미 확장 전후 매칭을 함께 평가하는 조건으로 좁힌다. 상위 topic 일치가 세부 기술 식별 성공으로 계산되지 않도록 별도로 보고한다. 이 조건을 충족하지 못하는 구간에는 원문의 precision·recall을 적용하지 않는다.

- critic의 "soft debut 이전이어도 최초 논문은 이미 존재할 수 있다"에 대한 반론
  - 재반박: [S03, §5.3.1 Debutant topics; A-augur.md L2505](../sources/A-augur.md) "After analysing the difference between the original debut (herein labelled hard debut) and the soft debut, it appears that most of the topics have their soft debut at most two years after their hard debut."
  - 인정하되 조건 좁힘: 최초 논문보다 1–2년 빠르다는 해석은 철회 대상이며 1라운드에서도 주장하지 않았다. 반면 우리 조기 인지 목적에는 최초 용어 출현 후 연구 흐름이 형성되는 과정을 인지하는 활용도 포함할 수 있다는 것이 Advocate의 해석이다. 적용 범위를 'soft debut에 이르는 후보 조합의 사전 제시'로 한정하고, 최초 논문일·최초 수집일·5편 도달일 대비 제시 시점을 각각 측정한다. 새 키워드 알림 대비 추가 가치가 확인된 범위에서만 조기 인지 효과를 주장하되, 해당 비교를 수행할 방법 후보로서 A03을 지지한다.
