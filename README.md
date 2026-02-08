# AI Agent Platform

> **The next generation of autonomous workforce.** A professional-grade, full-stack platform for building, orchestrating, and visualizing intelligent AI agents.

## 🎬 Live Demo

![AI Agent Platform Demo](assets/frontpage.gif)

*Watch the Research Agents in action: planning multi-stage strategies, executing parallel searches, and generating executive reports.*

---

## 🤖 Meet the Agents

### 📋 Meeting Prep AI (CrewAI)
*Prepare for important business meetings in minutes.*

| Agent | Role |
|-------|------|
| Company Intel Researcher | Gathers company overview, key executives, and recent news |
| Meeting Strategy Analyst | Identifies talking points and potential opportunities |
| Briefing Coordinator | Creates a 5-minute executive briefing |

**Key Features:**
- **Company Snapshot**: What they do, size, headquarters
- **Key People**: CEO and relevant executives to know
- **Talking Points**: Conversation starters based on recent news
- **Smart Questions**: Show you did your homework

### 📧 The Sales Intelligence Team (6 Agents)
*A collaborative team specialized in high-conversion outreach.*

| Agent | Role |
|-------|------|
| Professional Agent | PAS (Problem-Agitation-Solution) framework |
| Engaging Agent | AIDA (Attention-Interest-Desire-Action) framework |
| Busy Executive Agent | BLUF (Bottom Line Up Front) - under 75 words |
| Sales Manager | Evaluates all 3 drafts, picks the best |
| Subject Specialist | Crafts catchy line |
| HTML Formatter | Converts to professional HTML |

### 🔍 Deep Research Team (OpenAI SDK)
*A research squad for learning and exploration.*

| Agent | Role |
|-------|------|
| Research Planner | Breaks topic into 3 surgical search strategies |
| Search Analyst | Executes searches and analyzes results |
| Research Writer | Synthesizes findings with academic citations |

**Key Features:**
- **Parallel Intelligence**: 3 searches execute simultaneously
- **Professional Citations**: Numbered references linked to sources
- **Executive Reports**: Key Takeaways + deep dive sections

---

## 🧠 The Engine: Multi-Agent Orchestration

- **Platform for Teams**: A scalable architecture designed to host multiple diverse agent squads (CrewAI, Custom SDKs, etc.).
- **Secure Access**: Integrated PIN-gate protection for public demonstrations.
- **Rate Limiting**: Built-in API protection to prevent abuse while allowing thorough testing.
- **Reporting Engine**: Automatic conversion of agent findings into professional, styled HTML reports.

---

## 🎨 UI/UX Features

- **Fixed-Height Console**: Agent process logs displayed in a scrollable 400px window.
- **Dynamic Navigation**: Tab-based layout for seamless switching between agent teams.
- **Secure Login**: PIN-entry screen to gate access to the platform.

---

# 🛠️ Technical Reference

## 🏗️ Architecture

```
Agent_tools/
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   │   ├── sales/         # 6-agent sales pipeline
│   │   │   ├── research/      # 3-agent research squad
│   │   │   └── meeting_prep/  # CrewAI meeting intelligence
│   │   ├── middleware/        # Rate limiting & security
│   │   ├── core/              # Shared config & utilities
│   │   ├── api.py             # FastAPI Unified API
│   │   └── main.py            # CLI entry point
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/        # React UI components (Forms, Log, Login)
    │   ├── utils/             # Error handling & helpers
    │   └── App.jsx            # Platform orchestrator
    └── package.json
```

## 🚀 Quick Start & Browser Usage

### 1. Prerequisites & Setup

> [!IMPORTANT]
> **Python Version**: Use **Python 3.12 or 3.13**. CrewAI is currently incompatible with 3.14.

1. **Clone and navigate**
```bash
git clone https://github.com/Samrude1/Agentsquad.git
cd Agent_tools
```

2. **Backend Setup**
```bash
python -m venv .venv
.\.venv\Scripts\activate  # Windows
pip install -r backend/requirements.txt
cp .env.example .env      # Add your API keys and APP_PIN here
```

3. **Frontend Setup**
```bash
cd frontend
npm install
```

### 2. Starting the Platform in Browser

To run the platform and access it via your web browser, follow these steps in two separate terminals:

**Terminal 1: Start the Backend (API)**
```bash
# Ensure venv is activated
uvicorn backend.app.api:app --reload
```
*The API will run at `http://localhost:8000`*

**Terminal 2: Start the Frontend (UI)**
```bash
cd frontend
npm run dev
```
*The UI will run at `http://localhost:5173`*

**Accessing the App:**
1. Open your browser to **[http://localhost:5173](http://localhost:5173)**.
2. Enter the **PIN code** (default is `0000`, configured in your `.env` file).
3. Select an agent team from the top tabs and start creating!

> **💡 Quick Start Tip:** See [`RUNTHIS.md`](RUNTHIS.md) for a condensed startup guide.

## 🛡️ Security & Rate Limiting

The platform includes built-in protection for portfolio/demo deployments:

- **PIN Authentication**: Configurable via `APP_PIN` environment variable
- **Rate Limiting**: 
  - 5 agent requests per 15 minutes (per IP)
  - 10 agent requests per hour
  - 25 agent requests per day
  - Prevents API abuse while allowing thorough testing

**For deployment details**, see [`RATE_LIMITS.md`](RATE_LIMITS.md).

## 🧪 Tech Stack

- **Backend**: Python 3.12/3.13, FastAPI, CrewAI, OpenAI Agents SDK
- **LLM**: Gemini 2.5 Flash
- **Search Engine**: Tavily AI, DuckDuckGo
- **Frontend**: React 18, Vite, Vanilla CSS

---

## 🤝 Contributing & License

Designed for demonstration and portfolio use. Licensed under MIT.
Built with ❤️ by Samrude1.
