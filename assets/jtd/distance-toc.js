(()=>{
 const rail=document.querySelector('.page-toc-rail');if(!rail)return;
 const sections=[...document.querySelectorAll('.main-content h3[id]')];
 const links=[...rail.querySelectorAll('li')];
 let current='';
 function update(){
  let section=sections[0];for(const h of sections){if(h.getBoundingClientRect().top<=140)section=h;else break;}
  if(!section)return;
  if(current!==section.id){current=section.id;let owner='';
   for(const li of links){const a=li.querySelector('a');if(li.classList.contains('toc-level-3')){owner=a.hash.slice(1);li.classList.toggle('active-section',owner===current);}else li.hidden=owner!==current;}
   document.querySelectorAll('#site-nav a').forEach(a=>{const active=a.hash==='#'+current&&a.pathname===location.pathname;a.classList.toggle('active',active);if(active){const ul=a.closest('ul');const parent=ul.parentElement;if(parent.classList.contains('nav-list-item')){parent.classList.add('active');const button=parent.querySelector('button');if(button)button.setAttribute('aria-expanded','true');}}});
  }
  const visible=links.filter(li=>!li.hidden&&li.classList.contains('toc-level-4'));let active=visible[0];
  for(const li of visible){const h=document.getElementById(li.querySelector('a').hash.slice(1));if(h&&h.getBoundingClientRect().top<=160)active=li;}
  rail.querySelectorAll('a').forEach(a=>a.removeAttribute('aria-current'));if(active)active.querySelector('a').setAttribute('aria-current','location');
 }
 let pending=false;window.addEventListener('scroll',()=>{if(!pending){pending=true;requestAnimationFrame(()=>{pending=false;update();});}},{passive:true});window.addEventListener('hashchange',update);window.addEventListener('load',update);update();
})();
