"""Read the Worksheet Maker's question bank (worksheet-maker/bank/*.txt) and write the review page.

The bank is plain text so it can be edited in any text editor. bank/README.md has the full format;
in short, every question starts with a line `=== <type> <id>`, then `key: value` lines, then the body:

    === mc mc-2C2-01
    c: 2C.2
    lv: 2
    Q: Which of the following would increase the demand for Australian dollars?
    A: Australians buying more imported cars
    B: A rise in the world price of iron ore
    C: Australian super funds buying US shares
    D: Lower interest rates in Australia
    ANS: B
    WHY: Overseas buyers need more Australian dollars to pay for the same exports.
"""
import html
import re
from pathlib import Path

FORMATS = {"mc", "sa", "er", "stim", "draw", "label", "read", "match", "cloze", "tf", "sort", "compare", "error", "chain"}
DEFAULT_M = {"mc": 1, "sa": 4, "er": 20, "draw": 4, "label": 4, "sort": 4, "compare": 6, "error": 4, "chain": 4}
DEFAULT_K = {"mc": [], "sa": ["explain"], "er": ["discuss"], "draw": ["diagram"], "label": ["diagram"], "read": ["diagram", "calc"],
             "sort": ["compare"], "compare": ["compare"], "error": ["evaluate"], "tf": ["recall"], "chain": ["explain"]}
KEYS = ("Q", "A", "B", "C", "D", "ANS", "WHY", "LEAD", "TABLE", "PTS", "PLAN", "CATS", "COLS", "TEXT", "DIA", "TITLE", "TRIGGER", "WORDS", "NOTE")
KEY_RE = re.compile(r"^(" + "|".join(KEYS) + r"):\s?(.*)$")
PART_RE = re.compile(r"^PART\s+(\([a-z]+\)(?:\([ivx]+\))?)\s+(\d+)\s*:\s*(.*)$")
HEAD_RE = re.compile(r"^===\s+(\w+)\s+([\w.\-]+)\s*$")
META_RE = re.compile(r"^(c|m|lv|k|ss|like|checked)\s*:\s*(.*)$")


def _split(v):
    return [x for x in re.split(r"[\s,]+", v.strip()) if x]


def _table(rows):
    out = []
    for r in rows:
        cells = [c.strip() for c in r.strip().strip("|").split("|")]
        out.append(cells)
    return out


