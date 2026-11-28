"""Diagram specs (the DIA: line of a bank question) -> SVG in the house style (econ_diagrams.py).

A spec is the diagram type, then words, then optional key=value settings:

    adas AD left              AD-AS; AD or AS shifts right or left (AS is called AS, as in the syllabus)
    lras AD right             AD shifts right against a fixed LRAS (SRAS is named because LRAS is there)
    lras growth               LRAS shifts right (long-run growth)
    fx D right                market for the Australian dollar; D or S shifts
    labour S left             labour market; D or S shifts
    minwage                   labour market with a minimum wage above equilibrium (unemployment)
    sd D right good=coffee    any market; D or S shifts
    ceiling good=rental housing      price ceiling (shortage)
    floor good=wheat                 price floor (surplus)
    tariff good=steel         free trade -> tariff (Pw, Pw+t, Q1-Q4, revenue, deadweight losses)
    quota good=cheese         quota (importers keep the extra revenue from the higher price)
    subsidy good=canned fruit production subsidy to import-competing producers
    extern good=electricity   negative externality (MPC, MSC, D; market and efficient output)
    lorenz more | less        Lorenz curve moves away from (more) or towards (less) the line of equality
    phillips along | right    move along the Phillips curve, or the curve shifts right
    ppf growth | inside       PPF shifts out, or a point inside the frontier
    ppf points                points on (A, B), inside (C) and outside (D) the frontier

  Year 11 (2025 syllabus):
    tax good=cigarettes       per-unit tax: S1 -> S2, consumers pay P2, producers keep P3; revenue and deadweight loss
    extern pos good=vaccinations     positive externality in consumption (MPB, MSB, S; market and efficient output)
    ped elastic | inelastic | unit | perfectly-elastic | perfectly-inelastic    demand curve of that elasticity
    pes elastic | inelastic | unit | perfectly-elastic | perfectly-inelastic    supply curve of that elasticity
    along D fall | D rise | S rise | S fall     a movement along one curve (expansion or contraction) after a price change
    funds D right             loanable funds market (interest rate); D or S shifts
    lrac                      long-run average cost: economies and diseconomies of scale, the technical optimum
    cycle                     the business cycle around trend growth: peak, contraction, trough, expansion

Settings: `given` shows the student the starting diagram (otherwise blank, labelled axes);
`t=1..4` sets the topic colour; `good=...` names the product (may contain spaces, so put it last).

Label tasks use `label <type>`: the student copy replaces each label with a number. Types: adas, fx, tariff, minwage,
extern, lorenz, and for Year 11 sd, tax, pos (positive externality), lrac, cycle.
Read tasks use the numbered figures `fig1` ... `fig8` (exact numbers, so every answer is clean).
"""
import re
from econ_diagrams import Diagram, TOPIC

LETTERS = [f"({i})" for i in range(1, 11)]   # label tasks number the gaps: (1), (2) ... (letters would clash with D and S)


def parse(spec):
    spec = spec.strip()
    good = None
    m = re.search(r"\bgood=(.+)$", spec)
    if m:
        good, spec = m.group(1).strip(), spec[:m.start()].strip()
    words = spec.split()
    opts = {w.split("=", 1)[0]: w.split("=", 1)[1] for w in words if "=" in w}
    words = [w for w in words if "=" not in w]
    return words[0], words[1:], opts, good


def _col(opts, default):
    t = int(opts.get("t", default))
    return TOPIC[t]


def _x_on(d, name, y):
    (x1, y1), (x2, y2) = d.curves[name]["pts"][0], d.curves[name]["pts"][-1]
    return x1 + (y - y1) * (x2 - x1) / (y2 - y1)


# ---------------------------------------------------------------- shift diagrams
SHIFT_LINES = {   # data-space endpoints for the two curves and each shift
    "D0": ((1.0, 8.8), (8.6, 1.0)), "D+": ((2.6, 9.6), (9.6, 2.4)), "D-": ((0.2, 6.8), (6.6, 0.2)),
    "S0": ((1.0, 1.2), (8.6, 9.0)), "S+": ((2.6, 0.4), (9.6, 7.6)), "S-": ((0.2, 3.0), (6.8, 9.8)),
}


def shift_diagram(ylab, xlab, color, dname, sname, which, direction, yv, xv, stage):
    """stage: 'blank' | 'given' | 'answer'. which: 'D' or 'S'; direction: 'right' or 'left'.
    Original curve grey, new curve red, the curve that does not move in the topic colour."""
    d = Diagram(ylab, xlab, color)
    if stage == "blank":
        return d
    if stage == "given":
        d.line(dname, *SHIFT_LINES["D0"], color="main")
        d.line(sname, *SHIFT_LINES["S0"], color="main")
        d.point(dname, sname, yv + "1", xv + "1")
        return d
    sign = "+" if direction == "right" else "-"
    if which == "D":
        d.line(dname + "1", *SHIFT_LINES["D0"], color="grey")
        d.line(sname, *SHIFT_LINES["S0"], color="main")
        d.line(dname + "2", *SHIFT_LINES["D" + sign], color="red")
        d.shift(dname + "1", dname + "2", .3)
        d.point(dname + "1", sname, yv + "1", xv + "1")
        d.point(dname + "2", sname, yv + "2", xv + "2", "red")
    else:
        d.line(dname, *SHIFT_LINES["D0"], color="main")
        d.line(sname + "1", *SHIFT_LINES["S0"], color="grey")
        d.line(sname + "2", *SHIFT_LINES["S" + sign], color="red")
        d.shift(sname + "1", sname + "2", .7)
        d.point(dname, sname + "1", yv + "1", xv + "1")
        d.point(dname, sname + "2", yv + "2", xv + "2", "red")
    return d


