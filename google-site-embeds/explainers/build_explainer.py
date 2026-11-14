#!/usr/bin/env python3
"""Topic explainer pages: writes <slug>-text.html (pasted into a Sites text box) and <slug>-figures.html
(Sites > Embed > Embed code, drawn 400 px wide and scaled). Headline tiles load live from Economy at a Glance."""
import sys, os, json, glob, html
sys.path.insert(0, glob.glob('/root/.claude/skills/synced/*/hsc-econ-diagrams/scripts')[0] if glob.glob('/root/.claude/skills/synced/*/hsc-econ-diagrams/scripts') else '.')
import econ_diagrams as ed
STAMP = "Updated 14 November 2026"
INK, GREY = "#0b1330", "#5a6580"
TOOLS = "https://phillippain.github.io/HSC-Economics/"
GLANCE = TOOLS + "economy-at-a-glance/data/glance.json"
FONT = '<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;700;800&display=swap" rel="stylesheet">'
def css(c, cd):
    return ("<style>*{box-sizing:border-box}html,body{margin:0}body{font-family:Manrope,Arial,sans-serif;color:%s;background:#fff;font-size:14px;line-height:1.45}"
    "#p{width:400px;padding:2px}.top{display:flex;justify-content:space-between;align-items:baseline;border-bottom:2px solid C;padding-bottom:5px;margin-bottom:10px}"
    ".top b{font-size:14px;letter-spacing:.08em;text-transform:uppercase;color:D}.top span{font-size:11px;font-weight:700;color:%s}"
    ".f{background:#f8f9fc;border:1px solid #c9d2e4;border-radius:10px;padding:10px 12px;margin-bottom:12px}.f h4{margin:0 0 6px;font-size:13.5px;font-weight:800}.f h4 em{font-style:normal;color:D}"
    ".f small{display:block;font-size:11.5px;color:%s;margin-top:5px;line-height:1.35}svg{width:100%%;height:auto;display:block}"
    ".k{display:grid;grid-template-columns:1fr 1fr;gap:8px}.k div{background:#fff;border:1px solid #c9d2e4;border-left:5px solid C;border-radius:8px;padding:7px 9px}"
    ".k b{display:block;font-size:20px;font-weight:800;color:D;line-height:1.15}.k i{font-style:normal;font-size:11.5px;font-weight:700;color:#3b4663;display:block;line-height:1.25}.k u{text-decoration:none;font-size:10.5px;color:%s;display:block}"
    "table{border-collapse:collapse;width:100%%;font-size:12.5px}th{background:D;color:#fff;text-align:left;padding:5px 7px}td{border-bottom:1px solid #d7deec;padding:5px 7px;vertical-align:top;background:#fff}"
    ".ch{display:flex;flex-direction:column;align-items:stretch;gap:0}.ch div{background:#fff;border:1px solid #c9d2e4;border-radius:8px;padding:6px 9px;font-size:12.5px;font-weight:700;text-align:center}.ch span{text-align:center;color:D;font-weight:800;line-height:1.1;font-size:15px}"
    ".br{display:grid;grid-template-columns:118px 1fr 46px;align-items:center;gap:6px;font-size:12px;font-weight:700;margin:3px 0}.br s{display:block;height:13px;border-radius:3px;background:C;text-decoration:none}.br s.g{background:#9aa6c0}.br u{text-decoration:none;text-align:right;font-weight:800}.br i{font-style:normal;line-height:1.2}"
    ".sub{font-size:11.5px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:D;margin:8px 0 3px}.sub:first-of-type{margin-top:0}.lg{font-size:11px;font-weight:700;color:#3b4663;margin-bottom:5px}.lg s{display:inline-block;width:10px;height:10px;border-radius:2px;background:C;margin:0 4px 0 0;vertical-align:-1px}.lg s.g{background:#9aa6c0;margin-left:10px}"
    ".tw{margin-top:4px}.tw h4{margin:0 0 8px;font-size:14px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#1c3fb0;border-bottom:2px solid #1c3fb0;padding-bottom:5px}.tg{display:grid;grid-template-columns:1fr 1fr;gap:8px}"
    ".tb{display:flex;align-items:center;gap:8px;text-decoration:none;background:#1c3fb0;border-radius:10px;padding:9px 10px;min-height:56px}.tb:hover,.tb:focus{background:#122a7a}.tb svg{flex:0 0 26px;width:26px;height:26px;fill:none;stroke:#ffd24a;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}"
    ".tb b{display:block;font-size:12.5px;font-weight:800;color:#fff;line-height:1.2}.tb i{display:block;font-style:normal;font-size:10.5px;font-weight:500;color:#dfe6fb;line-height:1.25;margin-top:1px}"
    "</style>" % (INK, GREY, GREY, GREY)).replace("C", c).replace("D", cd)
