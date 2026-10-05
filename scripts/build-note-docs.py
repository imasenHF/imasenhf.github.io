"""Generate published Just the Docs reports from canonical HTML sources."""
from pathlib import Path
import re,json,html,argparse
R=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('note',choices=['w-band-epr','x-band-epr-medical','electron-electron-distance']);NOTE=parser.parse_args().note
O=R/'notes'/NOTE;O.mkdir(parents=True,exist_ok=True);BASE='/notes/'+NOTE+'/'
source=(R/'_note_sources'/f'{NOTE}.html').read_text();frontmatter=source.split('---',2)[1];s=source.split('---',2)[2]
def plain(t):return html.unescape(re.sub('<[^>]+>','',t)).strip()
def clean(t):return re.sub(r'^(?:第\s*\d+\s*章\s*|\d+(?:\.\d+)*[.、．]?\s+)','',t)
def promote(t):
 t=re.sub(r'<h3([^>]*)>(.*?)</h3>',lambda m:'<h2'+m[1]+'>'+clean(m[2])+'</h2>',t,flags=re.S)
 return re.sub(r'<h4([^>]*)>(.*?)</h4>',lambda m:'<h3'+m[1]+'>'+clean(m[2])+'</h3>',t,flags=re.S)
pages=[];groups=[];aliases={}
def add(slug,title,body,old='',parent=None,oldid=None):
 head='<h1'+(' id="'+html.escape(oldid,quote=True)+'"' if oldid else '')+'>'+html.escape(title)+'</h1>'
 if old and old!=title:head+='<p class="doc-subtitle">'+html.escape(old)+'</p>'
 pages.append(dict(slug=slug,title=title,body=head+body,parent=parent))
 if oldid:aliases[oldid]=slug+'.html#'+oldid
