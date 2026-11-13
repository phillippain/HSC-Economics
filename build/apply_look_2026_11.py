#!/usr/bin/env python3
"""One-off (November 2026): apply the "White and cobalt" look to every tool.

White page background (no grid), cobalt accent #1746d1, Manrope for headings and body, a
cobalt rule under the masthead, and the gold "Other tools" / Home buttons kept from the
shared menu. Edits templates and hand-kept pages in place; run the builds afterwards.
The fonts for the template-built tools are inlined from evidence-finder/build/fonts.css.
"""
import re, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
def sub(s, pairs, name):
    for a, b in pairs:
        n = s.count(a)
        if not n: print(f'  note: {name}: not found: {a[:50]!r}')
        s = s.replace(a, b)
    return s
MARK = '/* look:white-cobalt */'
SHARED = [
 ('--bg:#e8ecf4; --grid:rgba(36,71,214,.075); --grid2:rgba(36,71,214,.12);', '--bg:#ffffff; --grid:transparent; --grid2:transparent;'),
 ('--card:#ffffff; --card2:#f4f6fb; --ink:#0e1526; --mut:#4a5468; --rule:#d3d9e6; --rule2:#b9c2d6;', '--card:#ffffff; --card2:#f3f6fd; --ink:#101a3a; --mut:#4a5578; --rule:#d8deee; --rule2:#b8c2de;'),
 ('--acc:#2447d6; --acc-ink:#ffffff; --acc-soft:#e3e9fd;', '--acc:#1746d1; --acc-ink:#ffffff; --acc-soft:#eaf0fe;'),
 ('--grid:rgba(140,165,255,.06); --grid2:rgba(140,165,255,.10);', '--grid:transparent; --grid2:transparent;'),
 ("'Bricolage Grotesque','Avenir Next',", "'Manrope','Avenir Next',"),
 ("--body:'Public Sans',", "--body:'Manrope',"),
]
for t in ['evidence-finder/build/template.html'] + sorted(str(p.relative_to(R)) for p in R.glob('*/template.html')):
    p = R / t; s = p.read_text(encoding='utf-8')
    if MARK in s: print('already done:', t); continue
    s = sub(s, SHARED, t)
    m = re.search(r'\.mast\{[^}]*\}', s); assert m, t
    s = s[:m.end()] + '\n' + MARK + '\n.mast{border-bottom:4px solid var(--acc);padding-bottom:14px;margin-bottom:16px}\n.mast h1{font-weight:800;letter-spacing:-.01em}' + s[m.end():]
    p.write_text(s, encoding='utf-8'); print('restyled', t)

GF = re.compile(r'(https://fonts\.googleapis\.com/css2\?)([^"\']*)')
def gfont(s):
    def f(m):
        fams = [x for x in m.group(2).split('&') if x.startswith('family=') and not re.match(r'family=(Bricolage\+Grotesque|IBM\+Plex\+Sans|IBM\+Plex\+Serif|Atkinson\+Hyperlegible|Inter|Source\+Serif\+4|Public\+Sans|Manrope)\b', x)]
        return m.group(1) + '&'.join(['family=Manrope:wght@400;500;600;700;800'] + fams + ['display=swap'])
    return GF.sub(f, s)
def fontnames(s):
    return re.sub(r'''(["'])(Bricolage Grotesque|IBM Plex Sans|IBM Plex Serif|Atkinson Hyperlegible|Inter|Source Serif 4)\1''', lambda m: m.group(1) + 'Manrope' + m.group(1), s)
def head_only(p, fn):
    """Apply fn to everything before the first data/script payload so stored text is never touched."""
    s = p.read_text(encoding='utf-8')
    cut = min([i for i in (s.find('<script type="application/json"'), s.find('<script>const DATA'), s.find('</style>', s.find('SITEMENU:END'))) if i > 0] or [len(s)])
    cut = s.find('</style>', s.find('SITEMENU:END')) if s.find('</style>', s.find('SITEMENU:END')) > 0 else cut
    head, rest = s[:cut], s[cut:]
    if MARK in head: print('already done:', p.relative_to(R)); return
    head = fn(head)
    i = head.find('<style', head.find('SITEMENU:END') if 'SITEMENU:END' in head else 0); j = head.find('>', i) + 1
    head = head[:j] + '\n' + MARK + head[j:]
    p.write_text(head + rest, encoding='utf-8'); print('restyled', p.relative_to(R))

head_only(R / 'hsc-question-finder-site/index.html', lambda h: fontnames(gfont(sub(h, [
 ('--bg:#f4f6f9; --surface:#ffffff; --surface-2:#eef1f6; --line:#dbe0e8; --line-soft:#e8ecf2;', '--bg:#ffffff; --surface:#ffffff; --surface-2:#f3f6fd; --line:#d8deee; --line-soft:#e6ebf7;'),
 ('--accent:#1f3864; --accent-soft:#e5ebf5;', '--accent:#1746d1; --accent-soft:#eaf0fe;'),
 ('--ink:#141922; --ink-2:#48525f;', '--ink:#101a3a; --ink-2:#4a5578;'),
], 'question finder'))))
BAND = [('--bg:#F2F5F9;', '--bg:#FFFFFF;'), ('--band:#10253F; --band-ink:#F2F5F9; --band-muted:#B7C5DA;', '--band:#FFFFFF; --band-ink:#101a3a; --band-muted:#4a5578;')]
def once(pairs):
    def f(h):
        for a, b in pairs:
            if a not in h: print('  note: not found:', a[:40])
            h = h.replace(a, b, 1)   # first occurrence is the light theme
        return fontnames(gfont(h))
    return f
head_only(R / 'diagram-lab/index.html', once(BAND))
head_only(R / 'protection-explainer/index.html', once(BAND))
head_only(R / 'mind-map/index.html', once([('--bg:#f4f6f8;', '--bg:#ffffff;')]))
head_only(R / 'economy-at-a-glance/index.html', once([]))

p = R / 'build/build_sitemenu.py'; s = p.read_text(encoding='utf-8')
if 'd9ad16' not in s:
    s = sub(s, [("font-family:'Public Sans','Segoe UI'", "font-family:'Manrope','Public Sans','Segoe UI'"),
                ('background:#ffd24a;color:#1a1d2b;border-radius:999px;', 'background:#ffd24a;color:#1a1d2b;border:1px solid #d9ad16;border-radius:999px;'),
                ('.sm-btn:focus-visible{outline:3px solid #2447d6', '.sm-btn:focus-visible{outline:3px solid #1746d1'),
                ('.sm-a svg{font-size:18px;color:#2447d6}', '.sm-a svg{font-size:18px;color:#1746d1}'),
                ('a.sm-a:hover,a.sm-a:focus-visible{background:#e3e9fd;', 'a.sm-a:hover,a.sm-a:focus-visible{background:#eaf0fe;')], 'sitemenu')
    p.write_text(s, encoding='utf-8'); print('restyled build/build_sitemenu.py')
