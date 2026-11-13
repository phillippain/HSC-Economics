#!/usr/bin/env python3
"""Build bop-explorer/index.html from template.html and data/bop.json.

    python3 bop-explorer/build.py           # write index.html (and review.html)
    python3 bop-explorer/build.py --check   # change nothing; fail if index.html is out of date

data/bop.json holds the transactions to sort, the shocks to trace and Australia's record
(real data: see history.source). The 24 transactions are sized so the finished balance of
payments sums to zero; the build checks that. Past HSC questions come from the Question Finder.
"""
import json, sys, html as H
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
FONTS = REPO / "evidence-finder" / "build" / "fonts.css"
QF = REPO / "hsc-question-finder-site" / "index.html"
ACC = {"goods": "Goods", "services": "Services", "primary": "Primary income", "secondary": "Secondary income", "capital": "Capital account", "financial": "Financial account"}

data = json.loads((HERE / "data" / "bop.json").read_text(encoding="utf8"))
tot = {a: 0 for a in ACC}
for x in data["tx"]:
    assert x["a"] in ACC and x["s"] in ("cr", "dr") and x["v"] > 0, x
    tot[x["a"]] += x["v"] if x["s"] == "cr" else -x["v"]
assert sum(tot.values()) == 0, f"the transactions must balance: {tot}"
b = data["base"]
assert tot["goods"] + tot["services"] == b["bogs"] and tot["primary"] == b["primary"] and tot["secondary"] == b["secondary"] and tot["capital"] == b["capital"], "base must match the transactions"
for s in data["shocks"]:
    for k in ("now", "later"):
        assert set(s[k]["why"]) <= {"bogs", "primary", "rate"}, s["id"]
assert all(len(r) == 3 for r in data["history"]["rows"])
src = QF.read_text(encoding="utf8"); i = src.index("const DATA = ") + 13
qf, _ = json.JSONDecoder().raw_decode(src[i:])
data["hsc"] = [{"y": it["y"], "s": it["s"], "l": it["l"], "m": it["m"], "t": it["t"]}
               for it in sorted(qf["items"], key=lambda it: (-it["y"], it["q"], it["l"])) if it["s"] != "I" and any(c.startswith("2B") for c in it["c"])]
page = (HERE / "template.html").read_text(encoding="utf8")
page = page.replace("/*__FONTS__*/", FONTS.read_text(encoding="utf8") if FONTS.exists() else "")
page = page.replace("__DATA__", json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))

def review():
    e = H.escape
    rate = {"up": "appreciates", "down": "depreciates", "same": "little change"}
    out = ['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Balance of Payments Explorer: content for review</title>'
           '<style>body{font:16px/1.5 system-ui,sans-serif;max-width:900px;margin:24px auto;padding:0 16px;color:#0b1330}h2{border-top:1px solid #c9d2e4;padding-top:12px;margin-top:22px}table{border-collapse:collapse;width:100%}td,th{border:1px solid #c9d2e4;padding:4px 8px;text-align:left;vertical-align:top;font-size:.93rem}li{margin:3px 0}</style></head><body>'
           '<h1>Balance of Payments Explorer: content for review</h1><p>' + e(data["note"]) + ' Edit <code>bop-explorer/data/bop.json</code> and rebuild to change anything.</p>'
           '<h2>Transactions to sort</h2><table><tr><th>Transaction</th><th>Account</th><th>Side</th><th>$bn</th><th>Reason shown</th></tr>']
    out += [f'<tr><td>{e(x["t"])}</td><td>{ACC[x["a"]]}</td><td>{"Credit" if x["s"] == "cr" else "Debit"}</td><td>{x["v"]}</td><td>{e(x["why"])}</td></tr>' for x in data["tx"]]
    out.append("</table><h2>Shocks to trace</h2><p>Changes are in $ billion from a base of goods and services +15, primary income −18, secondary income −2.</p>")
    for s in data["shocks"]:
        out.append(f'<h3>{e(s["name"])} (dollar: {rate[s["rate"]]})</h3><ul>')
        for k, lab in (("now", "At first"), ("later", "Later")):
            st = s[k]; out.append(f'<li><b>{lab}:</b> goods and services {st["bogs"]:+d}, primary income {st["primary"]:+d}. ' + " ".join(e(v) for v in st["why"].values()) + (" " + e(st["fin"]) if st.get("fin") else "") + "</li>")
        out.append("</ul>")
    h = data["history"]
    out.append(f'<h2>Australia\'s record (real data)</h2><p>{e(h["source"])}. Retrieved {e(h["retrieved"])}. {e(h["method"])}</p><table><tr><th>Year to June</th><th>Trade balance (% GDP)</th><th>Current account (% GDP)</th></tr>'
               + "".join(f"<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td></tr>" for r in h["rows"]) + "</table>"
               '<p>The structure notes and the "what to notice" points are in <code>template.html</code>.</p></body></html>')
    return "".join(out)

target = HERE / "index.html"
if "--check" in sys.argv:
    ok = target.exists() and target.read_text(encoding="utf8") == page
    print("bop-explorer/index.html is up to date" if ok else "bop-explorer/index.html is OUT OF DATE: run bop-explorer/build.py")
    sys.exit(0 if ok else 1)
target.write_text(page, encoding="utf8")
(HERE / "review.html").write_text(review(), encoding="utf8")
print(f'Wrote {target} ({len(page)//1024} KB): {len(data["tx"])} transactions, {len(data["shocks"])} shocks, {len(data["history"]["rows"])} years of data, {len(data["hsc"])} past HSC questions.')
