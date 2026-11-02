#!/usr/bin/env python3
"""Turn a digest (from build/digest.py) plus written summaries into an email-ready HTML page.

    python3 render_email.py DIGEST.json SUMMARIES.json OUT.html [--title "..."] [--artifact]

SUMMARIES.json maps a record id to its two-sentence summary. An entry may also be an object:
    {"summary": "Two sentences.", "stats": [0, 2, 3], "caveat": "One short caution."}
`stats` picks which figures (by their index in the digest) to show, up to 3; without it the
first three are used. `caveat` is shown in small type under the summary. An optional
"_skip": ["id", ...] drops records (housekeeping edits) from the email. A record with no
summary falls back to the one-line `summary` in the record and is listed on stderr.

The email is one table-based block with inline styles (the only styling Gmail and Outlook keep
when pasted), inside <div id="email">. Above it, outside the block, sits a "Copy for email"
bar that is not copied. --artifact writes the fragment the Artifact tool wants.
"""
import argparse, datetime, html, json, re, sys

INK, MUTED, LINE, ACC, HL = "#0e1526", "#4a5468", "#d3d9e6", "#2447d6", "#ffe14d"
FONT = "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"
HEAD = "'Bricolage Grotesque','Avenir Next','Segoe UI',Helvetica,Arial,sans-serif"
TYPE_COLOR = {"news": "#2447d6", "stats": "#0e7a5f", "report": "#8a3fb0", "graph": "#b0561a", "case": "#4a5468"}
ICON = {"h09:T1": "🌏", "h09:T2": "🦘", "h09:T3": "📉", "h09:T4": "🏦",
        "y12:Y1": "📉", "y12:Y2": "🏦", "y12:Y3": "🌏",
        "y11:P1": "💡", "y11:P2": "🛒", "y11:P3": "🏠", "y11:P4": "💳", "y11:P5": "🏛️", "y11:P6": "🚢",
        "other": "📄"}
COURSE_HEAD = {"hsc": "HSC · 2009 syllabus (Year 12 until the HSC in 2027)",
               "hsc25": "HSC · 2025 syllabus (first examined 2028)",
               "prelim": "Year 11 (Preliminary) · 2025 syllabus",
               "other": "Not yet tagged to a syllabus"}
FW_LINE = {"h09": "HSC 2009", "y12": "HSC 2025", "y11": "Year 11"}


def e(s):
    return html.escape(str(s if s is not None else ""), quote=True)


# ---- colour helpers: keep white text on topic colours readable (WCAG AA) ----
def _rgb(h):
    h = h.lstrip("#")
    return [int(h[i:i + 2], 16) for i in (0, 2, 4)]


