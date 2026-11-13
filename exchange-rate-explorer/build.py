#!/usr/bin/env python3
"""Build exchange-rate-explorer/index.html from template.html and data/systems.json.

    python3 exchange-rate-explorer/build.py           # write index.html (and review.html)
    python3 exchange-rate-explorer/build.py --check   # change nothing; fail if index.html is out of date

data/systems.json holds the four systems, the shocks and Australia's timeline. Past HSC questions on
exchange rates (2009 syllabus dot points 2C.1 to 2C.6) are read from the class Question Finder.
"""
import json, sys, html as H
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
FONTS = REPO / "evidence-finder" / "build" / "fonts.css"
QF = REPO / "hsc-question-finder-site" / "index.html"

data = json.loads((HERE / "data" / "systems.json").read_text(encoding="utf8"))
assert [s["id"] for s in data["systems"]] == ["float", "managed", "flex", "fixed"]
for s in data["systems"]:
    assert len(s["pros"]) == 3 and len(s["cons"]) == 3, s["id"]
assert len({s["id"] for s in data["shocks"]}) == len(data["shocks"])
src = QF.read_text(encoding="utf8"); i = src.index("const DATA = ") + 13
qf, _ = json.JSONDecoder().raw_decode(src[i:])
data["hsc"] = [{"y": it["y"], "s": it["s"], "l": it["l"], "m": it["m"], "t": (qf["mcq"].get(str(it["y"]), {}).get(str(it["q"]), {}).get("q") if it["s"] == "I" else it["t"]) or it["t"],
                "c": [c for c in it["c"] if c.startswith("2C")]}
               for it in sorted(qf["items"], key=lambda it: (-it["y"], it["q"], it["l"])) if any(c == "2C.4" or c == "2C.5" for c in it["c"])]
page = (HERE / "template.html").read_text(encoding="utf8")
page = page.replace("/*__FONTS__*/", FONTS.read_text(encoding="utf8") if FONTS.exists() else "")
page = page.replace("__DATA__", json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))

def review():
    e = H.escape
    out = ['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Exchange Rate Explorer: content for review</title>'
           '<style>body{font:16px/1.5 system-ui,sans-serif;max-width:860px;margin:24px auto;padding:0 16px;color:#0b1330}h2{border-top:1px solid #c9d2e4;padding-top:12px;margin-top:22px}dt{font-weight:700;margin-top:6px}dd{margin:0}li{margin:2px 0}</style></head><body>'
           '<h1>Exchange Rate Explorer: content for review</h1><p>Everything below was written for the site. Edit <code>exchange-rate-explorer/data/systems.json</code> and rebuild to change it. ' + e(data["note"]) + '</p><h2>The four systems</h2>']
    for s in data["systems"]:
        out.append(f'<h3>{e(s["name"])}: {e(s["short"])}</h3><dl>' + "".join(f"<dt>{k}</dt><dd>{e(s[f])}</dd>" for k, f in [("Who sets the rate", "who"), ("What the central bank does", "bank"), ("Reserves", "reserves"), ("Monetary policy", "money"), ("Examples", "examples")])
                   + "<dt>Advantages</dt><dd><ul>" + "".join(f"<li>{e(x)}</li>" for x in s["pros"]) + "</ul></dd><dt>Disadvantages</dt><dd><ul>" + "".join(f"<li>{e(x)}</li>" for x in s["cons"]) + "</ul></dd></dl>")
    out.append("<h2>Shocks</h2><ul>" + "".join(f'<li><b>{e(s["name"])}</b> (demand {s["dD"]:+d}, supply {s["dS"]:+d}): {e(s["why"])}</li>' for s in data["shocks"]) + "</ul>")
    out.append("<h2>Australia's exchange rate history</h2><ul>" + "".join(f'<li><b>{e(t["when"])}: {e(t["what"])}.</b> {e(t["detail"])}</li>' for t in data["timeline"]) + "</ul>")
    out.append("<p>The sentences the tool generates after each shock (what the central bank does, what it means for the economy) are in the <code>explain()</code> function in <code>template.html</code>.</p></body></html>")
    return "".join(out)

target = HERE / "index.html"
if "--check" in sys.argv:
    ok = target.exists() and target.read_text(encoding="utf8") == page
    print("exchange-rate-explorer/index.html is up to date" if ok else "exchange-rate-explorer/index.html is OUT OF DATE: run exchange-rate-explorer/build.py")
    sys.exit(0 if ok else 1)
target.write_text(page, encoding="utf8")
(HERE / "review.html").write_text(review(), encoding="utf8")
print(f'Wrote {target} ({len(page)//1024} KB): {len(data["systems"])} systems, {len(data["shocks"])} shocks, {len(data["hsc"])} past HSC questions.')
