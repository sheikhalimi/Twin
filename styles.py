"""Styling constants for the digital twin Gradio app."""

GOLD = "#ecad0a"
BLUE = "#209dd7"
PURPLE = "#753991"

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap');

:root {
  --twin-gold: #c9970a;
  --twin-gold-soft: #f5e6b8;
  --twin-blue: #1a6fa8;
  --twin-purple: #5c2d75;
  --twin-bg: #0e1117;
  --twin-surface: #161b26;
  --twin-surface-2: #1c2333;
  --twin-surface-elevated: #222b3d;
  --twin-border: rgba(255, 255, 255, 0.1);
  --twin-border-strong: rgba(255, 255, 255, 0.18);
  --twin-text: #f3f4f7;
  --twin-muted: #9aa3b2;
  --twin-shadow: 0 8px 32px rgba(0, 0, 0, 0.28);
  --twin-radius: 16px;
  --twin-radius-sm: 12px;
  --twin-font-base: 16px;
  --twin-font-sm: 14.5px;
  --twin-font-lg: 17px;
}

body:not(.dark) {
  --twin-bg: #eef1f6;
  --twin-surface: #ffffff;
  --twin-surface-2: #f6f8fb;
  --twin-surface-elevated: #ffffff;
  --twin-border: rgba(15, 23, 42, 0.1);
  --twin-border-strong: rgba(15, 23, 42, 0.16);
  --twin-text: #0f172a;
  --twin-muted: #5b6475;
  --twin-gold-soft: #fdf6e3;
  --twin-shadow: 0 10px 40px rgba(15, 23, 42, 0.08);
}

footer, .built-with, .show-api, .api-docs { display: none !important; }

html {
  font-size: 16px;
}

html, body, gradio-app {
  background: var(--twin-bg) !important;
  min-height: 100vh;
}

body::before {
  content: '';
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  background:
    radial-gradient(ellipse 70% 45% at 50% -5%, rgba(201, 151, 10, 0.07), transparent 60%),
    radial-gradient(ellipse 50% 30% at 100% 0%, rgba(26, 111, 168, 0.05), transparent 55%);
}

/* ---------- Layout: medium, confident presence ---------- */
.gradio-container {
  position: relative;
  z-index: 1;
  background: transparent !important;
  color: var(--twin-text) !important;
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
  font-size: var(--twin-font-base) !important;
  width: 100% !important;
  max-width: 1040px !important;
  min-width: 0 !important;
  margin: 0 auto !important;
  padding: 48px 32px 64px !important;
}
.gradio-container .main, .gradio-container .contain, .gradio-container .wrap {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
}
.gradio-container * { min-width: 0; }

/* ---------- Professional header ---------- */
.gradio-container h1 {
  color: var(--twin-text) !important;
  font-size: 2.125rem !important;   /* 34px */
  font-weight: 700 !important;
  letter-spacing: -0.025em !important;
  line-height: 1.2 !important;
  border: 0 !important;
  padding: 0 !important;
  margin: 0 0 28px !important;
  text-align: center !important;
}

.gradio-container h1::after {
  content: '';
  display: block;
  width: 48px;
  height: 3px;
  background: var(--twin-gold);
  margin: 14px auto 0;
  border-radius: 2px;
}

.gradio-container p.description,
.gradio-container .description {
  display: block !important;
  text-align: center !important;
  color: var(--twin-muted) !important;
  font-size: var(--twin-font-base) !important;
  font-weight: 400 !important;
  line-height: 1.6 !important;
  margin: -12px 0 28px !important;
  max-width: 680px !important;
  margin-left: auto !important;
  margin-right: auto !important;
}


/* ---------- Main card wrapper ---------- */
.gradio-container .main {
  display: flex !important;
  flex-direction: column !important;
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: var(--twin-radius) !important;
  box-shadow: var(--twin-shadow) !important;
  padding: 28px 28px 24px !important;
  position: relative;
  overflow: hidden;
}

.gradio-container .main::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--twin-gold), var(--twin-blue), var(--twin-purple));
}

.block, .form {
  background: transparent !important;
  box-shadow: none !important;
}

/* ---------- Chatbot ---------- */
.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container {
  display: none !important;
}

.chatbot, .chatbot.block {
  background: var(--twin-surface-2) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: var(--twin-radius-sm) !important;
  min-height: 520px !important;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.04) !important;
  overflow: hidden !important;
}

.chatbot .placeholder, .chatbot .placeholder * {
  color: var(--twin-muted) !important;
  font-size: var(--twin-font-sm) !important;
  line-height: 1.5 !important;
}

