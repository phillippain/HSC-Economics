#!/usr/bin/env python3
"""Build the Worksheet Maker: data.json (every question it can put on a worksheet), index.html and review.html.

    python3 worksheet-maker/build.py           # write data.json, index.html and review.html
    python3 worksheet-maker/build.py --check   # change nothing; fail if any of them is out of date
    python3 worksheet-maker/build.py --report  # also print how many questions each dot point has, by type

Where the questions come from (nothing is copied by hand, so a rebuild picks up every change):
  * Past HSC questions, figures, NESA marking criteria and answer keys: hsc-question-finder-site/index.html
  * Why each multiple-choice answer is right: multiple-choice-drill/data/explanations.json
  * Questions on this year's news and data: evidence-finder/data/evidence.json
  * Key terms: glossary/data/glossary.json (terms are matched to dot points in bank/maps.json)
  * Cause and effect chains: chain-builder/data/chains.json
  * Pathways (put the steps in order): mind-map/index.html
  * Calculations: the generators in calculation-trainer/template.html (copied into the page)
  * The new practice questions written for this tool: worksheet-maker/bank/*.txt (see bank/README.md)
  * Diagrams: drawn here from the specs in bank/*.txt with build/econ_diagrams.py (the house style)

Rebuild after any of those change. The page also reads the Evidence Finder live when it opens,
so news filed after the last build still appears on the site.
"""
import hashlib, html, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(HERE / "build"))
import bank as BANK          # noqa: E402  the bank parser (build/bank.py)
import diagrams as DIA       # noqa: E402  diagram specs -> SVG (build/diagrams.py)

QF = REPO / "hsc-question-finder-site" / "index.html"
SYL = REPO / "evidence-finder" / "data" / "syllabus.json"
EVID = REPO / "evidence-finder" / "data" / "evidence.json"
GLOSS = REPO / "glossary" / "data" / "glossary.json"
CHAINS = REPO / "chain-builder" / "data" / "chains.json"
MAP = REPO / "mind-map" / "index.html"
CALC = REPO / "calculation-trainer" / "template.html"
MCEX = REPO / "multiple-choice-drill" / "data" / "explanations.json"
FONTS = REPO / "evidence-finder" / "build" / "fonts.css"

CHECK, REPORT = "--check" in sys.argv, "--report" in sys.argv
ARTIFACT = Path(sys.argv[sys.argv.index("--artifact") + 1]) if "--artifact" in sys.argv else None
SITE = "https://phillippain.github.io/HSC-Economics/"


def js_object(src, name):
    """Read `const NAME = {...}` (strict JSON) out of a page."""
    m = re.search(r"(?:const|let|var)\s+" + name + r"\s*=\s*", src)
    return json.JSONDecoder().raw_decode(src[m.end():])[0]


def joined(lines):
    """NESA sample answers come as the PDF's lines: join them back into prose."""
    out = ""
    for ln in lines or []:
        ln = ln.strip()
        if not ln:
            continue
        if out.endswith("-") and not out.endswith(" -"):
            out = out[:-1] + ln
        else:
            out = (out + " " + ln).strip()
    return out


def clean(s):
    return re.sub(r"\s+", " ", str(s or "")).strip()


FOOTER = re.compile(r"\s*(?:BOSTES|NESA|Board of Studies)\s+\d{4}\s+HSC\s+Economics\s+Marking\s+Guidelines\.?", re.I)
GRID = re.compile(r"^(?:Question\s+Marks\s+Content|Mapping\s+Grid)|Examination\s+Mapping\s+Grid|^\d+\s*(?:\([a-z]+\))*\s*\d+\s+Topic\s+\d", re.I)
JOIN_AFTER = re.compile(r"\b(?:the|a|an|of|and|or|to|in|on|for|with|by|as|which|that|may|will|be|its|their|from|than|is|are)$", re.I)


