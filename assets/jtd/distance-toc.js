(()=>{
 const rail=document.querySelector('.page-toc-rail');if(!rail)return;
 const links=[...rail.querySelectorAll('a')];
 const headings=links.map(a=>({a,h:document.getElementById(a.hash.slice(1))})).filter(x=>x.h);
 function update(){let active=headings[0];for(const item of headings){if(item.h.getBoundingClientRect().top<=160)active=item;else break;}
  links.forEach(a=>a.removeAttribute('aria-current'));if(active)active.a.setAttribute('aria-current','location');}
 let pending=false;window.addEventListener('scroll',()=>{if(!pending){pending=true;requestAnimationFrame(()=>{pending=false;update();});}},{passive:true});window.addEventListener('hashchange',update);window.addEventListener('load',update);update();
})();