def parse_block(fmt, iid, lines, where, problems):
    """One block of lines -> one item (or tf statements). Returns (item or None, [tf statements])."""
    x = {"id": "bk:" + iid, "src": "bank", "f": fmt, "c": [], "k": list(DEFAULT_K.get(fmt, [])), "rev": 1}
    fields, lists, table, parts = {}, {}, None, []
    cur_key, cur_list = None, None
    tfs = []
    for raw in lines:
        ln = raw.rstrip()
        if not ln.strip():
            cur_key = None if cur_key not in ("WHY", "ANS", "Q", "TEXT", "LEAD") else cur_key
            continue
        m = META_RE.match(ln)
        if m and not fields and not parts and cur_list is None:
            k, v = m.group(1), m.group(2).strip()
            if k == "c":
                x["c"] = _split(v)
            elif k == "m":
                x["m"] = int(v)
            elif k == "lv":
                x["lv"] = int(v)
            elif k == "k":
                x["k"] = _split(v)
            elif k == "ss":
                x["ss"] = _split(v)
            elif k == "like":
                x["like"] = _split(v)
            elif k == "checked":
                x["rev"] = 0 if v.strip().lower() in ("yes", "y", "true", "1") else 1
            continue
        pm = PART_RE.match(ln)
        if pm:
            parts.append({"label": pm.group(1), "m": int(pm.group(2)), "q": pm.group(3).strip()})
            cur_key, cur_list = "PARTQ", None
            continue
        km = KEY_RE.match(ln)
        if km:
            k, v = km.group(1), km.group(2)
            cur_list = None
            if k == "TABLE":
                table = {"cap": v.strip(), "rows": []}
                cur_key = "TABLE"
            elif k in ("PTS", "PLAN"):
                target = parts[-1] if parts else fields
                target.setdefault(k, [])
                if v.strip():
                    target[k].append(v.strip())
                cur_key, cur_list = k, target[k]
            else:
                target = parts[-1] if (parts and k in ("ANS", "WHY")) else fields
                target[k] = v.strip()
                cur_key = k
            continue
        if ln.lstrip().startswith("|") and cur_key == "TABLE":
            table["rows"].append(ln)
            continue
        if ln.lstrip().startswith("- "):
            item = ln.lstrip()[2:].strip()
            if cur_list is not None:
                cur_list.append(item)
            else:
                lists.setdefault("-", []).append(item)
            continue
        # a continuation line
        if cur_list is not None and cur_list:
            cur_list[-1] += " " + ln.strip()
        elif cur_key == "PARTQ" and parts:
            parts[-1]["q"] += " " + ln.strip()
        elif cur_key and cur_key not in ("TABLE",):
            target = parts[-1] if (parts and cur_key in ("ANS", "WHY")) else fields
            target[cur_key] = (target.get(cur_key, "") + " " + ln.strip()).strip()
        elif lists.get("-"):
            lists["-"][-1] += " " + ln.strip()
        else:
            problems.append(f"{where}: {iid}: stray line {ln!r}")

    def need(*keys):
        for k in keys:
            if not fields.get(k):
                problems.append(f"{where}: {iid}: missing {k}:")

    if not x["c"]:
        problems.append(f"{where}: {iid}: no dot points (c:)")
    if table:
        x["table"] = {"cap": table["cap"], "rows": _table(table["rows"])}
        if len(x["table"]["rows"]) < 2:
            problems.append(f"{where}: {iid}: a table needs a heading row and at least one row")
    if fields.get("LEAD"):
        x["lead"] = fields["LEAD"]
    if fields.get("NOTE"):
        x["note"] = fields["NOTE"]

    if fmt == "mc":
        need("Q", "A", "B", "C", "D", "ANS")
        x["q"] = fields.get("Q", "")
        x["o"] = [fields.get(L, "") for L in "ABCD"]
        x["key"] = _split(fields.get("ANS", ""))
        if not x["key"] or any(k not in "ABCD" for k in x["key"]):
            problems.append(f"{where}: {iid}: ANS must be A, B, C or D")
        if fields.get("WHY"):
            x["e"] = {"why": fields["WHY"], "not": {}}
        x.setdefault("m", 1)
    elif fmt in ("sa", "read"):
        if parts:
            x["parts"] = [{"label": p["label"], "m": p["m"], "q": p["q"], "pts": p.get("PTS", []), "ans": p.get("ANS", "")} for p in parts]
            x["m"] = sum(p["m"] for p in parts)
            for p in x["parts"]:
                if not p["pts"] and not p["ans"]:
                    problems.append(f"{where}: {iid} {p['label']}: give PTS: or ANS:")
        else:
            need("Q")
            x["q"] = fields.get("Q", "")
            x["pts"] = fields.get("PTS", [])
            if fields.get("ANS"):
                x["ans"] = fields["ANS"]
            if not x["pts"] and not x.get("ans"):
                problems.append(f"{where}: {iid}: give PTS: or ANS:")
            x.setdefault("m", DEFAULT_M.get(fmt, 4))
        if fmt == "read":
            need("DIA")
            x["dia"] = fields.get("DIA", "")
    elif fmt == "er":
        need("Q")
        x["q"] = fields.get("Q", "")
        x["pts"] = fields.get("PTS", [])
        if fields.get("PLAN"):
            x["plan"] = fields["PLAN"]
        x["m"] = x.get("m", 20)
    elif fmt in ("draw", "label"):
        need("DIA", "Q")
        x["dia"], x["q"] = fields.get("DIA", ""), fields.get("Q", "")
        if fields.get("ANS"):
            x["ans"] = fields["ANS"]
        x.setdefault("m", DEFAULT_M[fmt])
    elif fmt == "sort":
        need("Q", "CATS")
        x["q"] = fields.get("Q", "")
        x["cats"] = [c.strip() for c in fields.get("CATS", "").split("|") if c.strip()]
        x["rows"] = []
        for it in lists.get("-", []):
            if "=>" not in it:
                problems.append(f"{where}: {iid}: sort line needs '=> category': {it!r}")
                continue
            t, cat = [s.strip() for s in it.split("=>", 1)]
            if cat not in x["cats"]:
                problems.append(f"{where}: {iid}: {cat!r} is not one of CATS")
            x["rows"].append({"t": t, "cat": cat})
        x.setdefault("m", max(2, round(len(x["rows"]) / 2)))
    elif fmt == "compare":
        need("Q", "COLS")
        x["q"] = fields.get("Q", "")
        x["cols"] = [c.strip() for c in fields.get("COLS", "").split("|")]
        x["rows"] = []
        for it in lists.get("-", []):
            if "=>" not in it:
                problems.append(f"{where}: {iid}: compare line needs 'heading => cell | cell': {it!r}")
                continue
            h, cells = it.split("=>", 1)
            cells = [c.strip() for c in cells.split("|")]
            if len(cells) != len(x["cols"]):
                problems.append(f"{where}: {iid}: row {h.strip()!r} has {len(cells)} cells for {len(x['cols'])} columns")
            x["rows"].append({"h": h.strip(), "cells": [{"t": c.lstrip("!").strip(), "given": c.startswith("!")} for c in cells]})
        x.setdefault("m", len(x["rows"]))
    elif fmt == "error":
        need("TEXT")
        x["q"] = fields.get("Q", "")
        x["text"] = fields.get("TEXT", "")
        errs = re.findall(r"\[\[(.+?)=>(.+?)\]\]", x["text"])
        if not errs:
            problems.append(f"{where}: {iid}: TEXT needs at least one [[wrong => right]]")
        x["n"] = len(errs)
        x.setdefault("m", len(errs))
    elif fmt == "tf":
        for it in lists.get("-", []):
            mm = re.match(r"^(T|F)\s*:\s*(.*)$", it)
            if not mm:
                problems.append(f"{where}: {iid}: true/false lines start '- T:' or '- F:': {it!r}")
                continue
            if mm.group(1) == "T":
                stmt, _, why = mm.group(2).partition("=>")
                tfs.append({"id": f"tf:{iid}:{len(tfs)}", "c": x["c"], "t": stmt.strip(), "f": None, "why": why.strip()})
            else:
                if "=>" not in mm.group(2):
                    problems.append(f"{where}: {iid}: a false statement needs '=> correction': {it!r}")
                    continue
                f, t = [s.strip() for s in mm.group(2).split("=>", 1)]
                tfs.append({"id": f"tf:{iid}:{len(tfs)}", "c": x["c"], "t": t, "f": f, "why": ""})
        return None, tfs
    elif fmt == "chain":
        need("TRIGGER")
        x["title"] = fields.get("TITLE", "")
        x["trigger"] = fields.get("TRIGGER", "")
        x["steps"] = []
        for it in lists.get("-", []):
            mm = re.match(r"^(.*?)=>\s*(up|down)\s*(?:\|\s*(.*))?$", it)
            if not mm:
                problems.append(f"{where}: {iid}: chain lines are '- variable => up | why': {it!r}")
                continue
            x["steps"].append({"v": mm.group(1).strip(), "d": 1 if mm.group(2) == "up" else -1, "why": (mm.group(3) or "").strip()})
        x.setdefault("m", len(x["steps"]))
    else:
        problems.append(f"{where}: {iid}: unknown type {fmt!r}")
    return x, tfs