/* ---------- Messages ---------- */
.message-row,
.message-row > div,
.message-row .role,
.message-wrap, .bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  border: 0 !important;
  box-shadow: none !important;
  padding: 14px 18px !important;
  border-radius: var(--twin-radius-sm) !important;
  max-width: 88% !important;
  animation: twin-fade-in 0.3s ease-out both;
}

@keyframes twin-fade-in {
  from { opacity: 0; transform: translateY(4px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* User */
.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble {
  background: var(--twin-blue) !important;
  color: #ffffff !important;
  border-radius: var(--twin-radius-sm) var(--twin-radius-sm) 6px var(--twin-radius-sm) !important;
}

/* Assistant */
.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble {
  background: var(--twin-surface-elevated) !important;
  color: var(--twin-text) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: var(--twin-radius-sm) var(--twin-radius-sm) var(--twin-radius-sm) 6px !important;
}

.message-row.bot-row .message,
.message-row.bot-row .bubble,
.message-row.bot-row .message-bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .bubble,
.message-row[data-role="assistant"] .message-bubble {
  border-left: 3px solid var(--twin-purple) !important;
}

.message-row.bot-row .message .message,
.message-row.bot-row .message .bubble,
.message-row.bot-row .message .message-bubble,
.message-row.bot-row .bubble .message,
.message-row.bot-row .bubble .bubble,
.message-row.bot-row .bubble .message-bubble,
.message-row.bot-row .message-bubble .message,
.message-row.bot-row .message-bubble .bubble,
.message-row.bot-row .message-bubble .message-bubble,
.message-row[data-role="assistant"] .message .message,
.message-row[data-role="assistant"] .message .bubble,
.message-row[data-role="assistant"] .message .message-bubble,
.message-row[data-role="assistant"] .bubble .message,
.message-row[data-role="assistant"] .bubble .bubble,
.message-row[data-role="assistant"] .bubble .message-bubble,
.message-row[data-role="assistant"] .message-bubble .message,
.message-row[data-role="assistant"] .message-bubble .bubble,
.message-row[data-role="assistant"] .message-bubble .message-bubble {
  border-left: 0 !important;
}

/* Bubble typography — readable medium size */
.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  font-size: var(--twin-font-sm) !important;
  line-height: 1.65 !important;
}
.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p,
.message-row .prose p {
  font-size: var(--twin-font-sm) !important;
  line-height: 1.65 !important;
  margin: 0 0 10px !important;
  color: inherit !important;
}
.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child,
.message-row .prose p:last-child { margin-bottom: 0 !important; }

.message-row .message strong,
.message-row .message-bubble strong,
.message-row .bubble strong {
  font-weight: 600 !important;
  color: inherit !important;
}

.message-row .message *,
.message-row .message-bubble *,
.message-row .bubble * {
  background: transparent !important;
  border-color: transparent !important;
  box-shadow: none !important;
  color: inherit !important;
}
.message-row .message a,
.message-row .message-bubble a {
  color: var(--twin-gold) !important;
  font-weight: 500 !important;
  text-decoration: underline;
  text-underline-offset: 3px;
}

/* ---------- Input ---------- */
.input-row,
.gr-input-row,
.chat-input-row,
form[class*="input"] {
  align-items: stretch !important;
  gap: 12px !important;
  margin-top: 8px !important;
}

textarea, input[type="text"] {
  background: var(--twin-surface-elevated) !important;
  border: 1px solid var(--twin-border-strong) !important;
  border-radius: var(--twin-radius-sm) !important;
  color: var(--twin-text) !important;
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: var(--twin-font-base) !important;
  padding: 16px 18px !important;
  line-height: 1.5 !important;
  min-height: 56px !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}
textarea:focus, input[type="text"]:focus {
  border-color: var(--twin-gold) !important;
  outline: none !important;
  box-shadow: 0 0 0 3px var(--twin-gold-soft) !important;
}
textarea::placeholder, input::placeholder {
  color: var(--twin-muted) !important;
  font-size: var(--twin-font-sm) !important;
}

/* ---------- Buttons ---------- */
button {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
  letter-spacing: 0.04em !important;
  text-transform: uppercase !important;
  font-size: 12.5px !important;
  font-weight: 600 !important;
  border: 1px solid var(--twin-border-strong) !important;
  border-radius: var(--twin-radius-sm) !important;
  background: var(--twin-surface-elevated) !important;
  color: var(--twin-text) !important;
  padding: 0 22px !important;
  min-height: 56px !important;
  min-width: 56px !important;
  align-self: stretch !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer;
  transition: border-color 0.2s ease, background 0.2s ease, color 0.2s ease !important;
}
button:hover {
  border-color: var(--twin-gold) !important;
  color: var(--twin-gold) !important;
}

button.primary,
button[variant="primary"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary {
  background: var(--twin-gold) !important;
  border: 1px solid var(--twin-gold) !important;
  color: #1a1a1a !important;
  min-height: 56px !important;
  min-width: 56px !important;
  box-shadow: 0 2px 8px rgba(201, 151, 10, 0.25) !important;
}
button.primary:hover,
button.submit:hover,
.submit-button:hover,
button.lg.primary:hover {
  background: #dbaa0e !important;
  border-color: #dbaa0e !important;
  color: #1a1a1a !important;
}

button.submit svg,
button.submit-button svg,
.submit-button svg,
button.primary svg,
button[variant="primary"] svg {
  width: 20px !important;
  height: 20px !important;
  margin: 0 auto !important;
  display: block !important;
  color: #1a1a1a !important;
  fill: currentColor !important;
  stroke: currentColor !important;
}

/* ---------- Example prompts ---------- */
.examples, .examples-holder, [data-testid="examples"] {
  background: transparent !important;
  padding: 0 !important;
  margin-top: 24px !important;
}

.examples::before,
.examples-holder::before,
[data-testid="examples"]::before {
  content: 'Suggested questions';
  display: block;
  font-size: 12px !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  color: var(--twin-muted) !important;
  margin-bottom: 12px !important;
}

.examples table, .examples-table {
  background: transparent !important;
  border: 0 !important;
  display: flex !important;
  flex-wrap: wrap !important;
  gap: 10px !important;
}
.examples tr, .examples td {
  display: contents !important;
  border: 0 !important;
  background: transparent !important;
}

.examples button, .example, .examples td button, [data-testid="examples"] button {
  background: var(--twin-surface-2) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: var(--twin-radius-sm) !important;
  color: var(--twin-text) !important;
  text-transform: none !important;
  letter-spacing: 0 !important;
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: var(--twin-font-sm) !important;
  font-weight: 500 !important;
  padding: 12px 18px !important;
  text-align: left !important;
  min-height: 0 !important;
  align-self: auto !important;
  display: inline-flex !important;
  align-items: center !important;
  line-height: 1.45 !important;
  transition: border-color 0.2s ease, background 0.2s ease !important;
}
.examples button:hover, .example:hover, [data-testid="examples"] button:hover {
  border-color: var(--twin-blue) !important;
  color: var(--twin-blue) !important;
  background: var(--twin-surface) !important;
}

/* ---------- Icon buttons ---------- */
.icon-button, .chatbot .icon-button {
  color: var(--twin-muted) !important;
  background: transparent !important;
  border: 0 !important;
  border-radius: 8px !important;
  min-height: 0 !important;
  min-width: 0 !important;
  align-self: auto !important;
  padding: 6px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}
.icon-button:hover, .chatbot .icon-button:hover {
  color: var(--twin-gold) !important;
  background: var(--twin-gold-soft) !important;
}

/* ---------- Scrollbar ---------- */
::-webkit-scrollbar { width: 9px; height: 9px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
  background: var(--twin-border-strong);
  border-radius: 99px;
}
::-webkit-scrollbar-thumb:hover { background: var(--twin-muted); }

::selection {
  background: var(--twin-gold-soft);
  color: var(--twin-text);
}

/* ---------- Mobile: still medium-readable ---------- */
@media (max-width: 720px) {
  .gradio-container {
    padding: 32px 18px 48px !important;
    font-size: 15px !important;
  }
  .gradio-container h1 { font-size: 1.75rem !important; }
  .gradio-container .markdown p,
  .gradio-container p.description { font-size: 15.5px !important; }
  .gradio-container .main { padding: 20px 16px 18px !important; }
  .chatbot, .chatbot.block { min-height: 440px !important; }
  textarea, input[type="text"] { font-size: 15px !important; min-height: 52px !important; }
  button { min-height: 52px !important; min-width: 52px !important; }
}
"""

JS = """
() => {
  document.title = 'Digital Twin — Career Assistant';

  const focusInput = () => {
    const areas = document.querySelectorAll('textarea');
    if (areas.length) areas[areas.length - 1].focus();
  };
  setTimeout(focusInput, 300);

  const watchTextarea = (area) => {
    if (area.dataset.twinWatched) return;
    area.dataset.twinWatched = '1';
    let wasDisabled = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, { attributes: true, attributeFilter: ['disabled', 'readonly'] });
  };

  const scan = () => document.querySelectorAll('textarea').forEach(watchTextarea);
  setTimeout(scan, 500);
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
}
"""
