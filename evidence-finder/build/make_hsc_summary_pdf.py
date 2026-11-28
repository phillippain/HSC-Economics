#!/usr/bin/env python3
"""Make a one-page A4 HSC Economics news summary PDF from a story record.

    python3 make_hsc_summary_pdf.py <record.json> <output folder> [--force]

Writes  <output folder>/12Eco_Topic N_<Short_name>.pdf  in the house style of the
teacher's news summaries (topic pill, headline, lede, What happened, stat tiles,
key terms, diagram panel, flow chart, Syllabus link, Try this, sources).
Prints one line beginning SAVED, EXISTS or ERROR (and NOTE lines for anything left out).

Needs Playwright with Chromium and the Inter font (present in Claude's cloud workspace).
Diagrams come from the hsc-econ-diagrams skill's scripts/econ_diagrams.py when it can be
found; without it the page is built with no diagram panel.

The record (JSON):
  date          "2026-11-30"                      the digest date
  topic         1-4                               the story's main HSC topic
  title         headline, under about 70 characters
  short_name    3-5 words for the file name, e.g. "RBA holds cash rate"
  sources_line  "ABC News · RBA"                  publisher names
  published     "30 Nov 2026"
  lede          one or two sentences
  what_happened 3-5 bullets; **double asterisks** make bold
  stats         up to 3 [value, label] pairs, e.g. ["4.85%", "cash rate, highest since 2008"]
  key_terms     2-3 [term, definition] pairs
  diagram       optional: {"preset": "ad_as", "args": {"shift": "SRAS left"},
                           "title": "...", "explain": "..."}   (or "svg_file": path)
  exam_angle    one or two sentences
  flow          {"title": "...", "steps": [5 short strings]}   (the last is the outcome)
  syllabus_link "Topic 4 – monetary policy: ..."
  questions     1-2 [question, marks] pairs
  sources       [label, url] pairs
"""
import glob, html, json, os, re, sys

TOPICS = {1: ("The Global Economy", "#2563EB", "#EAF1FE"),
          2: ("Australia's Place in the Global Economy", "#0D9488", "#E3F4F2"),
          3: ("Economic Issues", "#D97706", "#FDF0DD"),
          4: ("Economic Policies and Management", "#7C3AED", "#F0EAFE")}
PRESETS = {"supply_shift": {"direction", "good", "elastic_demand", "ylabel", "xlabel"},
           "demand_shift": {"direction", "good", "ylabel", "xlabel"},
           "tariff": {"good"}, "price_ceiling": {"good"}, "price_floor": {"good", "ylabel", "xlabel"},
           "subsidy": {"good"}, "ad_as": {"shift"}, "lras_growth": set(),
           "phillips": {"expectations_shift"}, "fx_market": {"show_counterfactual"},
           "lorenz": {"second"}, "ppf": {"growth"}}
REQUIRED = ("date", "topic", "title", "short_name", "sources_line", "published", "lede",
            "what_happened", "key_terms", "exam_angle", "flow", "syllabus_link", "questions", "sources")


def fmt(s):
    """Escape, then turn **bold** and X_1 style subscripts-free text into HTML."""
    s = html.escape(str(s), quote=False)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)


def file_name(rec):
    words = re.sub(r"[^A-Za-z0-9%.\- ]+", " ", str(rec["short_name"])).split()
    return f"12Eco_Topic {int(rec['topic'])}_{'_'.join(words)[:60].strip('_.')}.pdf"


def diagram_svg(rec, colour, notes):
    d = rec.get("diagram")
    if not d:
        return None
    if d.get("svg_file"):
        try:
            return open(d["svg_file"], encoding="utf-8").read()
        except OSError as e:
            notes.append(f"diagram left out: {e}")
            return None
    name, args = d.get("preset"), dict(d.get("args") or {})
    if name not in PRESETS or set(args) - PRESETS[name]:
        notes.append(f"diagram left out: unknown preset or argument ({name}, {sorted(args)})")
        return None
    here = os.path.dirname(os.path.abspath(__file__))
    cands = [os.environ.get("ECON_DIAGRAMS", ""), here] + \
        sorted(glob.glob("/root/.claude/skills/**/hsc-econ-diagrams/scripts", recursive=True)) + \
        sorted(glob.glob("/mnt/skills/**/hsc-econ-diagrams/scripts", recursive=True))
    lib = next((c for c in cands if c and os.path.exists(os.path.join(c, "econ_diagrams.py"))), None)
    if not lib:
        notes.append("diagram left out: econ_diagrams.py (hsc-econ-diagrams skill) not found")
        return None
    sys.path.insert(0, lib)
    try:
        import econ_diagrams as ed
        fn = getattr(ed, name)
        if name == "phillips":
            args.setdefault("color", colour)
            return fn(**args).svg()
        return fn(color=colour, **args).svg() if name != "lras_growth" else fn(colour).svg()
    except Exception as e:                                  # a bad argument must not lose the page
        notes.append(f"diagram left out: {type(e).__name__}: {e}")
        return None