def lras_diagram(color, variant, stage):
    d = Diagram("Price level", "Real GDP", color)
    if stage == "blank":
        return d
    if variant == "growth":
        d.vline("LRAS1" if stage == "answer" else "LRAS", 4.6, "ink")
        d.line("AD", (1.0, 8.6), (8.6, 1.0), "main")
        if stage == "given":
            d.point("AD", "LRAS", "P1", "Y1")
            return d
        d.vline("LRAS2", 6.8, "red")
        d.arrow_between((4.6, 8.6), (6.8, 8.6), "red", frac=.5)
        d.point("AD", "LRAS1", "P1", "Y1")
        d.point("AD", "LRAS2", "P2", "Y2", "red")
        return d
    # AD right against fixed LRAS: the extra demand only raises prices
    d.vline("LRAS", 5.0, "ink")
    d.line("SRAS", (1.0, 1.4), (8.8, 9.2), "grey")
    d.line("AD1" if stage == "answer" else "AD", (1.0, 8.8), (8.6, 1.2), "main" if stage == "given" else "grey")
    if stage == "given":
        d.point("AD", "SRAS", "P1", "Y1")
        return d
    d.line("AD2", (2.8, 9.6), (9.6, 2.8), "red")
    d.shift("AD1", "AD2", .3)
    d.point("AD1", "SRAS", "P1", "Y1")
    d.point("AD2", "SRAS", "P2", "Y2", "red")
    return d


def minwage(color, stage, letters=None):
    d = Diagram("Wage rate", "Quantity of labour", color)
    if stage == "blank":
        return d
    L = letters or {}
    d.line("D", (1.0, 9.0), (9.0, 1.0), label=L.get("D", "D"))
    d.line("S", (1.0, 1.0), (9.0, 9.0), "grey", label=L.get("S", "S"))
    d.point("D", "S", L.get("We", "We"), L.get("Qe", "Qe"))
    if stage == "given":
        return d
    w = 6.8
    qd, qs = _x_on(d, "D", w), _x_on(d, "S", w)
    d.hline("Wmin", w, axis_label=L.get("Wmin", "Wmin"), color="red", x1=8.6, curve_label=L.get("mw", "Minimum wage"))
    d.mark((qd, w), xlab=L.get("Qd", "Qd"), color="red", r=2.6)
    d.mark((qs, w), xlab=L.get("Qs", "Qs"), color="red", r=2.6)
    d.axis_span(qd, qs, "red", L.get("un", "Unemployment"))
    return d


def floor_ceiling(kind, color, good, stage):
    d = Diagram("Price", f"Quantity of {good}" if good else "Quantity", color)
    if stage == "blank":
        return d
    d.line("D", (1.0, 9.0), (9.0, 1.0))
    d.line("S", (1.0, 1.0), (9.0, 9.0), "grey")
    d.point("D", "S", "Pe", "Qe")
    if stage == "given":
        return d
    level = 3.2 if kind == "ceiling" else 6.8
    qd, qs = _x_on(d, "D", level), _x_on(d, "S", level)
    lab = "Pmax" if kind == "ceiling" else "Pmin"
    d.hline(lab, level, axis_label=lab, color="red", x1=8.6, curve_label="Price " + kind)
    d.mark((qs, level), xlab="Qs", color="red", r=2.6)
    d.mark((qd, level), xlab="Qd", color="red", r=2.6)
    d.axis_span(qd, qs, "red", "Shortage" if kind == "ceiling" else "Surplus")
    return d


