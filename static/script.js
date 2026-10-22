const views = {
  chat: document.getElementById("chatView"),
  project: document.getElementById("projectView"),
  metrics: document.getElementById("metricsView"),
  implementation: document.getElementById("implementationView")
};

const titles = {
  chat: "AI Assistant",
  project: "Project Overview",
  metrics: "Metrics & Testing",
  implementation: "Implementation"
};

function showSection(name) {
  Object.entries(views).forEach(([key, view]) => {
    view.classList.toggle("active", key === name);
  });
  document.querySelectorAll(".nav-item").forEach(button => {
    button.classList.toggle("active", button.dataset.section === name);
  });
  document.getElementById("pageTitle").textContent = titles[name] || "AI Assistant";
  if (name === "metrics") {
    loadMetrics();
  }
}

document.querySelectorAll(".nav-item").forEach(button => {
  button.addEventListener("click", () => showSection(button.dataset.section));
});

const form = document.getElementById("questionForm");
const input = document.getElementById("questionInput");
const messages = document.getElementById("messages");
const sendButton = document.getElementById("sendButton");

function addUserMessage(question) {
  const row = document.createElement("div");
  row.className = "user-message";
  const content = document.createElement("div");
  content.className = "message-content";
  const p = document.createElement("p");
  p.textContent = question;
  content.appendChild(p);
  const avatar = document.createElement("div");
  avatar.className = "avatar";
  avatar.textContent = "YOU";
  row.append(content, avatar);
  messages.appendChild(row);
  messages.scrollTop = messages.scrollHeight;
}

function addAssistantMessage(data) {
  const row = document.createElement("div");
  row.className = "assistant-message";
  const avatar = document.createElement("div");
  avatar.className = "avatar";
  avatar.textContent = "OS";
  const content = document.createElement("div");
  content.className = "message-content";
  const heading = document.createElement("strong");
  heading.textContent = "OSLabAI response";
  const p = document.createElement("p");
  p.innerHTML = DOMPurify.sanitize(
      marked.parse(data.answer || "")
  );
  const meta = document.createElement("div");
  meta.className = "message-meta";
  [
      `Source topic: ${data.topic}`,
      `Matching score: ${data.score}`,
      `Response time: ${Number(data.response_time_ms).toFixed(2)} ms`
  ].forEach((text) => {
      const item = document.createElement("span");
      item.textContent = text;
      meta.appendChild(item);
  });
  content.append(heading, p, meta);
  row.append(avatar, content);
  messages.appendChild(row);
  messages.scrollTop = messages.scrollHeight;
}

async function askQuestion(question) {
  addUserMessage(question);
  sendButton.disabled = true;
  const loadingRow = document.createElement("div");
  loadingRow.className = "assistant-message";
  loadingRow.id = "loadingRow";
  const loadingAvatar = document.createElement("div");
  loadingAvatar.className = "avatar";
  loadingAvatar.textContent = "OS";
  const loadingText = document.createElement("div");
  loadingText.className = "message-content loading";
  loadingText.textContent = "Searching the current knowledge base…";
  loadingRow.append(loadingAvatar, loadingText);
  messages.appendChild(loadingRow);
  messages.scrollTop = messages.scrollHeight;

  try {
    const response = await fetch("/ask", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({question})
    });
    const data = await response.json();
    document.getElementById("loadingRow")?.remove();
    addAssistantMessage(data);
  } catch (error) {
    document.getElementById("loadingRow")?.remove();
    addAssistantMessage({
      answer: "Could not reach the local Python server. Check that app.py is running and try again.",
      topic: "None",
      score: 0,
      response_time_ms: 0
    });
  } finally {
    sendButton.disabled = false;
    input.focus();
  }
}

form.addEventListener("submit", event => {
  event.preventDefault();
  const question = input.value.trim();
  if (!question) return;
  input.value = "";
  askQuestion(question);
});

document.querySelectorAll(".suggestion").forEach(button => {
  button.addEventListener("click", () => {
    showSection("chat");
    askQuestion(button.dataset.question);
  });
});

document.getElementById("newChat").addEventListener("click", () => {
  messages.innerHTML = `<div class="assistant-message"><div class="avatar">OS</div><div class="message-content"><strong>New conversation</strong><p>Ask a question about Operating Systems to get started.</p></div></div>`;
  showSection("chat");
  input.focus();
});
async function loadMetrics() {
    try {
        const response = await fetch("/metrics");

        if (!response.ok) {
            throw new Error("Failed to load metrics");
        }

        const data = await response.json();

        document.getElementById("metricPassages").textContent =
            data.knowledge_base_passages;

        document.getElementById("metricTotalQuestions").textContent =
            data.total_questions;

        document.getElementById("metricAnswered").textContent =
            data.answered_questions;

        document.getElementById("metricRejected").textContent =
            data.rejected_questions;

        document.getElementById("metricFailed").textContent =
            data.failed_requests;

        document.getElementById("metricResponseTime").textContent =
            `${data.average_response_time_ms} ms`;

    } catch (error) {
        console.error("Unable to update dashboard metrics:", error);
    }
}