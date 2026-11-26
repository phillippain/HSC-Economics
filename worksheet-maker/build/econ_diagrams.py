"""
econ_diagrams.py: draw HSC Economics diagrams as clean, self-contained SVG
in the "Economy This Week" house style.

You describe the economics, and the engine handles the geometry:
  * curves are given in a 0–10 data space (x right, y UP), so you never hand-compute pixels
  * equilibrium points are found by real curve intersection, with dashed guides
    dropped to BOTH axes and labelled there (P1/Q1, e1/Q1, π1/U1 ...)
  * the y-axis title sits above the arrow and the x-axis title sits below the tick labels,
    so they never collide
  * curve labels sit at the end of their own curve
  * labels like P1, S2, AD2, LRAS1, PC2, Pw, Pw+t, π1 (or anything written X_y) get real subscripts

Quick use:
    from econ_diagrams import Diagram, TOPIC
    d = Diagram("Price", "Quantity of oil", color=TOPIC[1])
    d.line("D", (5.2, 9.5), (6.8, 0.6), color="main")      # steep (inelastic) demand
    d.line("S1", (1.2, 1.0), (9.5, 7.6), color="grey")
    d.line("S2", (0.3, 2.6), (8.0, 9.0), color="red")
    d.shift("S1", "S2")                                     # arrow showing the shift
    d.point("D", "S1", "P1", "Q1")                         # intersection with guides + axis labels
    d.point("D", "S2", "P2", "Q2", color="red")
    svg = d.svg()

Presets (one call, returns a Diagram you can tweak further):
    supply_shift, demand_shift, tariff, price_ceiling, price_floor, subsidy,
    ad_as, lras_growth, phillips, fx_market, lorenz, ppf
Run `python econ_diagrams.py --gallery out_dir` to render every preset to SVG plus an HTML gallery.
"""
import itertools, math, re, html, os, sys

_MARKER_IDS = itertools.count(1)   # arrowhead marker ids: ah1, ah2, ... in drawing order

# ------------------------------------------------------------------ palette
TOPIC = {1: "#2563EB", 2: "#0D9488", 3: "#D97706", 4: "#7C3AED"}       # topic colours
TINT = {1: "#EAF1FE", 2: "#E3F4F2", 3: "#FDF0DD", 4: "#F0EAFE"}
NAMED = {"grey": "#9CA3AF", "red": "#DC2626", "green": "#16A34A", "ink": "#111827",
         "slate": "#64748B", "amber": "#D97706", "dark": "#374151"}
LABEL_GREY = "#374151"
ARROW_MIN = 22.5   # px: arrowhead is 7.5px long, so the shaft is at least 2x the head
SPAN_MIN = 20      # px: double-headed arrows (5px heads) keep at least 10px of shaft
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"

def _lighten(hex_, f=0.55):
    h = hex_.lstrip("#"); r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    r, g, b = (int(c + (255 - c) * f) for c in (r, g, b))
    return f"#{r:02X}{g:02X}{b:02X}"

# ------------------------------------------------------------------ subscripts
_AUTO = re.compile(r"^(P|Q|S|D|e|AD|AS|SRAS|LRAS|PC|Y|U|C|I|MC|MR|AC|ATC|AVC|MB|MSB|MSC|MPB|MPC|π|i|r|E|W|L|K|X|M|PPF|L)(\d+|w|e|f|s|d|max|min)(\+t|\+s|-s)?$")

def sub_label(s, shift=2.6):
    """Return SVG-safe markup with subscripts.
    Auto: 'P1' 'AD2' 'LRAS1' 'Pw' 'Pw+t' 'π1' 'Qe'.  Explicit: 'S_{world}' or 'D_dom'."""
    if "_" in s:
        m = re.match(r"^(.*?)_\{?([^}]*)\}?(.*)$", s)
        base, sub, rest = m.group(1), m.group(2), m.group(3)
    else:
        m = _AUTO.match(s)
        if not m:
            return html.escape(s)
        base, sub, rest = m.group(1), m.group(2), m.group(3) or ""
    out = f'{html.escape(base)}<tspan dy="{shift}" font-size="72%">{html.escape(sub)}</tspan>'
    if rest:
        out += f'<tspan dy="-{shift}">{html.escape(rest)}</tspan>'
    return out

def html_sub(text):
    """Subscript diagram labels inside ordinary HTML prose (e.g. 'S1 to S2' -> S<sub>1</sub> to S<sub>2</sub>).
    Leaves words like FY28 or Q&A alone."""
    t = re.sub(r"(?<![\w#/.-])(P|Q|S|D|e|AD|AS|SRAS|LRAS|PC|Y|U)(\d)(?![\w])", r"\1<sub>\2</sub>", text)
    t = re.sub(r"π(\d)", r"π<sub>\1</sub>", t)
    t = re.sub(r"\bPw\b", "P<sub>w</sub>", t)
    return t