# ---------------------------------------------------------------- protection
def protection(kind, color, good, stage, letters=None):
    """Free trade at Pw, then a tariff, a quota or a production subsidy (import-competing producers)."""
    L = letters or {}
    d = Diagram("Price", f"Quantity of {good}" if good else "Quantity", color)
    if stage == "blank":
        return d
    d.line("D", (0.8, 9.4), (9.4, 0.6), label=L.get("D", "D"))
    s_col = "#0D9488" if color != "#0D9488" else "#2563EB"
    pw, t = 2.6, 1.6
    if kind == "subsidy":
        d.line("S1" if stage == "answer" else "S", (0.6, 0.4), (8.6, 9.6), color=s_col, label=L.get("S1", "S1" if stage == "answer" else "S"))
    else:
        d.line("S", (0.6, 0.4), (8.6, 9.6), color=s_col, label=L.get("S", "S"))
    sname = "S1" if (kind == "subsidy" and stage == "answer") else "S"
    q1, q4 = _x_on(d, sname, pw), _x_on(d, "D", pw)
    d.hline("Pw", pw, axis_label=L.get("Pw", "Pw"), color="grey", x1=q4)
    if stage == "given":
        d.mark((q1, pw), xlab="Q1", r=0)
        d.mark((q4, pw), xlab="Q2", r=0)
        d.axis_span(q1, q4, "grey", "Imports")
        return d
    if kind == "subsidy":
        # S shifts right by the subsidy; consumers still pay Pw; production rises Q1 -> Q2
        k, sub = (9.6 - 0.4) / (8.6 - 0.6), t            # slope of S1; the subsidy per unit (same size as the tariff)
        d.line("S2", (0.6 + sub / k, 0.4), (8.6, 9.6 - sub), color="red", label=L.get("S2", "S2"))
        d.shift("S1", "S2", .6)
        q2 = _x_on(d, "S2", pw)
        ps = pw + sub                                     # the price producers receive
        d.shade([(q1, pw), (q2, pw), (q2, ps)], "#FCA5A5")
        d.shade([(0, pw), (q1, pw), (q2, ps), (0, ps)], "#BBF7D0", label=L.get("ps", "PS gain"), label_color="#166534")
        d.hline("Ps", ps, axis_label=L.get("Ps", "Pw+s"), color="red", x1=q2)   # producers receive the world price plus the subsidy
        d.mark((q1, pw), xlab="Q1", r=0)
        d.mark((q2, pw), xlab="Q2", color="red", r=0)
        d.mark((q4, pw), xlab="Q3", r=0)
        d.axis_span(q2, q4, "red", "Imports after")
        d.axis_span(q1, q4, "grey", "Imports before")
        return d
    q2, q3 = _x_on(d, "S", pw + t), _x_on(d, "D", pw + t)
    d.shade([(q1, pw), (q2, pw + t), (q2, pw)], "#FCA5A5")
    d.shade([(q3, pw + t), (q4, pw), (q3, pw)], "#FCA5A5")
    lab = L.get("rev", "Revenue" if kind == "tariff" else "Importers")
    d.shade([(q2, pw), (q3, pw), (q3, pw + t), (q2, pw + t)], "#FDE68A", label=lab, stroke="#D97706")
    d.hline("Pwt", pw + t, axis_label=L.get("Pwt", "Pw+t" if kind == "tariff" else "P1"), color="red", x1=q3)
    for x, lab, red in ((q1, "Q1", False), (q2, "Q2", True), (q3, "Q3", True), (q4, "Q4", False)):
        d.mark((x, pw + t if red else pw), xlab=lab, color="red" if red else "dark", r=0)
    d.axis_span(q2, q3, "red", "Quota" if kind == "quota" else "Imports after")
    d.axis_span(q1, q4, "grey", "Imports before")
    return d


def extern(color, good, stage, letters=None):
    L = letters or {}
    d = Diagram("Price, cost", f"Quantity of {good}" if good else "Quantity", color)
    if stage == "blank":
        return d
    d.line("D", (1.0, 9.0), (9.0, 1.0), label=L.get("D", "D (MPB)"))
    d.line("MPC", (1.0, 1.0), (9.0, 9.0), "grey", label=L.get("MPC", "MPC (S)"))
    d.point("D", "MPC", L.get("Pm", "P_m"), L.get("Qm", "Q_m"))
    if stage == "given":
        return d
    d.line("MSC", (0.2, 2.6), (7.4, 9.8), "red", label=L.get("MSC", "MSC"))
    d.point("D", "MSC", L.get("Ps", "Ps"), L.get("Qs", "Qs"), "red")
    qs, qm = d.intersect("D", "MSC"), d.intersect("D", "MPC")
    d.shade([qs, qm, (qm[0], qm[0] + 2.4)], "#FCA5A5")            # MSC is y = x + 2.4: the deadweight loss
    return d


def lorenz(color, variant, stage, letters=None):
    """'more' = inequality rises (the curve bows further from the line); 'less' = it falls."""
    L = letters or {}
    d = Diagram("Cumulative % of income", "Cumulative % of households", color, origin="0")
    if stage == "blank":
        return d
    d.line("EQ", (0, 0), (9.6, 9.6), "ink", width=1.4, label="")
    d.note(4.3, 5.2, L.get("eq", "Line of equality"), "dark", "end", 8.5)
    near, far = (6.6, 2.2), (7.8, 0.4)          # control points: nearer to and further from the line
    first = near if variant == "more" else far
    if stage == "given":
        d.curve("L1", (0, 0), first, (9.6, 9.6), "main", label="")
        d.note(7.2, 4.1 if first == near else 2.6, L.get("L1", "L1"), "dark", "start", 9)
    else:
        second = far if variant == "more" else near
        d.curve("L1", (0, 0), first, (9.6, 9.6), "grey", label="")
        d.curve("L2", (0, 0), second, (9.6, 9.6), "red", label="")
        for ctrl, text, col in ((first, "L1", "dark"), (second, "L2", "red")):
            if ctrl == near:
                d.note(6.2, 4.9, text, col, "end", 8.5)
            else:
                d.note(7.5, 3.0, text, col, "start", 8.5)
    if letters:
        d.note(5.5, 4.4, L.get("A", "A"), "dark", "middle", 11)
        d.note(8.2, 1.4, L.get("B", "B"), "dark", "middle", 11)
    return d


def phillips(color, variant, stage):
    d = Diagram("Inflation rate", "Unemployment rate", color)
    if stage == "blank":
        return d
    d.curve("PC1" if variant == "right" and stage == "answer" else "PC", (0.8, 9.0), (2.2, 1.6), (9.4, 1.2), "grey" if stage == "answer" else "main")
    name = "PC1" if variant == "right" and stage == "answer" else "PC"
    if stage == "given":
        return d
    if variant == "right":
        d.curve("PC2", (1.8, 9.8), (3.2, 4.0), (9.6, 3.6), "red")
        A = (3.7, d._y_on(name, 3.7))
        B = (5.0, d._y_on("PC2", 5.0))
        d.mark(A, "π1", "U1", tag="A", tag_pos="sw")
        d.mark(B, "π2", "U2", color="red", tag="B", tag_pos="ne")
        d.arrow_between(A, B, "red", frac=0.45)
    else:  # a movement along the curve (lower unemployment, higher inflation)
        A = (5.0, d._y_on(name, 5.0))
        B = (2.6, d._y_on(name, 2.6))
        d.mark(A, "π1", "U1", tag="A", tag_pos="ne")
        d.mark(B, "π2", "U2", color="red", tag="B", tag_pos="ne")
        d.arrow_between(A, B, "red", frac=0.45)
    return d


