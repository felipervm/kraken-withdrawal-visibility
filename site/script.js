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
});
