#!/usr/bin/env python3
"""Build calculation-trainer/index.html from template.html.

    python3 calculation-trainer/build.py           # write index.html
    python3 calculation-trainer/build.py --check   # change nothing; fail if index.html is out of date

The question generators, formulas and wording are in template.html (the SK list).
This script inlines the shared fonts and adds, for each skill, the list of HSC questions
that examined it, read from the Question Finder (questions tagged as calculations).
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QF = REPO / "hsc-question-finder-site" / "index.html"
FONTS = REPO / "evidence-finder" / "build" / "fonts.css"

# skill id -> the 2009 syllabus dot points whose calculation questions it practises
CODES = {
    "growth": ["3A.4"], "realgdp": ["3A.4"], "tariff": ["1C.2"], "cab": ["2B.1"], "bop": ["2B.2", "2B.3"],
    "tot": ["2B.4"], "nfl": ["3D.1"], "mult": ["3A.3"], "leak": ["3A.2"], "labour": ["3B.1"],
    "infl": ["3C.1", "3C.3"], "gini": ["3E.1"], "budget": ["4C.1"],
}


def examined():
    s = QF.read_text(encoding="utf8")
    i = s.index("const DATA =")
    items = json.JSONDecoder().raw_decode(s[s.index("{", i):])[0]["items"]
    out = {}
    for skill, codes in CODES.items():
        hits = sorted({(q["y"], q["l"]) for q in items if "calc" in q["k"] and set(q["c"]) & set(codes)})
        out[skill] = [f"{y} {l}" for y, l in hits]
    return out


html = (HERE / "template.html").read_text(encoding="utf8")
html = html.replace("/*__FONTS__*/", FONTS.read_text(encoding="utf8") if FONTS.exists() else "")
data = {"examined": examined()}
html = html.replace("__DATA__", json.dumps(data, ensure_ascii=False, separators=(",", ":")))
target = HERE / "index.html"
if "--check" in sys.argv:
    ok = target.exists() and target.read_text(encoding="utf8") == html
    print("calculation-trainer/index.html is up to date" if ok else "calculation-trainer/index.html is OUT OF DATE: run calculation-trainer/build.py")
    sys.exit(0 if ok else 1)
target.write_text(html, encoding="utf8")
print(f'Wrote {target} ({len(html)//1024} KB): past questions listed for {sum(1 for v in data["examined"].values() if v)} skills, {sum(len(v) for v in data["examined"].values())} references.')
