/* A lightweight, dependency-free, scroll-led editorial motion layer. */
(()=>{'use strict';
const reduced=window.matchMedia('(prefers-reduced-motion: reduce)');
if(reduced.matches||!('IntersectionObserver' in window))return;
const root=document.documentElement;
const main=document.querySelector('main');
if(!main)return;
const progress=document.createElement('div');progress.className='motion-progress';progress.setAttribute('aria-hidden','true');document.body.appendChild(progress);
const exclusions=new Set(['SCRIPT','STYLE','NOSCRIPT']);
const lines=(h)=>{
  if(h.querySelector('.motion-line'))return;
  const original=h.innerHTML;
  if(!/<br\s*\/?\s*>/i.test(original))return;
  // Preserve inline formatting within each existing heading line.
  const parts=original.split(/<br\s*\/?\s*>/i);
  if(parts.length<2||parts.length>4)return;
  h.innerHTML=parts.map(p=>'<span class="motion-line"><span>'+p+'</span></span>').join('');
};
const heads=[...main.querySelectorAll('h1,h2')].filter(h=>h.closest('section')&& !h.closest('#decision-intelligence'));
for(const h of heads){lines(h);h.classList.add('motion-headline');}
const figures=[...main.querySelectorAll('figure.visual-card')];
figures.forEach(el=>el.classList.add('motion-image'));
const generic=[...main.querySelectorAll('section .section-label,section .hero-analyst-line,section .rec-lead,section .rec-disclaimer,section .large,section .quote,section .recommendation,section .rec-grid,section .method-grid,section .validation-grid')].filter(el=>!el.closest('.motion-headline')&&!exclusions.has(el.tagName));
generic.forEach((el,i)=>{el.classList.add(el.classList.contains('rec-grid')?'motion-grid':'motion-reveal');if(i%4===1)el.classList.add('motion-delay-1');if(i%4===2)el.classList.add('motion-delay-2');});
const targets=[...heads,...figures,...generic];
const observer=new IntersectionObserver(entries=>{for(const e of entries){if(e.isIntersecting){e.target.classList.add('motion-in');observer.unobserve(e.target);}}},{rootMargin:'0px 0px -8% 0px',threshold:0.06});
targets.forEach(el=>observer.observe(el));
root.classList.add('motion-ready');
let scheduled=false;
const update=()=>{scheduled=false;const max=Math.max(1,document.documentElement.scrollHeight-window.innerHeight);progress.style.transform='scaleX('+Math.max(0,Math.min(1,window.scrollY/max))+')'};
const onScroll=()=>{if(!scheduled){scheduled=true;requestAnimationFrame(update)}};
window.addEventListener('scroll',onScroll,{passive:true});window.addEventListener('resize',onScroll,{passive:true});update();
// Avoid invisible text following focus or anchor navigation.
document.addEventListener('focusin',event=>{const target=event.target.closest('.motion-reveal,.motion-headline,.motion-image');if(target)target.classList.add('motion-in')});
})();
