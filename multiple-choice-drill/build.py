#!/usr/bin/env python3
"""Build multiple-choice-drill/index.html from template.html.

    python3 multiple-choice-drill/build.py           # write index.html
    python3 multiple-choice-drill/build.py --check   # change nothing; fail if index.html is out of date

Every question, option, figure and answer key is read from the Question Finder
(hsc-question-finder-site/index.html), so the drill never holds its own copy. Figure
images are loaded from ../hsc-question-finder-site/figs/. Rebuild after the Question Finder changes.
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QF = REPO / "hsc-question-finder-site" / "index.html"
SYL = REPO / "evidence-finder" / "data" / "syllabus.json"
FONTS = REPO / "evidence-finder" / "build" / "fonts.css"

# dot point -> Calculation Trainer skill, used for questions tagged as calculations
CALC = {"3A.4": "realgdp", "1C.2": "tariff", "2B.1": "cab", "2B.2": "bop", "2B.3": "bop", "2B.4": "tot", "3D.1": "nfl",
        "3A.3": "mult", "3A.2": "leak", "3B.1": "labour", "3C.1": "infl", "3C.3": "infl", "3E.1": "gini", "4C.1": "budget"}


def build():
    s = QF.read_text(encoding="utf8")
    i = s.index("const DATA =")
    D = json.JSONDecoder().raw_decode(s[s.index("{", i):])[0]
    syl = json.loads(SYL.read_text(encoding="utf8"))
    fw = {f["id"]: f for f in syl["frameworks"]}
    points = {p["id"] for f in ("h09",) for t in fw[f]["topics"] for sec in t["sections"] for p in sec["points"]}
    qs, nokey = [], set()
    for it in D["items"]:
        if it["s"] != "I":
            continue
        y, n = str(it["y"]), str(it["q"])
        m = D["mcq"].get(y, {}).get(n)
        key = D["key"].get(y, {}).get(n)
        assert m and len(m["o"]) == 4, f"{y} Q{n}: no question text or not four options"
        if not key:  # paper added before NESA published its marking guidelines: leave it out until there is a key
            nokey.add(it["y"])
            continue
        assert re.fullmatch(r"[A-D]( and [A-D])?", key), f"{y} Q{n}: bad answer key {key!r}"
        figs = D["figs"].get(y, {}).get("I", {}).get(n, [])
        q = {"id": f"{y}-{n}", "y": it["y"], "n": it["q"], "q": m["q"], "o": [o[1] for o in m["o"]], "k": key.split(" and "),
             "c": [c for c in it["c"] if c in points], "t": it["t"]}
        mat = next((b for b in figs if b["t"] == "opt"), None)
        if mat:
            assert [r[0] for r in mat["rows"]] == ["A", "B", "C", "D"], f"{y} Q{n}: option table rows"
            q["m"] = {"head": mat["head"], "rows": [r[1:] for r in mat["rows"]]}
            assert all(len(r) == len(mat["head"]) for r in q["m"]["rows"]), f"{y} Q{n}: option table columns"
        rest = [b for b in figs if b["t"] != "opt"]
        if rest:
            q["f"] = rest
        if "calc" in it["k"]:
            sk = next((CALC[c] for c in it["c"] if c in CALC), None)
            q["calc"] = sk or ""
        qs.append(q)
    fws = [{"id": f["id"], "sub": f["sub"], "topics": [
        {"id": t["id"], "label": t.get("label", ""), "name": t["name"], "color": t["color"],
         "sections": [{"id": x["id"], "name": x["name"], "points": x["points"]} for x in t["sections"] if not x.get("skills")]}
        for t in f["topics"]]} for f in (fw["h09"], fw["y12"])]
    out = {"q": qs, "fw": fws, "xwalk": syl["xwalk"], "nokey": sorted(nokey)}
    html = (HERE / "template.html").read_text(encoding="utf8")
    html = html.replace("/*__FONTS__*/", FONTS.read_text(encoding="utf8") if FONTS.exists() else "")
    html = html.replace("__DATA__", json.dumps(out, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))
    return html, out


if __name__ == "__main__":
    html, out = build()
    target = HERE / "index.html"
    if "--check" in sys.argv:
        ok = target.exists() and target.read_text(encoding="utf8") == html
        print("multiple-choice-drill/index.html is up to date" if ok else "multiple-choice-drill/index.html is OUT OF DATE: run multiple-choice-drill/build.py")
        sys.exit(0 if ok else 1)
    target.write_text(html, encoding="utf8")
    q = out["q"]
    print(f'Wrote {target} ({len(html)//1024} KB): {len(q)} questions from {len({x["y"] for x in q})} papers, '
          f'{sum(1 for x in q if x.get("f"))} with a table or figure, {sum(1 for x in q if x.get("m"))} with an option table, '
          f'{sum(1 for x in q if len(x["k"]) > 1)} with two accepted answers, {sum(1 for x in q if not x["c"])} untagged.'
          + (f' Left out (no answer key yet): {out["nokey"]}.' if out['nokey'] else ''))
