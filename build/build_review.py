#!/usr/bin/env python3
"""Teacher review sheets: everything Claude wrote for the tools, one printable page per tool.

    python3 build/build_review.py

Writes review/index.html and a page for each tool whose content is not already covered by its own
build (the Multiple Choice Drill and the two Explorers write their own review.html). The pages are
generated from the tools' data files and templates, so run this again after changing any of them.
They are not linked from the student menu and carry a noindex tag, but they are public to anyone
with the address.
"""
import ast, json, re, html as H
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "review"
e = H.escape
CSS = ("body{font:16px/1.5 system-ui,sans-serif;max-width:900px;margin:24px auto;padding:0 16px;color:#0b1330}h1{font-size:1.6rem}h2{border-top:2px solid #c9d2e4;padding-top:12px;margin-top:26px;font-size:1.25rem}"
       "h3{font-size:1.02rem;margin:14px 0 4px}h4{font-size:.9rem;margin:10px 0 2px;text-transform:uppercase;letter-spacing:.04em;color:#3b4663}li{margin:3px 0}ul,ol{margin:2px 0;padding-left:1.3rem}"
       "table{border-collapse:collapse;width:100%}td,th{border:1px solid #c9d2e4;padding:4px 8px;text-align:left;vertical-align:top;font-size:.93rem}.up{color:#1c7d52;font-weight:700}.dn{color:#c93a22;font-weight:700}"
       ".box{background:#fff3c9;border:1px solid #d9ad16;border-radius:8px;padding:8px 12px}.card{border:1px solid #c9d2e4;border-radius:10px;padding:10px 14px;margin:8px 0}pre{white-space:pre-wrap;font:14px/1.45 ui-monospace,monospace}"
       "section{break-inside:avoid}@media print{a{color:inherit}}")

def page(name, title, intro, body):
    (OUT / name).write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title><style>{CSS}</style></head>'
                            f'<body><p><a href="index.html">All review sheets</a></p><h1>{e(title)}</h1><p>{intro}</p>{body}</body></html>', encoding="utf8")

def show(o, depth=3):
    """Generic renderer for JSON content."""
    if isinstance(o, dict):
        return "".join(f"<h{min(depth, 4)}>{e(str(k))}</h{min(depth, 4)}>{show(v, depth + 1)}" for k, v in o.items() if v not in (None, "", [], {}))
    if isinstance(o, list):
        if all(not isinstance(x, (dict, list)) for x in o):
            return "<ul>" + "".join(f"<li>{e(str(x))}</li>" for x in o) + "</ul>"
        if all(isinstance(x, list) and all(not isinstance(y, (dict, list)) for y in x) for x in o):
            return "<table>" + "".join("<tr>" + "".join(f"<td>{e(str(y))}</td>" for y in x) + "</tr>" for x in o) + "</table>"
        return "".join(f'<div class="card">{show(x, depth)}</div>' for x in o)
    return f"<p>{e(str(o))}</p>"

def chains():
    data = json.loads((ROOT / "chain-builder/data/chains.json").read_text(encoding="utf8"))["chains"]
    arrow = lambda d: '<span class="up">▲ rises</span>' if d > 0 else '<span class="dn">▼ falls</span>' if d < 0 else "changes"
    links = lambda ls: "<ol>" + "".join(f'<li><b>{e(l["v"])}</b> {arrow(l.get("d", 0))}: {e(l.get("why", ""))}</li>' for l in ls) + "</ol>"
    body = []
    for c in data:
        b = f'<section><h2>{e(c["title"])}</h2><p><i>{e(c.get("short", ""))}</i> · dot points {e(", ".join(c.get("codes", [])))} · reverse: {e(str(c.get("reverse") or "none"))}</p><p><b>Trigger:</b> {e(c["trigger"])}</p><h3>Start of the chain</h3>{links(c.get("stem", []))}'
        for s in c.get("strands", []):
            b += f'<h3>Strand: {e(s["name"])}</h3>{links(s["links"])}'
        if c.get("tail"): b += f'<h3>End of the chain</h3>{links(c["tail"])}'
        if c.get("overall"): b += f'<p><b>Overall:</b> {e(c["overall"])}</p>'
        b += f'<p><b>How long it takes:</b> {e(c.get("lag", ""))}</p><h3>Where the chain can break</h3><ul>' + "".join(f"<li>{e(x)}</li>" for x in c.get("limits", [])) + f'</ul><p><b>Diagram:</b> {e(str(c.get("diagram", "")))}</p></section>'
        body.append(b)
    page("chain-builder.html", "Chain Builder: content for review", f"{len(data)} chains. Edit <code>chain-builder/data/chains.json</code>, then run the Chain Builder build.", "".join(body))
    return len(data)

