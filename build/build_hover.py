#!/usr/bin/env python3
"""Glossary hover definitions on every tool.

    python3 build/build_hover.py           # write glossary/hover.json and the hover block in every page
    python3 build/build_hover.py --check   # change nothing; fail if anything is out of date

Run it after glossary/data/glossary.json changes, and after build_sitemenu.py when a tool is added
(the list of pages comes from build_sitemenu.PAGES). The block sits between HOVER:START and HOVER:END
just before </body>, in templates and built pages alike, so rebuilding a tool keeps it.

How it behaves: the first time a glossary term appears in a paragraph it gets a dotted underline;
pointing at it, tabbing to it or tapping it shows the definition with a link to the Glossary.
Buttons, links, form fields, headings in the masthead, menus and diagrams are left alone.
SKIP_EXTRA keeps it out of places where a definition would give an answer away.
"""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_sitemenu import PAGES

ROOT = Path(__file__).resolve().parent.parent
CHECK = "--check" in sys.argv
NO_HOVER = {"gloss", "chain"}          # the Glossary itself; the Chain Builder has its own
STOP = {"global economy", "credit", "debt", "development", "income", "wealth", "award", "protection"}   # too ordinary to underline everywhere
SKIP_EXTRA = {"mcq": ".stem,.opts"}     # Multiple Choice Drill: not in the question or its options, only in the feedback
MARK = re.compile(r"<!-- HOVER:START.*?HOVER:END -->\n?", re.S)

def terms():
    out = []
    for t in json.loads((ROOT / "glossary" / "data" / "glossary.json").read_text(encoding="utf8"))["terms"]:
        name = re.sub(r"\s*\(.*?\)", "", t["term"]).strip()
        names = [name] + [a for a in re.findall(r"\(([A-Z][A-Za-z]{1,6})\)", t["term"]) if a.upper()[:2] == a[:2]]
        names = [n for n in names if n.lower() not in STOP and (len(n) >= 5 or n.isupper() and len(n) >= 3) and "/" not in n]
        if names:
            out.append({"i": t["id"], "t": t["term"], "d": t["def"], "n": names})
    return out

CSS = """.gdef{text-decoration:underline dotted;text-decoration-thickness:1.5px;text-underline-offset:3px;cursor:help}
.gdef:focus-visible{outline:2px solid #1c3fb0;outline-offset:2px;border-radius:3px}
.gdtip{position:fixed;z-index:2000;max-width:min(360px,calc(100vw - 16px));background:#0b1330;color:#fff;border-radius:10px;padding:10px 12px;font:500 14px/1.45 'Manrope','Segoe UI',system-ui,sans-serif;box-shadow:0 10px 30px rgba(10,14,40,.35);text-align:left}
.gdtip b{display:block;font-weight:800;margin-bottom:2px}.gdtip a{color:#ffd24a;font-weight:700;display:inline-block;margin-top:6px}
@media print{.gdef{text-decoration:none}.gdtip{display:none!important}}"""

