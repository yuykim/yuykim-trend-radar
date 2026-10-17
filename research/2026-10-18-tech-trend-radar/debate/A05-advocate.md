## Advocate 1라운드

- 주장: A05의 한계는 작은 emerging topic까지 찾아야 하는 우리 조건에도 조건부 적용된다. 큰 연구 군집에서의 성공만으로 전체 후보에 대한 성장 예측이 검증됐다고 주장할 수 없다.
  - 근거: [S05, Results → Test #1, Fig. 3 해석; A-growth.md L326](../sources/A-growth.md) "When all RCs are included, neither model reaches the 25% CSI threshold in any year."
  - 조건 차이와 적용 논리: 원 연구의 citation-based research community(RC)와 우리 Physical AI topic의 구성은 다르지만, 작은 후보를 포함하는 모집단과 큰 군집만 남긴 모집단을 구별해야 한다는 논리는 동일하다. 25% CSI는 해당 연구의 기준이며 우리 성능의 상한이 아니다. 우리 조건에 적용하는 결론은 작은 신규 topic을 포함한 별도 평가 전에는 전체 조기 탐지의 성공을 주장할 수 없다는 것이다.

- 주장: 성능이 좋아 보이는 결과가 군집 크기 제한에 의존한다는 점은 우리 목적에서 특히 중요하다. 새 topic을 인지하려는 시스템에서 작은 군집을 제외하면 가장 필요한 후보를 평가에서 빠뜨릴 수 있다.
  - 근거: [S05, Results → Test #1; A-growth.md L322](../sources/A-growth.md) "This is done for all RCs and for the subset of RCs with at least 20 papers in the FY."
  - 근거: [S05, Results → Test #1, Fig. 3 해석; A-growth.md L326](../sources/A-growth.md) "When small RCs are excluded, the STS5 model is well above the threshold in all years, while the DC5 model is above the threshold in all relative years except -2, -1 and 0."
  - 조건 차이와 적용 논리: 원문의 FY는 forecast year이며 20편은 해당 연도의 군집 논문 수 기준이다. 우리 topic이 같은 단위라는 보장은 없으므로 기준 자체를 복사할 필요는 없다. 다만 좁은 Physical AI에서 작은 신규 topic을 다룬다는 우리 목표는 제외 표본의 성능을 확인해야 할 이유를 강화한다. 전체 후보와 작은 후보의 누락률·precision·recall을 함께 확인하는 조건에서 이 한계를 적용한다.

- 주장: 미래 성장 군집 수를 이용해 정한 예측 목록과 미래 정보를 포함한 군집 모델의 성능은, 매일 당시 정보로 운영하는 우리 레이더의 성능 근거로 바로 사용할 수 없다.
  - 근거: [S05, Results → Test #1; A-growth.md L322](../sources/A-growth.md) "The number of forecasts ( _N_ ) to be made is set at 1.5 times the number of RCs that experienced exceptional growth."
  - 근거: [S05, Results → Test #1, Fig. 3 해석; A-growth.md L326](../sources/A-growth.md) "While the STS5 model is above the threshold, this is only for cases where relative year is less than zero (recall that the STS5 forecasts for RY less than zero are using future information)."
  - 조건 차이와 적용 논리: 우리 운영에서는 앞으로 성장할 군집 수를 미리 알 수 없고, 미래 문헌으로 만든 군집도 사용할 수 없다. 데이터 공급자나 도메인을 바꾸어도 이 시간 제약은 동일하다. 따라서 알림 수를 미리 고정하고, 군집 생성·계수 추정·평가를 시간순으로 분리한 검증을 통과하기 전까지 성장 예측을 검증된 기능으로 제시해서는 안 된다는 A05의 한계를 지지한다.

- 주장: 무료 데이터와 매일 갱신이라는 우리 조건은 A05의 한계를 해소하는 근거가 되지 않는다. 문헌 coverage와 미래 일반화까지 검증해야 한다는 한계를 그대로 운영 판단에 반영해야 한다.
  - 근거: [S05, Flaws and Future Directions; A-growth.md L497](../sources/A-growth.md) "Predictability in the past does not guarantee predictability in the future."
  - 근거: [S05, Flaws and Future Directions; A-growth.md L499](../sources/A-growth.md) "Forecasts can only be made with the data available, and any biases in the data (e.g., by language, nationality, completeness) naturally bias the resulting forecasts."
  - 조건 차이와 적용 논리: Scopus와 OpenAlex/arXiv의 차이는 coverage와 실제 성능을 바꾸므로, 원 연구와 동일하게 실패한다고 단정할 수는 없다. 그러나 데이터 편향과 미래 일반화의 검증 필요성은 우리 무료 API 환경에도 적용된다. 매일 확인한다는 것은 관측 빈도의 조건이며 원 연구의 3년 성장 target에 대한 검증을 대신하지 않는다. 우리 데이터에서 단순 성장 baseline과 작은 topic을 포함한 시간순 평가를 수행하기 전에는 A05의 한계를 유지해야 한다.

## Advocate 2라운드 (반박)

- critic의 "전체 실패를 근거로 좁은 도메인에서도 성장 예측이 어렵다고 확정하는 추론은 막는다"에 대한 반론
  - 재반박: [S05, Results → Test #1, Fig. 3 해석; A-growth.md L326](../sources/A-growth.md) "When all RCs are included, neither model reaches the 25% CSI threshold in any year."
  - 재반박: [S05, Results → Test #1, 평가 모집단; A-growth.md L322](../sources/A-growth.md) "This is done for all RCs and for the subset of RCs with at least 20 papers in the FY."
  - 인정하되 조건 좁힘: 분야에 따른 예측 가능성까지 부정할 수 없다는 지적은 인정한다. 그러나 Computing Technology의 좋은 성능도 20편 이상이라는 제한을 공유하므로, Physical AI가 좁은 분야라는 이유만으로 작은 신규 topic까지 포함한 성공을 뒷받침하지는 못한다. A05에서 방어하는 한계는 Physical AI의 실패 확정이 아니라, 제한된 큰 군집의 결과를 전체 emerging topic의 성장 예측 성공으로 일반화할 근거가 없다는 것이다. 모든 작은 topic의 예측을 필수 기능으로 요구하지는 않되, 작은 후보를 포함한다고 주장하는 범위에는 이 한계를 적용한다.

- critic의 "25% CSI 미달은 특정 3년 성장 target과 효용 기준에 대한 실패다"에 대한 반론
  - 재반박: [S05, Results → Test #1, 예측 점수의 의미; A-growth.md L322](../sources/A-growth.md) "Note that this prediction score does not predict growth rate but is intended to rank RCs."
  - 인정하되 조건 좁힘: 개인 사용자의 아침 후보 검토 가치가 없다는 결론은 인정하지 않으며, 25% CSI를 우리 효용 기준으로 강제하지도 않는다. 다만 원문의 점수 자체가 성장률 예측값이 아니라 순위화 점수이므로, 그것을 '미래에 뜰 기술의 성장률을 예측한다'는 근거로 확대할 수 없다는 한계는 유지된다. Q2의 후보 관련성·발견 시점과 Q3의 미래 성장 예측을 따로 평가하고, A05는 후자에 대한 성능 주장과 모집단 일반화에 한정해 적용한다. 후보 발견 기능의 가능성은 이 반대 증거와 양립한다.

- critic의 "작은 RC에서의 실패를 작은 emerging topic의 본질적 예측 곤란으로 볼 수 없다"에 대한 반론
  - 재반박: [S05, Methods → Exceptional Growth; A-growth.md L178](../sources/A-growth.md) "We posit that small RCs may, in fact, be an artifact of information leakage."
  - 인정하되 조건 좁힘: 군집 구성과 작은 수의 효과가 관측된 실패에 섞였을 수 있다는 점을 인정한다. 이 문장은 저자의 원인 가설이므로 본질적인 예측 불가능성을 입증하지 않는다. 그러나 측정·군집 구성의 영향이 해소되지 않았다는 사실은 작은 신규 topic의 성장 예측이 이미 검증됐다는 해석도 막는다. A05를 불가피한 실패 법칙이 아니라 실제 조건에서 아직 해결되지 않은 성장 예측 한계로 유지한다. 당시 자료로 구성한 군집, 중복 제거, 최소 절대 증가량과 사전 고정 알림 수를 사용한 별도 평가에서 충분한 성능이 확인된 범위에 한해 이 한계를 해소할 수 있다.
