#!/usr/bin/env python3
"""Builds the reference-note embeds (text, data, inline SVG charts) for the thin sub-topic pages.
Run: python3 build_reference.py  -> writes ref-<page>-text.html (pasted into a Sites text box) and
ref-<page>-charts.html (Sites > Embed > Embed code). The embed keeps its shape at every width."""
import html, os
STAMP = "Updated 14 November 2026"
INK, GREY = "#0b1330", "#5a6580"
FONT = '<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;700;800&display=swap" rel="stylesheet">'

def css(c):
    return ("<style>*{box-sizing:border-box}html,body{margin:0}body{font-family:Manrope,Arial,sans-serif;color:%s;background:#fff;font-size:15px;line-height:1.5}"
    "#p{width:900px;padding:2px 4px}.top{display:flex;justify-content:space-between;align-items:baseline;border-bottom:2px solid C;padding-bottom:6px;margin-bottom:12px}"
    ".top b{font-size:15px;letter-spacing:.08em;text-transform:uppercase;color:C}.top span{white-space:nowrap;margin-left:12px;font-size:12px;font-weight:700;color:%s}"
    ".g{display:grid;grid-template-columns:1.25fr 1fr;gap:22px}h3{font-size:16px;font-weight:800;margin:14px 0 4px;color:C}h3:first-child{margin-top:0}p{margin:0 0 8px}ul{margin:0 0 8px;padding-left:18px}li{margin-bottom:3px}"
    ".k{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin:0 0 14px}.k div{background:#f3f5fa;border:1px solid #c9d2e4;border-left:6px solid C;border-radius:10px;padding:9px 12px}"
    ".k b{display:block;font-size:22px;font-weight:800;color:C;line-height:1.15}.k i{font-style:normal;font-size:12.5px;font-weight:700;color:#3b4663;line-height:1.3;display:block}"
    ".c{background:#f8f9fc;border:1px solid #c9d2e4;border-radius:10px;padding:10px 12px;margin-bottom:12px}.c h4{margin:0 0 6px;font-size:13.5px;font-weight:800}.c small{display:block;font-size:11.5px;color:%s;margin-top:4px;line-height:1.35}svg{width:100%%;height:auto;display:block}"
    ".x{background:#fff8e1;border:1px dashed #d9a400;border-radius:10px;padding:9px 12px;margin:10px 0 0}.x b{color:#8a6a00}"
    "table{border-collapse:collapse;width:100%%;font-size:13.5px;margin-bottom:8px}th{background:C;color:#fff;text-align:left;padding:5px 8px}td{border-bottom:1px solid #d7deec;padding:5px 8px;vertical-align:top}"
    ".s{font-size:12px;color:%s;margin-top:12px;border-top:1px solid #d7deec;padding-top:6px}.s a{color:#1c3fb0}"
    ".m{display:none;font-size:12px;font-weight:700;color:#8a6a00;background:#fff8e1;border-radius:8px;padding:5px 9px;margin-bottom:8px}@media(max-width:599px){.m{display:block}#p{width:auto}.g{grid-template-columns:1fr}.k{grid-template-columns:1fr}}</style>" % (INK, GREY, GREY, GREY)).replace("C", c)

JS = "<script>function z(){var w=innerWidth,p=document.getElementById('p');p.style.zoom=w>=600?(w/900):1}addEventListener('resize',z);z()</script>"
e = html.escape

def hbar(title, items, c, note="", unit="", vmax=None, w=380):
    vmax = vmax or max(v for _, v, *_ in items)
    lab = 150; bw = w - lab - 58; rh = 26; h = len(items) * rh + 4
    o = ['<svg viewBox="0 0 %d %d" role="img" aria-label="%s">' % (w, h, e(title))]
    for i, it in enumerate(items):
        l, v = it[0], it[1]; col = it[2] if len(it) > 2 else c
        y = i * rh + 4; L = max(2, bw * v / vmax)
        o.append('<text x="%d" y="%d" font-size="12" font-weight="700" text-anchor="end" fill="%s">%s</text>' % (lab - 8, y + 14, INK, e(l)))
        o.append('<rect x="%d" y="%d" width="%.1f" height="18" rx="3" fill="%s"/>' % (lab, y, L, col))
        o.append('<text x="%.1f" y="%d" font-size="12" font-weight="800" fill="%s">%s%s</text>' % (lab + L + 5, y + 14, INK, ("%g" % v), unit))
    o.append("</svg>")
    return '<div class="c"><h4>%s</h4>%s%s</div>' % (e(title), "".join(o), "<small>%s</small>" % note if note else "")