def load(folder, points):
    """Every *.txt file in the bank folder. A file whose first line is "# reviewed" has been checked by the
    teacher: its questions lose the "not yet reviewed" flag. One question can be marked with "checked: yes"."""
    items, tfs, problems = [], [], []
    for path in sorted(Path(folder).glob("*.txt")):
        block, head = [], None
        text = path.read_text(encoding="utf8")
        reviewed = text.lstrip().lower().startswith("# reviewed")
        lines = text.splitlines() + ["=== end end"]
        first_item = len(items)
        for i, ln in enumerate(lines, 1):
            m = HEAD_RE.match(ln)
            if m:
                if head:
                    fmt, iid, start = head
                    if fmt not in FORMATS:
                        problems.append(f"{path.name}:{start}: unknown type {fmt!r}")
                    else:
                        x, t = parse_block(fmt, iid, block, f"{path.name}:{start}", problems)
                        if x:
                            items.append(x)
                        tfs.extend(t)
                head, block = (m.group(1), m.group(2), i), []
            elif head:
                block.append(ln)
            elif ln.strip() and not ln.startswith("#"):
                problems.append(f"{path.name}:{i}: text before the first === line")
        if reviewed:
            for x in items[first_item:]:
                x["rev"] = 0
    for x in items + tfs:
        bad = [c for c in x["c"] if c not in points]
        if bad:
            problems.append(f"{x['id']}: unknown dot points {bad}")
    return items, tfs, problems