e = html.escape
def fig(n, title, body, note=""):
    return '<div class="f"><h4><em>Figure %d.</em> %s</h4>%s%s</div>' % (n, e(title), body, "<small>%s</small>" % note if note else "")
def live(tiles):
    """tiles: [(glance id, label, fallback value, fallback period)]"""
    h = '<div class="k">' + "".join('<div><b data-id="%s">%s</b><i>%s</i><u data-p="%s">%s</u></div>' % (i, v, e(l), i, e(p)) for i, l, v, p in tiles) + "</div>"
    js = ("<script>fetch('%s?t='+Date.now(),{cache:'no-store'}).then(function(r){return r.ok?r.json():null}).then(function(d){if(!d)return;d.forEach(function(x){"
          "var b=document.querySelector('[data-id=\"'+x.id+'\"]'),p=document.querySelector('[data-p=\"'+x.id+'\"]');if(b&&x.display)b.textContent=x.display;if(p&&x.period)p.textContent=x.period})}).catch(function(){})</script>") % GLANCE
    return h, js
def linechart(pts, c, ymax, band=None, unit="%", w=376, h=180):
    x0, x1 = pts[0][1], pts[-1][1]; L, R, T, B = 28, 14, 14, 24
    X = lambda x: L + (w - L - R) * (x - x0) / (x1 - x0); Y = lambda y: T + (h - T - B) * (1 - y / ymax)
    o = ['<svg viewBox="0 0 %d %d" role="img" aria-label="line chart">' % (w, h)]
    if band: o.append('<rect x="%d" y="%.1f" width="%d" height="%.1f" fill="#cfe8d6"/><text x="%d" y="%.1f" font-size="9.5" font-weight="700" text-anchor="end" fill="#256b3a">%s</text>' % (L, Y(band[1]), w - L - R, Y(band[0]) - Y(band[1]), w - R - 4, Y(band[0]) + 11, e(band[2])))
    for k in range(5):
        yv = ymax * k / 4
        o.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="#d7deec"/><text x="%d" y="%.1f" font-size="9.5" text-anchor="end" fill="%s">%g</text>' % (L, w - R, Y(yv), Y(yv), L - 4, Y(yv) + 3, GREY, yv))
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.8" stroke-linejoin="round"/>' % ("".join(("M" if i == 0 else "L") + "%.1f %.1f" % (X(x), Y(y)) for i, (_, x, y) in enumerate(pts)), c))
    for i, (lab, x, y) in enumerate(pts):
        o.append('<circle cx="%.1f" cy="%.1f" r="3.5" fill="%s"/>' % (X(x), Y(y), c))
        if lab:
            o.append('<text x="%.1f" y="%.1f" font-size="10" font-weight="800" text-anchor="%s" fill="%s">%g%s</text>' % (X(x) + (6 if i == 0 else 0), Y(y) - (2 if i == 0 else 7), "start" if i == 0 else "middle", INK, y, unit))
            o.append('<text x="%.1f" y="%d" font-size="9.5" text-anchor="%s" fill="%s">%s</text>' % (X(x), h - 7, "end" if i == len(pts) - 1 else "middle", GREY, e(lab)))
    return "".join(o) + "</svg>"