def _lum(rgb):
    f = lambda c: (c / 255 / 12.92) if c / 255 <= 0.03928 else (((c / 255 + 0.055) / 1.055) ** 2.4)
    r, g, b = (f(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def strong(h):
    """Darken a colour until white text on it has contrast >= 4.5."""
    rgb = _rgb(h)
    for _ in range(40):
        if 1.05 / (_lum(rgb) + 0.05) >= 4.5:
            break
        rgb = [int(c * 0.93) for c in rgb]
    return "#%02x%02x%02x" % tuple(rgb)


def tint(h, k=0.12):
    """The colour mixed 88% with white, for chip backgrounds."""
    return "#%02x%02x%02x" % tuple(int(255 - (255 - c) * k) for c in _rgb(h))


def pretty(iso):
    try:
        return datetime.date.fromisoformat(iso).strftime("%A %-d %B %Y")
    except (ValueError, TypeError):
        return iso or ""


def short_date(iso):
    try:
        return datetime.date.fromisoformat(iso).strftime("%-d %b %Y")
    except (ValueError, TypeError):
        return iso or ""


def clip(text, n):
    text = (text or "").strip()
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def pill(text, fg, bg, border=None, upper=True):
    b = f"border:1px solid {border};" if border else ""
    return (f'<span style="display:inline-block;font:700 11px/1.2 {FONT};letter-spacing:.04em;'
            f'{"text-transform:uppercase;" if upper else ""}max-width:100%;color:{fg};background:{bg};{b}padding:5px 8px;'
            f'border-radius:10px;margin:0 6px 4px 0;">{e(text)}</span>')


def button(label, url, fg, bg, border):
    if not url:
        return ""
    return (f'<a href="{e(url)}" style="display:inline-block;font:600 13px/1 {FONT};color:{fg};'
            f'background:{bg};border:1.5px solid {border};text-decoration:none;'
            f'padding:10px 14px;border-radius:8px;margin:0 8px 8px 0;">{label}</a>')


def stat_rows(it, picks):
    figs = {f["i"]: f for f in it["figures"]}
    chosen = [figs[i] for i in picks if i in figs][:3] if picks else it["figures"][:3]
    rows = ""
    for f in chosen:
        m = re.match(r"^(.*?)\s*(\(.*\))?$", f.get("value", ""))
        big, small = (m.group(1), m.group(2) or "") if m else (f.get("value", ""), "")
        meta = " · ".join(x for x in [f"as at {f['asAt']}" if f.get("asAt") else "", f.get("source", "")] if x)
        rows += (f'<tr><td style="padding:6px 0;">'
                 f'<span style="font:700 16px/1.5 {HEAD};color:{INK};background:{HL};padding:1px 5px;">{e(big)}</span>'
                 + (f' <span style="font:12px/1.4 {FONT};color:{MUTED};">{e(small)}</span>' if small else "")
                 + f'<div style="font:13px/1.4 {FONT};color:{INK};margin-top:3px;">{e(f.get("label", ""))}'
                 f' <span style="font:11px/1.4 {FONT};color:{MUTED};">({e(meta)})</span></div></td></tr>')
    if not rows:
        return ""
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" '
            f'style="margin:0 0 10px;border-top:1px solid {LINE};border-bottom:1px solid {LINE};">{rows}</table>')


def dot_points(it, colour, soft):
    """Chips for the home syllabus' 'about' dot points, then a plain line of codes for the others."""
    home_fw = (it["home"] or ["h09"])[0]
    chips = ""
    for p in it["tags"][home_fw]["about"][:3]:
        chips += pill(f"{p['code']} · {clip(p['text'], 60)}", colour, soft, upper=False)
    lines = ""
    for fw in ("h09", "y12", "y11"):
        if fw == home_fw:
            continue
        codes = [p["code"] for p in it["tags"][fw]["about"]]
        if codes:
            lines += (f'<div style="font:12px/1.5 {FONT};color:{MUTED};margin:0 0 2px;">'
                      f'<strong style="color:{INK};">{FW_LINE[fw]}:</strong> {e(" · ".join(codes[:6]))}'
                      f'{" …" if len(codes) > 6 else ""}</div>')
    return f'<div style="margin:0 0 4px;">{chips}</div>{lines}'


def card(it, spec, g, labels):
    colour = strong(g["color"])
    soft = tint(g["color"])
    summary = spec.get("summary") or it["summary"]
    badge = pill("New", "#ffffff", "#1c7d52") if it["status"] == "new" else pill("Updated", "#1b1600", HL)
    when = it["date_text"] or short_date(it["date"])
    outlets = ", ".join(it["outlets"])
    also = ""
    if it["also_topics"]:
        names = [labels[k].split(": ", 1)[-1] for k in it["also_topics"] if k in labels]
        if names:
            also = (f'<div style="font:12px/1.5 {FONT};color:{MUTED};margin:2px 0 8px;">Also relevant to: '
                    f'<strong style="color:{INK};">{e("; ".join(names))}</strong></div>')
    caveat = (f'<div style="font:italic 12px/1.5 {FONT};color:{MUTED};margin:0 0 10px;">{e(spec["caveat"])}</div>'
              if spec.get("caveat") else "")
    btns = (button("Open the card &rarr;", it["card_url"], "#ffffff", colour, colour)
            + button(e(it["pdf_label"] or "PDF") + " (PDF)", it["pdf_url"], colour, "#ffffff", colour)
            + button("Original source", it["source_url"], colour, "#ffffff", colour))
    return f"""
<div style="flex:1 1 340px;min-width:0;margin:0 7px 14px;display:flex;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border:1px solid {LINE};border-left:6px solid {colour};border-radius:10px;background:#ffffff;">
<tr><td valign="top" style="padding:16px 18px 6px 18px;vertical-align:top;">
  <div style="margin:0 0 8px;">{badge}{pill(it["type_label"], "#ffffff", TYPE_COLOR.get(it["type"], MUTED))}<span style="font:12px/1 {FONT};color:{MUTED};">{"filed" if it["status"] == "new" else "first filed"} {e(short_date(it["added"]))}</span></div>
  <div style="font:700 18px/1.3 {HEAD};color:{INK};margin:0 0 4px;"><a href="{e(it["card_url"])}" style="color:{INK};text-decoration:none;">{e(it["title"])}</a></div>
  <div style="font:12px/1.4 {FONT};color:{MUTED};margin:0 0 8px;">{e(outlets)}{" · " if outlets and when else ""}{e(when)}</div>
  <div style="font:15px/1.6 {FONT};color:#1b2330;margin:0 0 10px;">{e(summary)}</div>
  {caveat}{stat_rows(it, spec.get("stats"))}{dot_points(it, colour, soft)}{also}
  <div style="padding:6px 0 0;">{btns}</div>
</td></tr></table></div>"""


def at_a_glance(groups):
    total = max(1, max((len(g["items"]) for g in groups), default=1))
    rows = ""
    for g in groups:
        n, pct = len(g["items"]), max(8, round(100 * len(g["items"]) / total))
        name = f"{g['part']}: {g['label']}" if g["part"] else g["label"]
        rows += (f'<tr><td style="padding:3px 10px 3px 0;font:600 13px/1.3 {FONT};color:{INK};" width="42%">'
                 f'{ICON.get(g["key"], "📄")}&nbsp; {e(clip(name, 44))}</td>'
                 f'<td style="padding:3px 0;"><table role="presentation" width="{pct}%" cellpadding="0" cellspacing="0"><tr>'
                 f'<td style="background:{strong(g["color"])};border-radius:6px;height:20px;font:700 12px/20px {FONT};color:#fff;padding:0 8px;">{n}</td></tr></table></td></tr>')
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0">{rows}</table>'


def render(digest, summaries, title, max_width=0):
    groups, labels = digest["groups"], digest.get("topic_labels", {})
    n_new, n_upd = digest["counts"]["new"], digest["counts"]["updated"]
    bits = ([f"{n_new} new item{'s' if n_new != 1 else ''}"] if n_new else []) + ([f"{n_upd} updated"] if n_upd else [])
    headline = " · ".join(bits) or "Nothing new"
    start, today = digest["window_start"], digest["today"]
    span = pretty(today) if start >= today else f"{pretty(start)} to {pretty(today)}"
    site = digest.get("site_url", "")

    body, last = "", None
    for g in groups:
        col = strong(g["color"])
        if g["course"] != last:
            last = g["course"]
            body += (f'<tr><td style="padding:14px 0 10px;font:700 11px/1 {FONT};letter-spacing:.14em;'
                     f'text-transform:uppercase;color:{MUTED};border-bottom:1px solid {LINE};">{e(COURSE_HEAD[g["course"]])}</td></tr>'
                     f'<tr><td style="height:12px;"></td></tr>')
        n = len(g["items"])
        body += f"""
<tr><td style="padding:0 0 12px 0;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{col};border-radius:10px;">
<tr><td width="56" style="padding:12px 0 12px 14px;"><div style="width:40px;height:40px;border-radius:20px;background:#ffffff;text-align:center;font:22px/40px {FONT};">{ICON.get(g["key"], "📄")}</div></td>
<td style="padding:12px 10px;"><div style="font:700 18px/1.25 {HEAD};color:#ffffff;">{e(g["label"])}</div>
<div style="font:12px/1.4 {FONT};color:#ffffff;opacity:.9;margin-top:2px;">{e(g["part"])}</div></td>
<td align="right" style="padding:12px 16px;font:700 13px/1 {FONT};color:#ffffff;white-space:nowrap;">{n} item{'s' if n != 1 else ''}</td></tr></table></td></tr>"""
        cards = ""
        for it in g["items"]:
            s = summaries.get(it["id"])
            spec = {"summary": s} if isinstance(s, str) else (s or {})
            if not spec.get("summary"):
                print(f"warning: no summary for {it['id']}; used the record's one-line summary", file=sys.stderr)
            cards += card(it, spec, g, labels)
        ghost = '<div style="flex:1 1 340px;min-width:0;margin:0 7px;height:0;"></div>'
        body += '<tr><td><div style="display:flex;flex-wrap:wrap;margin:0 -7px;">' + cards + ghost * 3 + '</div></td></tr>'
    if not groups:
        body = (f'<tr><td style="padding:24px;font:15px/1.6 {FONT};color:{MUTED};text-align:center;">'
                f'Nothing was added or updated in this period.</td></tr>')

    glance = (f'<tr><td style="padding:18px 24px 6px;"><div style="font:700 11px/1 {FONT};letter-spacing:.14em;'
              f'text-transform:uppercase;color:{MUTED};margin-bottom:10px;">At a glance</div>{at_a_glance(groups)}</td></tr>'
              if groups else "")
    how = f"""
<tr><td style="padding:14px 24px 4px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f4f6fb;border-radius:10px;">
<tr><td style="padding:12px 14px;font:13px/1.6 {FONT};color:{INK};">
<strong>How to use each item</strong> &nbsp; <span style="color:{ACC};">①&nbsp;Read the summary</span> &nbsp;&rarr;&nbsp;
<span style="color:{ACC};">②&nbsp;Pick out the statistics and dot points</span> &nbsp;&rarr;&nbsp;
<span style="color:{ACC};">③&nbsp;Open the card for the full evidence, or the PDF to print</span></td></tr></table></td></tr>"""
    foot = f"""
<tr><td style="padding:18px 24px 22px;border-top:1px solid {LINE};font:12px/1.6 {FONT};color:{MUTED};">
Browse everything in the <a href="{e(site)}" style="color:{ACC};font-weight:600;">HSC Economics Evidence Finder</a>.
Dot points are shown for the syllabus each item is filed under, with the others listed beneath.</td></tr>"""
    cap = f"max-width:{max_width}px;margin:0 auto;" if max_width else ""
    return f"""<div id="email" style="background:#e8ecf4;padding:18px 8px;">
<table role="presentation" align="center" width="100%" cellpadding="0" cellspacing="0" style="{cap}background:#ffffff;border-radius:14px;border:1px solid {LINE};">
<tr><td style="background:{INK};border-radius:14px 14px 0 0;padding:24px 24px 20px;border-bottom:5px solid {HL};">
<div style="font:700 11px/1 {FONT};letter-spacing:.16em;text-transform:uppercase;color:{HL};">HSC Economics · Evidence Finder</div>
<div style="font:700 27px/1.2 {HEAD};color:#ffffff;margin:8px 0 6px;">{e(title)}</div>
<div style="font:14px/1.5 {FONT};color:#c9d3ee;">{e(span)} &nbsp;·&nbsp; <strong style="color:#ffffff;">{e(headline)}</strong></div></td></tr>
{glance}{how}
<tr><td style="padding:16px 24px 6px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0">{body}</table></td></tr>
{foot}
</table></div>"""


ARTIFACT_PAGE = """<title>__TITLE__</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
  /* A slim copy bar over one email column. The email block keeps its own light, inline-styled design so it pastes into Gmail/Outlook unchanged. */
  :root{--bg:#e8ecf4;--bar:#0e1526;--bar-fg:#ffffff;--bar-soft:#c9d3ee;--btn:#ffe14d;--btn-fg:#1b1600;--focus:#2447d6}
  @media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#0c1120;--bar:#151c30;--bar-fg:#e9eefb;--bar-soft:#a2aec9;--btn:#ffe14d;--btn-fg:#1b1600;--focus:#8fa6ff;color-scheme:dark}}
  :root[data-theme="dark"]{--bg:#0c1120;--bar:#151c30;--bar-fg:#e9eefb;--bar-soft:#a2aec9;--btn:#ffe14d;--btn-fg:#1b1600;--focus:#8fa6ff;color-scheme:dark}
  body{background:var(--bg);color:var(--bar-fg);padding-inline:max(16px,env(safe-area-inset-left,0px)) max(16px,env(safe-area-inset-right,0px));padding-block:14px 28px;font-family:-apple-system,'Segoe UI',Helvetica,Arial,sans-serif}
  .bar{margin:0 0 14px;background:var(--bar);color:var(--bar-fg);border-radius:12px;padding:12px 14px;display:flex;gap:12px;align-items:center;flex-wrap:wrap}
  .bar button{font:700 14px/1 inherit;border:0;border-radius:8px;padding:11px 16px;background:var(--btn);color:var(--btn-fg);cursor:pointer}
  .bar button:focus-visible{outline:3px solid var(--focus);outline-offset:2px}
  .bar .hint{flex:1 1 220px;min-width:0;color:var(--bar-soft);font-size:13px;line-height:1.45}
  #msg{font-weight:600;font-size:13px;color:var(--bar-fg)}
</style>
<div class="bar"><button id="copybtn" type="button">Copy for email</button>
<span class="hint">Copies the update below, with its colours and links, ready to paste into a new email.</span><span id="msg" role="status"></span></div>
__EMAIL__
<script>
document.getElementById('copybtn').addEventListener('click',function(){
  var el=document.getElementById('email'),msg=document.getElementById('msg');
  function done(ok){msg.textContent=ok?'Copied. Paste it into a new email.':'Copy blocked here: select the update and copy it (Ctrl/Cmd+C).';}
  function viaSelection(){
    try{var r=document.createRange();r.selectNode(el);var s=window.getSelection();s.removeAllRanges();s.addRange(r);
        var ok=document.execCommand('copy');done(ok);}catch(x){done(false);}
  }
  try{
    if(navigator.clipboard&&window.ClipboardItem){
      navigator.clipboard.write([new ClipboardItem({'text/html':new Blob([el.outerHTML],{type:'text/html'}),
        'text/plain':new Blob([el.innerText],{type:'text/plain'})})]).then(function(){done(true)},viaSelection);
    } else viaSelection();
  }catch(x){viaSelection();}
});
</script>"""

PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>__TITLE__</title>
<style>html,body{margin:0;background:#dfe4ec;}body{font-family:-apple-system,'Segoe UI',Helvetica,Arial,sans-serif}</style></head>
<body>__EMAIL__</body></html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("digest")
    ap.add_argument("summaries")
    ap.add_argument("out")
    ap.add_argument("--title", default="What's new in the Evidence Finder")
    ap.add_argument("--page-title", default="Economics evidence update")
    ap.add_argument("--max-width", type=int, default=0)
    ap.add_argument("--artifact", action="store_true")
    a = ap.parse_args()
    digest = json.load(open(a.digest, encoding="utf-8"))
    summaries = json.load(open(a.summaries, encoding="utf-8")) if a.summaries != "-" else {}
    skip = set(summaries.pop("_skip", []))
    if skip:
        kept = []
        for g in digest["groups"]:
            g["items"] = [i for i in g["items"] if i["id"] not in skip]
            if g["items"]:
                kept.append(g)
        digest["groups"] = kept
        digest["counts"] = {s: sum(i["status"] == s for g in kept for i in g["items"]) for s in ("new", "updated")}
    block = render(digest, summaries, a.title, a.max_width)
    page = (ARTIFACT_PAGE.replace("__TITLE__", e(a.page_title)) if a.artifact
            else PAGE.replace("__TITLE__", e(a.title))).replace("__EMAIL__", block)
    open(a.out, "w", encoding="utf-8").write(page)
    print(f"wrote {a.out} ({digest['counts']['new']} new, {digest['counts']['updated']} updated)")


if __name__ == "__main__":
    main()