def ppf(color, variant, stage):
    d = Diagram("Capital goods", "Consumer goods", color)
    if stage == "blank":
        return d
    d.curve("PPF1" if (variant == "growth" and stage == "answer") else "PPF", (0, 7.0), (6.6, 6.6), (7.0, 0), "main",
            label="PPF1" if (variant == "growth" and stage == "answer") else "PPF")
    if stage == "given":
        return d
    if variant == "growth":
        d.curve("PPF2", (0, 9.0), (8.6, 8.6), (9.0, 0), "red", label="PPF2")
        d.shift("PPF1", "PPF2", at=0.5, frac=0.4)
    elif variant == "points":   # on the frontier (efficient), inside (unemployed resources), outside (unattainable)
        d.mark((3.4, 6.2), tag="A", tag_pos="sw", guides=False)
        d.mark((6.2, 3.4), tag="B", tag_pos="sw", guides=False)
        d.mark((2.8, 2.8), tag="C", tag_pos="ne", guides=False, color="red")
        d.mark((6.6, 6.6), tag="D", tag_pos="ne", guides=False, color="red")
        d.note(0.3, 1.7, "Inside: unemployed resources", "red", "start", 8.5, 400)
        d.note(5.0, 7.7, "Outside: unattainable", "red", "start", 8.5, 400)
    else:  # a point inside the frontier: unemployed resources
        d.mark((3.2, 3.0), tag="A", tag_pos="sw", guides=False, color="red")
        d.note(3.5, 2.2, "Unemployed resources", "red", "start", 8.5, 400)
    return d


# ---------------------------------------------------------------- Year 11 (2025 syllabus)
def tax(color, good, stage, letters=None):
    """A per-unit indirect tax on producers: S1 shifts up by the tax to S2. Consumers pay P2, producers keep P3
    (P2 less the tax) and the quantity falls from Q1 to Q2. Shaded: the tax revenue and the deadweight loss."""
    L = letters or {}
    d = Diagram("Price", f"Quantity of {good}" if good else "Quantity", color)
    if stage == "blank":
        return d
    d.line("D", (1.0, 9.0), (9.0, 1.0), label=L.get("D", "D"))                     # y = 10 - x
    s1 = "S1" if stage == "answer" else "S"
    d.line(s1, (1.0, 1.0), (9.0, 9.0), "grey" if stage == "answer" else "main", label=L.get("S1", s1))   # y = x
    if stage == "given":
        d.point("D", s1, "P1", "Q1")
        return d
    t = 2.2
    d.line("S2", (0.2, 0.2 + t), (7.2, 7.2 + t), "red", label=L.get("S2", "S2"))   # y = x + t
    d.shift("S1", "S2", .72)
    q2 = (10 - t) / 2
    p2, p3 = 10 - q2, 10 - q2 - t
    d.shade([(0, p3), (q2, p3), (q2, p2), (0, p2)], "#FDE68A", stroke="#D97706")
    d.note(q2 / 2, 5.35, L.get("rev", "Tax revenue"), "#92400E", "middle", 8.5)
    d.shade([(q2, p2), (q2, p3), (5.0, 5.0)], "#FCA5A5")
    d.point("D", "S1", L.get("P1", "P1"), L.get("Q1", "Q1"))
    d.point("D", "S2", L.get("P2", "P2"), L.get("Q2", "Q2"), "red")
    d.hline("P3", p3, axis_label=L.get("P3", "P3"), color="red", x1=q2)
    return d


def extern_pos(color, good, stage, letters=None):
    """A positive externality in consumption: marginal social benefit (MSB) lies above the private demand
    curve (MPB), so the market settles at Q_m, below the efficient Qs. Shaded: the welfare lost."""
    L = letters or {}
    d = Diagram("Price, benefit", f"Quantity of {good}" if good else "Quantity", color)
    if stage == "blank":
        return d
    d.line("S", (1.0, 1.0), (9.0, 9.0), label=L.get("S", "S (MSC)"))                 # y = x
    d.line("MPB", (0.6, 8.6), (8.0, 1.2), "grey", label=L.get("MPB", "D (MPB)"))      # y = 9.2 - x
    d.point("MPB", "S", L.get("Pm", "P_m"), L.get("Qm", "Q_m"))
    if stage == "given":
        return d
    d.line("MSB", (1.8, 9.6), (9.6, 1.8), "red", label=L.get("MSB", "MSB"))           # y = 11.4 - x
    d.point("MSB", "S", L.get("Ps", "Ps"), L.get("Qs", "Qs"), "red")
    d.shade([(4.6, 4.6), (4.6, 6.8), (5.7, 5.7)], "#FCA5A5")                          # between MSB and S, Q_m to Qs
    return d


