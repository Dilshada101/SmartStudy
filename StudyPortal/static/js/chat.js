function getCsrfToken() {
  const name = 'csrftoken=';
  const cookies = document.cookie.split(';');
  for (let c of cookies) {
    c = c.trim();
    if (c.startsWith(name)) return decodeURIComponent(c.substring(name.length));
  }
  const el = document.querySelector('input[name=csrfmiddlewaretoken]');
  return el ? el.value : '';
}

function appendMessage(role, text) {
  const log = document.getElementById('chat-log');
  const wrap = document.createElement('div');
  wrap.className = 'mb-3';
  const bubble = document.createElement('div');
  bubble.className = role === 'user' ? 'p-3 bg-primary text-white rounded-3' : 'p-3 bg-light rounded-3';
  bubble.style.whiteSpace = 'pre-wrap';
  bubble.textContent = text;
  wrap.appendChild(bubble);
  log.appendChild(wrap);
  log.scrollTop = log.scrollHeight;
}

document.addEventListener('DOMContentLoaded', () => {
  const chatForm = document.getElementById('chat-form');
  const chatInput = document.getElementById('chat-input');
  const roleSelect = document.getElementById('role-select');
  const pptForm = document.getElementById('ppt-form');

  chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const message = chatInput.value.trim();
    if (!message) return;
    appendMessage('user', message);
    chatInput.value = '';

    const res = await fetch('/chat/api/prompt/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCsrfToken(),
      },
      body: JSON.stringify({ message, role: roleSelect.value })
    });
    if (!res.ok) {
      appendMessage('assistant', 'Request failed.');
      return;
    }
    const data = await res.json();
    appendMessage('assistant', data.reply || '');
  });

  pptForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const topic = document.getElementById('ppt-topic').value.trim();
    const slides = parseInt(document.getElementById('ppt-slides').value, 10) || 8;
    const bullets = parseInt(document.getElementById('ppt-bullets').value, 10) || 4;
    const role = document.getElementById('ppt-role').value;
    if (!topic) return;

    const res = await fetch('/chat/api/generate_ppt/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCsrfToken(),
      },
      body: JSON.stringify({ topic, slides, bullets, role })
    });
    if (!res.ok) {
      appendMessage('assistant', 'PPT generation failed.');
      return;
    }
    const blob = await res.blob();
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${topic.replace(/\s+/g,'_')}.pptx`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
  });
});


