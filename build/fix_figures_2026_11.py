#!/usr/bin/env python3
"""One-off (November 2026): figure images in the Question Finder were re-cropped to remove
stray lines of question text, page furniture ("OR", "Please turn over", page numbers) and
margin strips. This updates the stored display sizes, refiles two tables that sat under the
wrong question, and cleans three question texts. Refuses to run twice."""
import json, sys, pathlib
P = pathlib.Path(__file__).resolve().parent.parent / 'hsc-question-finder-site' / 'index.html'
h = P.read_text(encoding='utf-8'); A = 'const DATA = '; i = h.index(A) + len(A)
D, n = json.JSONDecoder().raw_decode(h[i:])
DIMS = json.loads('''{"2009-I-12-1.webp": [1259, 246], "2009-I-8-1.webp": [1198, 144], "2009-II-Q21-1.webp": [875, 283], "2009-III-Q25-1.webp": [1266, 1187], "2010-II-Q23-1.webp": [1216, 220], "2011-II-Q22-1.webp": [1045, 349], "2011-II-Q23-1.webp": [827, 316], "2011-III-Q25-1.webp": [1296, 1077], "2012-II-Q23-1.webp": [781, 770], "2012-III-Q25-1.webp": [1271, 1117], "2013-II-Q24-1.webp": [474, 434], "2013-III-Q25-1.webp": [1268, 926], "2013-III-Q26-1.webp": [1352, 968], "2014-III-Q25-1.webp": [1379, 965], "2014-III-Q26-1.webp": [1379, 1116], "2015-I-13-1.webp": [468, 455], "2015-III-Q25-1.webp": [1268, 1120], "2016-III-Q25-1.webp": [1337, 1572], "2016-III-Q26-1.webp": [1241, 1039], "2017-III-Q25-1.webp": [1379, 920], "2017-III-Q26-1.webp": [1379, 1067], "2018-III-Q25-1.webp": [1379, 1136], "2018-III-Q26-1.webp": [1418, 1122], "2019-I-14-1.webp": [669, 327], "2019-II-Q24-1.webp": [1253, 343], "2019-III-Q25-1.webp": [1379, 1836], "2019-III-Q26-1.webp": [1379, 1857], "2020-I-20-1.webp": [653, 510], "2020-II-Q21-1.webp": [905, 198], "2020-II-Q23-1.webp": [912, 639], "2020-III-Q25-1.webp": [1215, 1388], "2020-III-Q26-1.webp": [1215, 1574], "2021-II-Q22-1.webp": [801, 531], "2021-III-Q25-1.webp": [1251, 1694], "2021-III-Q26-1.webp": [1251, 1320], "2022-I-11-1.webp": [633, 526], "2022-III-Q25-1.webp": [1256, 1840], "2022-III-Q26-1.webp": [1245, 1738], "2023-I-13-1.webp": [929, 292], "2023-I-19-1.webp": [865, 567], "2023-III-Q25-1.webp": [1167, 1778], "2023-III-Q26-1.webp": [1192, 1085], "2024-I-6-1.webp": [669, 284], "2024-III-Q25-1.webp": [1168, 1277], "2024-III-Q26-1.webp": [1169, 1134], "2025-I-17-1.webp": [1112, 537], "2025-III-Q25-1.webp": [1379, 1618], "2025-III-Q26-1.webp": [1379, 1242]}''')
F = D['figs']
if '14' in F['2019']['I']: sys.exit('already applied')
F['2019']['I']['14'] = F['2019']['I'].pop('13'); F['2019']['I']['14'][0]['f'] = '2019-I-14-1.webp'
F['2024']['I']['6'] = F['2024']['I'].pop('5'); F['2024']['I']['6'][0]['f'] = '2024-I-6-1.webp'
D['mcq']['2019']['14'].update(q='The following information is for a hypothetical economy. How many people are employed part time in this economy?', v=True)
D['mcq']['2024']['6'].update(q='The following information is for a hypothetical economy. What is the labour force participation rate for this economy?', v=True)
o = D['mcq']['2025']['20']['o'][3]; assert o[1].startswith('P1 − P3 2025 HIGHER'), o; o[1] = 'P1 − P3'
seen = set()
for y in F.values():
    for sec in y.values():
        for bl in sec.values():
            for b in bl:
                if b['t'] == 'img' and b['f'] in DIMS:
                    b['w'], b['h'] = round(DIMS[b['f']][0] / 3), round(DIMS[b['f']][1] / 3); seen.add(b['f'])
assert seen == set(DIMS), set(DIMS) - seen
for y, qs in D['mcq'].items():
    for k, q in qs.items():
        for L, t in q['o']:
            if 'HIGHER SCHOOL' in t or len(t) > 220: print('check option text:', y, k, L, t[:80])
P.write_text(h[:i] + json.dumps(D, ensure_ascii=False, separators=(',', ':')) + h[i + n:], encoding='utf-8')
print('updated', len(seen), 'images')
