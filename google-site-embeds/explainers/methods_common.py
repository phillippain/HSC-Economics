"""Shared bits for the five 'methods of protection' explainer pages (Topic 1, 1C.2)."""
C, CD = "#2447d6", "#1a3399"
SITE = "https://sites.google.com/education.nsw.gov.au/hsceconomics-at-sscbwb/topic-1/protection/"
PAGES = [("tariffs", "Tariffs"), ("quotas", "Quotas"), ("subsidies", "Subsidies"),
         ("local-content-rules", "Local content rules"), ("export-incentives", "Export incentives")]


def nav(current):
    """A line of links to the other method pages, for the foot of the explainer text."""
    links = []
    for slug, name in PAGES:
        if slug == current:
            links.append("<b>%s</b>" % name)
        else:
            links.append('<a href="%smethods/%s">%s</a>' % (SITE, slug, name))
    return ('<p><b>Other methods:</b> %s. See also <a href="%s">Protection</a> (reasons and effects) and '
            '<a href="%smethods">Methods of protection</a> (all five compared).</p>') % (" · ".join(links), SITE, SITE)


def x_on(d, name, y):
    (x1, y1), (x2, y2) = d.curves[name]["pts"]
    return x1 + (y - y1) * (x2 - x1) / (y2 - y1)


def quota_diagram(ed, good="cheese"):
    """Small importing country: world price Pw; a quota fixes imports at Q2-Q3, so the domestic price rises to P1
    where S + quota meets D. Importers keep the extra revenue (gold); deadweight losses red."""
    d = ed.Diagram("Price", "Quantity of %s" % good, ed.TOPIC[1])
    d.line("D", (0.8, 9.4), (9.4, 0.6), "main")
    d.line("S", (0.6, 0.4), (8.6, 9.6), color="#0D9488")
    pw, p1 = 2.6, 4.2
    q1, q4 = x_on(d, "S", pw), x_on(d, "D", pw)
    q2, q3 = x_on(d, "S", p1), x_on(d, "D", p1)
    quota = q3 - q2
    d.line("S+quota", (q1 + quota, pw), (x_on(d, "S", 7.4) + quota, 7.4), "red")
    d.shade([(q1, pw), (q2, p1), (q2, pw)], "#FCA5A5")
    d.shade([(q3, p1), (q4, pw), (q3, pw)], "#FCA5A5")
    d.shade([(q2, pw), (q3, pw), (q3, p1), (q2, p1)], "#FDE68A", label="Importers", stroke="#D97706")
    d.hline("Pw", pw, axis_label="Pw", color="grey", x1=q4)
    d.hline("P1", p1, axis_label="P1", color="red", x1=q3)
    for x, lab, red in ((q1, "Q1", False), (q2, "Q2", True), (q3, "Q3", True), (q4, "Q4", False)):
        d.mark((x, p1 if red else pw), xlab=lab, color="red" if red else "dark", r=0)
    d.axis_span(q2, q3, "red", "Quota"); d.axis_span(q1, q4, "grey", "Imports before")
    return d


def subsidy_diagram(ed, good="steel"):
    """Import-competing producer subsidy at the world price: S shifts right to S+subsidy, domestic output rises
    from Q1 to Q2, consumption stays at Q3 and the price stays at Pw, so imports shrink."""
    d = ed.Diagram("Price", "Quantity of %s" % good, ed.TOPIC[1])
    d.line("D", (0.8, 9.4), (9.4, 0.6), "main")
    d.line("S1", (0.6, 0.4), (8.6, 9.6), color="#0D9488")
    d.line("S2", (2.2, 0.4), (9.0, 8.1), "green")
    d.shift("S1", "S2", .6)
    pw = 3.0
    q1, q2, q3 = x_on(d, "S1", pw), x_on(d, "S2", pw), x_on(d, "D", pw)
    d.hline("Pw", pw, axis_label="Pw", color="grey", x1=q3)
    d.mark((q1, pw), xlab="Q1", color="dark", r=0)
    d.mark((q2, pw), xlab="Q2", color="green", r=3)
    d.mark((q3, pw), xlab="Q3", color="dark", r=0)
    d.axis_span(q2, q3, "green", "Imports after"); d.axis_span(q1, q3, "grey", "Imports before")
    return d


def lcr_diagram(ed, good="Australian drama"):
    """A local content rule raises demand for the local product: D shifts right, local price and output rise."""
    d = ed.Diagram("Price", "Quantity of %s" % good, ed.TOPIC[1])
    d.line("S", (1.0, 1.0), (9.0, 9.0), "grey")
    d.line("D1", (0.8, 8.2), (8.2, 0.8), "main")
    d.line("D2", (2.0, 9.4), (9.4, 2.0), "red")
    d.shift("D1", "D2")
    d.point("D1", "S", "P1", "Q1")
    d.point("D2", "S", "P2", "Q2", color="red")
    return d


def export_subsidy_diagram(ed, good="wheat"):
    """Exporting country: world price Pw is above the domestic equilibrium, so the country exports Q2-Q3.
    An export subsidy s per unit lets producers earn Pw+s on exports, so the domestic price rises too:
    local consumption falls (Q2 to Q1), output rises (Q3 to Q4) and exports grow (Q1 to Q4)."""
    d = ed.Diagram("Price", "Quantity of %s" % good, ed.TOPIC[1])
    d.line("D", (0.6, 9.4), (9.4, 0.6), "main")
    d.line("S", (0.6, 0.6), (9.4, 9.4), color="#0D9488")
    pw, s = 6.0, 1.4
    q2, q3 = x_on(d, "D", pw), x_on(d, "S", pw)
    q1, q4 = x_on(d, "D", pw + s), x_on(d, "S", pw + s)
    d.shade([(q1, pw + s), (q4, pw + s), (q4, pw), (q1, pw)], "#FDE68A", label="Subsidy cost", stroke="#D97706")
    d.hline("Pw", pw, axis_label="Pw", color="grey", x1=q3)
    d.hline("Pws", pw + s, axis_label="Pw+s", color="red", x1=q4)
    for x, lab, red, y in ((q1, "Q1", True, pw + s), (q2, "Q2", False, pw), (q3, "Q3", False, pw), (q4, "Q4", True, pw + s)):
        d.mark((x, y), xlab=lab, color="red" if red else "dark", r=0)
    d.axis_span(q2, q3, "grey", "Exports before"); d.axis_span(q1, q4, "red", "Exports after")
    return d