CSS = """
@page { size: A4; margin: 0 }
* { box-sizing: border-box }
html, body { margin: 0; padding: 0 }
body { font-family: Inter, 'Helvetica Neue', Arial, sans-serif; color: #111827; -webkit-print-color-adjust: exact }
.page { width: 210mm; height: 297mm; padding: 11mm 12mm 9mm; display: flex; flex-direction: column; overflow: hidden; font-size: calc(10.6px * var(--k)) }
.top { display: flex; justify-content: space-between; align-items: center }
.pill { background: var(--c); color: #fff; font-size: 8.4px; font-weight: 700; letter-spacing: 1.1px; text-transform: uppercase; padding: 4px 11px; border-radius: 20px }
.src { font-size: 8.6px; color: #6B7280 }
h1 { font-family: 'Inter Display', Inter, sans-serif; font-weight: 800; font-size: calc(25px * var(--k)); letter-spacing: -0.6px; line-height: 1.12; margin: 11px 0 9px }
.lede { border-left: 3px solid var(--c); padding: 1px 0 1px 11px; font-size: calc(12px * var(--k)); line-height: 1.5; margin-bottom: 11px }
.cols { display: grid; grid-template-columns: 1.62fr 1fr; gap: 16px; margin-bottom: 11px }
h4 { font-size: 8.2px; letter-spacing: 1.2px; text-transform: uppercase; color: var(--c); margin: 0 0 4px; font-weight: 800 }
ul { margin: 0 0 8px; padding-left: 15px } li { line-height: 1.48; margin-bottom: 3px }
.terms p { margin: 0 0 2px; line-height: 1.5 } .terms b { color: var(--c) }
.tiles { display: flex; flex-direction: column; gap: 7px }
.tile { background: var(--t); border-radius: 9px; padding: 8px 11px }
.tile .n { font-family: 'Inter Display', Inter, sans-serif; font-weight: 800; font-size: calc(21px * var(--k)); color: var(--c); letter-spacing: -0.4px; line-height: 1.15 }
.tile .l { font-size: 9.2px; color: #374151; line-height: 1.35 }
.panel { border: 1px solid #E5E7EB; background: #FAFBFC; border-radius: 14px; padding: 11px 13px 12px; margin-bottom: 10px }
.ph { display: flex; align-items: center; gap: 8px; margin-bottom: 9px; font-size: 12px; font-weight: 700 }
.tag { background: var(--c); color: #fff; font-size: 8.2px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; padding: 3px 8px; border-radius: 5px; white-space: nowrap }
.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; align-items: center }
.grid2 svg { width: 100%; height: auto; max-height: calc(205px * var(--k)) }
.explain { font-size: calc(10.4px * var(--k)); line-height: 1.55 }
.note { border: 1.3px dashed var(--c); border-radius: 9px; padding: 8px 11px; font-size: calc(10.3px * var(--k)); line-height: 1.5; margin-top: 9px; background: #fff }
.note.solo { margin-top: 0 } .note b.h { color: var(--c) }
.flow { display: flex; align-items: stretch }
.step { flex: 1; border: 1.3px solid var(--c); background: #fff; border-radius: 9px; padding: 8px 6px; font-size: calc(9.6px * var(--k)); text-align: center; display: flex; align-items: center; justify-content: center; line-height: 1.35 }
.step.hi { background: var(--c); color: #fff; font-weight: 700 }
.arrow { width: 16px; display: flex; align-items: center; justify-content: center; color: #6B7280 }
.bottom { display: grid; grid-template-columns: 1fr 1.25fr; gap: 10px }
.syl { background: #F3F4F6; border-radius: 11px; padding: 10px 12px; line-height: 1.5 }
.try { background: var(--c); color: #fff; border-radius: 11px; padding: 10px 12px; line-height: 1.5 }
.try h4 { color: #fff } .try p { margin: 0 0 3px }
.grow { flex: 1 }
.links { font-size: 7.4px; color: #6B7280; line-height: 1.5; margin-top: 8px }
.links a { color: #6B7280; text-decoration: none }
.foot { display: flex; justify-content: space-between; border-top: 1px solid #E5E7EB; margin-top: 6px; padding-top: 5px; font-size: 7.4px; color: #9CA3AF }
sub { font-size: 70%; vertical-align: sub; line-height: 0 }
"""