def could_list(items):
    """NESA's 'answers could include' lists, without the page footer or the mapping grid that follows them in the PDF."""
    out = []
    for a in items or []:
        a = clean(FOOTER.sub("", a))
        if GRID.search(a):
            break
        if a and out and (a[0].islower() or out[-1].endswith(("-", ",")) or JOIN_AFTER.search(out[-1])):
            out[-1] = (out[-1][:-1] if out[-1].endswith("-") else out[-1] + " ") + a   # a bullet that ran onto the next line
        elif a:
            out.append(a)
    return out


# ---------------------------------------------------------------- past HSC questions
def hsc_items(D, EX):
    items = []
    syl_ok = {d["c"] for t in D["syl"] for h in t["h"] for d in h["d"]}
    crit = D["crit"]
    figs = D["figs"]
    for it in D["items"]:
        y, s, lab = it["y"], it["s"], it["l"]
        base = {"id": s + str(y) + lab, "src": "hsc", "y": y, "sec": s, "l": lab, "n": it["q"],
                "c": [c for c in it["c"] if c in syl_ok], "k": it["k"], "m": it["m"]}
        if it.get("p"):
            base["ss"] = [it["p"]]
        if s == "I":
            mc = D["mcq"].get(str(y), {}).get(str(it["q"]))
            if not mc or len(mc["o"]) != 4:
                continue
            key = D["key"].get(str(y), {}).get(str(it["q"]))
            fb = figs.get(str(y), {}).get("I", {}).get(str(it["q"]), [])
            x = dict(base, f="mc", q=clean(mc["q"]), o=[clean(o[1]) for o in mc["o"]])
            if key:
                x["key"] = key.split(" and ")
            else:
                x["note"] = clean(it["t"])          # 2026: NESA has not published the key yet
            mat = next((b for b in fb if b["t"] == "opt"), None)
            if mat:
                x["mat"] = {"head": mat["head"], "rows": [r[1:] for r in mat["rows"]]}
            rest = [b for b in fb if b["t"] != "opt"]
            if rest:
                x["fig"] = rest
            e = EX.get(f"{y}-{it['q']}")
            if e:
                x["e"] = {"why": e["why"], "not": e.get("not", {})}
            items.append(x)
            continue
        cr = crit.get(f"{y}|{lab}")
        if s == "II":
            s2 = D["s2"].get(str(y), {}).get(lab) or {}
            x = dict(base, f="sa", q=clean(s2.get("t") or it["t"]))
            if s2.get("lead"):
                x["lead"] = clean(s2["lead"])
            fb = figs.get(str(y), {}).get("II", {}).get(str(it["q"]), [])
            mine = [b for b in fb if not b.get("show") or lab in b["show"]]
            if mine:
                x["fig"] = [{k: v for k, v in b.items() if k != "show"} for b in mine]
            x["grp"] = f"{y}-{it['q']}"
            x["part"] = lab[len("Q" + str(it["q"])):] or ""
        else:
            x = dict(base, f="er", q=clean(it["t"]))
            fb = figs.get(str(y), {}).get("III", {}).get(str(it["q"]), []) if s == "III" else []
            if fb:
                x["fig"] = fb
        st = clean(it.get("st"))
        if st and not st.lower().startswith("no stimulus") and not x.get("fig"):
            x["st"] = st                            # the paper's stimulus, described (no image held)
        if cr:
            x["crit"] = cr["c"]
            if cr.get("s"):
                x["samp"] = clean(FOOTER.sub("", joined(cr["s"])))
            if cr.get("a"):
                x["could"] = could_list(cr["a"])
        items.append(x)
    return items


