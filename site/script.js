'use strict';
const states = {
 review: { icon: '◌', title: 'Review in progress', description: 'Your withdrawal request is being reviewed. A release date is not available in this concept.', next: 'Monitor your registered email for verified requests and updates. Use your existing support reference when contacting support.', boundary: 'Only show this state when disclosure is permitted. A status refresh must not imply a new case decision.' },
 action: { icon: '↗', title: 'Customer action requested', description: 'This demonstration assumes that a permitted information request has been issued.', next: 'Open the verified request using the approved in-app route or registered email. If you cannot find it, contact support using your existing reference.', boundary: 'Do not expose investigation details, request passwords or claim that submitting documents guarantees release.' },
 complete: { icon: '✓', title: 'Review completed', description: 'The review is complete in this demonstration. Review completion alone does not establish withdrawal success.', next: 'Check the withdrawal record for its approved outcome. If another restriction applies, follow the next step shown for that restriction.', boundary: 'Only show completion from an authoritative approved event. Keep review outcome and transfer settlement separate.' }
};
document.getElementById('review-state').addEventListener('change', (event) => {
 const state = states[event.target.value];
 document.querySelector('.status-icon').textContent = state.icon;
 document.getElementById('status-title').textContent = state.title;
 document.getElementById('status-description').textContent = state.description;
 document.getElementById('status-next').textContent = state.next;
 document.getElementById('status-boundary').textContent = state.boundary;
});