ELASTIC = {   # degree -> (demand line, P1, P2), (supply line, P1, P2); data space 0-10
    "elastic": ((((0.4, 6.4), (9.4, 3.4)), 4.4, 5.4), (((0.4, 2.4), (9.4, 5.4)), 3.4, 4.4)),
    "inelastic": ((((3.4, 9.4), (6.2, 1.0)), 4.4, 6.4), (((3.2, 0.4), (6.2, 9.4)), 4.4, 6.4)),
}


def elasticity(curve, degree, color, good, stage):
    """Degrees of price elasticity of demand (curve 'D') or supply ('S'): perfectly-elastic, elastic, unit,
    inelastic, perfectly-inelastic. Elastic, unit and inelastic show a price change P1 -> P2 and the quantity
    change Q1 -> Q2 it causes."""
    degree = {"perfect-elastic": "perfectly-elastic", "perfect-inelastic": "perfectly-inelastic", "unitary": "unit"}.get(degree, degree)
    d = Diagram("Price", f"Quantity of {good}" if good else "Quantity", color)
    if stage != "answer":                      # nothing to give: the curve is the answer
        return d
    e = "PED" if curve == "D" else "PES"
    if degree == "perfectly-elastic":
        d.line(curve, (0.4, 5.0), (9.0, 5.0))
        d.ytick(5.0, "P1")
        d.note(0.6, 5.5, f"{e} = ∞ (perfectly elastic)", "main", "start", 8.5)
        return d
    if degree == "perfectly-inelastic":
        d.vline(curve, 5.0, "main", label=curve)
        d.xtick(5.0, "Q1")
        d.note(5.3, 8.4, f"{e} = 0 (perfectly inelastic)", "main", "start", 8.5)
        return d
    if degree == "unit":
        if curve == "D":                       # a rectangular hyperbola, P x Q constant (drawn as a smooth curve)
            d.curve("D", (1.6, 8.75), (2.73, 2.59), (9.2, 1.52), label="D")
            a, b = (2.6, d._y_on("D", 2.6)), (5.6, d._y_on("D", 5.6))
            (q1, p1), (q2, p2) = b, a          # the price rises: from b up to a
        else:                                  # any straight supply line through the origin
            d.line("S", (0.0, 0.0), (9.0, 9.0), label="S")
            (q1, p1), (q2, p2) = (3.6, 3.6), (6.4, 6.4)
        note = f"{e} = 1 (unit elastic)"
    else:
        ln, p1, p2 = ELASTIC[degree][0 if curve == "D" else 1]
        d.line(curve, *ln)
        q1, q2 = _x_on(d, curve, p1), _x_on(d, curve, p2)
        note = f"{e} {'>' if degree == 'elastic' else '<'} 1 ({degree})"
    d.mark((q1, p1), "P1", "Q1")
    d.mark((q2, p2), "P2", "Q2", color="red")
    if curve == "S" and degree in ("inelastic", "unit"):       # these supply curves fill the top right
        d.note(0.4, 9.0, note, "main", "start", 8.5)
    else:
        d.note(9.4, 9.0, note, "main", "end", 8.5)
    return d


def along(curve, direction, color, good, stage):
    """A movement along one curve when the good's own price changes: an expansion or contraction of demand
    (curve 'D') or of supply ('S'). direction is the price: 'fall' or 'rise'."""
    d = Diagram("Price", f"Quantity of {good}" if good else "Quantity", color)
    if stage == "blank":
        return d
    if curve == "D":
        d.line("D", (1.0, 9.0), (9.0, 1.0))
        a, b = ((3.6, 6.4), (6.4, 3.6)) if direction == "fall" else ((6.4, 3.6), (3.6, 6.4))
        word, off, tag = ("Expansion" if direction == "fall" else "Contraction") + " of demand", (0.45, 0.45), "sw"
    else:
        d.line("S", (1.0, 1.0), (9.0, 9.0))
        a, b = ((3.6, 3.6), (6.4, 6.4)) if direction == "rise" else ((6.4, 6.4), (3.6, 3.6))
        word, off, tag = ("Expansion" if direction == "rise" else "Contraction") + " of supply", (-0.45, 0.45), "se"
    d.mark(a, "P1", "Q1", tag="A", tag_pos=tag)
    if stage == "given":
        return d
    d.mark(b, "P2", "Q2", color="red", tag="B", tag_pos=tag)
    d.arrow_between((a[0] + off[0], a[1] + off[1]), (b[0] + off[0], b[1] + off[1]), "red", frac=0.55)
    if curve == "D":
        d.note((a[0] + b[0]) / 2 + 2.4 * off[0], (a[1] + b[1]) / 2 + 2.4 * off[1], word, "red", "start", 8.5)
    else:
        top = max(a, b, key=lambda p: p[1])
        d.note(top[0] - 0.3, top[1] + 1.2, word, "red", "end", 8.5)
    return d


def lrac(color, stage, letters=None):
    """A long-run average cost curve: economies of scale while it falls, diseconomies once it rises; the
    technical optimum is the output where long-run average cost is lowest."""
    L = letters or {}
    d = Diagram("Average cost", "Output", color)
    if stage == "blank":
        return d
    d.curve("LRAC", (0.8, 8.8), (5.0, -1.6), (9.2, 8.8), label=L.get("LRAC", "LRAC"))   # lowest at (5.0, 3.6)
    if stage == "given":
        return d
    d.mark((5.0, 3.6), "AC_{min}", "Q*", color="red")
    d.note(5.0, 5.75, L.get("opt", "Technical optimum"), "red", "middle", 8.5)
    d.arrow((5.0, 5.45), (5.0, 3.95), "red")
    d.note(0.9, 2.2, L.get("eos", "Economies of scale"), "dark", "start", 8.5)
    d.note(9.4, 2.2, L.get("dos", "Diseconomies of scale"), "dark", "end", 8.5)
    return d