# ---------------------------------------------------------------- this year's news (Evidence Finder)
def evidence_items(E, points):
    items = []
    for e in E:
        qs = [q for q in (e.get("questions") or []) if q.get("q")]
        c = [p for p in (e.get("about") or {}).get("h09", []) if p in points]
        if not qs or not c:
            continue
        figs = [{"label": clean(f.get("label")), "value": clean(f.get("value")), "asAt": clean(f.get("asAt")),
                 "source": clean(f.get("source"))} for f in (e.get("figures") or [])][:6]
        x = {"id": "ev:" + e["id"], "src": "ev", "f": "stim", "c": c, "c25": (e.get("about") or {}).get("y12", []),
             "date": e["date"], "title": clean(e["title"]), "outlets": e.get("outlets") or [], "lede": clean(e.get("lede")),
             "figs": figs, "qs": [{"q": clean(q["q"]), "m": int(q.get("marks") or 2)} for q in qs[:4]],
             "guide": clean(e.get("angle")), "terms": [{"term": t["term"], "def": t["def"]} for t in (e.get("terms") or [])][:4],
             "k": ["stimulus", "extract"] + (["table"] if figs else [])}
        x["m"] = sum(q["m"] for q in x["qs"])
        items.append(x)
    return items


# ---------------------------------------------------------------- cause and effect (Chain Builder, Topic Map)
UPDOWN = {1: "rises", -1: "falls"}


def chain_items(C):
    items, tf = [], []
    for ch in C["chains"]:
        for si, st in enumerate(ch["strands"]):
            steps = ch["stem"] + st["links"]
            items.append({"id": f"ch:{ch['id']}:{si}", "src": "auto", "f": "chain", "c": ch["codes"], "k": ["explain"],
                          "title": ch["title"], "strand": st["name"], "trigger": ch["trigger"],
                          "steps": [{"v": s["v"], "d": s["d"], "why": s["why"]} for s in steps], "m": len(steps)})
            items.append({"id": f"or:{ch['id']}:{si}", "src": "auto", "f": "order", "c": ch["codes"], "k": ["explain"],
                          "title": f"{ch['title']}: {st['name'].lower()}", "blurb": ch["trigger"],
                          "steps": [f"{s['v']} {'rises' if s['d'] > 0 else 'falls'}" for s in steps], "m": len(steps)})
            for s in st["links"]:
                tf.append({"id": f"tf:{ch['id']}:{si}:{s['v'][:24]}", "c": ch["codes"],
                           "t": f"{ch['title']}: {s['v'][0].lower() + s['v'][1:]} {UPDOWN[s['d']]}.",
                           "f": f"{ch['title']}: {s['v'][0].lower() + s['v'][1:]} {UPDOWN[-s['d']]}.", "why": s["why"]})
    return items, tf


def pathway_items(M, node_map):
    labels = {n["id"]: n["label"] for t in M["topics"] for g in t["groups"] for n in g["nodes"]}
    items = []
    for i, p in enumerate(M["pathways"]):
        c = sorted({dp for nid in p["ids"] for dp in node_map.get(nid, [])})
        items.append({"id": f"pw:{i}", "src": "auto", "f": "order", "c": c, "k": ["explain"], "title": p["title"],
                      "blurb": p["blurb"], "steps": [labels.get(n, n) for n in p["ids"]], "closing": p["closing"],
                      "m": len(p["ids"])})
    return items


# ---------------------------------------------------------------- calculation generators
def calc_code():
    s = CALC.read_text(encoding="utf8")
    a = s.index("/* ---------- helpers ---------- */")
    b = s.index("const BY = Object.fromEntries")
    code = s[a:b]
    assert "const SK = [" in code and "let RNG" in code, "Calculation Trainer generators not found"
    return code


