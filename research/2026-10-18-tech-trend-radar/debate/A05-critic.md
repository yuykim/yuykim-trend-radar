## Critic 1라운드

- 주장: A05의 전체 RC 실패를 좁은 Physical AI의 성장 예측 한계로 그대로 일반화할 수 없다. 원 연구 자체가 분야별 성능 차이를 보고한다.
  - 근거: [S05, *A Novel Approach to Predicting Exceptional Growth in Research*, Results → Test #2, A-growth.md L344](../sources/A-growth.md#L344) "Even though the overall CSI scores are quite high, given field-level differences in citation behavior and characteristics, we expect that performance may differ dramatically by field or discipline."
  - 근거: [S05, Results → Test #3, A-growth.md L381](../sources/A-growth.md#L381) "Table 7 shows that nine of 11 DC2 disciplines in the DC5 model meet the FUSE criteria, while ten of the 11 DC2s in the STS5 model meet the criteria."
  - 조건 차이와 무효화 이유: 원문의 전체 RC는 여러 분야를 포함하지만 우리는 Physical AI로 모집단을 좁힌다. Table 6의 Computing Tech DC5 결과도 precision 42.9%, recall 64.5%다(L360). 이 결과들은 FY 20편 이상이라는 제한이 있으므로 작은 topic의 성공 증거로 쓰지는 않는다. 다만 전체 실패를 근거로 좁은 도메인에서도 성장 예측이 어렵다고 확정하는 추론은 막는다. 우리 도메인의 크기별 평가 전에는 한계의 전이도 미확정이다.

- 주장: 25% CSI 미달은 특정 3년 성장 target과 효용 기준에 대한 실패다. 우리 개인 사용자의 조기 인지 가치가 없다는 결론으로 확장할 수 없다.
  - 근거: [S05, Background → Identification of Emerging Topics, A-growth.md L47](../sources/A-growth.md#L47) "After consulting with potential users and others, a heuristic metric was agreed upon."
  - 근거: [S05, Methods → 성장 정의, A-growth.md L164](../sources/A-growth.md#L164) "The target year (TY) is three years after the forecast year."
  - 근거: [S05, Results → Test #1, A-growth.md L322](../sources/A-growth.md#L322) "Note that this prediction score does not predict growth rate but is intended to rank RCs."
  - 조건 차이와 무효화 이유: 원문은 publication share의 exceptional growth를 3년 뒤 이진 결과로 평가한다. 우리 주목적은 매일 아침 관련 기술을 인지하는 것이며, scope.md에는 모든 작은 topic의 3년 성장을 특정 CSI로 맞혀야 한다는 요구가 없다. 적은 검토 후보의 관련성·발견 시점이라는 효용과 원문의 전체 성장 분류 성능은 다르다. 검토 가능한 알림 수와 허용 누락을 사전에 정해 평가해야 하며, 갱신 주기만 짧게 하면 성장 예측이 개선된다고 주장하는 것은 아니다.

- 주장: 작은 RC에서의 실패를 작은 emerging topic의 본질적 예측 곤란으로 볼 수 없다. 원문은 군집 생성 과정과 작은 수의 효과도 원인 후보로 제시한다.
  - 근거: [S05, Methods → Exceptional Growth, A-growth.md L178](../sources/A-growth.md#L178) "We posit that small RCs may, in fact, be an artifact of information leakage."
  - 근거: [S05, 같은 절, A-growth.md L184](../sources/A-growth.md#L184) "For example, an RC with 5 papers in the FY only needs to have 7 papers in the TY to achieve exceptional growth using our annual 8% growth threshold."
  - 조건 차이와 무효화 이유: 미래 정보를 쓴 군집의 분할과 5편→7편 같은 작은 수의 변화가 실패 결과에 섞여 있을 수 있다. 이는 저자의 가설이지 확정 원인은 아니지만, 전체 CSI 미달을 신규 topic의 불가피한 난도로 해석하지 못하게 한다. 우리 과거 시점별 topic 구성·중복 제거·최소 증가량 정의로도 같은 실패가 생기는지 확인해야 이 한계를 적용할 수 있다.

## Critic 2라운드 (반박)

- advocate의 "큰 연구 군집에서의 성공만으로 전체 후보에 대한 성장 예측이 검증됐다고 주장할 수 없다"에 대한 반론
  - 재반박: [S05, Results → Test #2, A-growth.md L344](../sources/A-growth.md#L344) "Even though the overall CSI scores are quite high, given field-level differences in citation behavior and characteristics, we expect that performance may differ dramatically by field or discipline."
  - 재반박: [S05, Results → Test #1, A-growth.md L326](../sources/A-growth.md#L326) "When all RCs are included, neither model reaches the 25% CSI threshold in any year."
  - 반박 논리와 요구 조건: 큰 군집만으로 전체 후보의 성공을 주장할 수 없다는 점은 인정한다. 그러나 그 논리는 모든 Physical AI topic에서 예측이 어렵다는 결론도 허용하지 않는다. 전체 분야·전체 크기를 합친 실패와 좁은 도메인의 실패는 구분해야 한다. scope.md가 가장 작은 모든 topic의 성장 예측을 필수 조건으로 정하지도 않았다. 작은 후보를 포함하는 발견 성능과 관측량이 충분한 topic의 성장 예측을 각각 평가하는 조건에서는 후자의 가능성을 전체 CSI 실패로 배제할 수 없다. 이것은 작은 후보를 제외하고 전체 성공을 선언하자는 주장이 아니다.

- advocate의 "미래 성장 군집 수를 이용해 정한 예측 목록과 미래 정보를 포함한 군집 모델의 성능은 ... 바로 사용할 수 없다"에 대한 반론
  - 재반박: [S05, Results → Test #1, A-growth.md L322](../sources/A-growth.md#L322) "The number of forecasts ( _N_ ) to be made is set at 1.5 times the number of RCs that experienced exceptional growth."
  - 재반박: [S05, Methods → Composite Indicator, A-growth.md L284](../sources/A-growth.md#L284) "We used two forecast years (2013 and 2014) with positive RY (1 and 2) from the DC5 model."
  - 반박 논리와 요구 조건: 미래의 성장 군집 수로 N을 정하거나 미래 자료로 군집을 만드는 평가는 운영 근거로 부족하다는 지적은 타당하다. 다만 그 결함은 보고된 성공뿐 아니라 전체 실패를 우리 운영으로 옮길 때도 작용한다. 원문은 DC5의 양의 RY와 STS5의 음의 RY를 구분하므로 모든 평가를 같은 누출 사례로 취급해서도 안 된다. DC5도 계수 추정 FY 2013–2014와 2014 평가의 중첩이 있어 독립 검증으로 승격하지 않는다. 당시 자료로 구성한 군집, 앞선 기간의 학습, 사전 고정 N으로 다시 평가해야 하며, 그 결과 전에는 A05를 우리 도메인의 실패 증거로 확정할 수 없다.
