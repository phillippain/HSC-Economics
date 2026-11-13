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
    EX = json.loads((HERE / "data" / "explanations.json").read_text(encoding="utf8")) if (HERE / "data" / "explanations.json").exists() else {}
    used, checks = set(), {}
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
        e = EX.get(q["id"])
        if e:
            wrong = [l for l in "ABCD" if l not in q["k"]]
            assert e.get("why") and sorted(e.get("not", {})) == wrong, f"{q['id']}: explanation must have 'why' and a note for each wrong option {wrong}"
            q["e"] = {"why": e["why"], "not": e["not"]}; used.add(q["id"])
            if e.get("check"):
                checks[q["id"]] = e["check"]  # teacher note: shown on review.html only, never in the drill
        qs.append(q)
    fws = [{"id": f["id"], "sub": f["sub"], "topics": [
        {"id": t["id"], "label": t.get("label", ""), "name": t["name"], "color": t["color"],
         "sections": [{"id": x["id"], "name": x["name"], "points": x["points"]} for x in t["sections"] if not x.get("skills")]}
        for t in f["topics"]]} for f in (fw["h09"], fw["y12"])]
    assert not set(EX) - used, f"explanations for unknown questions: {sorted(set(EX) - used)}"
    out = {"q": qs, "fw": fws, "xwalk": syl["xwalk"], "nokey": sorted(nokey)}
    html = (HERE / "template.html").read_text(encoding="utf8")
    html = html.replace("/*__FONTS__*/", FONTS.read_text(encoding="utf8") if FONTS.exists() else "")
    html = html.replace("__DATA__", json.dumps(out, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))
    build.checks = checks
    return html, out


def review(out):
    """Teacher review sheet: every written explanation on one printable page."""
    import html as H
    e = H.escape
    rows, flagged = [], []
    for q in out["q"]:
        if "e" not in q:
            continue
        opts = "".join(f'<li class="{"k" if l in q["k"] else ""}"><b>{l}</b> {e(o)}'
                       + (f'<span>{e(q["e"]["why"])}</span>' if l in q["k"] else f'<span>{e(q["e"]["not"][l])}</span>') + "</li>"
                       for l, o in zip("ABCD", q["o"]))
        fig = " <i>(has a table or figure: see the drill or the Question Finder)</i>" if q.get("f") or q.get("m") else ""
        chk = build.checks.get(q["id"])
        if chk:
            flagged.append(f'<li><a href="#q{q["id"]}">HSC {q["y"]} Q{q["n"]}</a>: {e(chk)}</li>')
        fig += f'</p><p class="chk"><b>Please check:</b> {e(chk)}' if chk else ""
        rows.append(f'<section id="q{q["id"]}"><h2>HSC {q["y"]} Q{q["n"]} <small>answer {" or ".join(q["k"])} · {" ".join(q["c"])}</small></h2><p>{e(q["q"])}{fig}</p><ol>{opts}</ol></section>')
    n = len(rows)
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Multiple Choice Drill: explanations for review</title><style>body{font:16px/1.5 system-ui,sans-serif;max-width:860px;margin:24px auto;padding:0 16px;color:#101a3a}'
            'h1{font-size:1.5rem}h2{font-size:1.05rem;margin:22px 0 4px;border-top:1px solid #d8deee;padding-top:14px}small{font-weight:400;color:#4a5578}'
            'ol{list-style:none;padding:0;margin:8px 0}li{margin:6px 0;padding:6px 10px;border:1px solid #d8deee;border-radius:8px}li.k{border-color:#17693a;background:#eef8f1}'
            'li span{display:block;color:#33405f;font-size:.93rem}.chk{background:#fff3c9;border:1px solid #d9ad16;border-radius:8px;padding:6px 10px;font-size:.93rem}section{break-inside:avoid}</style></head><body>'
            f'<h1>Multiple Choice Drill: explanations for review</h1><p>{n} of {len(out["q"])} questions have an explanation. The green option is the NESA answer; the note under it is the '
            '"why", and the note under each other option says why it is wrong. These were written for the site, not by NESA. To change one, edit <code>multiple-choice-drill/data/explanations.json</code> '
            'and run <code>python3 multiple-choice-drill/build.py</code>.</p>'
            + (f'<h2>Flagged for your check ({len(flagged)})</h2><ul>{"".join(flagged)}</ul>' if flagged else "") + "".join(rows) + "</body></html>")


if __name__ == "__main__":
    html, out = build()
    target = HERE / "index.html"
    if "--check" in sys.argv:
        ok = target.exists() and target.read_text(encoding="utf8") == html
        print("multiple-choice-drill/index.html is up to date" if ok else "multiple-choice-drill/index.html is OUT OF DATE: run multiple-choice-drill/build.py")
        sys.exit(0 if ok else 1)
    target.write_text(html, encoding="utf8")
    (HERE / "review.html").write_text(review(out), encoding="utf8")
    q = out["q"]
    print(f'Wrote {target} ({len(html)//1024} KB): {len(q)} questions from {len({x["y"] for x in q})} papers, '
          f'{sum(1 for x in q if x.get("f"))} with a table or figure, {sum(1 for x in q if x.get("m"))} with an option table, '
          f'{sum(1 for x in q if len(x["k"]) > 1)} with two accepted answers, {sum(1 for x in q if not x["c"])} untagged.'
          + f' {sum(1 for x in q if x.get("e"))} with an explanation.'
          + (f' Left out (no answer key yet): {out["nokey"]}.' if out['nokey'] else ''))
