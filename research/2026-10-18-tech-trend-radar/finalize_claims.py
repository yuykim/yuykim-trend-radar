"""Consolidate existing claim tables while preserving IDs and evidence."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

VERDICTS = {
    "A03": "topic 결합 기반 후보 생성 방법을 시험하는 데 한정한다. 당시 이용 가능했던 문헌·vocabulary·ontology, 독립적인 threshold 검증, coverage 확인, 고정 알림 예산의 신규 키워드 baseline 비교와 사용자 편익 평가가 필요하다. 원문의 매칭 성능·평가 window를 Physical AI 정확도·선행 시간으로 이식하지 않는다. 최종 판정: [토론](debate/A03.md).",
    "A05": "전체 RC 실패를 Physical AI의 필연적 실패로, 큰 군집 성능을 작은 신기술의 성공으로 일반화하지 않는다. 당시 자료만 사용하고 군집·특징·학습·평가를 시간순 분리하며 알림 수를 사전 고정한다. 작은 topic 탐지와 미래 성장 평가는 구별하고 단순 추세 baseline을 넘는지 검증한다. 최종 판정: [토론](debate/A05.md).",
    "B01": "사람이 검토할 후보를 모으는 보조 경로의 시험으로 제한한다. 공개·수집 시점과 coverage, 중복·자동 배포·저자 홍보·독립 언급을 구분하고 시간순 baseline 비교를 수행한다. Physical AI 영향력 예측·추가 가치·사용자 편익은 미검증이다. tw3 결론과 tw7 성능 수치를 혼합하지 않으며 A06과 같은 표본을 독립 근거로 중복 집계하지 않는다. 최종 판정: [토론](debate/B01.md).",
}


def main():
    rows = []
    for name in ("claims-A.md", "claims-B.md"):
        path = ROOT / name
        lines = path.read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines):
            if not re.match(r"^\| [AB]\d{2} \|", line):
                continue
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) != 9:
                continue
            if cols[0] in VERDICTS:
                cols[7], cols[8] = "조건부 적용", VERDICTS[cols[0]]
                lines[i] = "| " + " | ".join(cols) + " |"
            rows.append(lines[i])
        if name == "claims-A.md":
            lines = [line.replace("적용 판단 토론은 A05 1건에 대해 Advocate·Critic 각 2라운드와 Judge 판정을 수행했으며 debate/A05.md에 기록했다.",
                                  "적용 판단 토론은 A03·A05에 대해 Advocate·Critic 각 2라운드 원 발언과 Codex Judge 판정을 debate/A03.md·debate/A05.md에 기록했다.") for line in lines]
        else:
            lines = [line.replace("[B01-social.md](debate/B01-social.md)", "[B01.md](debate/B01.md)") for line in lines]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    header = """# 기술 트렌드 레이더 — 최종 claim 통합표

범위는 [scope.md](scope.md). A/B ID는 기존 조사와의 추적성을 위해 유지했다. A03·A05·B01의 최종 판정은 원래 전체 토론을 대조한 `debate/<ID>.md`를 따른다. Claude usage 소진으로 사용자가 Codex 인계를 요청하여 지정 Sonnet/Opus 대신 Codex가 판정했다. 축약 판정인 B01-social.md는 이전 기록으로 보존하며 최종 판정은 B01.md다.

‘조건부 적용’은 후보 방법의 시험을 허용하는 범위이며 Physical AI 성능이나 제품 가치가 검증됐다는 뜻이 아니다. 원문과의 인용 일치도 실험 재현을 뜻하지 않는다. A06/B01은 동일 연구·동일 표본이며 독립 근거로 중복 계산하지 않는다. API 정책은 조회일의 조건이며 이후 변경될 수 있다.

| ID | 주장 | 출처 | 직접 인용문 | 1차/2차 | 실험 조건 | 우리 조건과의 차이 | 판정 | 판정 근거 |
|---|---|---|---|---|---|---|---|---|
"""
    (ROOT / "claims.md").write_text(header + "\n".join(rows) + "\n", encoding="utf-8")
    print(f"Consolidated {len(rows)} claims; updated 3 final debate verdicts.")


if __name__ == "__main__":
    main()