if NOTE=='w-band-epr':
 DOC_TITLE='W 波段 EPR：原理与应用';DOC_SHORT='W 波段 EPR';SUBTITLE='高场效应、应用体系与实验条件'
 s=s[s.index('<div class="report-body">')+len('<div class="report-body">'):];s=s[:s.rfind('{% endraw %}')];s=re.sub(r'\s*</div>\s*</div>\s*$','',s)
 parts=list(re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>',s,re.S));intro=s[parts[0].end():parts[1].start()]
 add('index',DOC_TITLE,'<p class="fs-6 fw-300">'+SUBTITLE+'</p><p><span class="label">磁共振</span> <span class="label">EPR</span> <span class="label">W-band</span></p><h2 id="摘要">摘要</h2>'+intro)
 for i,p in enumerate(parts[1:],1):
  title=['理论基础','应用主线','应用地图','领域映射','适用性判断','仪器需求','案例索引','结论'][i-1];slug=f'chapter-{i}';body=s[p.end():parts[i+1].start() if i+1<len(parts) else len(s)];children=[]
  if i==2:
   hs=list(re.finditer(r'<h3 id="([^"]+)">(.*?)</h3>',body,re.S));parentbody=body[:hs[0].start()]
   for j,h in enumerate(hs,1):
    cs=f'application-{j}';ct=['电子结构分辨','高自旋体系','局域结构','分子运动','量子自旋动力学'][j-1];cb=body[h.end():hs[j].start() if j<len(hs) else len(body)];cb=re.sub(r'<h4([^>]*)>(.*?)</h4>',lambda m:'<h2'+m[1]+'>'+clean(m[2])+'</h2>',cb,flags=re.S)
    add(cs,ct,cb,plain(clean(h[2])),(slug,title),h[1]);children.append((cs,ct))
   body=parentbody+'<p>各应用主线分别列于子页面，每页包括理论依据、适用体系、案例和适用边界。</p><h2>子页面</h2><ul>'+''.join('<li><a href="'+BASE+cs+'.html">'+ct+'</a></li>' for cs,ct in children)+'</ul>'
  else:body=promote(body)
  add(slug,title,body,plain(p[2]),oldid=p[1]);groups.append((slug,title,children))
elif NOTE=='x-band-epr-medical':
 DOC_TITLE='医学 EPR：方法与应用';DOC_SHORT='医学 EPR';SUBTITLE='X 波段连续波、脉冲方法与低频成像扩展'
 s=re.search(r'<main[^>]*>(.*?)</main>',s,re.S)[1];parts=list(re.finditer(r'<h2([^>]*)>(.*?)</h2>',s,re.S))
 titles=['范围与数据','自由基与氧化还原','金属蛋白与酶','蛋白结构与距离','治疗与医用材料','临床样本与剂量学','低频与成像','结论','收录规则','技术边界','案例与配置','资料来源']
 first=parts[0];intro=s[first.end():parts[1].start()];add('index',DOC_TITLE,'<p class="fs-6 fw-300">'+SUBTITLE+'</p><p><span class="label">EPR</span><span class="label">医学应用</span></p><h2 id="摘要">摘要</h2>'+intro)
 for i,p in enumerate(parts[1:],1):
  slug=f'chapter-{i}';ident=re.search(r'id="([^"]+)"',p[1]);add(slug,titles[i-1],promote(s[p.end():parts[i+1].start() if i+1<len(parts) else len(s)]),plain(p[2]),oldid=ident[1] if ident else None);groups.append((slug,titles[i-1],[]))
else:
 DOC_TITLE='电子—电子距离测定：原理、方法与数据解释';DOC_SHORT='电子—电子距离';SUBTITLE='连续波与脉冲偶极谱的实验设计、相位选择与距离反演'
 s=re.search(r'<main[^>]*>(.*?)</main>',s,re.S)[1];articles=list(re.finditer(r'<article\b[^>]*class="chapter"[^>]*>(.*?)</article>',s,re.S));assert len(articles)==17
 intro=s[s.index('<section class="abstract"'):s.index('<section class="part-divider"')];add('index',DOC_TITLE,'<p class="fs-6 fw-300">'+SUBTITLE+'</p><p><span class="label">EPR</span><span class="label">距离测量</span></p>'+intro)
 titles=['偶极作用与距离核','距离分布与观测模型','相干路径与相位循环','自旋体系与样品','CW 短距离测定','四脉冲 DEER','多脉冲 DEER','双量子相干 DQC','SIFTER 与 SIDRE','RIDME','光诱导偶极谱','参数与实验优化','距离反演与不确定度','软件与方法选择','应用案例','伪影与诊断','方法进展']
 for i,a in enumerate(articles,1):
  body=a[1]
  if i in [1,5,12,15]:
   divider=re.search(r'<section class="part-divider" id="part-'+str(i)+r'">(.*?)</section>',s,re.S)
   if divider:body=divider[0]+body
  # Keep the source chapter H2, section H3 and detail H4, with original numbering.
  body=re.sub(r'<nav class="chapter-jump".*?</nav>', '', body, flags=re.S)
  slug=f'chapter-{i}'
  numbered_title=f'第{i}章 '+titles[i-1]
  add(slug,numbered_title,body,oldid=slug)
  groups.append((slug,numbered_title,[]))
 refs=s[s.index('<section id="references"'):];add('references','参考文献',refs);groups.append(('references','参考文献',[]))
 for i in [1,5,12,15]:aliases[f'part-{i}']=f'chapter-{i}.html'
# Preserve cross-page anchors before rewriting href values.
for p in pages:
 for ident in re.findall(r'\bid="([^"]+)"',p['body']):aliases[ident]=p['slug']+'.html#'+ident
for p in pages:
 def link(m):
  from urllib.parse import unquote
  ident=unquote(html.unescape(m[1]));return 'href="'+BASE+html.escape(aliases[ident],quote=True)+'"' if ident in aliases else m[0]
 p['body']=re.sub(r'href="#([^"]+)"',link,p['body'])
(O/'anchor-map.json').write_text(json.dumps(aliases,ensure_ascii=False))

icons='''<svg xmlns="http://www.w3.org/2000/svg" style="display:none"><symbol id="svg-arrow-right" viewBox="0 0 24 24"><path d="m9 6 6 6-6 6" fill="none" stroke="currentColor" stroke-width="2"/></symbol><symbol id="svg-search" viewBox="0 0 24 24"><circle cx="10" cy="10" r="6" fill="none" stroke="currentColor" stroke-width="2"/><path d="m15 15 6 6" stroke="currentColor" stroke-width="2"/></symbol><symbol id="svg-menu" viewBox="0 0 24 24"><path d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" stroke-width="2"/></symbol><symbol id="svg-doc" viewBox="0 0 24 24"><path d="M5 3h10l4 4v14H5zM8 11h8M8 15h8" fill="none" stroke="currentColor" stroke-width="1.5"/></symbol><symbol id="svg-link" viewBox="0 0 16 16"><path d="m6 10 4-4M5 7 3 9a2 2 0 0 0 3 3l2-2M8 6l2-2a2 2 0 0 1 3 3l-2 2" stroke="currentColor" fill="none"/></symbol></svg>'''
def navitem(slug,title,children=[]):
 button='<button class="nav-list-expander btn-reset" aria-label="展开 '+html.escape(title,quote=True)+'" aria-expanded="false"><svg viewBox="0 0 24 24"><use href="#svg-arrow-right"/></svg></button>' if children else ''
 return '<li class="nav-list-item">'+button+'<a class="nav-list-link" href="'+BASE+slug+'.html">'+html.escape(title)+'</a>'+('<ul class="nav-list">'+''.join(navitem(*c) for c in children)+'</ul>' if children else '')+'</li>'
nav='<ul class="nav-list">'+navitem('index','文档首页')+''.join(navitem(*g) for g in groups)+'</ul>'
if NOTE=='electron-electron-distance':
 # Reproduce the original visual hierarchy: parts contain chapters.
 def entry(url,title,children=''):
  button='<button class="nav-list-expander btn-reset" aria-label="展开 '+html.escape(title,quote=True)+'" aria-expanded="false"><svg viewBox="0 0 24 24"><use href="#svg-arrow-right"/></svg></button>' if children else ''
  return '<li class="nav-list-item">'+button+'<a class="nav-list-link" href="'+BASE+url+'">'+html.escape(title)+'</a>'+('<ul class="nav-list">'+children+'</ul>' if children else '')+'</li>'
 items=entry('index.html#summary','摘要与报告范围')+entry('index.html#abbreviations','缩写与术语')
 for first,last,label in [(1,4,'第一部分 物理与实验基础'),(5,11,'第二部分 实验方法、脉冲序列与相干选择'),(12,14,'第三部分 参数、数据分析与软件实现'),(15,17,'第四部分 应用案例、异常诊断与方法进展')]:
  children=''.join(entry('chapter-'+str(i)+'.html',pages[i]['title']) for i in range(first,last+1))
  items+=entry('chapter-'+str(first)+'.html#part-'+str(first),label,children)
 nav='<ul class="nav-list">'+items+entry('references.html','参考文献')+'</ul>'
math=r'''<script>window.MathJax={tex:{inlineMath:[['\\(','\\)'],['$','$']],displayMath:[['\\[','\\]'],['$$','$$']]},options:{skipHtmlTags:['script','noscript','style','textarea','pre','code']}};</script><script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>'''
settings='''<details class="doc-theme"><summary aria-label="主题设置" title="主题设置"><svg width="20" height="20" viewBox="0 0 24 24"><path d="M4 7h10M18 7h2M4 17h2M10 17h10M14 4v6M6 14v6" stroke="currentColor" fill="none"/></svg></summary><div class="theme-options">'''+''.join('<button data-theme="'+k+'" aria-label="'+n+'" title="'+n+'"></button>' for k,n in [('sage','鼠尾草绿'),('mist','雾蓝'),('sand','暖砂'),('mauve','灰紫'),('gray','浅灰')])+'</div></details>'
index={}
for page in pages:
 slug,title,body=page['slug'],page['title'],page['body'];heads=list(re.finditer(r'<h[23]([^>]*)>(.*?)</h[23]>',body,re.S))
 for k,h in enumerate(heads):
  if 'id=' not in h[1]:body=body.replace(h[0],h[0].replace('<h','<h',1).replace('>',' id="section-'+str(k)+'">',1),1)
 if True:
  for k,h in enumerate(list(re.finditer(r'<h4([^>]*)>(.*?)</h4>',body,re.S))):
   if 'id=' not in h[1]:body=body.replace(h[0],h[0].replace('>',' id="detail-'+str(k)+'">',1),1)
 # Native inline page contents.
 toc=[]
 for level,attrs,t in re.findall(r'<h(['+('34' if NOTE=='electron-electron-distance' else '234')+r'])([^>]*)>(.*?)</h\1>',body,re.S):
  ident=re.search(r'id="([^"]+)"',attrs)
  if ident:toc.append('<li class="toc-level-'+level+'"><a href="#'+html.escape(ident[1],quote=True)+'">'+html.escape(html.unescape(re.sub('<[^>]+>','',t)).strip())+'</a></li>')
 pos=body.index('</h1>')+5
 rail=''
 if toc:
  rail='<aside class="page-toc-rail" aria-label="小节目录"><details class="page-toc" open><summary>本章目录</summary><ul>'+''.join(toc)+'</ul></details></aside>'

 body=re.sub(r'(<h[123] id="([^"]+)"[^>]*>)(.*?)(</h[123]>)',lambda m:m[1]+'<a class="anchor-heading" href="#'+html.escape(m[2],quote=True)+'" aria-label="链接到本节"><svg viewBox="0 0 16 16"><use href="#svg-link"/></svg></a>'+m[3]+m[4],body,flags=re.S)
 crumbs='<li class="breadcrumb-nav-list-item"><a href="'+BASE+'index.html">'+DOC_SHORT+'</a></li>'
 if page['parent']:ps,pt=page['parent'];crumbs+='<li class="breadcrumb-nav-list-item"><a href="'+BASE+ps+'.html">'+html.escape(pt)+'</a></li>'
 if slug!='index':crumbs+='<li class="breadcrumb-nav-list-item"><span>'+html.escape(title)+'</span></li>'
 if slug=='index':body+='<hr><h2>文档章节</h2><ul>'+''.join('<li><a href="'+BASE+g[0]+'.html">'+html.escape(g[1])+'</a></li>' for g in groups)+'</ul>'
 footer='''<hr><footer><p><a href="#top" id="back-to-top">Back to top</a></p><p class="text-small text-grey-dk-000">© 2026 Hyphoon <a href="mailto:wuhaifeng@ustc.edu.cn">wuhaifeng@ustc.edu.cn</a>. All rights reserved. 引用请注明作者与来源；转载、改编或商业使用请事先联系作者。</p><p class="text-small text-grey-dk-000">This site uses <a href="https://just-the-docs.com/">Just the Docs</a>, a documentation theme for Jekyll.</p></footer>'''
 pagehtml='''<!doctype html><html lang="zh-CN" data-theme="mist"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'''+html.escape(title)+''' · '+DOC_SHORT+'</title><link rel="icon" href="/assets/images/imasen_phi_logo/favicon.ico"><link rel="stylesheet" href="/assets/jtd/just-the-docs-default.css"><link rel="stylesheet" href="'''+'''/assets/jtd/note-themes.css?v=4"><link rel="stylesheet" href="/assets/css/section-brand.css?v=20261005-brand"><script defer src="/assets/jtd/lunr.min.js"></script><script defer src="'''+'''/assets/jtd/zh-search.js"></script><script defer src="'''+BASE+'''just-the-docs.js"></script><script defer src="'''+'''/assets/jtd/note-theme.js?v=4"></script>'''+math+'''</head><body>'''+icons+'''<a class="skip-to-main" href="#main-content">跳至正文</a><div class="side-bar"><div class="site-header"><div class="section-brand"><a class="section-brand-icon-link" href="/" aria-label="返回主页"><img class="section-brand-icon" src="/assets/images/imasen_phi_logo/imasen-phi-64.png" width="48" height="48" alt=""></a><div class="section-brand-text"><a class="section-brand-title" href="/">plastocyanin<span class="section-brand-dot">.</span></a><a class="section-brand-subtitle" href="/notes/" aria-label="返回 Notebook">N<span class="section-brand-gold">o</span>teb<span class="section-brand-gold">oo</span>k</a></div></div><button id="menu-button" class="site-button btn-reset" aria-label="菜单" aria-expanded="false"><svg viewBox="0 0 24 24"><use href="#svg-menu"/></svg></button></div><nav id="site-nav" class="site-nav" aria-label="文档导航">'''+nav+'''</nav><div class="site-footer"><a href="/notes/">返回 Notebook</a></div></div><div class="main" id="top"><div id="main-header" class="main-header"><div class="search" role="search"><div class="search-input-wrap"><input type="text" id="search-input" class="search-input" tabindex="0" placeholder="搜索 '+DOC_SHORT+' 文档" autocomplete="off"><label for="search-input" class="search-label"><span class="sr-only">搜索 '+DOC_SHORT+' 文档</span><svg viewBox="0 0 24 24" class="search-icon"><use href="#svg-search"/></svg></label></div><div id="search-results" class="search-results"></div></div>'''+settings+'''</div><div class="main-content-wrap"><nav class="breadcrumb-nav" aria-label="Breadcrumb"><ol class="breadcrumb-nav-list">'''+crumbs+'''</ol></nav><div class="main-content" id="main-content"><main>'''+body+footer+'''</main></div></div></div><div class="search-overlay"></div><script type="module">import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';mermaid.initialize({startOnLoad:true,securityLevel:'strict',theme:'default'});</script></body></html>'''
 pagehtml=pagehtml.replace("'+DOC_SHORT+'",DOC_SHORT)
 if NOTE=='electron-electron-distance':
  version=__import__('hashlib').sha256((R/'assets/jtd/distance-content.css').read_bytes()).hexdigest()[:10]
  pagehtml=pagehtml.replace('</head>','<link rel="stylesheet" href="/assets/jtd/distance-content.css?v='+version+'"><script defer src="/assets/jtd/distance-toc.js?v=1"></script></head>')
  pagehtml=pagehtml.replace('<body>','<body class="distance-doc">')
 pagehtml=pagehtml.replace('<main>'+body,'<main>'+rail+body).replace('<body>', '<body class="doc-with-right-toc">').replace('class="distance-doc"','class="distance-doc doc-with-right-toc"')
 if NOTE!='electron-electron-distance':pagehtml=pagehtml.replace('</head>','<script defer src="/assets/jtd/distance-toc.js?v=1"></script></head>')
 pagehtml=pagehtml.replace('</head>','<script defer src="/assets/jtd/note-anchors.js?v=1"></script></head>')
 import hashlib
 for asset in ['note-themes.css','note-theme.js','note-anchors.js','distance-toc.js']:
  version=hashlib.sha256((R/'assets/jtd'/asset).read_bytes()).hexdigest()[:10]
  pagehtml=re.sub(re.escape(asset)+r'\?v=[^"]+',asset+'?v='+version,pagehtml)
 if slug=='index':
  meta=re.sub(r'(?m)^layout:.*$', 'layout: false',frontmatter)
  meta=re.sub(r'(?m)^title:.*$', 'title: '+json.dumps(DOC_TITLE,ensure_ascii=False),meta)
  (R/'_notes'/f'{NOTE}.html').write_text('---\n'+meta.strip()+'\n---\n{% raw %}\n'+pagehtml+'\n{% endraw %}\n')
 else:(O/(slug+'.html')).write_text(pagehtml)
 # Sections in the upstream search-data format.
 chunks=list(re.finditer(r'<h[123]([^>]*)>(.*?)</h[123]>',body,re.S))
 for k,h in enumerate(chunks):
  ident=re.search(r'id="([^"]+)"',h[1]);url=BASE+slug+'.html'+('#'+ident[1] if ident else '')
  txt=plain(body[h.end():chunks[k+1].start() if k+1<len(chunks) else len(body)])
  index[str(len(index))]=dict(title=plain(h[2]),content=txt,url=url,relUrl=url,doc=title,section=plain(h[2]))
(O/'search-data.json').write_text(json.dumps(index,ensure_ascii=False))
js=(R/'assets/jtd/just-the-docs.js').read_text().replace("'/assets/js/search-data.json'",repr(BASE+'search-data.json'))
js=js.replace("this.ref('id');","this.pipeline.remove(lunr.trimmer,lunr.stemmer);this.searchPipeline.remove(lunr.stemmer);this.ref('id');")
(O/'just-the-docs.js').write_text(js)
print(NOTE,len(pages),'pages',len(index),'sections',sum(p['body'].count('<table') for p in pages),'tables')