# ---------------------------------------------------------------- the teacher's review page
NAMES = {"mc": "Multiple choice", "sa": "Short answer", "er": "Extended response", "draw": "Draw a diagram",
         "label": "Label a diagram", "read": "Read a diagram", "sort": "Sort and classify", "compare": "Compare table",
         "error": "Spot the error", "chain": "Cause and effect chain"}


def review_page(items, tfs, points, dias=None):
    e = html.escape

    def tbl(t):
        if not t:
            return ""
        rows = t["rows"]
        return ('<table><thead><tr>' + "".join(f"<th>{e(c)}</th>" for c in rows[0]) + "</tr></thead><tbody>"
                + "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>" for r in rows[1:]) + "</tbody></table>")

    def ul(xs):
        return "<ul>" + "".join(f"<li>{e(v)}</li>" for v in xs) + "</ul>" if xs else ""

    def err_html(text):
        return re.sub(r"\[\[(.+?)=&gt;(.+?)\]\]", r'<s>\1</s> <ins>\2</ins>', e(text))

    out, toc = [], {}
    items = [x for x in items if x.get("rev")]
    for x in items:
        toc.setdefault(x["f"], 0)
        toc[x["f"]] += 1
        body = ""
        if x.get("lead"):
            body += f"<p>{e(x['lead'])}</p>"
        body += tbl(x.get("table"))
        if x.get("dia") and dias and x["dia"] in dias:
            dd = dias[x["dia"]]
            body += f'<div class="dia"><figure>{dd["s"]}<figcaption>Student copy</figcaption></figure><figure>{dd["a"]}<figcaption>Answer</figcaption></figure></div>'
        if x["f"] == "mc":
            body += f"<p>{e(x['q'])}</p><ol type='A'>" + "".join(
                f"<li class='{'k' if L in x['key'] else ''}'>{e(o)}</li>" for L, o in zip("ABCD", x["o"])) + "</ol>"
            if x.get("e"):
                body += f"<p class='why'><b>Why {'/'.join(x['key'])}:</b> {e(x['e']['why'])}</p>"
        elif x.get("parts"):
            for p in x["parts"]:
                body += f"<p><b>{e(p['label'])}</b> {e(p['q'])} <small>({p['m']} marks)</small></p>{ul(p['pts'])}"
                if p.get("ans"):
                    body += f"<p class='why'>{e(p['ans'])}</p>"
        elif x["f"] in ("sa", "er", "draw", "label", "read"):
            body += f"<p>{e(x.get('q', ''))}</p>{ul(x.get('pts'))}"
            if x.get("plan"):
                body += "<p><b>Plan</b></p>" + ul(x["plan"])
            if x.get("ans"):
                body += f"<p class='why'>{e(x['ans'])}</p>"
        elif x["f"] == "sort":
            body += f"<p>{e(x['q'])}</p><table><thead><tr><th>Item</th><th>Category</th></tr></thead><tbody>" + "".join(
                f"<tr><td>{e(r['t'])}</td><td>{e(r['cat'])}</td></tr>" for r in x["rows"]) + "</tbody></table>"
        elif x["f"] == "compare":
            body += f"<p>{e(x['q'])}</p><table><thead><tr><th></th>" + "".join(f"<th>{e(c)}</th>" for c in x["cols"]) + "</tr></thead><tbody>" + "".join(
                "<tr><th>" + e(r["h"]) + "</th>" + "".join(f"<td>{'<i>(given)</i> ' if c['given'] else ''}{e(c['t'])}</td>" for c in r["cells"]) + "</tr>"
                for r in x["rows"]) + "</tbody></table>"
        elif x["f"] == "error":
            body += f"<p>{e(x.get('q') or '')}</p><p class='err'>{err_html(x['text'])}</p>"
        elif x["f"] == "chain":
            body += f"<p><b>{e(x['title'])}</b>: {e(x['trigger'])}</p><ol>" + "".join(
                f"<li>{e(s['v'])} {'↑' if s['d'] > 0 else '↓'} <small>{e(s['why'])}</small></li>" for s in x["steps"]) + "</ol>"
        like = f" · modelled on {' '.join(x['like'])}" if x.get("like") else ""
        out.append(f'<section id="{e(x["id"])}"><h2>{e(NAMES.get(x["f"], x["f"]))} <small>{e(x["id"][3:])} · '
                   f'{e(" ".join(x["c"]))} · {x.get("m", "")} marks · level {x.get("lv", "-")}{e(like)}</small></h2>{body}</section>')
    tfo = "".join(f"<li><b>{'False' if t['f'] else 'True'}:</b> {e(t['f'] or t['t'])}"
                  + (f" <ins>→ {e(t['t'])}</ins>" if t["f"] else "") + f" <small>{e(' '.join(t['c']))}</small></li>" for t in tfs)
    counts = " · ".join(f"{NAMES.get(k, k)} {v}" for k, v in sorted(toc.items()))
    return ('<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="robots" content="noindex">'
            '<meta name="viewport" content="width=device-width,initial-scale=1"><title>Worksheet Maker: new questions for review</title>'
            '<style>body{font:15px/1.5 system-ui,sans-serif;max-width:900px;margin:24px auto;padding:0 16px;color:#101a3a}'
            'h1{font-size:1.5rem}h2{font-size:1rem;margin:22px 0 6px;border-top:1px solid #d8deee;padding-top:14px}small{font-weight:400;color:#4a5578}'
            'table{border-collapse:collapse;margin:8px 0;font-size:14px}td,th{border:1px solid #c9d2e4;padding:4px 8px;text-align:left;vertical-align:top}'
            'th{background:#eef2fb}li.k{font-weight:700;color:#17693a}.why{background:#eef8f1;border-left:3px solid #17693a;padding:4px 10px}'
            '.err s{color:#b42318}.err ins{color:#17693a;text-decoration:none;font-weight:700}ins{color:#17693a;text-decoration:none}'
            '.dia{display:flex;gap:16px;flex-wrap:wrap}.dia figure{margin:0;width:300px}.dia figcaption{font-size:12px;color:#4a5578}'
            'section{break-inside:avoid}</style></head><body><h1>Worksheet Maker: new questions for review</h1>'
            f'<p>These {len(items)} questions and {len(tfs)} true/false statements were written for the Worksheet Maker by Claude and have not yet been checked. '
            'Each shows its answer. To change one, edit the file in <code>worksheet-maker/bank/</code> named in the heading and run '
            '<code>python3 worksheet-maker/build.py</code>. When you have checked a whole file, make its first line <code># reviewed</code>; to clear one question, add the line <code>checked: yes</code> under its heading. Checked questions drop off this page and lose the “not yet reviewed” label on the worksheet page.</p>'
            f'<p>{e(counts)}</p>' + "".join(out) + f'<h2>True or false statements ({len(tfs)})</h2><ul>{tfo}</ul></body></html>')