# ------------------------------------------------------------------ geometry helpers
def _seg_intersect(p1, p2, p3, p4):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(d) < 1e-12:
        return None
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / d
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / d
    if -1e-9 <= t <= 1 + 1e-9 and -1e-9 <= u <= 1 + 1e-9:
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    return None

def _bezier(p0, p1, p2, n=60):
    return [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0],
             (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]) for t in (i / n for i in range(n + 1))]


class Diagram:
    """An economics diagram in data space x,y ∈ [0,10] (y up)."""

    def __init__(self, ylabel, xlabel, color=TOPIC[1], width=300, height=200, origin="0"):
        self.ylabel, self.xlabel, self.c = ylabel, xlabel, color
        self.W, self.H = width, height
        self.ox, self.oy = 38, height - 22          # axis origin in px
        self.right, self.top = width - 34, 18       # plot extent (room for curve labels on right)
        self.curves, self.layers, self.points = {}, [], []
        self.origin = origin
        self._xticks, self._yticks = [], []
        self._axis_spans = []

    # ---- coordinate transform
    def X(self, x): return self.ox + x / 10 * (self.right - self.ox)
    def Y(self, y): return self.oy - y / 10 * (self.oy - self.top)
    def px(self, p): return (self.X(p[0]), self.Y(p[1]))

    def _col(self, c):
        if c in (None, "main"): return self.c
        if c == "light": return _lighten(self.c)
        return NAMED.get(c, c)

    # ---- curves
    def line(self, name, a, b, color="main", dash=False, width=2.2, label=None, label_pos="end"):
        """Straight curve from data point a to b. `name` is used for intersections; label defaults to name."""
        return self._add(name, [a, b], color, dash, width, label, label_pos)

    def curve(self, name, a, ctrl, b, color="main", dash=False, width=2.2, label=None, label_pos="end"):
        """Quadratic Bézier curve (e.g. Phillips curve, Lorenz curve, PPF)."""
        return self._add(name, _bezier(a, ctrl, b), color, dash, width, label, label_pos)

    def vline(self, name, x, color="ink", dash=False, width=2.2, label=None, y0=0, y1=9.6):
        """Vertical curve such as LRAS or a fixed supply. Label goes on top."""
        return self._add(name, [(x, y0), (x, y1)], color, dash, width, label, "top")

    def hline(self, name, y, axis_label=None, color="grey", dash=True, width=1.3, x0=0, x1=9.4, curve_label=None):
        """Horizontal line such as world price Pw, Pw+t, a price ceiling or the inflation target.
        `axis_label` is written on the y-axis; `curve_label` (optional) at the right end."""
        self._add(name, [(x0, y), (x1, y)], color, dash, width, "", "end")
        if curve_label:   # sits just past the right-hand end of the line, vertically centred on it
            self.note(x1 + 0.15, y - 0.13, curve_label, color if color != "grey" else "dark", "start", 8.5)
        if axis_label:
            self._yticks.append((y, axis_label, self._col(color) if color not in ("grey",) else LABEL_GREY))
        return self

    def _add(self, name, pts, color, dash, width, label, label_pos):
        self.curves[name] = dict(pts=pts, color=self._col(color), dash=dash, width=width,
                                 label=name if label is None else label, label_pos=label_pos)
        self.layers.append(("curve", name))
        return self

    # ---- annotations
    def intersect(self, a, b):
        A, B = self.curves[a]["pts"], self.curves[b]["pts"]
        for i in range(len(A) - 1):
            for j in range(len(B) - 1):
                p = _seg_intersect(A[i], A[i + 1], B[j], B[j + 1])
                if p: return p
        raise ValueError(f"{a} and {b} do not intersect inside the plot. Adjust their endpoints.")

    def point(self, a, b, ylab=None, xlab=None, color="dark", name=None, guides=True, r=3.6, tag=None, tag_pos="nw"):
        """Mark the intersection of curves a and b. Drops dashed guides to both axes and labels them
        (e.g. ylab='P1', xlab='Q1'). `tag` writes a letter such as 'A' next to the point."""
        p = self.intersect(a, b)
        self.points.append(dict(p=p, ylab=ylab, xlab=xlab, color=self._col(color), guides=guides, r=r, tag=tag, tag_pos=tag_pos))
        if name: self.curves.setdefault("_pts", {})
        return p

    def mark(self, p, ylab=None, xlab=None, color="dark", guides=True, r=3.6, tag=None, tag_pos="nw"):
        """Mark an arbitrary data point (x,y) with optional guides and axis labels.
        tag_pos ('nw','ne','sw','se') puts a letter tag (A, B) off the curve: choose the side away from the curve."""
        self.points.append(dict(p=p, ylab=ylab, xlab=xlab, color=self._col(color), guides=guides, r=r, tag=tag, tag_pos=tag_pos))

    def xtick(self, x, label, color=None):
        self._xticks.append((x, label, color or LABEL_GREY))

    def ytick(self, y, label, color=None):
        self._yticks.append((y, label, color or LABEL_GREY))

    def shade(self, pts, fill="#FCA5A5", opacity=1.0, label=None, label_color="#92400E", stroke=None):
        """Shade a polygon given in data coords (e.g. deadweight loss, tariff revenue, surplus)."""
        self.layers.insert(0, ("shade", dict(pts=pts, fill=fill, opacity=opacity, label=label,
                                              label_color=label_color, stroke=stroke)))
        return self

    def band(self, y0, y1, label=None, fill="#DCFCE7", label_color="#16A34A"):
        """Horizontal band, e.g. the RBA's 2–3% target."""
        return self.shade([(0, y0), (9.4, y0), (9.4, y1), (0, y1)], fill=fill, label=None).note(9.3, (y0 + y1) / 2 - 0.25, label or "", label_color, anchor="end", size=8.5)

    def _dense(self, name, n=200):
        pts = self.curves[name]["pts"]
        if len(pts) > 2: return pts
        (x1, y1), (x2, y2) = pts
        return [(x1 + t / n * (x2 - x1), y1 + t / n * (y2 - y1)) for t in range(n + 1)]

    def shift(self, a, b, at=0.75, color=None, frac=0.3, flatten=0.6):
        """Short arrow from curve a towards curve b, starting at fraction `at` along curve a,
        centred in the gap. Its direction starts square to the curves (shortest on-screen gap) and is
        then tilted towards horizontal by `flatten` (0 = square to the curves, 1 = fully horizontal),
        which reads more naturally as a left/right shift."""
        A = self._dense(a); pa = A[min(int(at * (len(A) - 1)), len(A) - 1)]
        Ax, Ay = self.px(pa)
        pb = min(self._dense(b), key=lambda q: (self.X(q[0]) - Ax) ** 2 + (self.Y(q[1]) - Ay) ** 2)
        Bx, By = self.px(pb)
        dx, dy = Bx - Ax, By - Ay; n = math.hypot(dx, dy) or 1
        dx, dy = dx / n, dy / n
        hx = 1.0 if dx >= 0 else -1.0
        vx, vy = dx + flatten / max(1e-6, 1 - flatten) * hx, dy
        m = math.hypot(vx, vy); vx, vy = vx / m, vy / m
        # ray in pixel space -> data space, then find where it meets curve b
        far = ((Ax + vx * 600 - self.ox) / (self.right - self.ox) * 10, (self.oy - (Ay + vy * 600)) / (self.oy - self.top) * 10)
        try:
            pb = self.ray_hit(b, pa, far)
        except ValueError:
            pass                                       # fall back to the square-on direction
        return self.arrow_between(pa, pb, color or self.curves[b]["color"], frac)

    def arrow_between(self, pa, pb, color="red", frac=0.3):
        """Short arrow centred in the gap between two data points (takes up `frac` of the gap)."""
        mx, my = pb[0] - pa[0], pb[1] - pa[1]; h = (1 - frac) / 2
        return self.arrow((pa[0] + mx * h, pa[1] + my * h), (pa[0] + mx * (1 - h), pa[1] + my * (1 - h)), color)

    def ray_hit(self, name, origin, target):
        """Where the straight ray origin→target first crosses curve `name` (data coords)."""
        self.curves["__ray"] = dict(pts=[origin, target]); p = self.intersect("__ray", name); del self.curves["__ray"]; return p

    def arrow(self, s, e, color="red"):
        self.layers.append(("arrow", dict(s=s, e=e, color=self._col(color))))
        return self

    def note(self, x, y, text, color="dark", anchor="start", size=9, weight=700):
        self.layers.append(("note", dict(x=x, y=y, text=text, color=self._col(color), anchor=anchor, size=size, weight=weight)))
        return self

    def bar(self, x0, x1, y, color="grey", width=3, arrows=False):
        """Horizontal range marker, e.g. imports before/after a tariff, a shortage or surplus.
        arrows=True draws a thin line with small arrowheads at both ends (↔)."""
        self.layers.append(("bar", dict(x0=x0, x1=x1, y=y, color=self._col(color), w=width, arrows=arrows)))
        return self

    def span(self, x0, x1, y, color="red"):
        """Double-headed arrow between two quantities (↔) drawn inside the plot at height y."""
        return self.bar(x0, x1, y, color, 1.4, arrows=True)

    def axis_span(self, x0, x1, color="red", label=None):
        """↔ arrow for a quantity range (shortage, surplus, imports) drawn BELOW the axis:
        between the quantity labels (Q1, Qd ...) and the x-axis title. Multiple calls stack in rows;
        an optional label sits just past the right-hand arrowhead."""
        self._axis_spans.append(dict(x0=x0, x1=x1, color=self._col(color), label=label))
        return self

    @staticmethod
    def _min_len(s, e, L):
        """Lengthen a short arrow about its midpoint so its shaft is at least twice the arrowhead."""
        dx, dy = e[0] - s[0], e[1] - s[1]; n = math.hypot(dx, dy)
        if n >= L or n == 0: return s, e
        mx, my = (s[0] + e[0]) / 2, (s[1] + e[1]) / 2; ux, uy = dx / n, dy / n
        return (mx - ux * L / 2, my - uy * L / 2), (mx + ux * L / 2, my + uy * L / 2)

    def _max_note_x(self):
        far = max([self.X(max(sp["x0"], sp["x1"])) for sp in self._axis_spans] or [0])
        m = max([far + 10 + len(sp["label"]) * 4.8 for sp in self._axis_spans if sp["label"]] or [0])
        for kind, v in self.layers:
            if kind == "note" and v["anchor"] == "start":
                m = max(m, self.X(v["x"]) + len(v["text"]) * v["size"] * 0.56)
        return m

    # ---- render
    def svg(self, standalone=True):
        W, H, ox, oy = self.W, self.H, self.ox, self.oy
        o = []
        # A counter, not hash(): Python randomises string hashes per run, which made every build differ
        # (and the Worksheet Maker's --check fail). The counter also keeps ids unique on one page.
        uid = f"ah{next(_MARKER_IDS)}"
        o.append(f'<defs><marker id="{uid}" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">'
                 f'<path d="M0,0 L8,4 L0,8 z" fill="#111827"/></marker>'
                 f'<marker id="{uid}c" markerWidth="5" markerHeight="5" refX="4.6" refY="2.5" orient="auto">'
                 f'<path d="M0,0 L5,2.5 L0,5 z" fill="context-stroke"/></marker>'
                 f'<marker id="{uid}d" markerWidth="5" markerHeight="5" refX="4.2" refY="2.5" orient="auto-start-reverse" markerUnits="userSpaceOnUse">'
                 f'<path d="M0,0 L5,2.5 L0,5 z" fill="context-stroke"/></marker></defs>')
        # shades first
        for kind, v in self.layers:
            if kind == "shade":
                pts = " ".join(f"{self.X(x):.1f},{self.Y(y):.1f}" for x, y in v["pts"])
                st = f' stroke="{v["stroke"]}" stroke-width="1"' if v["stroke"] else ""
                o.append(f'<polygon points="{pts}" fill="{v["fill"]}" fill-opacity="{v["opacity"]}"{st}/>')
                if v["label"]:
                    cx = sum(self.X(x) for x, _ in v["pts"]) / len(v["pts"]); cy = sum(self.Y(y) for _, y in v["pts"]) / len(v["pts"])
                    o.append(self._t(cx, cy + 3, v["label"], v["label_color"], 8.5, 700, "middle", raw=True))
        # guides
        for pt in self.points:
            if pt["guides"]:
                x, y = self.px(pt["p"]); gc = _lighten(pt["color"], .45) if pt["color"] != NAMED["dark"] else "#9CA3AF"
                if pt["ylab"]: o.append(f'<line x1="{ox}" y1="{y:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="{gc}" stroke-width="1" stroke-dasharray="3,3"/>')
                if pt["xlab"]: o.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x:.1f}" y2="{oy}" stroke="{gc}" stroke-width="1" stroke-dasharray="3,3"/>')
        # axes
        o.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="6" stroke="#111827" stroke-width="1.4" marker-end="url(#{uid})"/>')
        o.append(f'<line x1="{ox}" y1="{oy}" x2="{W-8}" y2="{oy}" stroke="#111827" stroke-width="1.4" marker-end="url(#{uid})"/>')
        o.append(self._t(ox, -4, self.ylabel, "#111827", 10, 700, "middle", raw=True))
        rows = [oy + 24 + k * 12 for k in range(len(self._axis_spans))]
        ends = []
        for sp in self._axis_spans:
            x0p, x1p = sorted((self.X(sp["x0"]), self.X(sp["x1"])))
            if x1p - x0p < SPAN_MIN:                       # keep the shaft at least 2x each arrowhead
                m = (x0p + x1p) / 2; x0p, x1p = m - SPAN_MIN / 2, m + SPAN_MIN / 2
            ends.append((x0p, x1p))
        label_x = max(e[1] for e in ends) + 6 if ends else 0   # all span labels start at the same x
        for r, sp, (x0p, x1p) in zip(rows, self._axis_spans, ends):
            o.append(f'<line x1="{x0p:.1f}" y1="{r}" x2="{x1p:.1f}" y2="{r}" stroke="{sp["color"]}" stroke-width="1.4" marker-start="url(#{uid}d)" marker-end="url(#{uid}d)"/>')
            if sp["label"]:
                o.append(self._t(label_x, r + 3, sp["label"], sp["color"], 8.5, 700, "start", raw=True))
        self._title_y = (rows[-1] + 19) if rows else oy + 27
        o.append(self._t(W - 8, self._title_y, self.xlabel, "#111827", 10, 700, "end", raw=True))
        if self.origin: o.append(self._t(ox - 10, oy + 12, self.origin, LABEL_GREY, 9, 400, "start", raw=True))
        # curves, bars, arrows, notes in insertion order
        for kind, v in self.layers:
            if kind == "curve":
                c = self.curves[v]; pts = [self.px(p) for p in c["pts"]]
                d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
                da = ' stroke-dasharray="5,3"' if c["dash"] else ""
                o.append(f'<path d="{d}" fill="none" stroke="{c["color"]}" stroke-width="{c["width"]}"{da} stroke-linecap="round"/>')
                if c["label"]:
                    if c["label_pos"] == "top":
                        o.append(self._t(pts[-1][0], pts[-1][1] - 5, c["label"], c["color"], 9.5, 700, "middle"))
                    elif c["label_pos"] == "start":
                        o.append(self._t(pts[0][0] - 3, pts[0][1] - 4, c["label"], c["color"], 9.5, 700, "end"))
                    else:
                        (x1, y1), (x0, y0) = pts[-1], pts[-2]
                        ang = math.atan2(y1 - y0, x1 - x0)
                        lx, ly = x1 + 5 * math.cos(ang) + 2, y1 + 5 * math.sin(ang) + 4
                        o.append(self._t(lx, ly, c["label"], c["color"], 9.5, 700, "start"))
            elif kind == "bar" and v["arrows"]:
                o.append(f'<line x1="{self.X(v["x0"]):.1f}" y1="{self.Y(v["y"]):.1f}" x2="{self.X(v["x1"]):.1f}" y2="{self.Y(v["y"]):.1f}" stroke="{v["color"]}" stroke-width="{v["w"]}" marker-start="url(#{uid}d)" marker-end="url(#{uid}d)"/>')
            elif kind == "bar":
                o.append(f'<line x1="{self.X(v["x0"]):.1f}" y1="{self.Y(v["y"]):.1f}" x2="{self.X(v["x1"]):.1f}" y2="{self.Y(v["y"]):.1f}" stroke="{v["color"]}" stroke-width="{v["w"]}"/>')
            elif kind == "arrow":
                (sx, sy), (ex, ey) = self._min_len(self.px(v["s"]), self.px(v["e"]), ARROW_MIN)
                o.append(f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{v["color"]}" stroke-width="1.5" marker-end="url(#{uid}c)"/>')
            elif kind == "note":
                o.append(self._t(self.X(v["x"]), self.Y(v["y"]), v["text"], v["color"], v["size"], v["weight"], v["anchor"]))
        # points + axis labels
        for pt in self.points:
            x, y = self.px(pt["p"])
            o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{pt["r"]}" fill="{pt["color"]}"/>')
            lc = pt["color"] if pt["color"] != NAMED["dark"] else LABEL_GREY
            if pt["ylab"]: o.append(self._t(ox - 4, y + 3, pt["ylab"], lc, 9, 700, "end"))
            if pt["xlab"]: o.append(self._t(x, oy + 12, pt["xlab"], lc, 9, 700, "middle"))
            if pt["tag"]:
                dx, dy, anc = {"nw": (-7, -6, "end"), "ne": (7, -6, "start"), "sw": (-7, 13, "end"), "se": (7, 13, "start")}[pt.get("tag_pos", "nw")]
                o.append(self._t(x + dx, y + dy, pt["tag"], lc, 10, 700, anc))
        for y, lab, col in self._yticks:
            o.append(self._t(ox - 4, self.Y(y) + 3, lab, col, 9, 700, "end"))
        for x, lab, col in self._xticks:
            o.append(self._t(self.X(x), oy + 12, lab, col, 9, 700, "middle"))
        self._check_label_crowding()
        body = "".join(o)
        half = len(self.ylabel) * 2.9 + 4                       # approx half-width of the centred y-axis title
        x0 = min(0, int(ox - half)); right_pad = max(0, int(self._max_note_x() - W + 4))
        attrs = f'xmlns="http://www.w3.org/2000/svg" viewBox="{x0} -14 {W - x0 + right_pad} {self._title_y + 6 + 14}" font-family="{FONT}"'
        return f'<svg {attrs} width="100%">{body}</svg>' if standalone else body

    def _t(self, x, y, s, c, size, weight, anchor, raw=False):
        txt = html.escape(s) if raw else sub_label(s)
        return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{c}">{txt}</text>'

    def _check_label_crowding(self):
        xs = sorted([self.X(p["p"][0]) for p in self.points if p["xlab"]] + [self.X(x) for x, _, _ in self._xticks])
        ys = sorted([self.Y(p["p"][1]) for p in self.points if p["ylab"]] + [self.Y(y) for y, _, _ in self._yticks])
        for arr, axis, gap in ((xs, "x", 14), (ys, "y", 9)):
            for a, b in zip(arr, arr[1:]):
                if 0.5 < b - a < gap:
                    print(f"[econ_diagrams] warning: two {axis}-axis labels are only {b-a:.0f}px apart; "
                          f"widen the shift so they don't overlap.", file=sys.stderr)

    def save(self, path):
        with open(path, "w") as f:
            f.write(self.svg())
        return path


# ================================================================== presets
def supply_shift(direction="left", color=TOPIC[1], ylabel="Price", xlabel="Quantity", elastic_demand=False, good=None):
    """Supply shift with the new equilibrium. direction: 'left' (decrease) or 'right' (increase)."""
    d = Diagram(ylabel, xlabel if not good else f"Quantity of {good}", color)
    if elastic_demand:
        d.line("D", (1.0, 7.6), (9.2, 2.4), "main")
    else:
        d.line("D", (1.0, 9.0), (8.8, 0.8), "main")
    d.line("S1", (1.0, 1.0), (9.0, 9.0), "grey")
    if direction == "left":
        d.line("S2", (0.2, 2.6), (7.2, 9.6), "red"); d.shift("S1", "S2", .78)
        d.point("D", "S1", "P1", "Q1"); d.point("D", "S2", "P2", "Q2", "red")
    else:
        d.line("S2", (2.6, 0.2), (9.6, 7.2), "red"); d.shift("S1", "S2", .78)
        d.point("D", "S1", "P1", "Q1"); d.point("D", "S2", "P2", "Q2", "red")
    return d

def demand_shift(direction="right", color=TOPIC[1], ylabel="Price", xlabel="Quantity", good=None):
    d = Diagram(ylabel, xlabel if not good else f"Quantity of {good}", color)
    d.line("S", (1.0, 1.0), (9.0, 9.0), "grey")
    d.line("D1", (0.6, 8.6), (8.4, 0.8), "main")
    if direction == "right":
        d.line("D2", (2.2, 9.6), (9.4, 2.4), "red")
    else:
        d.line("D2", (0.2, 6.8), (6.8, 0.2), "red")
    d.shift("D1", "D2", .3)
    d.point("D1", "S", "P1", "Q1"); d.point("D2", "S", "P2", "Q2", "red")
    return d

def tariff(color=TOPIC[1], good="imports", pw=2.6, t=1.6, ylabel="Price"):
    """Small-country tariff: world price Pw, Pw+t, domestic S and D, Q1–Q4, tariff revenue,
    deadweight-loss triangles, and ↔ arrows for imports before (Q1–Q4) and after (Q2–Q3)."""
    d = Diagram(ylabel, f"Quantity of {good}", color)
    d.line("D", (0.8, 9.4), (9.4, 0.6), "main")
    d.line("S", (0.6, 0.4), (8.6, 9.6), color="#0D9488" if color != "#0D9488" else "#2563EB")
    def x_on(name, y):
        (x1, y1), (x2, y2) = d.curves[name]["pts"]; return x1 + (y - y1) * (x2 - x1) / (y2 - y1)
    q1, q4 = x_on("S", pw), x_on("D", pw); q2, q3 = x_on("S", pw + t), x_on("D", pw + t)
    d.shade([(q1, pw), (q2, pw + t), (q2, pw)], "#FCA5A5")
    d.shade([(q3, pw + t), (q4, pw), (q3, pw)], "#FCA5A5")
    d.shade([(q2, pw), (q3, pw), (q3, pw + t), (q2, pw + t)], "#FDE68A", label="Revenue", stroke="#D97706")
    d.hline("Pw", pw, axis_label="Pw", color="grey", x1=q4)          # stops at the demand curve
    d.hline("Pwt", pw + t, axis_label="Pw+t", color="red", x1=q3)
    for x, lab, red in ((q1, "Q1", False), (q2, "Q2", True), (q3, "Q3", True), (q4, "Q4", False)):
        d.mark((x, pw + t if red else pw), xlab=lab, color="red" if red else "dark", r=0)
    d.axis_span(q2, q3, "red", "Imports after"); d.axis_span(q1, q4, "grey", "Imports before")
    return d

def _floor_or_ceiling(d, level, kind):
    def x_on(name, y):
        (x1, y1), (x2, y2) = d.curves[name]["pts"]; return x1 + (y - y1) * (x2 - x1) / (y2 - y1)
    qd, qs = x_on("D", level), x_on("S", level)
    lab = "Pmax" if kind == "ceiling" else "Pmin"
    d.hline(lab, level, axis_label=lab, color="red", x1=8.3, curve_label="Price " + kind)
    # vertical guides from where the line meets D and S down to the quantity labels
    d.mark((qs, level), xlab="Qs", color="red", r=2.6)
    d.mark((qd, level), xlab="Qd", color="red", r=2.6)
    d.axis_span(qd, qs, "red", "Shortage" if kind == "ceiling" else "Surplus")
    return d

def price_ceiling(color=TOPIC[1], good="rental housing", ceiling=3.2):
    d = Diagram("Price", f"Quantity of {good}", color)
    d.line("D", (1.0, 9.0), (9.0, 1.0)); d.line("S", (1.0, 1.0), (9.0, 9.0), "grey")
    d.point("D", "S", "Pe", "Qe")
    return _floor_or_ceiling(d, ceiling, "ceiling")

def price_floor(color=TOPIC[1], good="labour", floor=6.8, ylabel="Price", xlabel=None):
    d = Diagram(ylabel, xlabel or f"Quantity of {good}", color)
    d.line("D", (1.0, 9.0), (9.0, 1.0)); d.line("S", (1.0, 1.0), (9.0, 9.0), "grey")
    d.point("D", "S", "Pe", "Qe")
    return _floor_or_ceiling(d, floor, "floor")

def subsidy(color=TOPIC[4], good="solar panels"):
    d = Diagram("Price", f"Quantity of {good}", color)
    d.line("D", (1.0, 9.0), (9.0, 1.0), "main"); d.line("S1", (1.0, 2.0), (8.5, 9.5), "grey")
    d.line("S2", (2.4, 0.6), (8.8, 7.0), "green")
    d.note(8.95, 5.9, "with subsidy", "green", "start", 8.5, 400)     # below S2, lower right
    d.shift("S1", "S2", .6)
    d.point("D", "S1", "P1", "Q1"); d.point("D", "S2", "P2", "Q2", "green")
    return d

def ad_as(shift="AD right", color=TOPIC[4]):
    """AD/AS with an upward-sloping SRAS. shift in {'AD right','AD left','SRAS left','SRAS right'}."""
    d = Diagram("Price level", "Real GDP", color)
    d.line("SRAS1", (1.0, 1.2), (8.6, 9.0), "grey") if "SRAS" in shift else d.line("SRAS", (1.0, 1.2), (8.6, 9.0), "grey")
    s_name = "SRAS1" if "SRAS" in shift else "SRAS"
    d.line("AD1" if "AD" in shift and "SRAS" not in shift else "AD", (1.0, 8.8), (8.6, 1.0), "main")
    a_name = "AD1" if "AD" in shift and "SRAS" not in shift else "AD"
    if shift == "AD right":
        d.line("AD2", (2.6, 9.6), (9.6, 2.4), "red"); d.shift("AD1", "AD2", .3)
        d.point("AD1", s_name, "P1", "Y1"); d.point("AD2", s_name, "P2", "Y2", "red")
    elif shift == "AD left":
        d.line("AD2", (0.2, 6.8), (6.6, 0.2), "red"); d.shift("AD1", "AD2", .3)
        d.point("AD1", s_name, "P1", "Y1"); d.point("AD2", s_name, "P2", "Y2", "red")
    elif shift == "SRAS left":
        d.line("SRAS2", (0.2, 3.0), (6.8, 9.8), "red"); d.shift("SRAS1", "SRAS2", .7)
        d.point(a_name, "SRAS1", "P1", "Y1"); d.point(a_name, "SRAS2", "P2", "Y2", "red")
    else:
        d.line("SRAS2", (2.6, 0.4), (9.6, 7.6), "red"); d.shift("SRAS1", "SRAS2", .7)
        d.point(a_name, "SRAS1", "P1", "Y1"); d.point(a_name, "SRAS2", "P2", "Y2", "red")
    return d

def lras_growth(color=TOPIC[4]):
    """Demand outruns capacity (AD1→AD2 against LRAS1), then capacity expands (LRAS2)."""
    d = Diagram("Price level", "Real GDP", color)
    d.vline("LRAS1", 4.9, "ink"); d.vline("LRAS2", 7.2, "main", dash=True, width=1.8)
    d.line("AD1", (1.0, 8.6), (8.6, 1.0), "grey"); d.line("AD2", (3.2, 9.0), (9.4, 2.8), "main")
    d.point("AD1", "LRAS1", "P1", "Y1"); d.point("AD2", "LRAS1", "P2", "", "red")
    d.point("AD2", "LRAS2", "", "Y2", "main")
    return d

def phillips(expectations_shift=True, target=(2.0, 3.0), color=TOPIC[3]):
    """Short-run Phillips curve, optionally shifted up by higher expectations, with A→B move."""
    d = Diagram("Inflation rate", "Unemployment rate", color)
    if target:
        d.band(target[0] * 0.9, target[1] * 0.9, f"{target[0]:g}–{target[1]:g}% target")
    d.curve("PC1", (0.8, 9.0), (2.2, 1.6), (9.4, 1.2), "grey")
    if expectations_shift:
        d.curve("PC2", (1.8, 9.8), (3.2, 4.0), (9.6, 3.6), "main")
        A = (3.7, d._y_on("PC1", 3.7)); B = (5.0, d._y_on("PC2", 5.0))
        d.mark(A, "π1", "U1", tag="A", tag_pos="sw")            # below-left: clear of PC1
        d.mark(B, "π2", "U2", color="red", tag="B", tag_pos="ne") # above-right: clear of PC2
        d.arrow_between(A, B, "red", frac=0.45)
    return d

def fx_market(color=TOPIC[2], show_counterfactual=True):
    """Market for AUD: demand shifts right as rates rise; optional dashed D3 'if only Australia raised rates'."""
    d = Diagram("Price of AUD (US¢)", "Quantity of AUD", color)
    d.line("S", (1.0, 1.2), (9.0, 8.8), "grey")
    d.line("D1", (0.4, 8.2), (6.8, 0.8), "main")
    d.line("D2", (2.8, 8.8), (9.0, 1.6), "#0F766E" if color == TOPIC[2] else "red")
    if show_counterfactual:
        d.line("D3", (5.2, 9.4), (9.6, 4.2), "slate", dash=True, width=1.5)
    d.shift("D1", "D2", .25)
    d.point("D1", "S", "e1", "Q1"); d.point("D2", "S", "e2", "Q2", "main")
    return d

def lorenz(color=TOPIC[3], second=False):
    """Lorenz curve with areas A and B marked (Gini = A / (A + B)). second=True adds a less-equal L2."""
    d = Diagram("Cumulative % of income", "Cumulative % of households", color, origin="0")
    d.line("EQ", (0, 0), (9.6, 9.6), "ink", width=1.4, label="")
    d.curve("L1", (0, 0), (6.6, 1.2), (9.6, 9.6), "main", label="")
    d.note(4.3, 5.2, "Line of equality", "dark", "end", 8.5)
    d.note(5.5, 4.2, "A", "dark", "middle", 11)
    d.note(8.0, 1.2, "B", "dark", "middle", 11)
    d.note(7.2, 3.1, "Lorenz curve", color, "start", 8.5)
    if second:
        d.curve("L2", (0, 0), (7.8, 0.4), (9.6, 9.6), "red", label="")
        d.note(6.2, 0.9, "L2 (less equal)", "red", "end", 8.5)
    d.note(0.4, 9.2, "Gini = A / (A + B)", "dark", "start", 8.5, 400)
    return d

def ppf(color=TOPIC[1], growth=True, goods=("Capital goods", "Consumer goods")):
    d = Diagram(goods[0], goods[1], color)
    d.curve("PPF1", (0, 7.0), (6.6, 6.6), (7.0, 0), "main", label="PPF1")
    if growth:
        d.curve("PPF2", (0, 9.0), (8.6, 8.6), (9.0, 0), "red", label="PPF2")
        d.shift("PPF1", "PPF2", at=0.5, frac=0.4)        # centred in the gap between the frontiers
    return d

# helper for bezier y at x
def _y_on(self, name, x):
    pts = self.curves[name]["pts"]
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        if min(x1, x2) <= x <= max(x1, x2) and x1 != x2:
            return y1 + (x - x1) * (y2 - y1) / (x2 - x1)
    raise ValueError(f"x={x} not on {name}")
Diagram._y_on = _y_on

PRESETS = dict(supply_shift=supply_shift, demand_shift=demand_shift, tariff=tariff, price_ceiling=price_ceiling,
               price_floor=price_floor, subsidy=subsidy, ad_as=ad_as, lras_growth=lras_growth, phillips=phillips,
               fx_market=fx_market, lorenz=lorenz, ppf=ppf)

def gallery(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    cards = []
    demos = [("supply_shift", supply_shift(good="oil")), ("demand_shift", demand_shift()),
             ("tariff", tariff(good="cheese")), ("price_ceiling", price_ceiling()), ("price_floor", price_floor(good="labour", ylabel="Wage")),
             ("subsidy", subsidy()), ("ad_as: AD right", ad_as("AD right")), ("ad_as: SRAS left", ad_as("SRAS left")),
             ("lras_growth", lras_growth()), ("phillips", phillips()), ("fx_market", fx_market()), ("lorenz", lorenz()), ("ppf", ppf())]
    for name, d in demos:
        fn = name.replace(": ", "_").replace(" ", "_") + ".svg"
        d.save(os.path.join(out_dir, fn))
        cards.append(f'<div class="card"><div class="t">{name}</div>{d.svg()}</div>')
    page = ('<!doctype html><meta charset="utf-8"><style>body{font-family:Inter,Arial,sans-serif;background:#fff;margin:24px}'
            '.g{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.card{border:1px solid #E5E7EB;background:#FAFBFC;border-radius:14px;padding:12px}'
            '.t{font-size:12px;font-weight:700;margin-bottom:6px}</style><div class="g">' + "".join(cards) + "</div>")
    with open(os.path.join(out_dir, "gallery.html"), "w") as f:
        f.write(page)
    return os.path.join(out_dir, "gallery.html")

if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--gallery":
        print(gallery(sys.argv[2]))
    else:
        print(__doc__)
