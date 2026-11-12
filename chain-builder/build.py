#!/usr/bin/env python3
"""Build chain-builder/index.html from template.html and data/chains.json.

    python3 chain-builder/build.py           # write index.html
    python3 chain-builder/build.py --check   # change nothing; fail if index.html is out of date

data/chains.json is the one list of chains: edit a link, a reason or a limit there, then run this.
Past questions come from the Question Finder, statistics from the Evidence Finder, hover
definitions from the Glossary and dot points from the shared syllabus file, so none is held twice.
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QF = REPO / "hsc-question-finder-site" / "index.html"
EV = REPO / "evidence-finder" / "data" / "evidence.json"
SYL = REPO / "evidence-finder" / "data" / "syllabus.json"
FONTS = REPO / "evidence-finder" / "build" / "fonts.css"
GLOSS = REPO / "glossary" / "data" / "glossary.json"


def questions():
    s = QF.read_text(encoding="utf8")
    i = s.index("const DATA =")
    return [q for q in json.JSONDecoder().raw_decode(s[s.index("{", i):])[0]["items"] if q["s"] in ("II", "III", "IV")]


def build():
    data = json.loads((HERE / "data" / "chains.json").read_text(encoding="utf8"))
    syl = json.loads(SYL.read_text(encoding="utf8"))
    fw = {f["id"]: f for f in syl["frameworks"]}
    points, topics, secs = {}, [], {}
    for t in fw["h09"]["topics"]:
        topics.append({"id": t["id"], "label": t["label"], "name": t["name"], "color": t["color"]})
        for s in t["sections"]:
            for p in s["points"]:
                points[p["id"]] = {"t": p["t"], "color": t["color"]}
    for t in fw["y12"]["topics"]:
        for s in t["sections"]:
            secs[s["id"]] = {"name": s["name"], "color": t["color"]}
    qs, ev = questions(), json.loads(EV.read_text(encoding="utf8"))
    tids = {t["id"] for t in topics}
    for c in data["chains"]:
        assert c["topic"] in tids, f'{c["id"]}: unknown topic {c["topic"]}'
        for code in c["codes"]:
            assert code in points, f'{c["id"]}: {code} is not a 2009 syllabus dot point'
        links = c["stem"] + [l for s in c["strands"] for l in s["links"]] + c["tail"]
        assert c["strands"] and all(l["v"] and l["why"] and l["d"] in (1, -1, 0) for l in links), f'{c["id"]}: incomplete link'
        cs = set(c["codes"])
        hit = [(len(cs & set(q["c"])) + (2 if q["s"] != "II" else 0), q) for q in qs if cs & set(q["c"]) and (q["s"] != "II" or q["m"] >= 4)]
        hit.sort(key=lambda x: (-x[0], -x[1]["y"], x[1]["l"]))
        c["qs"] = [{"k": f'{q["s"]}-{q["y"]}-{q["q"]}', "s": q["s"], "y": q["y"], "l": q["l"], "m": q["m"], "t": q["t"]} for _, q in hit[:6]]
    gl = [{"id": t["id"], "term": t["term"], "def": t["def"]} for t in json.loads(GLOSS.read_text(encoding="utf8"))["terms"]] if GLOSS.exists() else []
    figs = [{"id": r["id"], "date": r.get("date", ""), "about": r.get("about", {}).get("h09", []), "also": r.get("also", {}).get("h09", []),
             "figures": [{k: f.get(k, "") for k in ("label", "value", "asAt", "source")} for f in r.get("figures", [])[:3]]}
            for r in sorted(ev, key=lambda r: r.get("date", ""), reverse=True)
            if any(set(r.get("about", {}).get("h09", [])) & set(c["codes"]) for c in data["chains"])][:120]
    out = {"updated": data["updated"], "chains": data["chains"], "topics": topics, "points": points, "secs": secs,
           "xwalk": syl["xwalk"], "gloss": gl, "ev": figs}
    html = (HERE / "template.html").read_text(encoding="utf8")
    html = html.replace("/*__FONTS__*/", FONTS.read_text(encoding="utf8") if FONTS.exists() else "")
    html = html.replace("__DATA__", json.dumps(out, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))
    return html, out


if __name__ == "__main__":
    html, out = build()
    target = HERE / "index.html"
    if "--check" in sys.argv:
        ok = target.exists() and target.read_text(encoding="utf8") == html
        print("chain-builder/index.html is up to date" if ok else "chain-builder/index.html is OUT OF DATE: run chain-builder/build.py")
        sys.exit(0 if ok else 1)
    target.write_text(html, encoding="utf8")
    n = sum(len(c["stem"]) + len(c["tail"]) + sum(len(s["links"]) for s in c["strands"]) for c in out["chains"])
    print(f'Wrote {target} ({len(html)//1024} KB): {len(out["chains"])} chains, {n} links, {len(out["gloss"])} glossary terms for hover, {len(out["ev"])} evidence items.')