def main():
    s = QF.read_text(encoding="utf8")
    D = js_object(s, "DATA")
    syl = json.loads(SYL.read_text(encoding="utf8"))
    fw = {f["id"]: f for f in syl["frameworks"]}
    EX = json.loads(MCEX.read_text(encoding="utf8")) if MCEX.exists() else {}
    maps = json.loads((HERE / "bank" / "maps.json").read_text(encoding="utf8"))
    points = {p["id"]: p["t"] for t in fw["h09"]["topics"] for sec in t["sections"] for p in sec["points"]}

    items = hsc_items(D, EX)
    items += evidence_items(json.loads(EVID.read_text(encoding="utf8")), points)
    ch_items, tf = chain_items(json.loads(CHAINS.read_text(encoding="utf8")))
    items += ch_items
    items += pathway_items(js_object(MAP.read_text(encoding="utf8"), "D"), maps["nodes"])

    G = json.loads(GLOSS.read_text(encoding="utf8"))["terms"]
    gmap = maps["terms"]
    missing = [t["id"] for t in G if t["id"] not in gmap]
    assert not missing, f"glossary terms with no dot point in bank/maps.json: {missing}"
    gloss = [{"id": t["id"], "term": t["term"], "def": clean(t["def"]), "c": gmap[t["id"]]} for t in G]

    bank_items, bank_tf, problems = BANK.load(HERE / "bank", points)
    assert not problems, "bank problems:\n  " + "\n  ".join(problems)
    specs = list(DIA.BASE) + [x["dia"] for x in bank_items if x.get("dia")]
    dias = {}
    for sp in specs:
        if sp not in dias:
            try:
                dias[sp] = {"s": DIA.render(sp, answer=False), "a": DIA.render(sp, answer=True)}
            except Exception as err:
                raise SystemExit(f"diagram {sp!r}: {err}")
    for x in bank_items:
        if x["f"] == "label":
            x["labels"] = DIA.label_pairs(x["dia"])
            x.setdefault("m", len(x["labels"]))
    items += bank_items
    tf += bank_tf

    ids = [x["id"] for x in items]
    dup = {i for i in ids if ids.count(i) > 1}
    assert not dup, f"duplicate ids: {sorted(dup)[:10]}"
    for x in items:
        bad = [c for c in x["c"] if c not in points]
        assert not bad, f"{x['id']}: unknown dot points {bad}"

    calc = maps["calc"]
    trees = {}
    for key in ("h09", "y12"):
        f = fw[key]
        trees[key] = [{"id": t["id"], "label": t.get("label", ""), "name": t["name"], "color": t["color"],
                       "sections": [{"id": x["id"], "name": x["name"], "skills": bool(x.get("skills")),
                                     "points": [{"id": p["id"], "t": p["t"]} for p in x["points"]]} for x in t["sections"]]}
                      for t in f["topics"]]
    data = {"built": "", "prac": D["prac"] + [{"k": "recall", "n": "Recall key terms"}],
            "syl": trees, "xwalk": syl["xwalk"], "gloss": gloss, "tf": tf, "calc": calc, "dias": dias,
            "papers": {str(y): u for y, u in sorted(paper_links(s).items())}, "items": items}
    body = json.dumps({k: v for k, v in data.items() if k != "items"}, ensure_ascii=False, separators=(",", ":"))
    lines = ",\n".join(json.dumps(x, ensure_ascii=False, separators=(",", ":")) for x in items)
    digest = hashlib.sha1((body + lines).encode()).hexdigest()[:10]
    data_txt = body[:-1].replace('"built":""', f'"built":"{digest}"') + ',"items":[\n' + lines + "\n]}\n"

    page = (HERE / "template.html").read_text(encoding="utf8")
    page = page.replace("/*__FONTS__*/", FONTS.read_text(encoding="utf8") if FONTS.exists() else "")
    page = page.replace("/*__CALC__*/", calc_code()).replace("__DATAVER__", digest)
    review = BANK.review_page(bank_items, bank_tf, points, dias)

    outs = {HERE / "data.json": data_txt, HERE / "index.html": page, HERE / "review.html": review}
    if CHECK:
        stale = [p.name for p, t in outs.items() if not p.exists() or p.read_text(encoding="utf8") != t]
        print("worksheet-maker is up to date" if not stale else f"worksheet-maker is OUT OF DATE ({', '.join(stale)}): run worksheet-maker/build.py")
        sys.exit(1 if stale else 0)
    for p, t in outs.items():
        p.write_text(t, encoding="utf8")
    by = {}
    for x in items:
        by[x["src"] + "/" + x["f"]] = by.get(x["src"] + "/" + x["f"], 0) + 1
    print(f"Wrote data.json ({len(data_txt)//1024} KB, version {digest}): {len(items)} questions; "
          f"{len(gloss)} key terms, {len(tf)} true/false statements, {len(calc)} calculation skills.")
    print("  " + ", ".join(f"{k} {v}" for k, v in sorted(by.items())))
    print(f"Wrote index.html ({len(page)//1024} KB) and review.html ({len(bank_items)} new questions for review).")
    if REPORT:
        coverage(items, gloss, tf, calc, points)
    if ARTIFACT:
        write_artifact(ARTIFACT, page, data_txt)