def build_html(rec, k, notes):
    name, colour, tint = TOPICS[int(rec["topic"])]
    svg = diagram_svg(rec, colour, notes)
    d = rec.get("diagram") or {}
    stats = "".join(f'<div class="tile"><div class="n">{fmt(v)}</div><div class="l">{fmt(l)}</div></div>'
                    for v, l in (rec.get("stats") or [])[:3])
    bullets = "".join(f"<li>{fmt(b)}</li>" for b in rec["what_happened"][:5])
    terms = "".join(f"<p><b>{fmt(t)}</b> – {fmt(x)}</p>" for t, x in rec["key_terms"][:3])
    angle = f'<b class="h">Exam angle:</b> {fmt(rec["exam_angle"])}'
    if svg:
        panel = (f'<div class="panel"><div class="ph"><span class="tag">Diagram</span>{fmt(d.get("title", ""))}</div>'
                 f'<div class="grid2"><div>{svg}</div><div class="explain">{fmt(d.get("explain", ""))}</div></div>'
                 f'<div class="note">{angle}</div></div>')
    else:
        panel = f'<div class="panel"><div class="note solo">{angle}</div></div>'
    steps = [fmt(s) for s in rec["flow"]["steps"][:5]]
    flow = '<div class="arrow">→</div>'.join(
        f'<div class="step{" hi" if i == len(steps) - 1 else ""}">{s}</div>' for i, s in enumerate(steps))
    qs = "".join(f"<p>{fmt(q)} <b>({int(m)} mark{'s' if int(m) != 1 else ''})</b></p>" for q, m in rec["questions"][:2])
    links = " · ".join(f'<a href="{html.escape(u, quote=True)}">{fmt(l)}</a>' for l, u in rec["sources"][:5])
    foot_r = "Diagrams are illustrative, not to scale" if svg else fmt(rec["date"])
    return f"""<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><title>{fmt(rec['title'])}</title>
<style>{CSS}</style></head><body><div class="page" id="page" style="--c:{colour};--t:{tint};--k:{k}">
<div class="top"><span class="pill">Topic {int(rec['topic'])} · {html.escape(name)}</span><span class="src">{fmt(rec['sources_line'])} · {fmt(rec['published'])}</span></div>
<h1>{fmt(rec['title'])}</h1>
<div class="lede">{fmt(rec['lede'])}</div>
<div class="cols"><div><h4>What happened</h4><ul>{bullets}</ul><div class="terms"><h4>Key terms</h4>{terms}</div></div><div class="tiles">{stats}</div></div>
{panel}
<div class="panel"><div class="ph"><span class="tag">Flow chart</span>{fmt(rec['flow'].get('title', ''))}</div><div class="flow">{flow}</div></div>
<div class="bottom"><div class="syl"><h4>Syllabus link</h4>{fmt(rec['syllabus_link'])}</div><div class="try"><h4>Try this</h4>{qs}</div></div>
<div class="grow"></div>
<div class="links">Sources: {links}</div>
<div class="foot"><span>The Economy This Week · Year 12 HSC Economics</span><span>{foot_r}</span></div>
</div></body></html>"""


def main(argv):
    force = "--force" in argv
    argv = [a for a in argv if a != "--force"]
    if len(argv) != 2:
        print(__doc__)
        return 2
    try:
        rec = json.load(open(argv[0], encoding="utf-8"))
        missing = [k for k in REQUIRED if not rec.get(k)]
        if missing:
            raise ValueError("record is missing: " + ", ".join(missing))
        if int(rec["topic"]) not in TOPICS:
            raise ValueError("topic must be 1-4")
        if len(rec["flow"].get("steps", [])) < 3:
            raise ValueError("flow needs 3-5 steps")
        out = os.path.join(argv[1], file_name(rec))
        if os.path.exists(out) and not force:
            print(f"EXISTS {out}")
            return 0
        os.makedirs(argv[1], exist_ok=True)
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            b = p.chromium.launch()
            pg = b.new_page(viewport={"width": 794, "height": 1123})
            fits = False
            for k in (1.0, 0.96, 0.92, 0.88):
                notes = []
                pg.set_content(build_html(rec, k, notes))
                pg.evaluate("document.fonts.ready")
                over = pg.evaluate("(()=>{const p=document.getElementById('page');"
                                   "const g=p.querySelector('.grow').getBoundingClientRect().height;"
                                   "return p.scrollHeight>p.clientHeight+1 || g<4})()")
                if not over:
                    fits = True
                    break
            if not fits:
                b.close()
                raise ValueError("the content does not fit on one page even at the smallest size: "
                                 "shorten the bullets, the diagram explanation or the questions")
            pg.pdf(path=out, format="A4", print_background=True,
                   margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
            b.close()
        for n in notes:
            print(f"NOTE {n}")
        if k < 1:
            print(f"NOTE text scaled to {int(k * 100)}% to fit the page")
        print(f"SAVED {out}")
        return 0
    except Exception as e:
        print(f"ERROR {type(e).__name__}: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
