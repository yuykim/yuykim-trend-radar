# Claim B01 토론 기록

## 원 claim과 우리 조건

초기 소셜 언급을 Physical AI 논문의 향후 영향력 탐색을 위한 보조 신호로 사용할 수 있는가? 개인 1명, Robot Learning/World Model/VLA 중심, 무료 API·제한된 X/Reddit 접근, 매일 아침 후보 발견이 목적이다.

claim-verification 스킬의 지시에 따라 별도 advocate·critic·judge가 순차 검토했다. 지정된 sonnet/opus는 이 환경에서 제공되지 않아 각 역할에 기본 상속 모델을 사용했다. 파일의 직접 인용은 원문 영어를 유지한다.

## Advocate 1라운드

Eysenbach, Abstract—Conclusions: “Tweets can predict highly cited articles within the first 3 days of article publication.” (DOI: 10.2196/jmir.2012). JMIR 55편에서 얻은 결과지만, 인용 축적 전 초기 신호를 활용할 근거다. 매일 확인하는 우리 레이더에서 Physical AI 후보 논문의 검토 우선순위를 정하는 용도로 조건부 적용할 수 있다.

Haustein, Conclusion: “Therefore, they should not be considered as alternatives to citation-based indicators, but rather as complementary.” 확정적 영향력 평가보다 신기술 조기 인지가 목적인 우리 조건에서는 소셜 언급을 인용과 별도로 표시하는 보조 신호로 활용할 수 있다. 다만 Physical AI에서의 예측 성능은 별도 검증해야 한다.

## Critic 1라운드

‘보완적 지표’는 향후 학술 영향력 예측의 추가 가치를 뜻하지 않는다. Haustein, Conclusion: “tweets and citations are far from measuring the same impact”. 또한 “motivations to tweet need to be distinguished and further evaluated.”라고 제한한다. 의학 저널 55편의 예측 결과만으로 Physical AI에서 논문 신호 대비 추가 예측력이 있다고 판단할 수 없다.

보조 순위도 bot에 의해 왜곡될 수 있다. Bots, Conclusion and Future Directions: “This would be true if automated accounts were distributed equally.” bot 건수를 일률적으로 보정할 수 없으며, “current automated methods (such as _Bot or Not?_ ) were insufficient in identifying these accounts.”라는 탐지 한계도 있다. 무료 API 접근 제약이 있는 우리 조건에서는 소셜 원시 건수를 영향력 신호로 해석하기보다, 계정과 내용을 확인하는 발견 경로로 제한해야 한다.

## Advocate 2라운드

가장 강한 반론을 수용한다. Haustein의 서로 다른 영향력을 측정한다는 진술은 사회적 관심의 보완성이 향후 인용의 증분 예측가치를 입증하지 못함을 보여준다. Bots 논문의 당시 자동 탐지 한계도 인정한다. 따라서 주장을 ‘계정·내용을 확인한 소셜 언급을 후보 논문의 발견 경로로 활용’으로 좁힌다. Physical AI 향후 영향력 예측은 확인 불가이며, 분야별 검증 전 언급량으로 영향력 순위를 매기는 적용은 지지하지 않는다. 근거는 앞의 두 원문 인용과 동일하다.

## Critic 2라운드

축소된 조건을 수용한다. Bots, Conclusion은 “non-selective automated tweets should at least be identified, if not removed entirely.”라고 명시한다. 계정·내용을 확인하는 발견 경로로는 조건부 적용할 수 있다. 다만 발견 경로의 실용적 유용성도 Physical AI에서 실증된 결과는 아니다. 향후 영향력 예측과 언급량 기반 영향력 순위는 확인 불가로 유지한다.

## Judge의 인용문 대조 결과

별도 judge가 실제 `rg -n -o -F` 검색으로 아래 7개를 모두 확인했다. 경로 기준은 `../sources/`이며 폐기한 인용문은 없다.

| 인용 | 원문 파일:줄 | 결과 |
|---|---|---|
| Tweets can predict highly cited articles within the first 3 days of article publication. | B-S01-eysenbach.txt:5 | 검증됨 |
| Therefore, they should not be considered as alternatives to citation-based indicators, but rather as complementary. | B-S02-haustein.md:428 | 검증됨 |
| tweets and citations are far from measuring the same impact | B-S02-haustein.md:424 | 검증됨 |
| motivations to tweet need to be distinguished and further evaluated. | B-S02-haustein.md:430 | 검증됨 |
| This would be true if automated accounts were distributed equally. | B-S03-bots.md:158 | 검증됨 |
| current automated methods (such as _Bot or Not?_ ) were insufficient in identifying these accounts. | B-S03-bots.md:150 | 검증됨 |
| non-selective automated tweets should at least be identified, if not removed entirely. | B-S03-bots.md:162 | 검증됨 |

## 최종 판정

판정: **조건부 적용** — 계정·내용과 자동 게시 여부를 검토하여 일일 후보 발견에만 사용하고, 향후 영향력 예측 점수로 해석하지 않는 조건이다.

판정 근거: Eysenbach의 JMIR 55편 결과는 Physical AI에 대한 예측력을 입증하지 않으며, Haustein의 보완성도 증분 예측력을 뜻하지 않는다. 후보 발견 경로로 제한한 활용은 가능하지만, 우리 도메인의 미래 영향력 예측 성능과 발견 효율 증가는 별도 검증이 필요하다.

최종 판정은 claims-B.md B01에 반영했다. 이 토론은 코드 공개나 주가 관계망의 사용자 편익을 검증한 것으로 해석하지 않는다.