def cycle(color, stage, letters=None):
    """The business cycle: real GDP fluctuates around its rising trend. Peak, contraction, trough, expansion."""
    L = letters or {}
    d = Diagram("Real GDP", "Time", color)
    if stage == "blank":
        return d
    trend = lambda x: 2.8 + 0.4 * x
    d.line("TREND", (0.4, trend(0.4)), (9.4, trend(9.4)), "grey", dash=True, width=1.4, label=L.get("trend", "Trend"))
    amp, turns = 1.7, [(0.6, -1), (3.0, 1), (5.6, -1), (8.2, 1)]
    pts = [(x, trend(x) + s * amp) for x, s in turns]
    for i, ((xp, yp), (xt, yt)) in enumerate(zip(pts, pts[1:])):   # two quadratic pieces per swing, flat at each turn
        k, mid = (xt - xp) / 4, ((xp + xt) / 2, (yp + yt) / 2)
        d.curve(f"W{i}a", (xp, yp), (xp + k, yp), mid, label="")
        d.curve(f"W{i}b", mid, (xt - k, yt), (xt, yt), label="")
    if stage == "given":
        return d
    (_, _), (px_, py_), (tx, ty), _ = pts
    d.note(px_, py_ + 0.5, L.get("peak", "Peak"), "red", "middle", 8.5)
    d.note(tx, ty - 0.75, L.get("trough", "Trough"), "red", "middle", 8.5)
    d.note(3.9, 5.9, L.get("down", "Contraction"), "dark", "start", 8.5)
    d.note(7.2, 7.5, L.get("up", "Expansion"), "dark", "end", 8.5)
    return d


# ---------------------------------------------------------------- numbered figures for "read a diagram"
class Num:
    """Map real prices and quantities onto the engine's 0-10 data space."""

    def __init__(self, pmax, qmax):
        self.pmax, self.qmax = pmax, qmax

    def p(self, q, price):
        return (q / self.qmax * 9.4, price / self.pmax * 9.4)


def numbered(fig, color, answer):
    """The protection figures from the Diagram and Calculation Skills resource (exact numbers)."""
    F = FIGS[fig]
    N = Num(F["pmax"], F["qmax"])
    d = Diagram("Price ($)", F["xlab"], color)
    D, S = F["D"], F["S"]          # functions price -> quantity
    pts_d = [N.p(D(p), p) for p in F["drange"]]
    pts_s = [N.p(S(p), p) for p in F["srange"]]
    d.line("D", pts_d[0], pts_d[1])
    d.line("S1" if F.get("S2") else "S", pts_s[0], pts_s[1], color="#0D9488")
    if F.get("S2"):
        pts2 = [N.p(F["S2"](p), p) for p in F["s2range"]]
        d.line("S2", pts2[0], pts2[1], color="red")
    pw, p1 = F["pw"], F["p1"]
    d.hline("Pw", N.p(0, pw)[1], axis_label=f"{pw:g}", color="grey", x1=N.p(D(pw), pw)[0])
    if F["kind"] in ("tariff", "quota"):
        d.hline("P1", N.p(0, p1)[1], axis_label=f"{p1:g}", color="red", x1=N.p(D(p1), p1)[0])
        qs = [S(pw), S(p1), D(p1), D(pw)]
        for q, price in zip(qs, [pw, p1, p1, pw]):
            d.mark(N.p(q, price), xlab=f"{q:g}", color="dark", r=0)
        if answer:
            q1, q2, q3, q4 = qs
            d.shade([N.p(q1, pw), N.p(q2, p1), N.p(q2, pw)], "#FCA5A5")
            d.shade([N.p(q3, p1), N.p(q4, pw), N.p(q3, pw)], "#FCA5A5")
            d.shade([N.p(q2, pw), N.p(q3, pw), N.p(q3, p1), N.p(q2, p1)], "#FDE68A", stroke="#D97706")
    else:   # subsidy: consumers pay pw; producers receive p1
        S2 = F["S2"]
        d.hline("P1", N.p(0, p1)[1], axis_label=f"{p1:g}", color="red", x1=N.p(S(p1), p1)[0])
        for q, price in ((S(pw), pw), (S2(pw), pw), (D(pw), pw)):
            d.mark(N.p(q, price), xlab=f"{q:g}", color="dark", r=0)
        if answer:
            q1, q2 = S(pw), S2(pw)
            d.shade([N.p(q1, pw), N.p(q2, pw), N.p(q2, p1)], "#FCA5A5")
    return d