def line(title, pts, c, note="", unit="", ymax=None, step=False, extra=None, w=380, h=190, fmt="%g"):
    """pts: [(xlabel, xnum, y)]; extra: [(xlabel, xnum, y, label)] drawn dashed in gold/grey as targets."""
    allp = pts + [(a, b, cc) for a, b, cc, _ in (extra or [])]
    x0, x1 = min(p[1] for p in allp), max(p[1] for p in allp)
    ymax = ymax or max(p[2] for p in allp) * 1.15
    L, R, T, B = 34, 16, 14, 26
    X = lambda x: L + (w - L - R) * (x - x0) / (x1 - x0)
    Y = lambda y: T + (h - T - B) * (1 - y / ymax)
    o = ['<svg viewBox="0 0 %d %d" role="img" aria-label="%s">' % (w, h, e(title))]
    for k in range(5):
        yv = ymax * k / 4
        o.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="#d7deec"/>' % (L, w - R, Y(yv), Y(yv)))
        o.append('<text x="%d" y="%.1f" font-size="10" text-anchor="end" fill="%s">%s</text>' % (L - 4, Y(yv) + 3, GREY, ("%.0f" % yv)))
    d = ""
    for i, (_, x, y) in enumerate(pts):
        if i == 0: d += "M%.1f %.1f" % (X(x), Y(y))
        elif step: d += "H%.1f V%.1f" % (X(x), Y(y))
        else: d += "L%.1f %.1f" % (X(x), Y(y))
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="3" stroke-linejoin="round"/>' % (d, c))
    if extra:
        lx, ly = X(pts[-1][1]), Y(pts[-1][2])
        d2 = "M%.1f %.1f" % (lx, ly) + "".join("L%.1f %.1f" % (X(x), Y(y)) for _, x, y, _ in extra)
        o.append('<path d="%s" fill="none" stroke="#b8860b" stroke-width="2.5" stroke-dasharray="5 4"/>' % d2)
        for xl, x, y, lb in extra:
            o.append('<circle cx="%.1f" cy="%.1f" r="4" fill="#fff" stroke="#b8860b" stroke-width="2"/>' % (X(x), Y(y)))
            o.append('<text x="%.1f" y="%.1f" font-size="10.5" font-weight="800" text-anchor="middle" fill="#8a6a00">%s</text>' % (X(x), Y(y) - 8, e(lb)))
            o.append('<text x="%.1f" y="%d" font-size="10" text-anchor="middle" fill="%s">%s</text>' % (X(x), h - 8, GREY, e(xl)))
    for i, (xl, x, y) in enumerate(pts):
        if not step or xl:
            o.append('<circle cx="%.1f" cy="%.1f" r="4" fill="%s"/>' % (X(x), Y(y), c))
        if xl:
            anc = "start" if i == 0 else ("end" if (i == len(pts) - 1 and not extra) else "middle")
            o.append('<text x="%.1f" y="%.1f" font-size="10.5" font-weight="800" text-anchor="%s" fill="%s">%s%s</text>' % (X(x), Y(y) - 8, anc, INK, fmt % y, unit))
            o.append('<text x="%.1f" y="%d" font-size="10" text-anchor="middle" fill="%s">%s</text>' % (X(x), h - 8, GREY, e(xl)))
    o.append("</svg>")
    return '<div class="c"><h4>%s</h4>%s%s</div>' % (e(title), "".join(o), "<small>%s</small>" % note if note else "")

def tiles(ts): return '<div class="k">' + "".join("<div><b>%s</b><i>%s</i></div>" % t for t in ts) + "</div>"
def exam(t): return '<div class="x"><b>Use it in an exam:</b> %s</div>' % t
def src(links): return '<div class="s">Sources: ' + "; ".join('<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, n) for n, u in links) + ". Charts are drawn from the figures shown.</div>"

def split(slug, left, right):
    """Text goes in a native Sites text box (reflows on phones); visuals go in a small embed."""
    if slug == "international-organisations":
        m = left.index("<h3>Government economic forums"); n = right.index("<h3>How well")
        return left[m:] + right[n:], left[:m] + right[:n]
    if slug == "local-content":
        n = right.index("<h3>Other examples"); x = left.index('<div class="x">')
        return left[:x] + right[n:] + left[x:], right[:n]
    return left, right

JS2 = "<script>function z(){document.getElementById('p').style.zoom=innerWidth/400}addEventListener('resize',z);z()</script>"
def page(slug, c, title, ts, left, right, links):
    text, vis = split(slug, left, right)
    text = text.replace('<div class="x">', "<p>").replace("</div>", "</p>")
    t = ("<p><i>%s</i></p>" % STAMP) + text + "<p>Sources: " + "; ".join('<a href="%s">%s</a>' % (u, n) for n, u in links) + ".</p>"
    emb = (FONT + css(c) + "<style>#p{width:400px!important}.k{grid-template-columns:1fr!important}.m{display:none!important}</style>"
           + '<div id="p"><div class="top"><b>Key data</b><span>%s</span></div>%s%s</div>' % (STAMP, tiles(ts), vis) + JS2)
    d = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(d, "ref-%s-text.html" % slug), "w").write(t)
    open(os.path.join(d, "ref-%s-charts.html" % slug), "w").write(emb)
    return len(t), len(emb)

T1, T2, T4 = "#2447d6", "#0e8a8a", "#8a3fb0"
from content_ref import PAGES
if __name__ == "__main__":
    for p in PAGES(hbar, line, exam, T1, T2, T4):
        print(p[0], page(*p))