def write_artifact(out, page, data_txt):
    """A copy for Claude (a claude.ai artifact): every file it needs in one folder, no site menu or analytics,
    figures from its own figs/ folder, and links to the other tools pointing at the class site."""
    import shutil
    out.mkdir(parents=True, exist_ok=True)
    art = re.sub(r"<!-- GA:START.*?<!-- GA:END -->\n?", "", page, flags=re.S)
    art = re.sub(r"[ \t]*<!-- SITEMENU:START.*?<!-- SITEMENU:END -->\n?", "", art, flags=re.S)
    art = art.replace("../hsc-question-finder-site/", SITE + "hsc-question-finder-site/")
    # The PDF libraries load from the CDN artifacts allow (the same files as lib/, pinned), not from the artifact.
    cdn = "https://cdn.jsdelivr.net/npm/"
    libs = (f"window.WM_LIB = {{ pdfmake: '{cdn}pdfmake@0.2.23/build/pdfmake.min.js', "
            f"pdfjs: '{cdn}pdfjs-dist@3.11.174/build/pdf.min.js', worker: '{cdn}pdfjs-dist@3.11.174/build/pdf.worker.min.js', onPage: true }};")
    art = art.replace("<script>\n/* Calculation generators", "<script>window.WM_FIGBASE = 'figs/'; window.WM_LIVE_EVIDENCE = false; " + libs + "</script>\n<script>\n/* Calculation generators", 1)
    assert "WM_LIB" in art, "could not add the artifact settings to the page"
    (out / "index.html").write_text(art, encoding="utf8")
    (out / "data.json").write_text(data_txt, encoding="utf8")
    shutil.copytree(HERE / "fonts", out / "fonts", dirs_exist_ok=True)
    figs = REPO / "hsc-question-finder-site" / "figs"
    (out / "figs").mkdir(exist_ok=True)
    for f in figs.glob("*.webp"):
        shutil.copy2(f, out / "figs" / f.name)
    n = sum(1 for _ in out.rglob("*") if _.is_file())
    print(f"Wrote the Claude copy to {out} ({n} files)")


def paper_links(src):
    """The paper links the Question Finder uses (2015 on: the NESA page; earlier: the archive)."""
    out = {}
    m = re.search(r"const PAPER = \{(.*?)\};", src, re.S)
    for y, u in re.findall(r"(\d{4}):'([^']+)'", m.group(1) if m else ""):
        out[int(y)] = u if u.startswith("http") else "../hsc-question-finder-site/" + u
    for y in range(2015, 2027):
        out[y] = f"https://www.nsw.gov.au/education-and-training/nesa/curriculum/hsc-exam-papers/economics/{y}"
    return out


GROUPS = {"exam": ("mc", "sa", "stim", "er"), "dc": ("calc", "draw", "label", "read"),
          "know": ("match", "cloze", "define", "tf"), "think": ("chain", "order", "sort", "compare", "error")}


def coverage(items, gloss, tf, calc, points):
    print("\nDot point   exam(hsc/new/news)  diagrams+calcs  key terms  thinking")
    for p in points:
        def n(fmts, src=None):
            return sum(1 for x in items if p in x["c"] and x["f"] in fmts and (src is None or x["src"] == src))
        g = sum(1 for t in gloss if p in t["c"]) + sum(1 for t in tf if p in t["c"])
        cc = sum(1 for c in calc if p in c["c"])
        print(f"{p:<10} {n(GROUPS['exam'],'hsc'):>4}/{n(GROUPS['exam'],'bank'):>3}/{n(GROUPS['exam'],'ev'):>3}"
              f"   {n(GROUPS['dc']) + cc:>12}   {g:>9}   {n(GROUPS['think']):>8}")


if __name__ == "__main__":
    main()