FIGS = {   # D and S give quantity for a price; ranges are the prices at each end of the drawn line
    "fig1": dict(kind="tariff", xlab="Quantity of steel (million tonnes)", pmax=100, qmax=100, pw=20, p1=30,
                 D=lambda p: 100 - p, S=lambda p: p, drange=(100, 6), srange=(4, 96)),
    "fig6": dict(kind="tariff", xlab="Quantity of bicycles ('000)", pmax=200, qmax=150, pw=100, p1=120,
                 D=lambda p: 200 - p, S=lambda p: 0.5 * p - 20, drange=(196, 56), srange=(44, 196)),
    "fig2": dict(kind="quota", xlab="Quantity of cheese (million kg)", pmax=13, qmax=130, pw=4, p1=6,
                 D=lambda p: 130 - 10 * p, S=lambda p: 10 * p - 20, drange=(12.6, 1.0), srange=(2.4, 12.6)),
    "fig7": dict(kind="quota", xlab="Quantity of sugar (million kg)", pmax=7, qmax=140, pw=2, p1=3,
                 D=lambda p: 140 - 20 * p, S=lambda p: 20 * p - 20, drange=(6.8, 0.5), srange=(1.2, 6.8)),
    "fig3": dict(kind="subsidy", xlab="Quantity of canned fruit (million cans)", pmax=180, qmax=170, pw=50, p1=70,
                 D=lambda p: 170 - p, S=lambda p: p - 10, S2=lambda p: p + 10, drange=(168, 10), srange=(12, 176), s2range=(2, 158)),
    "fig8": dict(kind="subsidy", xlab="Quantity of solar panels ('000)", pmax=620, qmax=60, pw=200, p1=280,
                 D=lambda p: 60 - 0.1 * p, S=lambda p: 0.1 * p - 10, S2=lambda p: 0.1 * p - 2, drange=(596, 60), srange=(104, 600), s2range=(24, 590)),
}


# ---------------------------------------------------------------- label tasks
LABEL_SETS = {
    "adas": ["Price level", "Real GDP", "AD", "AS", "P1", "Y1"],
    "fx": ["Price of A$ (US$)", "Quantity of A$", "D", "S", "e1", "Q1"],
    "tariff": ["Pw", "Pw+t", "D", "S", "Revenue"],
    "minwage": ["D", "S", "Wmin", "Qd", "Qs", "Unemployment"],
    "extern": ["D (MPB)", "MPC (S)", "MSC", "Q_m", "Qs"],
    "lorenz": ["Line of equality", "L1", "A", "B"],
    "sd": ["Price", "Quantity", "D", "S", "Pe", "Qe"],
    "tax": ["S1", "S2", "P2", "P3", "Q2", "Tax revenue"],
    "pos": ["D (MPB)", "MSB", "S (MSC)", "Q_m", "Qs"],
    "lrac": ["LRAC", "Technical optimum", "Economies of scale", "Diseconomies of scale"],
    "cycle": ["Peak", "Trough", "Contraction", "Expansion", "Trend"],
}


def labelled(kind, color, answer):
    """Returns (diagram, [(letter, answer)])."""
    keys = LABEL_SETS[kind]
    letters = {k: (k if answer else LETTERS[i]) for i, k in enumerate(keys)}
    pairs = [(LETTERS[i], k) for i, k in enumerate(keys)]
    if kind == "adas":
        d = Diagram(letters["Price level"], letters["Real GDP"], color)
        d.line("AD", (1.0, 8.8), (8.6, 1.0), label=letters["AD"])
        d.line("AS", (1.0, 1.2), (8.6, 9.0), "grey", label=letters["AS"])
        d.point("AD", "AS", letters["P1"], letters["Y1"])
    elif kind == "fx":
        d = Diagram(letters["Price of A$ (US$)"], letters["Quantity of A$"], color)
        d.line("D", (1.0, 8.8), (8.6, 1.0), label=letters["D"])
        d.line("S", (1.0, 1.2), (8.6, 9.0), "grey", label=letters["S"])
        d.point("D", "S", letters["e1"], letters["Q1"])
    elif kind == "tariff":
        d = protection("tariff", color, None, "answer", letters={"Pw": letters["Pw"], "Pwt": letters["Pw+t"], "D": letters["D"],
                                                                  "S": letters["S"], "rev": letters["Revenue"]})
    elif kind == "minwage":
        d = minwage(color, "answer", letters={"D": letters["D"], "S": letters["S"], "Wmin": letters["Wmin"], "Qd": letters["Qd"],
                                              "Qs": letters["Qs"], "un": letters["Unemployment"], "mw": "" if not answer else "Minimum wage"})
    elif kind == "extern":
        d = extern(color, None, "answer", letters={"D": letters["D (MPB)"], "MPC": letters["MPC (S)"], "MSC": letters["MSC"],
                                                   "Qm": letters["Q_m"], "Qs": letters["Qs"], "Pm": "P_m", "Ps": "Ps",
                                                   "ext": "" if not answer else "External cost"})
    elif kind == "lorenz":
        d = lorenz(color, "more", "given", letters={"eq": letters["Line of equality"], "L1": letters["L1"],
                                                     "A": letters["A"], "B": letters["B"]})
    elif kind == "sd":
        d = Diagram(letters["Price"], letters["Quantity"], color)
        d.line("D", (1.0, 8.8), (8.6, 1.0), label=letters["D"])
        d.line("S", (1.0, 1.2), (8.6, 9.0), "grey", label=letters["S"])
        d.point("D", "S", letters["Pe"], letters["Qe"])
    elif kind == "tax":
        d = tax(color, None, "answer", letters={"S1": letters["S1"], "S2": letters["S2"], "P2": letters["P2"], "P3": letters["P3"],
                                                "Q2": letters["Q2"], "rev": letters["Tax revenue"]})
    elif kind == "pos":
        d = extern_pos(color, None, "answer", letters={"MPB": letters["D (MPB)"], "MSB": letters["MSB"], "S": letters["S (MSC)"],
                                                       "Qm": letters["Q_m"], "Qs": letters["Qs"]})
    elif kind == "lrac":
        d = lrac(color, "answer", letters={"LRAC": letters["LRAC"], "opt": letters["Technical optimum"],
                                           "eos": letters["Economies of scale"], "dos": letters["Diseconomies of scale"]})
    elif kind == "cycle":
        d = cycle(color, "answer", letters={"peak": letters["Peak"], "trough": letters["Trough"], "down": letters["Contraction"],
                                            "up": letters["Expansion"], "trend": letters["Trend"]})
    else:
        raise ValueError(f"no label set for {kind!r}")
    return d, pairs


