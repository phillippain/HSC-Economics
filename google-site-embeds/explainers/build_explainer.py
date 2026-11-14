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
    if band: o.append('<rect x="%d" y="%.1f" width="%d" height="%.1f" fill="#cfe8d6"/><text x="%d" y="%.1f" font-size="9.5" font-weight="700" text-anchor="end" fill="#256b3a">%s</text>' % (L, Y(band[1]), w - L - R, Y(band[0]) - Y(band[1]), w - R - 4, (Y(band[0]) + Y(band[1])) / 2 + 3.5, e(band[2])))
    for k in range(5):
        yv = ymax * k / 4
        o.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="#d7deec"/><text x="%d" y="%.1f" font-size="9.5" text-anchor="end" fill="%s">%g</text>' % (L, w - R, Y(yv), Y(yv), L - 4, Y(yv) + 3, GREY, yv))
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.8" stroke-linejoin="round"/>' % ("".join(("M" if i == 0 else "L") + "%.1f %.1f" % (X(x), Y(y)) for i, (_, x, y) in enumerate(pts)), c))
    for i, (lab, x, y) in enumerate(pts):
        o.append('<circle cx="%.1f" cy="%.1f" r="3.5" fill="%s"/>' % (X(x), Y(y), c))
        if lab:
            o.append('<text x="%.1f" y="%.1f" font-size="10" font-weight="800" text-anchor="middle" fill="%s">%g%s</text>' % (X(x), Y(y) - 7, INK, y, unit))
            o.append('<text x="%.1f" y="%d" font-size="9.5" text-anchor="%s" fill="%s">%s</text>' % (X(x), h - 7, "end" if i == len(pts) - 1 else "middle", GREY, e(lab)))
    return "".join(o) + "</svg>"
def chain(steps): return '<div class="ch">' + '<span>&#8595;</span>'.join("<div>%s</div>" % s for s in steps) + "</div>"
def table(head, rows): return "<table><tr>" + "".join("<th>%s</th>" % h for h in head) + "</tr>" + "".join("<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>" for r in rows) + "</table>"
def diagram(d): return d.svg(standalone=False) if 'standalone' in d.svg.__code__.co_varnames else d.svg()
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