def simulator():
    eps = json.loads((ROOT / "policy-simulator/data/episodes.json").read_text(encoding="utf8"))["episodes"]
    body = []
    for ep in eps:
        keep = {k: v for k, v in ep.items() if k not in ("id", "color", "path", "chain", "lab", "title", "period")}
        for k in ("monetary", "fiscal"):
            if k in keep:
                m = dict(keep[k]); m["options"] = [("✔ " if i == m.get("actual") else "") + o for i, o in enumerate(m["options"])]; m.pop("actual", None); keep[k] = m
        body.append(f'<section><h2>{e(ep["title"])} ({e(ep["period"])})</h2>{show(keep)}</section>')
    fig = ROOT / "policy-simulator/FIGURES-TO-CHECK.md"
    body.append(f'<h2>Figures and how each was verified</h2><div class="box">Figures marked "From memory" below still need checking against a source.</div><pre>{e(fig.read_text(encoding="utf8")) if fig.exists() else ""}</pre>')
    page("policy-simulator.html", "Policy Simulator: content for review", f"{len(eps)} episodes. A tick marks the option that was actually chosen. Edit <code>policy-simulator/data/episodes.json</code>, then run its build.", "".join(body))
    return len(eps)

def glossary():
    ts = json.loads((ROOT / "glossary/data/glossary.json").read_text(encoding="utf8"))["terms"]
    new = [t for t in ts if t.get("added")]; rev = [t for t in ts if t.get("revised")]
    row = lambda t: f'<tr><td><b>{e(t["term"])}</b><br><small>{e(", ".join(t.get("topics", [])))} · {e(str(t.get("added") or t.get("revised")))}</small></td><td>{e(t["def"])}</td></tr>'
    page("glossary.html", "Glossary: added and revised definitions for review",
         f"{len(new)} definitions were written for the site and {len(rev)} booklet definitions were revised; the other {len(ts) - len(new) - len(rev)} are from the Year 12 Economics Booklet. Edit <code>glossary/data/glossary.json</code>, then run the Glossary build and <code>build/build_hover.py</code>.",
         "<h2>Added</h2><table>" + "".join(map(row, new)) + "</table><h2>Revised from the booklet</h2><table>" + "".join(map(row, rev)) + "</table>")
    return len(new) + len(rev)

def macro():
    src = (ROOT / "macro-diagram-lab/template.html").read_text(encoding="utf8").split("\n")
    body, n, name, on = [], 0, None, False
    for ln in src:
        m = re.match(r"\s+\w+: \{ name: '([^']+)', sub: '([^']*)'", ln)
        if m: name = f"{m.group(1)}: {m.group(2)}"
        if re.match(r"\s+sc: \[\s*$", ln): on = True; body.append(f"<h2>{e(name or '')}</h2><table><tr><th>Scenario</th><th>Answer</th><th>Reason shown</th></tr>"); continue
        if on:
            s = ln.strip().rstrip(",")
            if not s.startswith("["): on = False; body.append("</table>"); continue
            try: row = ast.literal_eval(s)
            except Exception: body.append(f"<tr><td colspan=3>{e(s)}</td></tr>"); continue
            ans = " ".join(str(x) for x in row[1:-1]).replace("dn", "demand-side curve").replace("up", "supply-side curve").replace("-1", "shifts left / falls").replace("1", "shifts right / rises")
            body.append(f"<tr><td>{e(str(row[0]))}</td><td>{e(ans)}</td><td>{e(str(row[-1]))}</td></tr>"); n += 1
    page("macro-diagram-lab.html", "Macro Diagram Lab: scenarios for review", f"{n} scenarios, read from <code>macro-diagram-lab/template.html</code> (the <code>sc</code> lists in the <code>DG</code> object). The answer column is the raw key: which curve moves and in which direction.", "".join(body))
    return n

