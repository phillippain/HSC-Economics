#!/usr/bin/env python3
"""Build policy-simulator/index.html from template.html and data/episodes.json.

    python3 policy-simulator/build.py           # write index.html
    python3 policy-simulator/build.py --check   # change nothing; fail if index.html is out of date

data/episodes.json is the one list of episodes: edit a figure, an option or a reason there, then run this.
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FONTS = HERE.parent / "evidence-finder" / "build" / "fonts.css"

data = json.loads((HERE / "data" / "episodes.json").read_text(encoding="utf8"))
ids = set()
for e in data["episodes"]:
    assert e["id"] not in ids, f'duplicate id {e["id"]}'
    ids.add(e["id"])
    for k in ("monetary", "fiscal"):
        assert 0 <= e[k]["actual"] < len(e[k]["options"]), f'{e["id"]}: {k}.actual is not one of the options'
        assert e[k]["did"] and e[k]["why"], f'{e["id"]}: {k} needs "did" and "why"'
    assert e["diag"]["threat"] in ("inflation", "growth", "both") and e["diag"]["stance"] in ("exp", "neutral", "con")
    assert e["diag"]["source"] in ("weak", "strong", "supply", "both", "shutdown")
    assert e["sources"] and all(len(i) == 4 for i in e["indicators"]) and all(len(n) == 3 for n in e["next"])
html = (HERE / "template.html").read_text(encoding="utf8")
html = html.replace("/*__FONTS__*/", FONTS.read_text(encoding="utf8") if FONTS.exists() else "")
html = html.replace("__DATA__", json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))
target = HERE / "index.html"
if "--check" in sys.argv:
    ok = target.exists() and target.read_text(encoding="utf8") == html
    print("policy-simulator/index.html is up to date" if ok else "policy-simulator/index.html is OUT OF DATE: run policy-simulator/build.py")
    sys.exit(0 if ok else 1)
target.write_text(html, encoding="utf8")
print(f'Wrote {target} ({len(html)//1024} KB): {len(data["episodes"])} episodes.')
