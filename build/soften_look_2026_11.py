#!/usr/bin/env python3
"""One-off (November 2026): soften the White and cobalt look after classroom feedback.

Template-built tools: pale cool page (#f3f5fa) behind white panels, darker text, slightly
heavier body weight, deeper cobalt (#1c3fb0), thinner masthead rule. Protection explainer
and Protection diagram lab: navy title band restored on the same pale page.
Run the builds afterwards. Refuses to run twice."""
import pathlib
R = pathlib.Path(__file__).resolve().parent.parent
MARK = '/* look:softened */'
def edit(path, pairs, extra=''):
    p = R / path; s = p.read_text(encoding='utf-8')
    if MARK in s: print('already done:', path); return
    for a, b in pairs:
        assert s.count(a) == 1, (path, a)
        s = s.replace(a, b)
    if extra:
        a = '/* look:white-cobalt */'; assert s.count(a) == 1, path
        s = s.replace(a, a + '\n' + MARK + '\n' + extra)
    p.write_text(s, encoding='utf-8'); print('softened', path)
T = [('--bg:#ffffff; --grid:transparent; --grid2:transparent;', '--bg:#f3f5fa; --grid:transparent; --grid2:transparent;'),
     ('--card:#ffffff; --card2:#f3f6fd; --ink:#101a3a; --mut:#4a5578; --rule:#d8deee; --rule2:#b8c2de;', '--card:#ffffff; --card2:#e9eef8; --ink:#0b1330; --mut:#3b4663; --rule:#c9d2e4; --rule2:#a7b3cd;'),
     ('--acc:#1746d1; --acc-ink:#ffffff; --acc-soft:#eaf0fe;', '--acc:#1c3fb0; --acc-ink:#ffffff; --acc-soft:#e3eafb;'),
     ('.mast{border-bottom:4px solid var(--acc);', '.mast{border-bottom:2px solid var(--acc);')]
for t in ['evidence-finder/build/template.html'] + sorted(str(p.relative_to(R)) for p in R.glob('*/template.html')):
    edit(t, T, 'body{font-weight:500}')
B = [('--bg:#FFFFFF;', '--bg:#F3F5FA;'), ('--band:#FFFFFF; --band-ink:#101a3a; --band-muted:#4a5578;', '--band:#10253F; --band-ink:#F2F5F9; --band-muted:#B7C5DA;'),
     ('<!-- /* look:white-cobalt */ -->', '<!-- /* look:white-cobalt */ ' + MARK + ' -->\n<style>body{font-weight:500}</style>')]
edit('protection-explainer/index.html', B)
edit('diagram-lab/index.html', B)
