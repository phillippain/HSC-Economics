import subprocess, html
CSS = """
@page{size:A4;margin:14mm 14mm 15mm}
*{box-sizing:border-box}body{font-family:'Helvetica Neue',Helvetica,Arial,'DejaVu Sans',sans-serif;font-size:10.4pt;line-height:1.42;color:#0b1330;margin:0}
.top{border-bottom:3px solid VAR;padding-bottom:6px;margin-bottom:10px}
.top small{display:block;font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase;color:VAR;font-weight:700}
h1{font-size:19pt;margin:2px 0 2px;line-height:1.15}
.sub{font-size:9.5pt;color:#3b4663}
h2{font-size:11.5pt;color:VAR;margin:13px 0 5px;text-transform:uppercase;letter-spacing:.05em;border-bottom:1px solid #c9d2e4;padding-bottom:2px}
p{margin:0 0 6px}ul{margin:0 0 6px 16px;padding:0}li{margin-bottom:3px}
table{width:100%;border-collapse:collapse;margin:4px 0 8px;font-size:9.6pt}
th{background:VAR;color:#fff;text-align:left;padding:5px 7px;font-weight:700}
td{border:1px solid #c9d2e4;padding:5px 7px;vertical-align:top}
.box{background:#f3f5fa;border-left:5px solid VAR;padding:7px 10px;margin:6px 0 8px;border-radius:4px}
.box b.t{display:block;font-size:8.5pt;letter-spacing:.07em;text-transform:uppercase;color:VAR;margin-bottom:2px}
.act{border:1.5px solid VAR;border-radius:6px;padding:8px 10px;margin:8px 0;page-break-inside:avoid}
.act h3{margin:0 0 4px;font-size:10.6pt;color:VAR}
.lines{border-bottom:1px solid #a7b3cd;height:20px}
.src{font-size:8.3pt;color:#3b4663;margin-top:10px;border-top:1px solid #c9d2e4;padding-top:5px}
.mk{float:right;font-size:8.8pt;color:#3b4663;font-weight:700}
h2,h3{page-break-after:avoid}tr{page-break-inside:avoid}
"""
def lines(n): return ''.join('<div class="lines"></div>' for _ in range(n))
def doc(fname, colour, strap, title, sub, body):
    h = '<!doctype html><html><head><meta charset="utf-8"><style>'+CSS.replace('VAR',colour)+'</style></head><body><div class="top"><small>'+strap+'</small><h1>'+title+'</h1><div class="sub">'+sub+'</div></div>'+body+'</body></html>'
    open(fname+'.html','w').write(h)
    subprocess.run(['google-chrome','--headless','--no-sandbox','--disable-gpu','--no-pdf-header-footer','--print-to-pdf='+fname+'.pdf',fname+'.html'],check=True,capture_output=True)
exec(open('content.py').read())