def bars(items, vmax=None, fmt="%g", sub=None):
    """items: [(label, value)] -> horizontal bars in the topic colour."""
    vmax = vmax or max(v for _, v in items)
    return ('<div class="sub">%s</div>' % e(sub) if sub else "") + "".join('<div class="br"><i>%s</i><span><s style="width:%.1f%%"></s></span><u>%s</u></div>' % (e(l), 100 * v / vmax, fmt % v) for l, v in items)
def bars2(items, names, fmt="%g"):
    """items: [(label, a, b)] -> paired bars (topic colour, grey) with a legend."""
    vmax = max(max(a, b) for _, a, b in items)
    lg = '<div class="lg"><s></s>%s<s class="g"></s>%s</div>' % (e(names[0]), e(names[1]))
    return lg + "".join('<div class="br"><i>%s</i><span><s style="width:%.1f%%"></s></span><u>%s</u></div><div class="br" style="margin-top:-1px"><i></i><span><s class="g" style="width:%.1f%%"></s></span><u>%s</u></div>'
                        % (e(l), 100 * a / vmax, fmt % a, 100 * b / vmax, fmt % b) for l, a, b in items)
def colchart(pts, c, lo, hi, unit="%", w=376, h=190):
    """pts: [(label, value)] -> columns above and below a zero line (negatives in red)."""
    L, R, T, B = 8, 8, 16, 22; n = len(pts); bw = (w - L - R) / n
    Y = lambda v: T + (h - T - B) * (hi - v) / (hi - lo)
    o = ['<svg viewBox="0 0 %d %d" role="img" aria-label="column chart">' % (w, h)]
    for i, (lab, v) in enumerate(pts):
        x = L + i * bw + bw * .18; y0, y1 = sorted((Y(0), Y(v)))
        o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="%s"/>' % (x, y0, bw * .64, max(y1 - y0, 1), c if v >= 0 else "#c0392b"))
        o.append('<text x="%.1f" y="%.1f" font-size="10" font-weight="800" text-anchor="middle" fill="%s">%s%.1f%s</text>' % (x + bw * .32, (y0 - 4) if v >= 0 else (y1 + 11), INK, "\u2212" if v < 0 else "", abs(v), unit))
        o.append('<text x="%.1f" y="%d" font-size="9.5" text-anchor="middle" fill="%s">%s</text>' % (x + bw * .32, h - 6, GREY, e(lab)))
    o.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="%s" stroke-width="1.2"/>' % (L, w - R, Y(0), Y(0), INK))
    return "".join(o) + "</svg>"