# ---------------------------------------------------------------- entry points
# Always drawn, so the page (and Claude, in the Claude copy) can set a diagram task on any of them.
BASE = [f"{k} {w}{g}" for k, ws in (("adas", ("AD right", "AD left", "AS right", "AS left")), ("fx", ("D right", "D left", "S right", "S left")),
                                     ("labour", ("D right", "D left", "S right", "S left")), ("sd", ("D right", "D left", "S right", "S left")),
                                     ("lras", ("AD right", "growth")), ("lorenz", ("more", "less")), ("phillips", ("along", "right")),
                                     ("ppf", ("growth", "inside")))
        for w in ws for g in ("", " given")] + [f"{k}{g}" for k in ("minwage", "ceiling", "floor", "tariff", "quota", "subsidy", "extern") for g in ("", " given")]
# Year 11 (2025 syllabus). Elasticity diagrams have no "given" version: the curve is the answer.
BASE += [f"{k} {w}{g}" for k, ws in (("funds", ("D right", "D left", "S right", "S left")), ("along", ("D fall", "D rise", "S rise", "S fall")),
                                      ("extern", ("pos",)), ("ppf", ("points",)))
         for w in ws for g in ("", " given")] + [f"{k}{g}" for k in ("tax", "lrac", "cycle") for g in ("", " given")]
BASE += [f"{k} {w}" for k in ("ped", "pes") for w in ("elastic", "inelastic", "unit", "perfectly-elastic", "perfectly-inelastic")]

def build(spec, stage):
    kind, words, opts, good = parse(spec)
    if kind == "label":
        what = words[0]
        d, pairs = labelled(what, _col(opts, {"adas": 4, "fx": 2, "tariff": 1, "minwage": 4, "extern": 3, "lorenz": 3,
                                              "sd": 1, "tax": 1, "pos": 3, "lrac": 3, "cycle": 3}[what]),
                            answer=stage == "answer")
        return d, pairs
    if kind in FIGS:
        return numbered(kind, _col(opts, 1), stage == "answer"), None
    st = "answer" if stage == "answer" else ("given" if "given" in words else "blank")
    words = [w for w in words if w != "given"]
    if kind == "adas":
        which = "D" if words[0] == "AD" else "S"
        return shift_diagram("Price level", "Real GDP", _col(opts, 4), "AD", "AS", which, words[1], "P", "Y", st), None
    if kind == "lras":
        return lras_diagram(_col(opts, 4), "growth" if words[0] == "growth" else "ad", st), None
    if kind == "fx":
        return shift_diagram("Price of A$ (US$)", "Quantity of A$", _col(opts, 2), "D", "S", words[0], words[1], "e", "Q", st), None
    if kind == "labour":
        return shift_diagram("Wage rate", "Quantity of labour", _col(opts, 3), "D", "S", words[0], words[1], "W", "Q", st), None
    if kind == "sd":
        return shift_diagram("Price", f"Quantity of {good}" if good else "Quantity", _col(opts, 1), "D", "S", words[0], words[1], "P", "Q", st), None
    if kind == "minwage":
        return minwage(_col(opts, 4), st), None
    if kind in ("ceiling", "floor"):
        return floor_ceiling(kind, _col(opts, 1), good, st), None
    if kind in ("tariff", "quota", "subsidy"):
        return protection(kind, _col(opts, 1), good, st), None
    if kind == "extern":
        if words and words[0] == "pos":
            return extern_pos(_col(opts, 3), good, st), None
        return extern(_col(opts, 3), good, st), None
    if kind == "tax":
        return tax(_col(opts, 1), good, st), None
    if kind in ("ped", "pes"):
        return elasticity("D" if kind == "ped" else "S", words[0] if words else "elastic", _col(opts, 1), good, st), None
    if kind == "along":
        return along(words[0], words[1], _col(opts, 1), good, st), None
    if kind == "funds":
        return shift_diagram("Interest rate", "Quantity of loanable funds", _col(opts, 2), "D", "S", words[0], words[1], "r", "Q", st), None
    if kind == "lrac":
        return lrac(_col(opts, 3), st), None
    if kind == "cycle":
        return cycle(_col(opts, 3), st), None
    if kind == "lorenz":
        return lorenz(_col(opts, 3), words[0] if words else "more", st), None
    if kind == "phillips":
        return phillips(_col(opts, 3), words[0] if words else "along", st), None
    if kind == "ppf":
        return ppf(_col(opts, 1), words[0] if words else "growth", st), None
    raise ValueError(f"unknown diagram {kind!r} in {spec!r}")


def render(spec, answer):
    d, _ = build(spec, "answer" if answer else "student")
    return d.svg()


def label_pairs(spec):
    _, pairs = build(spec, "answer")
    return pairs or []