JS = r"""(function(){if(window.__gdef)return;window.__gdef=1;var BASE=%(base)s,EXTRA=%(extra)s;
var SKIP='a,button,input,textarea,select,option,label,summary,script,style,svg,canvas,code,pre,h1,nav,[contenteditable],[role=tab],.smbar,.gdtip,.gdef,.gt,[data-nogloss]'+(EXTRA?','+EXTRA:'');
var BLOCK='p,li,td,th,dd,dt,blockquote,figcaption,div,section,article';
var MAP={},RE=null,tip=null,cur=null,hideT=0,queue=[],busy=false,framed=false;try{framed=window.self!==window.top}catch(e){framed=true}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function build(list){var alts=[];list.forEach(function(t){t.n.forEach(function(n){MAP[n.toLowerCase()]={t:t,exact:n===n.toUpperCase()?n:null};alts.push(n.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'))})});
 alts.sort(function(a,b){return b.length-a.length});RE=new RegExp('(^|[^A-Za-z0-9])('+alts.join('|')+')(s|es)?(?![A-Za-z0-9])','gi')}
function wrap(node){var el=node.parentElement;if(!el||el.closest(SKIP))return;var text=node.nodeValue;if(text.length<4||!/[A-Za-z]{3}/.test(text))return;
 var block=el.closest(BLOCK)||el,m,last=0,parts=null;RE.lastIndex=0;
 while((m=RE.exec(text))){var hit=MAP[m[2].toLowerCase()];if(!hit||(hit.exact&&m[2]!==hit.exact)){RE.lastIndex=m.index+m[1].length+1;continue}
  var id=hit.t.i;if(block.querySelector('.gdef[data-g="'+id+'"]')||(parts&&parts.ids[id]))continue;
  parts=parts||{f:document.createDocumentFragment(),ids:{}};parts.ids[id]=1;var s=m.index+m[1].length,e=s+m[2].length+(m[3]||'').length;
  parts.f.appendChild(document.createTextNode(text.slice(last,s)));var sp=document.createElement('span');sp.className='gdef';sp.tabIndex=0;sp.setAttribute('data-g',id);sp.textContent=text.slice(s,e);parts.f.appendChild(sp);last=e}
 if(parts){parts.f.appendChild(document.createTextNode(text.slice(last)));node.parentNode.replaceChild(parts.f,node)}}
function collect(root){if(!root||root.nodeType!==1||root.closest(SKIP))return;var w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,null),n;while((n=w.nextNode()))queue.push(n);pump()}
function pump(){if(busy||!queue.length)return;busy=true;setTimeout(function(){var t0=Date.now();obs.disconnect();while(queue.length&&Date.now()-t0<12){var n=queue.shift();if(n.isConnected)wrap(n)}
 obs.observe(document.body,{childList:true,subtree:true});busy=false;pump()},queue.length>400?30:0)}
var obs=new MutationObserver(function(ms){ms.forEach(function(m){m.addedNodes.forEach(function(n){if(n.nodeType===1){if(!n.classList.contains('gdef')&&!n.classList.contains('gdtip'))collect(n)}else if(n.nodeType===3&&n.parentElement&&!n.parentElement.closest('.gdef,.gdtip'))queue.push(n)})});pump()});
function show(sp){var hit=null,id=sp.getAttribute('data-g');for(var k in MAP)if(MAP[k].t.i===id){hit=MAP[k].t;break}if(!hit)return;clearTimeout(hideT);cur=sp;
 if(!tip){tip=document.createElement('div');tip.className='gdtip';tip.setAttribute('role','tooltip');document.body.appendChild(tip);tip.addEventListener('mouseenter',function(){clearTimeout(hideT)});tip.addEventListener('mouseleave',hide)}
 tip.innerHTML='<b>'+esc(hit.t)+'</b>'+esc(hit.d)+'<br><a href="'+BASE+'glossary/#term='+id+'" target="_blank" rel="noopener">Open in the Glossary (new tab)</a>';tip.style.display='block';
 var r=sp.getBoundingClientRect(),w=tip.offsetWidth,h=tip.offsetHeight,x=Math.max(8,Math.min(r.left,window.innerWidth-w-8)),y=r.bottom+6;if(y+h>window.innerHeight-8&&r.top-h-6>8)y=r.top-h-6;tip.style.left=x+'px';tip.style.top=y+'px'}
function hide(){hideT=setTimeout(function(){if(tip)tip.style.display='none';cur=null},180)}
document.addEventListener('mouseover',function(e){var s=e.target.closest&&e.target.closest('.gdef');if(s)show(s)});
document.addEventListener('mouseout',function(e){if(e.target.closest&&e.target.closest('.gdef'))hide()});
document.addEventListener('focusin',function(e){var s=e.target.closest&&e.target.closest('.gdef');if(s)show(s)});
document.addEventListener('focusout',function(e){if(e.target.closest&&e.target.closest('.gdef'))hide()});
document.addEventListener('click',function(e){var s=e.target.closest&&e.target.closest('.gdef');if(s){show(s)}else if(tip&&!e.target.closest('.gdtip')){tip.style.display='none'}});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&tip)tip.style.display='none'});
window.addEventListener('scroll',function(){if(tip&&cur)tip.style.display='none'},true);
fetch(BASE+'glossary/hover.json').then(function(r){return r.json()}).then(function(l){build(l);collect(document.body)}).catch(function(){});
})();"""

def block(key, rel):
    base = "../"   # every tool page is served one folder below the site root, wherever its template is kept
    js = JS % {"base": json.dumps(base), "extra": json.dumps(SKIP_EXTRA.get(key, ""))}
    return ("<!-- HOVER:START built by build/build_hover.py; glossary definitions on hover -->\n"
            f"<style>\n{CSS}\n</style>\n<script>{js}</script>\n<!-- HOVER:END -->\n")

def main():
    stale, n = [], 0
    hov = json.dumps(terms(), ensure_ascii=False, separators=(",", ":"))
    hp = ROOT / "glossary" / "hover.json"
    if not hp.exists() or hp.read_text(encoding="utf8") != hov:
        stale.append("glossary/hover.json")
        if not CHECK: hp.write_text(hov, encoding="utf8")
    for key, files in PAGES.items():
        if key in NO_HOVER: continue
        for f in files:
            p = ROOT / f
            if not p.exists(): continue
            src = p.read_text(encoding="utf8"); bare = MARK.sub("", src); b = block(key, f)
            i = bare.rfind("</body>")
            new = bare[:i] + b + bare[i:] if i >= 0 else bare.rstrip("\n") + "\n" + b
            n += 1
            if new != src:
                stale.append(f)
                if not CHECK: p.write_text(new, encoding="utf8")
    print(f"glossary hover: {len(json.loads(hov))} terms, on {n} files")
    if CHECK:
        if stale: print("OUT OF DATE: " + ", ".join(stale) + ". Run python3 build/build_hover.py"); sys.exit(1)
        print("up to date"); return
    print("wrote: " + (", ".join(stale) if stale else "nothing, already up to date"))

if __name__ == "__main__":
    main()
