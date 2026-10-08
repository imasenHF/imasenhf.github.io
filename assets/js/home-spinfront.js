(function(){
  const root=document.getElementById('home-spinfront-calendar');
  if(!root)return;

  const calendar=document.getElementById('hy2-calendar');
  const itemsEl=document.getElementById('hy2-items');
  const months=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'];
  const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const cnToday=()=>new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Shanghai',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date());

  let items=[],dates=new Set(),labels=new Map(),tagMeta=new Map(),selected='',month='',scrollRaf=0;
  let dailyEpigraph={
    text:'The test of all knowledge is experiment.',
    author:'Richard P. Feynman',
    work:'The Feynman Lectures on Physics, Vol. I, Ch. 1',
    language:'en',
    source_url:'https://www.feynmanlectures.caltech.edu/I_01.html',
    source_ref:'1–1 Introduction'
  };

  function dayNumber(date){
    const [y,m,d]=date.split('-').map(Number);
    return Math.floor(Date.UTC(y,m-1,d)/86400000);
  }

  function epigraphInner(){
    const lang=esc(dailyEpigraph.language||'en');
    const text=esc(dailyEpigraph.text||'').replaceAll(' / ','<br>');
    const meta=[dailyEpigraph.author,dailyEpigraph.work].filter(Boolean).map(esc).join(' · ');
    const source=dailyEpigraph.source_url
      ? '<a href="'+esc(dailyEpigraph.source_url)+'" target="_blank" rel="noopener noreferrer" title="'+esc(dailyEpigraph.source_ref||'原始出处')+'">'+meta+'</a>'
      : meta;
    return '<strong>Daily epigraph</strong><span class="hy2-epigraph" data-lang="'+lang+'"><q>'+text+'</q><em>'+source+'</em></span><i class="hy2-scroll-cue">↓</i>';
  }

  function resetGuideHeight(){
    const guide=itemsEl.querySelector('.hy2-guide');
    const first=itemsEl.querySelector('.hy2-entry');
    if(!guide||!first)return;
    guide.style.height='auto';
    guide.style.height=Math.max(118,(itemsEl.clientHeight-first.offsetHeight)/2)+'px';
  }

  function renderEpigraph(){
    const guide=itemsEl.querySelector('.hy2-guide');
    if(!guide)return;
    guide.innerHTML=epigraphInner();
    requestAnimationFrame(resetGuideHeight);
  }

  async function loadDailyEpigraph(){
    try{
      const r=await fetch('/assets/data/epigraphs.json',{cache:'force-cache'});
      if(!r.ok)throw new Error('HTTP '+r.status);
      const lib=await r.json();
      const entries=lib.entries||[];
      if(!entries.length)return;
      const epoch=lib.rotation?.epoch||'2026-10-07';
      const delta=dayNumber(cnToday())-dayNumber(epoch);
      dailyEpigraph=entries[((delta%entries.length)+entries.length)%entries.length];
      renderEpigraph();
    }catch(err){
      console.warn('Daily epigraph library unavailable; using fallback.',err);
    }
  }

  function renderCalendar(){
    const [y,m]=month.split('-').map(Number);
    const offset=(new Date(y,m-1,1).getDay()+6)%7;
    const last=new Date(y,m,0).getDate();
    document.getElementById('hy2-month-en').textContent=months[m-1]+' · '+y;
    document.getElementById('hy2-month-cn').textContent=String(m).padStart(2,'0')+' 月';
    document.getElementById('hy2-ghost-month').textContent=String(m).padStart(2,'0');

    let html='MTWTFSS'.split('').map(x=>'<span class="week">'+x+'</span>').join('');
    html+='<span class="blank"></span>'.repeat(offset);
    for(let d=1;d<=last;d++){
      const date=month+'-'+String(d).padStart(2,'0');
      const has=dates.has(date),pick=date===selected;
      html+='<button type="button" class="'+(has?'has ':'')+(pick?'selected':'')+'" data-date="'+date+'" '+(has?'':'disabled ')+'aria-pressed="'+pick+'">'+d+'</button>';
    }
    calendar.innerHTML=html;
    calendar.querySelectorAll('[data-date]').forEach(btn=>btn.onclick=()=>selectDate(btn.dataset.date));
    document.getElementById('hy2-month-count').textContent=[...dates].filter(x=>x.startsWith(month)).length;
  }

  function tagHref(id){
    const t=tagMeta.get(id);
    if(!t)return'/spinfront/';
    const p=new URLSearchParams();
    p.set('view','all');
    p.set(t.dimension,id);
    return '/spinfront/?'+p.toString()+'#explore';
  }

  function itemHtml(x,i){
    const tagIds=[...(x.direction_ids||[]),...(x.experiment_type_ids||[]),...(x.method_ids||[]),...(x.application_ids||[]),...(x.instrument_component_ids||[])].slice(0,3);
    const source='/spinfront/'+selected+'/#'+x.item_id;
    const tagHtml=tagIds.map(id=>'<a href="'+esc(tagHref(id))+'" title="检索：'+esc(labels.get(id)||id)+'">'+esc(labels.get(id)||id.replaceAll('_',' '))+'</a>').join('');
    return '<article class="hy2-entry" data-index="'+i+'"><div class="hy2-index">'+String(i+1).padStart(2,'0')+'<small>'+esc(x.publication_date||'')+'</small></div><div><h3><a href="'+esc(source)+'">'+esc(x.title_cn)+'</a></h3><p>'+esc(x.summary_cn)+'</p><div class="hy2-tags">'+tagHtml+'</div></div></article>';
  }

  function updateFocus(){
    const rows=[...itemsEl.querySelectorAll('.hy2-entry')];
    if(!rows.length)return;
    const box=itemsEl.getBoundingClientRect(),center=box.top+box.height/2;
    let best=0,dist=Infinity;
    rows.forEach((row,i)=>{
      const r=row.getBoundingClientRect(),d=Math.abs((r.top+r.bottom)/2-center);
      if(d<dist){dist=d;best=i}
    });
    rows.forEach((row,i)=>{
      row.classList.toggle('is-focus',i===best);
      row.classList.toggle('is-near',Math.abs(i-best)===1);
    });
  }

  function renderReport(){
    const current=items.filter(x=>x.report_date===selected);
    document.getElementById('hy2-date').textContent=selected;
    document.getElementById('hy2-big-day').textContent=selected.slice(-2);
    document.getElementById('hy2-count').textContent=current.length+' 条日报内容';
    document.getElementById('hy2-full').href='/spinfront/';

    if(!current.length){
      itemsEl.innerHTML='<p class="hy2-loading">该日期暂无已发布日报。</p>';
      return;
    }

    itemsEl.innerHTML='<div class="hy2-guide">'+epigraphInner()+'</div>'+
      current.map((x,i)=>itemHtml(x,i)).join('')+
      '<div class="hy2-end">END OF DAILY BRIEF</div>';
    itemsEl.scrollTop=0;
    requestAnimationFrame(()=>{
      resetGuideHeight();
      updateFocus();
    });
  }

  function selectDate(date){
    selected=date;
    month=date.slice(0,7);
    renderCalendar();
    renderReport();
  }

  function shift(delta){
    const [y,m]=month.split('-').map(Number),d=new Date(y,m-1+delta,1);
    month=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0');
    renderCalendar();
  }

  document.getElementById('hy2-prev').onclick=()=>shift(-1);
  document.getElementById('hy2-next').onclick=()=>shift(1);
  itemsEl.addEventListener('scroll',()=>{
    if(scrollRaf)return;
    scrollRaf=requestAnimationFrame(()=>{
      scrollRaf=0;
      updateFocus();
    });
  },{passive:true});
  window.addEventListener('resize',()=>requestAnimationFrame(resetGuideHeight),{passive:true});

  async function init(){
    try{
      const [searchRes,taxRes]=await Promise.all([
        fetch('/spinfront/search-index.json',{cache:'no-store'}),
        fetch('/spinfront/taxonomy/taxonomy.json',{cache:'force-cache'})
      ]);
      if(!searchRes.ok)throw new Error('SpinFront index HTTP '+searchRes.status);
      const data=await searchRes.json();
      items=data.items||[];
      dates=new Set((data.issues||[]).map(x=>x.report_date));

      if(taxRes.ok){
        const tax=await taxRes.json();
        labels=new Map((tax.tags||[]).map(x=>[x.id,x.label_cn||x.label_en||x.id]));
        tagMeta=new Map((tax.tags||[]).map(x=>[x.id,x]));
      }

      const ordered=[...dates].sort();
      if(!ordered.length)throw new Error('SpinFront archive is empty');
      const today=cnToday();
      selected=dates.has(today)?today:ordered[ordered.length-1];
      month=selected.slice(0,7);
      renderCalendar();
      renderReport();
      loadDailyEpigraph();
    }catch(err){
      itemsEl.innerHTML='<p class="hy2-loading">SpinFront 日历暂时无法读取。</p>';
      console.error(err);
      loadDailyEpigraph();
    }
  }

  init();
})();