def chain(steps): return '<div class="ch">' + '<span>&#8595;</span>'.join("<div>%s</div>" % s for s in steps) + "</div>"
def table(head, rows): return "<table><tr>" + "".join("<th>%s</th>" % h for h in head) + "</tr>" + "".join("<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>" for r in rows) + "</table>"
def diagram(d): return d.svg(standalone=False) if 'standalone' in d.svg.__code__.co_varnames else d.svg()
# Tool buttons: icons are the same 24 x 24 stroke paths as the tools' own "Other tools" menu (build/build_sitemenu.py).
ICONS = {
 "qf": ("Question Finder", "hsc-question-finder-site/", '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4M9.5 12h6M9.5 16h6"/>'),
 "ef": ("Evidence Finder", "evidence-finder/", '<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.3"/>'),
 "essay": ("Extended Response Builder", "essay-builder/", '<path d="M4 20l1-4L16 5l3 3L8 19zM14 7l3 3"/>'),
 "chain": ("Chain Builder", "chain-builder/", '<circle cx="5" cy="12" r="2.5"/><circle cx="19" cy="12" r="2.5"/><path d="M7.5 12h9M13.5 9l3 3-3 3"/>'),
 "macro": ("Macro Diagram Lab", "macro-diagram-lab/", '<path d="M4 4v16h16"/><path d="M7 7l11 9M7 17l11-9"/><circle cx="12.5" cy="12" r="1.6"/>'),
 "policy": ("Policy Simulator", "policy-simulator/", '<path d="M4 20h16M6 20V10M10 20V10M14 20V10M18 20V10M3 10l9-6 9 6z"/>'),
 "calc": ("Calculation Trainer", "calculation-trainer/", '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 12h2M12 12h0M16 12h0M8 16h2M12 16h0M16 16h0"/>'),
 "mcq": ("Multiple Choice Drill", "multiple-choice-drill/", '<circle cx="6" cy="7" r="2.5"/><circle cx="6" cy="17" r="2.5"/><path d="M11 7h9M11 17h9M5 17l1 1 2-2"/>'),
 "fx": ("Exchange Rate Explorer", "exchange-rate-explorer/", '<path d="M4 8h14M14 4l4 4-4 4M20 16H6M10 12l-4 4 4 4"/>'),
 "bop": ("Balance of Payments Explorer", "bop-explorer/", '<path d="M12 4v16M6 20h12M5 8h14M5 8l-2.5 6h5zM19 8l-2.5 6h5z"/>'),
 "explain": ("Who Wins from Protection", "protection-explainer/", '<path d="M12 4v16M7.5 20h9M5 7h14M5 7l-3 7a3 3 0 006 0zM19 7l-3 7a3 3 0 006 0z"/>'),
 "lab": ("Protection Diagram Lab", "diagram-lab/", '<path d="M4 4v16h16"/><path d="M7 8l10 9M7 17l10-9"/>'),
 "glance": ("Economy at a Glance", "economy-at-a-glance/", '<path d="M4 20V10M10 20V4M16 20v-7M21 20H3"/>'),
 "gloss": ("Glossary", "glossary/", '<path d="M4 5c3-1 6-1 8 1 2-2 5-2 8-1v13c-3-1-6-1-8 1-2-2-5-2-8-1zM12 6v13"/>'),
 "map": ("Topic Map", "mind-map/", '<circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="6" r="2.5"/><path d="M8.5 18H15a3 3 0 000-6H9a3 3 0 010-6h6.5"/>'),
}
def tools(items):
    """items: [(key, what to do there)] -> 'Practise with the tools' block of buttons, two per row."""
    b = "".join('<a class="tb" target="_blank" rel="noopener" href="%s%s"><svg viewBox="0 0 24 24" aria-hidden="true">%s</svg><span><b>%s</b><i>%s</i></span></a>'
                % (TOOLS, ICONS[k][1], ICONS[k][2], e(ICONS[k][0]), e(d)) for k, d in items)
    return '<div class="tw"><h4>Practise with the tools</h4><div class="tg">%s</div></div>' % b
def tool(name, path): return '<a href="%s%s">%s</a>' % (TOOLS, path, name)

def build(slug, c, cd, text, figs, js):
    t = "<p><i>%s</i></p>" % STAMP + text
    emb = FONT + css(c, cd) + '<div id="p"><div class="top"><b>Figures and data</b><span>%s</span></div>%s</div>' % (STAMP, "".join(figs)) + js + \
          "<script>function z(){document.getElementById('p').style.zoom=innerWidth/400}addEventListener('resize',z);z()</script>"
    d = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(d, slug + "-text.html"), "w").write(t); open(os.path.join(d, slug + "-figures.html"), "w").write(emb)
    import re
    words = len(re.sub(r"<[^>]+>", " ", text).split())
    print(slug, "words", words, "text", len(t), "figures", len(emb))

if __name__ == "__main__":
    import importlib
    for m in sys.argv[1:] or ["inflation"]:
        importlib.import_module("page_" + m.replace("-", "_")).make(sys.modules[__name__])
