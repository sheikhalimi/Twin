"""Styling constants for the Digital Twin Gradio application."""

GOLD = "#B8833E"
BLUE = "#3E7C78"
PURPLE = "#6D5B7B"

EXAMPLES = [
    "Which frontend technologies and frameworks do you specialize in?",
    "Walk me through a recent frontend project.",
    "How do you approach responsive, accessible UI development?",
    "What is the best way to contact you about a frontend role?",
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=Playfair+Display:wght@600;700&display=swap');

:root {
  --bronze: #b8833e;
  --bronze-hover: #cf9a51;
  --bronze-soft: rgba(184, 131, 62, 0.16);
  --teal: #3e7c78;

  --background: #101716;
  --surface: #17211f;
  --surface-secondary: #1d2926;
  --surface-elevated: #25322f;

  --text: #f4f1ea;
  --muted: #a7b2ad;
  --border: rgba(220, 232, 226, 0.10);
  --border-strong: rgba(220, 232, 226, 0.18);
  --shadow: 0 18px 50px rgba(0, 0, 0, 0.28);
}

body:not(.dark) {
  --background: #f4f2ed;
  --surface: #ffffff;
  --surface-secondary: #f8f7f3;
  --surface-elevated: #f0f2ed;

  --text: #1c2926;
  --muted: #61706a;
  --border: rgba(35, 50, 45, 0.10);
  --border-strong: rgba(35, 50, 45, 0.17);
  --shadow: 0 18px 50px rgba(26, 40, 35, 0.10);
}

footer,
.built-with,
.show-api,
.api-docs {
  display: none !important;
}

html,
body,
gradio-app {
  min-height: 100vh;
  background: var(--background) !important;
}

body::before {
  content: "";
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  background:
    radial-gradient(ellipse 70% 45% at 50% -10%, rgba(184, 131, 62, 0.12), transparent 62%),
    radial-gradient(ellipse 45% 35% at 100% 5%, rgba(62, 124, 120, 0.08), transparent 60%);
}

#twin-app {
  position: relative;
  z-index: 1;
  max-width: 1060px !important;
  margin: 0 auto !important;
  padding: 54px 32px 68px !important;
  color: var(--text) !important;
  font-family: "DM Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
}

#twin-title h1 {
  margin: 0 0 20px !important;
  color: var(--text) !important;
  font-family: "Playfair Display", Georgia, serif !important;
  font-size: clamp(2rem, 4vw, 2.65rem) !important;
  font-weight: 700 !important;
  letter-spacing: -0.035em !important;
  line-height: 1.15 !important;
  text-align: center !important;
}

#twin-title h1::after {
  content: "";
  display: block;
  width: 42px;
  height: 3px;
  margin: 17px auto 0;
  border-radius: 99px;
  background: var(--bronze);
}

/* Centered introduction box */
#career-intro {
  max-width: 720px !important;
  margin: 0 auto 28px !important;
  padding: 20px 28px !important;
  color: var(--text) !important;
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-left: 3px solid var(--bronze) !important;
  border-radius: 14px !important;
  box-shadow: var(--shadow) !important;
  text-align: center !important;
}

#career-intro p {
  margin: 0 !important;
  color: var(--text) !important;
  font-size: 1rem !important;
  font-weight: 500 !important;
  line-height: 1.7 !important;
  text-align: center !important;
}

#twin-app .main {
  position: relative;
  overflow: hidden;
  padding: 30px !important;
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: 20px !important;
  box-shadow: var(--shadow) !important;
}

#twin-app .main::before {
  content: "";
  position: absolute;
  top: 0;
  right: 30px;
  left: 30px;
  height: 2px;
  border-radius: 99px;
  background: linear-gradient(
    90deg,
    transparent,
    var(--bronze),
    var(--teal),
    transparent
  );
}

.block,
.form {
  background: transparent !important;
  box-shadow: none !important;
}

.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container {
  display: none !important;
}

.chatbot,
.chatbot.block {
  min-height: 500px !important;
  overflow: hidden !important;
  background: var(--surface-secondary) !important;
  border: 1px solid var(--border) !important;
  border-radius: 14px !important;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.035) !important;
}

.message-row,
.message-row > div,
.message-row .role,
.message-wrap,
.bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  max-width: 86% !important;
  padding: 14px 18px !important;
  border: 1px solid transparent !important;
  border-radius: 14px !important;
  box-shadow: none !important;
  animation: message-in 0.28s ease-out both;
}

