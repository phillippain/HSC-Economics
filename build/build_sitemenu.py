#!/usr/bin/env python3
"""Put the same "Other tools" drop-down menu on every HSC Economics tool.

    python3 build/build_sitemenu.py           # write the menu into every page and template
    python3 build/build_sitemenu.py --check   # change nothing; fail if any page is out of date

One list, SITES below, feeds every menu. To add, rename or reorder a tool, edit SITES
(and PAGES if it is a new page), then run this script.

The menu is a slim bar at the top of the page, written between the SITEMENU:START and
SITEMENU:END markers. Templates and the pages built from them both carry it, so rebuilding
the Evidence Finder, the Extended Response Builder or the Glossary keeps the menu without
running this again. The first run puts the bar straight after <body>.

When a page is embedded in another site (an iframe), the links open in a new tab so the
embedded tool stays where it is.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECK = "--check" in sys.argv
# The class website: the Home button and the last row of the menu go here.
HOME = "https://sites.google.com/education.nsw.gov.au/hsceconomics-at-sscbwb/home"
HOME_NAME = "HSC Economics website"

# group, key, label, one-line description, folder, icon (24 x 24 stroke paths)
SITES = [
    ("Finders", "qf", "Question Finder", "Every HSC question, 2002 to 2025", "hsc-question-finder-site/",
     '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4M9.5 12h6M9.5 16h6"/>'),
    ("Finders", "ef", "Evidence Finder", "News, statistics and reports by dot point", "evidence-finder/",
     '<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.3"/>'),
    ("Writing and skills", "essay", "Extended Response Builder", "Plan a Section II, III or IV answer", "essay-builder/",
     '<path d="M4 20l1-4L16 5l3 3L8 19zM14 7l3 3"/>'),
    ("Writing and skills", "chain", "Chain Builder", "Cause and effect, one link at a time", "chain-builder/",
     '<circle cx="5" cy="12" r="2.5"/><circle cx="19" cy="12" r="2.5"/><path d="M7.5 12h9M13.5 9l3 3-3 3"/>'),
    ("Writing and skills", "macro", "Macro Diagram Lab", "AD–AS, the dollar, labour, Lorenz, externalities", "macro-diagram-lab/",
     '<path d="M4 4v16h16"/><path d="M7 7l11 9M7 17l11-9"/><circle cx="12.5" cy="12" r="1.6"/>'),
    ("Writing and skills", "policy", "Policy Simulator", "You set the cash rate and the budget", "policy-simulator/",
     '<path d="M4 20h16M6 20V10M10 20V10M14 20V10M18 20V10M3 10l9-6 9 6z"/>'),
    ("Writing and skills", "calc", "Calculation Trainer", "Every HSC calculation, with the working", "calculation-trainer/",
     '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 12h2M12 12h0M16 12h0M8 16h2M12 16h0M16 16h0"/>'),
    ("Writing and skills", "explain", "Who Wins from Protection", "Tariffs, quotas and subsidies explained", "protection-explainer/",
     '<path d="M12 4v16M7.5 20h9M5 7h14M5 7l-3 7a3 3 0 006 0zM19 7l-3 7a3 3 0 006 0z"/>'),
    ("Writing and skills", "lab", "Protection Diagram Lab", "Experiment, predict and build the diagram", "diagram-lab/",
     '<path d="M4 4v16h16"/><path d="M7 8l10 9M7 17l10-9"/>'),
    ("Reference", "glance", "Economy at a Glance", "The latest Australian indicators", "economy-at-a-glance/",
     '<path d="M4 20V10M10 20V4M16 20v-7M21 20H3"/>'),
    ("Reference", "gloss", "Economics Glossary", "Key terms, flashcards and a quiz", "glossary/",
     '<path d="M4 5c3-1 6-1 8 1 2-2 5-2 8-1v13c-3-1-6-1-8 1-2-2-5-2-8-1zM12 6v13"/>'),
    ("Reference", "map", "Topic Map", "See how the course fits together", "mind-map/",
     '<circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="6" r="2.5"/><path d="M8.5 18H15a3 3 0 000-6H9a3 3 0 010-6h6.5"/>'),
]

# key -> the files that carry the menu. Every tool sits one folder below the repo root.
PAGES = {
    "qf":      ["hsc-question-finder-site/index.html"],
    "ef":      ["evidence-finder/build/template.html", "evidence-finder/index.html"],
    "essay":   ["essay-builder/template.html", "essay-builder/index.html"],
    "chain":   ["chain-builder/template.html", "chain-builder/index.html"],
    "macro":   ["macro-diagram-lab/template.html", "macro-diagram-lab/index.html"],
    "policy":  ["policy-simulator/template.html", "policy-simulator/index.html"],
    "calc":    ["calculation-trainer/template.html", "calculation-trainer/index.html"],
    "explain": ["protection-explainer/index.html"],
    "lab":     ["diagram-lab/index.html"],
    "glance":  ["economy-at-a-glance/index.html"],
    "gloss":   ["glossary/template.html", "glossary/index.html"],
    "map":     ["mind-map/index.html"],
}

MARKED = re.compile(r"[ \t]*<!-- SITEMENU:START.*?<!-- SITEMENU:END -->\n", re.S)
BODY = re.compile(r"<body[^>]*>\n?")
FIRST_HEADER = re.compile(r"<header\b")   # the Topic Map has no <body> tag

CSS = """
.smbar{display:flex;justify-content:flex-end;padding:10px 20px 0;font-family:'Public Sans','Segoe UI',system-ui,-apple-system,sans-serif}
.smw{display:inline-flex;gap:8px;align-items:center;font-size:13px;line-height:1.3}
.sm{position:relative;display:inline-block;text-align:left}
.smw svg{width:1.15em;height:1.15em;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;flex:none}
.sm-btn{list-style:none;cursor:pointer;display:inline-flex;gap:7px;align-items:center;background:#ffd24a;color:#1a1d2b;border-radius:999px;padding:6px 13px;font-weight:700;white-space:nowrap;text-decoration:none;user-select:none;-webkit-user-select:none}
.sm-btn::-webkit-details-marker{display:none}
.sm-btn:hover{background:#ffe07a}
.sm-btn:focus-visible{outline:3px solid #2447d6;outline-offset:2px}
.sm[open] .sm-caret{transform:rotate(180deg)}
.sm-list{position:fixed;top:0;left:0;z-index:1000;width:min(340px,calc(100vw - 16px));max-height:calc(100vh - 90px);overflow:auto;background:#fff;color:#1a1d2b;border:1px solid #dcdfea;border-radius:14px;box-shadow:0 12px 34px rgba(10,14,40,.3);padding:8px;display:flex;flex-direction:column;gap:1px;font-weight:400}
.sm:not([open]) .sm-list{display:none}
.sm-h{font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.5px;color:#5a6072;padding:8px 10px 3px}
.sm-a{display:grid;grid-template-columns:22px 1fr;gap:10px;align-items:center;padding:7px 10px;border-radius:9px;color:inherit;text-decoration:none}
.sm-a svg{font-size:18px;color:#2447d6}
.sm-a b{display:block;font-size:14px;font-weight:700;color:inherit}
.sm-a em{display:block;font-style:normal;font-size:12px;color:#5a6072}
a.sm-a:hover,a.sm-a:focus-visible{background:#e3e9fd;outline:none}
.sm-cur{background:#fff3c9}
.sm-cur em{color:#7d5f00;font-weight:700}
.sm-ext{border-top:1px solid #dcdfea;margin-top:6px;padding-top:10px;border-radius:0 0 9px 9px}
@media print{.smbar{display:none !important}}
""".strip()

# Used only on pages that have a dark colour scheme of their own.
DARK_RULES = """.sm-list{background:#151c30;color:#e9eefb;border-color:#27304b}
.sm-h,.sm-a em{color:#a2aec9}
.sm-a svg{color:#8fa6ff}
a.sm-a:hover,a.sm-a:focus-visible{background:#212c52}
.sm-cur{background:#3a3010}
.sm-cur em{color:#e6bd45}
.sm-ext{border-color:#27304b}"""


def dark_css():
    sel = lambda pre: "\n".join(",".join(pre + " " + s for s in line.split("{")[0].split(",")) + "{" + line.split("{", 1)[1] for line in DARK_RULES.splitlines())
    return (sel(':root[data-theme="dark"]') + "\n@media (prefers-color-scheme:dark){\n" + sel(':root:not([data-theme="light"])') + "\n}")


# The list is position:fixed and placed under the button by script, so no page layout can
# clip it. It closes on Escape, an outside click, a page scroll or a resize.
JS = ("(function(){var d=document.getElementById('sitemenu');if(!d)return;var s=d.querySelector('summary'),l=d.querySelector('.sm-list');"
      "var framed=false;try{framed=window.self!==window.top}catch(e){framed=true}"
      "if(framed)d.parentNode.querySelectorAll('a').forEach(function(a){a.target='_blank';a.rel='noopener'});"
      "function place(){var b=s.getBoundingClientRect(),w=l.offsetWidth,x=Math.min(Math.max(8,b.right-w),window.innerWidth-w-8),y=b.bottom+8;"
      "l.style.left=x+'px';l.style.top=y+'px';l.style.maxHeight=Math.max(160,window.innerHeight-y-12)+'px'}"
      "function shut(){if(d.open)d.open=false}"
      "d.addEventListener('toggle',function(){if(d.open)place()});"
      "document.addEventListener('click',function(e){if(d.open&&!d.contains(e.target))shut()});"
      "document.addEventListener('keydown',function(e){if(e.key==='Escape'&&d.open){shut();s.focus()}});"
      "window.addEventListener('scroll',shut,{passive:true});window.addEventListener('resize',shut)})();")


def svg(paths, cls=""):
    return f'<svg{" class=" + chr(34) + cls + chr(34) if cls else ""} viewBox="0 0 24 24" aria-hidden="true">{paths}</svg>'


def menu(key, dark):
    grid = '<path d="M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h6v6h-6z"/>'
    house = '<path d="M3 11l9-7 9 7M5 10v10h14V10M10 20v-6h4v6"/>'
    rows, group = [], None
    for g, k, label, desc, path, icon in SITES:
        if g != group:
            rows.append(f'  <span class="sm-h">{g}</span>')
            group = g
        if k == key:
            rows.append(f'  <span class="sm-a sm-cur" aria-current="page">{svg(icon)}<span><b>{label}</b><em>You are here</em></span></span>')
        else:
            rows.append(f'  <a class="sm-a" href="../{path}">{svg(icon)}<span><b>{label}</b><em>{desc}</em></span></a>')
    home = ""
    if HOME:
        rows.append(f'  <a class="sm-a sm-ext" href="{HOME}">{svg(house)}<span><b>{HOME_NAME}</b><em>Back to the main class site</em></span></a>')
        home = f'<a class="sm-btn sm-home" href="{HOME}" aria-label="Home: back to the {HOME_NAME}">{svg(house)}Home</a>\n'
    return ("<!-- SITEMENU:START built by build/build_sitemenu.py; edit the list of tools there, not here -->\n"
            f"<style>\n{CSS}\n{dark_css() if dark else ''}\n</style>\n"
            f'<div class="smbar"><span class="smw">{home}'
            '<details class="sm" id="sitemenu"><summary class="sm-btn" aria-label="Other tools: open the list of HSC Economics tools">'
            f'{svg(grid)}Other tools{svg(chr(60) + "path d=" + chr(34) + "M6 9l6 6 6-6" + chr(34) + "/>", "sm-caret")}</summary>\n'
            '<div class="sm-list">\n' + "\n".join(rows) + "\n</div></details></span></div>\n"
            f"<script>{JS}</script>\n"
            "<!-- SITEMENU:END -->\n")


def patch(key, path):
    src = path.read_text(encoding="utf-8")
    bare = MARKED.sub("", src)
    block = menu(key, dark="prefers-color-scheme" in bare)
    if MARKED.search(src):
        return src, MARKED.sub(lambda m: block, src, count=1)
    m = BODY.search(src)
    if m:
        return src, src[:m.end()] + ("" if m.group(0).endswith("\n") else "\n") + block + src[m.end():]
    m = FIRST_HEADER.search(src)
    assert m, f"{path}: cannot find <body> or <header> to put the menu after"
    return src, src[:m.start()] + block + src[m.start():]


def main():
    stale, n = [], 0
    for key, files in PAGES.items():
        for f in files:
            p = ROOT / f
            if not p.exists():
                print(f"skipped (not found): {f}")
                continue
            old, new = patch(key, p)
            assert new.count("SITEMENU:START") == 1 and new.count('id="sitemenu"') == 1, f
            n += 1
            if old != new:
                stale.append(f)
                if not CHECK:
                    p.write_text(new, encoding="utf-8")
    print(f"site menu: Other tools list of {len(SITES)} tools{' plus the class website' if HOME else ''}, on {n} files")
    if CHECK:
        if stale:
            print("OUT OF DATE: " + ", ".join(stale) + ". Run python3 build/build_sitemenu.py")
            sys.exit(1)
        print("up to date")
        return
    print("wrote: " + (", ".join(stale) if stale else "nothing, already up to date"))


if __name__ == "__main__":
    main()
