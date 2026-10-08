'use strict';
const states = {
 review: { icon: '◌', title: 'Review in progress', description: 'Your withdrawal is being reviewed. A release date isn’t available yet.', next: 'Check your registered email for verified requests and updates. If you contact support, use your existing reference.', boundary: 'This message would appear only when the team can share the review state.' },
 action: { icon: '↗', title: 'We need something from you', description: 'There’s a request for information to help with the review.', next: 'Open the verified request in the app or your registered email. If you can’t find it, contact support using your existing reference.', boundary: 'Sending the information doesn’t guarantee that the withdrawal will be released.' },
 complete: { icon: '✓', title: 'Review completed', description: 'The review is complete. Check your withdrawal record to see its outcome.', next: 'If another restriction applies, follow the next step shown for that restriction. You can still contact support if you need help.', boundary: 'A completed review doesn’t mean the transfer has settled. This state needs a confirmed, approved event.' }
};
document.getElementById('review-state').addEventListener('change', (event) => {
 const state = states[event.target.value];
 document.querySelector('.status-icon').textContent = state.icon;
 document.getElementById('status-title').textContent = state.title;
 document.getElementById('status-description').textContent = state.description;
 document.getElementById('status-next').textContent = state.next;
 document.getElementById('status-boundary').textContent = state.boundary;
 if (!motionPreference.matches) {
  document.querySelector('.status-body').getAnimations().forEach(animation => animation.cancel());
  document.querySelector('.status-body').animate([
   { opacity: 0.35, transform: 'translateY(7px)' },
   { opacity: 1, transform: 'translateY(0)' }
  ], { duration: 360, easing: 'cubic-bezier(.22,1,.36,1)' });
 }
});

const motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
const pointerPreference = window.matchMedia('(hover: hover) and (pointer: fine)');
const cards = document.querySelectorAll('.method-grid article, .validation-grid article, .visual-card');
cards.forEach(card => {
 card.addEventListener('pointermove', event => {
  if (motionPreference.matches || !pointerPreference.matches || event.pointerType !== 'mouse') return;
  const bounds = card.getBoundingClientRect();
  const x = (event.clientX - bounds.left) / bounds.width - 0.5;
  const y = (event.clientY - bounds.top) / bounds.height - 0.5;
  card.style.setProperty('--tilt-x', `${-y * 3}deg`);
  card.style.setProperty('--tilt-y', `${x * 3}deg`);
 });
 card.addEventListener('pointerleave', () => {
  card.style.removeProperty('--tilt-x');
  card.style.removeProperty('--tilt-y');
 });
});

// Keep ambient movement quiet, and pause it when its section leaves the screen.
if ('IntersectionObserver' in window) {
 const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => entry.target.classList.toggle('motion-visible', entry.isIntersecting));
 }, { threshold: 0.08 });
 document.querySelectorAll('.hero, .visual-card').forEach(element => observer.observe(element));
}
motionPreference.addEventListener('change', () => {
 cards.forEach(card => {
  card.style.removeProperty('--tilt-x');
  card.style.removeProperty('--tilt-y');
 });
 if (motionPreference.matches) document.querySelector('.status-body').getAnimations().forEach(animation => animation.cancel());
});
