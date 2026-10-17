"""Read-only evidence and Markdown integrity audit; writes only its audit log."""
from pathlib import Path
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parent


def main():
    records = []
    for name, file_key in [("quote-verification-A.json", "source_text"),
                           ("B-quote-check.json", "file")]:
        for item in json.loads((ROOT / "sources" / name).read_text(encoding="utf-8")):
            relative = item[file_key]
            path = ROOT / relative if file_key == "source_text" else ROOT / "sources" / relative
            proc = subprocess.run(["rg", "-n", "-F", "-o", "--", item["quote"], str(path)],
                                  capture_output=True, encoding="utf-8")
            records.append({"id": item["id"], "file": str(path.relative_to(ROOT)),
                            "quote": item["quote"], "exit_code": proc.returncode,
                            "matches": proc.stdout.strip()})
    failures = [r for r in records if r["exit_code"] != 0]
    rows = []
    for name in ("claims-A.md", "claims-B.md"):
        for line in (ROOT / name).read_text(encoding="utf-8").splitlines():
            if re.match(r"^\| [AB]\d{2} \|", line):
                cols = [c.strip() for c in line.split("|")[1:-1]]
                if len(cols) != 9:
                    continue  # Quote-audit appendix tables reuse claim IDs.
                assert cols[7] in {"그대로 적용", "조건부 적용", "적용 불가", "확인 불가"}
                rows.append(cols[0])
    assert len(rows) == 27 and len(set(rows)) == 27
    source_texts = [p.read_text(encoding="utf-8") for p in (ROOT / "sources").iterdir()
                    if p.suffix in {".md", ".txt"}]
    debate_count = 0
    for claim_id in ("A03", "A05", "B01"):
        judge = (ROOT / "debate" / f"{claim_id}.md").read_text(encoding="utf-8")
        assert "인용문 대조 결과" in judge
        assert "최종 판정" in judge
        for role in ("advocate", "critic"):
            original = (ROOT / "debate" / f"{claim_id}-{role}.md").read_text(encoding="utf-8").strip()
            assert original in judge, (claim_id, role, "full original missing")
            quotes = [q for q in re.findall(r'"([^"\n]+)"', original)
                      if re.search("[a-zA-Z]", q) and not re.search(r"[\uac00-\ud7a3]", q)
                      and len(q.split()) > 3]
            for quote in quotes:
                assert any(quote in text for text in source_texts), (claim_id, quote)
            debate_count += len(quotes)
    assert debate_count == 59
    output = {"claim_count": len(rows), "quote_count": len(records),
              "debate_quote_occurrences": debate_count,
              "debate_full_rounds_preserved": True,
              "failure_count": len(failures), "records": records}
    (ROOT / "sources" / "continuation-audit.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Claims: {len(rows)}; exact quote excerpts: {len(records)}; failures: {len(failures)}")
    print(f"Debate quotes: {debate_count}; original rounds preserved: 6/6")
    assert not failures, failures


if __name__ == "__main__":
    main()
