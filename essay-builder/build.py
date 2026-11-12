#!/usr/bin/env python3
"""Build essay-builder/index.html from template.html.

Reads the questions and marking criteria out of the Question Finder page and the
evidence and syllabus out of the Evidence Finder data, so the builder never holds
its own copy of either. Run from anywhere:  python3 essay-builder/build.py
Add --check to change nothing and fail if index.html is out of date.
"""
import json, re, sys, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QF = REPO / "hsc-question-finder-site" / "index.html"
EV = REPO / "evidence-finder" / "data" / "evidence.json"
SYL = REPO / "evidence-finder" / "data" / "syllabus.json"
FONTS = REPO / "evidence-finder" / "build" / "fonts.css"


def qf_data():
    s = QF.read_text(encoding="utf8")
    i = s.index("const DATA =")
    data = json.JSONDecoder().raw_decode(s[s.index("{", i):])[0]
    papers = {int(y): u for y, u in re.findall(r"(\d{4}):'(https?://[^']+)'", s[s.index("const PAPER"):s.index("const PAPER") + 6000])}
    return data, papers


def trim_item(r):
    return {
        "id": r["id"], "title": r["title"], "date": r.get("date", ""), "type": r.get("type", ""),
        "summary": r.get("summary", ""),
        "about": {k: r.get("about", {}).get(k, []) for k in ("h09", "y12")},
        "also": {k: r.get("also", {}).get(k, []) for k in ("h09", "y12")},
        "issues": r.get("issues", []), "diagrams": r.get("diagrams", []),
        "figures": [{k: f.get(k, "") for k in ("label", "value", "asAt", "source", "issue")} for f in r.get("figures", [])],
    }


def build():
    D, papers = qf_data()
    syl = json.loads(SYL.read_text(encoding="utf8"))
    ev = json.loads(EV.read_text(encoding="utf8"))
    qs = []
    for it in D["items"]:
        if it["s"] not in ("II", "III", "IV"):
            continue
        q = {k: it[k] for k in ("s", "y", "q", "l", "m", "t", "c", "k")}
        if it.get("st") and not it["st"].lower().startswith("no stimulus"):
            q["st"] = it["st"]
        if it.get("ns"):
            q["ns"] = 1
        lead = (D.get("s2", {}).get(str(it["y"]), {}).get(it["l"]) or {}).get("lead")
        if lead:
            q["lead"] = lead
        crit = D["crit"].get(f'{it["y"]}|{it["l"]}')
        if crit and crit.get("c"):
            q["crit"] = crit["c"]
        qs.append(q)
    fws = []
    for f in syl["frameworks"]:
        if f["id"] not in ("h09", "y12"):
            continue
        fws.append({"id": f["id"], "label": f["label"], "sub": f["sub"], "topics": [
            {"id": t["id"], "name": t["name"], "label": t.get("label", ""), "color": t["color"],
             "sections": [{"id": s["id"], "name": s["name"], "points": s["points"]} for s in t["sections"] if not s.get("skills")]}
            for t in f["topics"]]})
    out = {
        "built": datetime.date.today().isoformat(),
        "q": qs, "fw": fws, "xwalk": syl["xwalk"], "issues": syl["issues"],
        "papers": papers,
        "mg": sorted(int(p.stem[3:]) for p in QF.parent.glob("mg-*.pdf")),
        "ev": [trim_item(r) for r in ev],
    }
    html = (HERE / "template.html").read_text(encoding="utf8")
    html = html.replace("/*__FONTS__*/", FONTS.read_text(encoding="utf8") if FONTS.exists() else "")
    html = html.replace("__DATA__", json.dumps(out, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))
    return html, out


if __name__ == "__main__":
    html, out = build()
    target = HERE / "index.html"
    if "--check" in sys.argv:
        strip = lambda s: re.sub(r'"built":"[^"]*"', "", s)
        ok = target.exists() and strip(target.read_text(encoding="utf8")) == strip(html)
        print("index.html is up to date" if ok else "index.html is OUT OF DATE: run build.py")
        sys.exit(0 if ok else 1)
    target.write_text(html, encoding="utf8")
    n = {s: sum(1 for q in out["q"] if q["s"] == s) for s in ("II", "III", "IV")}
    print(f'Wrote {target} ({len(html)//1024} KB): {n["II"]} short-answer parts, {n["III"]} Section III and {n["IV"]} Section IV questions, '
          f'{len(out["ev"])} evidence items with {sum(len(e["figures"]) for e in out["ev"])} statistics.')
