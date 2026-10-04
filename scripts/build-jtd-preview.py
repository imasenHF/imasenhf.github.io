"""Build a separate multipage Notes preview with upstream Just the Docs assets.
The source report remains authoritative. Production Notes are not changed.
"""
from pathlib import Path
import re,json,html
R=Path(__file__).resolve().parents[1]; O=R/'preview/w-band-docs';O.mkdir(parents=True,exist_ok=True)
BASE='/preview/w-band-docs/'
s=(R/'_notes/w-band-epr.html').read_text().split('---',2)[2]
s=s[s.index('<div class="report-body">')+len('<div class="report-body">'):]
s=s[:s.rfind('{% endraw %}')];s=re.sub(r'\s*</div>\s*</div>\s*$','',s)
def plain(t):
 t=re.sub('<[^>]+>','',t);t=re.sub(r'\\[()]','',t);return html.unescape(t).strip()
def clean(t):return re.sub(r'^\d+(?:\.\d+)*[.、．]?\s+','',t)
parts=list(re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>',s,re.S)); pages=[]; groups=[]
intro=s[parts[0].end():parts[1].start()]
pages.append(dict(slug='index',title='W 波段 EPR',body='<h1>W 波段 EPR</h1><p class="fs-6 fw-300">物理基础、主要应用主线与代表性案例</p><p><span class="label">磁共振</span> <span class="label">EPR</span> <span class="label">W-band</span></p><h2 id="摘要">摘要</h2>'+intro,parent=None))
for i,p in enumerate(parts[1:],1):
 oldtitle=plain(p[2]); title=['理论基础','应用主线','应用地图','领域映射','适用性判断','仪器需求','案例索引','结论'][i-1];slug=f'chapter-{i}';body=s[p.end():parts[i+1].start() if i+1<len(parts) else len(s)]
 children=[]
 if i==2:
  h3=list(re.finditer(r'<h3 id="([^"]+)">(.*?)</h3>',body,re.S))
  parentbody=body[:h3[0].start()]
  for j,h in enumerate(h3,1):
   cslug=f'application-{j}';ctitle=plain(clean(h[2]));cb=body[h.end():h3[j].start() if j<len(h3) else len(body)]
   cb=re.sub(r'<h4([^>]*)>(.*?)</h4>',lambda m:'<h2'+m[1]+'>'+clean(m[2])+'</h2>',cb,flags=re.S)
   children.append((cslug,ctitle));pages.append(dict(slug=cslug,title=ctitle,body='<h1>'+clean(h[2])+'</h1>'+cb,parent=(slug,title)))
  body=parentbody+'<p>五条应用主线分别列于下方子页面，每页包括理论依据、适用体系、案例和适用边界。</p><h2>子页面</h2><ul>'+''.join('<li><a href="'+BASE+cs+'.html">'+html.escape(ct)+'</a></li>' for cs,ct in children)+'</ul>'
 else:
  body=re.sub(r'<h3([^>]*)>(.*?)</h3>',lambda m:'<h2'+m[1]+'>'+clean(m[2])+'</h2>',body,flags=re.S)
  body=re.sub(r'<h4([^>]*)>(.*?)</h4>',lambda m:'<h3'+m[1]+'>'+clean(m[2])+'</h3>',body,flags=re.S)
 pages.append(dict(slug=slug,title=title,body='<h1>'+title+'</h1><p class="doc-subtitle">'+html.escape(oldtitle)+'</p>'+body,parent=None));groups.append((slug,title,children))
icons='''<svg xmlns="http://www.w3.org/2000/svg" style="display:none"><symbol id="svg-arrow-right" viewBox="0 0 24 24"><path d="m9 6 6 6-6 6" fill="none" stroke="currentColor" stroke-width="2"/></symbol><symbol id="svg-search" viewBox="0 0 24 24"><circle cx="10" cy="10" r="6" fill="none" stroke="currentColor" stroke-width="2"/><path d="m15 15 6 6" stroke="currentColor" stroke-width="2"/></symbol><symbol id="svg-menu" viewBox="0 0 24 24"><path d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" stroke-width="2"/></symbol><symbol id="svg-doc" viewBox="0 0 24 24"><path d="M5 3h10l4 4v14H5zM8 11h8M8 15h8" fill="none" stroke="currentColor" stroke-width="1.5"/></symbol><symbol id="svg-link" viewBox="0 0 16 16"><path d="m6 10 4-4M5 7 3 9a2 2 0 0 0 3 3l2-2M8 6l2-2a2 2 0 0 1 3 3l-2 2" stroke="currentColor" fill="none"/></symbol></svg>'''
def navitem(slug,title,children=[]):
 button='<button class="nav-list-expander btn-reset" aria-label="展开 '+html.escape(title,quote=True)+'" aria-expanded="false"><svg viewBox="0 0 24 24"><use href="#svg-arrow-right"/></svg></button>' if children else ''
 return '<li class="nav-list-item">'+button+'<a class="nav-list-link" href="'+BASE+slug+'.html">'+html.escape(title)+'</a>'+('<ul class="nav-list">'+''.join(navitem(*c) for c in children)+'</ul>' if children else '')+'</li>'
nav='<ul class="nav-list">'+navitem('index','文档首页')+''.join(navitem(*g) for g in groups)+'</ul>'
math=r'''<script>window.MathJax={tex:{inlineMath:[['\\(','\\)'],['$','$']],displayMath:[['\\[','\\]'],['$$','$$']]},options:{skipHtmlTags:['script','noscript','style','textarea','pre','code']}};</script><script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>'''
settings='''<details class="doc-theme"><summary aria-label="主题设置" title="主题设置"><svg width="20" height="20" viewBox="0 0 24 24"><path d="M4 7h10M18 7h2M4 17h2M10 17h10M14 4v6M6 14v6" stroke="currentColor" fill="none"/></svg></summary><div class="theme-options">'''+''.join('<button data-theme="'+k+'" aria-label="'+n+'" title="'+n+'"></button>' for k,n in [('sage','鼠尾草绿'),('mist','雾蓝'),('sand','暖砂'),('mauve','灰紫'),('gray','浅灰')])+'</div></details>'
index={}
for page in pages:
 slug,title,body=page['slug'],page['title'],page['body'];heads=list(re.finditer(r'<h[23]([^>]*)>(.*?)</h[23]>',body,re.S))
 for k,h in enumerate(heads):
  if 'id=' not in h[1]:body=body.replace(h[0],h[0].replace('<h','<h',1).replace('>',' id="section-'+str(k)+'">',1),1)
 # Native inline page contents.
 toc=[]
 for level,attrs,t in re.findall(r'<h([23])([^>]*)>(.*?)</h\1>',body,re.S):
  ident=re.search(r'id="([^"]+)"',attrs)
  if ident:toc.append('<li class="toc-level-'+level+'"><a href="#'+html.escape(ident[1],quote=True)+'">'+html.escape(html.unescape(re.sub('<[^>]+>','',t)).strip())+'</a></li>')
 pos=body.index('</h1>')+5
 if toc:body=body[:pos]+'<details class="page-toc" open><summary>本页目录</summary><ul>'+''.join(toc)+'</ul></details>'+body[pos:]
 body=re.sub(r'(<h[123] id="([^"]+)"[^>]*>)(.*?)(</h[123]>)',lambda m:m[1]+'<a class="anchor-heading" href="#'+html.escape(m[2],quote=True)+'" aria-label="链接到本节"><svg viewBox="0 0 16 16"><use href="#svg-link"/></svg></a>'+m[3]+m[4],body,flags=re.S)
 crumbs='<li class="breadcrumb-nav-list-item"><a href="'+BASE+'index.html">W 波段 EPR</a></li>'
 if page['parent']:ps,pt=page['parent'];crumbs+='<li class="breadcrumb-nav-list-item"><a href="'+BASE+ps+'.html">'+html.escape(pt)+'</a></li>'
 if slug!='index':crumbs+='<li class="breadcrumb-nav-list-item"><span>'+html.escape(title)+'</span></li>'
 if slug=='index':body+='<hr><h2>文档章节</h2><ul>'+''.join('<li><a href="'+BASE+g[0]+'.html">'+html.escape(g[1])+'</a></li>' for g in groups)+'</ul>'
 footer='''<hr><footer><p><a href="#top" id="back-to-top">Back to top</a></p><p class="text-small text-grey-dk-000">© 2026 Hyphoon <a href="mailto:wuhaifeng@ustc.edu.cn">wuhaifeng@ustc.edu.cn</a>. All rights reserved. 引用请注明作者与来源；转载、改编或商业使用请事先联系作者。</p><p class="text-small text-grey-dk-000">This site uses <a href="https://just-the-docs.com/">Just the Docs</a>, a documentation theme for Jekyll.</p></footer>'''
 pagehtml='''<!doctype html><html lang="zh-CN" data-theme="mist"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>'''+html.escape(title)+''' · W 波段 EPR</title><link rel="icon" href="/assets/images/imasen_phi_logo/favicon.ico"><link rel="stylesheet" href="/assets/jtd/just-the-docs-default.css"><link rel="stylesheet" href="'''+BASE+'''themes.css?v=3"><script defer src="/assets/jtd/lunr.min.js"></script><script defer src="'''+BASE+'''zh-search.js"></script><script defer src="'''+BASE+'''just-the-docs.js"></script><script defer src="'''+BASE+'''theme.js?v=3"></script>'''+math+'''</head><body>'''+icons+'''<a class="skip-to-main" href="#main-content">跳至正文</a><div class="side-bar"><div class="site-header"><a class="brand-home" href="/" aria-label="返回主页"><img src="/assets/images/imasen_phi_logo/favicon.ico" width="36" height="36" alt=""></a><a href="'''+BASE+'''index.html" class="site-title lh-tight">W 波段 EPR</a><button id="menu-button" class="site-button btn-reset" aria-label="菜单" aria-expanded="false"><svg viewBox="0 0 24 24"><use href="#svg-menu"/></svg></button></div><nav id="site-nav" class="site-nav" aria-label="文档导航">'''+nav+'''</nav><div class="site-footer"><a href="/notes/">返回 Notes</a></div></div><div class="main" id="top"><div id="main-header" class="main-header"><div class="search" role="search"><div class="search-input-wrap"><input type="text" id="search-input" class="search-input" tabindex="0" placeholder="搜索 W 波段 EPR 文档" autocomplete="off"><label for="search-input" class="search-label"><span class="sr-only">搜索 W 波段 EPR 文档</span><svg viewBox="0 0 24 24" class="search-icon"><use href="#svg-search"/></svg></label></div><div id="search-results" class="search-results"></div></div>'''+settings+'''</div><div class="main-content-wrap"><nav class="breadcrumb-nav" aria-label="Breadcrumb"><ol class="breadcrumb-nav-list">'''+crumbs+'''</ol></nav><div class="main-content" id="main-content"><main>'''+body+footer+'''</main></div></div></div><div class="search-overlay"></div><script type="module">import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';mermaid.initialize({startOnLoad:true,securityLevel:'strict',theme:'default'});</script></body></html>'''
 (O/(slug+'.html')).write_text(pagehtml)
 # Sections in the upstream search-data format.
 chunks=list(re.finditer(r'<h[12]([^>]*)>(.*?)</h[12]>',body,re.S))
 for k,h in enumerate(chunks):
  ident=re.search(r'id="([^"]+)"',h[1]);url=BASE+slug+'.html'+('#'+ident[1] if ident else '')
  txt=plain(body[h.end():chunks[k+1].start() if k+1<len(chunks) else len(body)])
  index[str(len(index))]=dict(title=plain(h[2]),content=txt,url=url,relUrl=url,doc=title,section=plain(h[2]))
(O/'search-data.json').write_text(json.dumps(index,ensure_ascii=False))
js=(R/'assets/jtd/just-the-docs.js').read_text().replace("'/assets/js/search-data.json'",repr(BASE+'search-data.json'))
js=js.replace("this.ref('id');","this.pipeline.remove(lunr.trimmer,lunr.stemmer);this.searchPipeline.remove(lunr.stemmer);this.ref('id');")
(O/'just-the-docs.js').write_text(js)
print('Generated',len(pages),'pages;',len(index),'search sections; 13 original tables:',sum(p['body'].count('<table') for p in pages))