def trainer():
    src = (ROOT / "calculation-trainer/template.html").read_text(encoding="utf8")
    parts = re.split(r"\n \{ id: '", src)[1:]
    clean = lambda s: re.sub(r"\s+", " ", re.sub(r"\$\{[^{}]*(\{[^{}]*\}[^{}]*)*\}", "[…]", re.sub(r"<[^>]+>", " ", s))).strip()
    body, n = [], 0
    for p in parts:
        m = re.match(r"(\w+)', topic: '(\w+)', name: '([^']+)', formula: \[(.*?)\],\s*\n", p, re.S)
        if not m: continue
        forms = re.findall(r"'((?:[^'\\]|\\.)*)'", m.group(4)); end = p.find("\n];")
        blk = p[:end] if end > 0 else p
        qs = [clean(q) for q in re.findall(r"q: `((?:[^`\\]|\\.)*)`", blk)]; watch = re.findall(r"watch: '((?:[^'\\]|\\.)*)'", blk) + re.findall(r'watch: "((?:[^"\\]|\\.)*)"', blk) + [clean(w) for w in re.findall(r"watch: `((?:[^`\\]|\\.)*)`", blk)]
        n += len(qs)
        body.append(f'<section><h2>{e(m.group(3))} <small>({m.group(2)})</small></h2><h3>Formula as shown</h3><ul>' + "".join(f"<li>{e(f)}</li>" for f in forms) + "</ul><h3>Question wording</h3><ul>" + "".join(f"<li>{e(q)}</li>" for q in qs)
                    + "</ul><h3>Watch out for</h3><ul>" + "".join(f"<li>{e(w.replace(chr(92), ''))}</li>" for w in watch) + "</ul></section>")
    page("calculation-trainer.html", "Calculation Trainer: wording for review", f"{len(body)} skills and {n} question wordings, read from <code>calculation-trainer/template.html</code>. Numbers are generated at random, so each […] stands for a number, table or phrase filled in when the question is drawn. To see finished questions, use the trainer itself.", "".join(body))
    return n

def main():
    OUT.mkdir(exist_ok=True)
    rows = [("chain-builder.html", "Chain Builder", f"{chains()} cause-and-effect chains: every link and its reason"),
            ("policy-simulator.html", "Policy Simulator", f"{simulator()} episodes: briefings, options, what was decided and why, plus the figures still to verify"),
            ("glossary.html", "Glossary", f"{glossary()} added or revised definitions"),
            ("macro-diagram-lab.html", "Macro Diagram Lab", f"{macro()} scenarios and their answers"),
            ("calculation-trainer.html", "Calculation Trainer", f"{trainer()} question wordings, formulas and tips"),
            ("../multiple-choice-drill/review.html", "Multiple Choice Drill", "340 answer explanations, flagged ones first"),
            ("../exchange-rate-explorer/review.html", "Exchange Rate Explorer", "the four systems, the shocks and Australia's history"),
            ("../bop-explorer/review.html", "Balance of Payments Explorer", "24 transactions, 8 shocks and the real data table")]
    (OUT / "index.html").write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta name="viewport" content="width=device-width,initial-scale=1"><title>HSC Economics tools: review sheets</title><style>{CSS}</style></head><body>'
        '<h1>HSC Economics tools: review sheets</h1><p>Everything written for the tools rather than taken from NESA, the booklet or a published source, one printable page per tool. Read a sheet, then tell Claude what to change (quote the heading and the sentence), or edit the data file named at the top of the sheet and rebuild.</p>'
        '<table><tr><th>Tool</th><th>What is on the sheet</th></tr>' + "".join(f'<tr><td><a href="{h}"><b>{e(t)}</b></a></td><td>{e(d)}</td></tr>' for h, t, d in rows) + '</table>'
        '<p>Not on these sheets because they come from a source: HSC questions, keys and criteria (NESA), booklet definitions and scaffolds, Evidence Finder items (each links to its source), and Economy at a glance figures (ABS and RBA). The 2026 dot-point tags in the Question Finder are also worth a look.</p></body></html>', encoding="utf8")
    print("review sheets written to review/: " + ", ".join(r[1] for r in rows[:5]))

if __name__ == "__main__":
    main()