@keyframes message-in {
  from {
    opacity: 0;
    transform: translateY(5px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble,
.message-row[data-role="user"] .bubble {
  color: #ffffff !important;
  background: linear-gradient(135deg, #3e7c78, #326965) !important;
  border-radius: 14px 14px 5px 14px !important;
}

.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble,
.message-row[data-role="assistant"] .bubble {
  color: var(--text) !important;
  background: var(--surface-elevated) !important;
  border-color: var(--border) !important;
  border-left: 3px solid var(--bronze) !important;
  border-radius: 14px 14px 14px 5px !important;
}

.message-row .message,
.message-row .message-bubble,
.message-row .bubble,
.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p {
  color: inherit !important;
  font-size: 0.94rem !important;
  line-height: 1.7 !important;
}

.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p {
  margin: 0 0 10px !important;
}

.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child {
  margin-bottom: 0 !important;
}

.message-row .message a,
.message-row .message-bubble a,
.message-row .bubble a {
  color: var(--bronze) !important;
  font-weight: 600 !important;
  text-decoration: underline;
  text-underline-offset: 3px;
}

.input-row,
.gr-input-row,
.chat-input-row,
form[class*="input"] {
  align-items: stretch !important;
  gap: 12px !important;
  margin-top: 12px !important;
}

textarea,
input[type="text"] {
  min-height: 56px !important;
  padding: 15px 18px !important;
  color: var(--text) !important;
  background: var(--surface-elevated) !important;
  border: 1px solid var(--border-strong) !important;
  border-radius: 14px !important;
  font-family: "DM Sans", sans-serif !important;
  font-size: 1rem !important;
  line-height: 1.5 !important;
}

textarea:focus,
input[type="text"]:focus {
  outline: none !important;
  border-color: var(--bronze) !important;
  box-shadow: 0 0 0 4px var(--bronze-soft) !important;
}

textarea::placeholder,
input::placeholder {
  color: var(--muted) !important;
}

/* Centered suggested-question box */
.examples,
.examples-holder,
[data-testid="examples"] {
  display: block !important;
  max-width: 850px !important;
  margin: 28px auto 0 !important;
  padding: 22px !important;
  background: var(--surface-secondary) !important;
  border: 1px solid var(--border) !important;
  border-radius: 14px !important;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.03) !important;
}

.examples::before,
.examples-holder::before,
[data-testid="examples"]::before {
  content: "Suggested questions";
  display: block;
  margin-bottom: 16px !important;
  color: var(--muted) !important;
  font-size: 0.72rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.1em !important;
  text-align: center !important;
  text-transform: uppercase !important;
}

/* Professional two-column question layout */
.examples table,
.examples-table {
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  gap: 12px !important;
  width: 100% !important;
  background: transparent !important;
  border: 0 !important;
}

.examples tr,
.examples td {
  display: contents !important;
  background: transparent !important;
  border: 0 !important;
}

.examples button,
.example,
.examples td button,
[data-testid="examples"] button {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 100% !important;
  min-height: 64px !important;
  padding: 14px 18px !important;
  color: var(--text) !important;
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: 10px !important;
  font-family: "DM Sans", sans-serif !important;
  font-size: 0.88rem !important;
  font-weight: 500 !important;
  letter-spacing: 0 !important;
  line-height: 1.45 !important;
  text-align: center !important;
  text-transform: none !important;
  transition: transform 0.2s ease, border-color 0.2s ease, color 0.2s ease !important;
}

.examples button:hover,
.example:hover,
[data-testid="examples"] button:hover {
  color: var(--teal) !important;
  background: var(--surface-elevated) !important;
  border-color: var(--teal) !important;
  transform: translateY(-1px);
}

button {
  border-radius: 14px !important;
}

button.primary,
button[variant="primary"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary {
  color: #1b1812 !important;
  background: var(--bronze) !important;
  border-color: var(--bronze) !important;
  box-shadow: 0 5px 14px rgba(184, 131, 62, 0.22) !important;
}

button.primary:hover,
button[variant="primary"]:hover,
button.submit:hover,
button.submit-button:hover,
.submit-button:hover,
button.lg.primary:hover {
  color: #1b1812 !important;
  background: var(--bronze-hover) !important;
  border-color: var(--bronze-hover) !important;
}

::-webkit-scrollbar {
  width: 9px;
  height: 9px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: var(--border-strong);
  border-radius: 99px;
}

@media (max-width: 720px) {
  #twin-app {
    padding: 34px 18px 48px !important;
  }

  #twin-app .main {
    padding: 20px 16px !important;
  }

  #career-intro {
    padding: 18px 20px !important;
  }

  .chatbot,
  .chatbot.block {
    min-height: 440px !important;
  }

  .examples,
  .examples-holder,
  [data-testid="examples"] {
    padding: 18px !important;
  }

  .examples table,
  .examples-table {
    grid-template-columns: 1fr !important;
  }

  .message-row .message,
  .message-row .message-bubble,
  .message-row .bubble {
    max-width: 92% !important;
  }
}
"""

JS = """
() => {
  document.title = "Digital Twin — Career Assistant";

  const focusInput = () => {
    const inputs = document.querySelectorAll("textarea");

    if (inputs.length) {
      inputs[inputs.length - 1].focus();
    }
  };

  setTimeout(focusInput, 300);
}
"""