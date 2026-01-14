# AI Agent Platform

> **The next generation of autonomous workforce.** A professional-grade, full-stack platform for building, orchestrating, and visualizing intelligent AI agents.

## 🎬 Live Demo

![AI Agent Platform Demo](demo_assets/frontpage.gif)

*Watch the Research Agent in action: planning multi-stage strategies, executing parallel searches, and generating executive reports.*

---

## 🤖 Meet the Agents

### 📧 The Sales Intelligence Team (6 Agents)
*A collaborative team specialized in high-conversion outreach.*

| Agent | Role |
|-------|------|
| Professional Agent | PAS (Problem-Agitation-Solution) framework |
| Engaging Agent | AIDA (Attention-Interest-Desire-Action) framework |
| Busy Executive Agent | BLUF (Bottom Line Up Front) - under 75 words |
| Sales Manager | Evaluates all 3 drafts, picks the best |
| Subject Specialist | Crafts catchy, high-conversion subject lines |
| HTML Formatter | Converts to clean, professional HTML |

**Key Features:**
- **Competitive Drafting**: 3 personas write competing emails, manager picks the winner
- **Smart Recipient Handling**: Adapts greetings for individuals ("Dear John") vs companies ("To the team at Sony")
- **Human-in-the-Loop**: Draft Mode lets you preview, edit, or discard before sending
- **Zero Placeholders**: 100% finished emails, every time

### 🔍 The Deep Research Team (3 Agents)
*A research squad capable of synthesizing the entire web into actionable insights.*

| Agent | Role |
|-------|------|
| Research Planner | Breaks topic into 3 surgical search strategies |
| Search Analyst | Executes searches + analyzes results (×3 parallel) |
| Research Writer | Synthesizes with citations and executive summary |

**Key Features:**
- **Parallel Intelligence**: 3 searches execute simultaneously via Tavily AI
- **Professional Citations**: Numbered references linked to named sources
- **Executive Reports**: Key Takeaways + deep dive sections
- **Organized Outputs**: Unique timestamped folders for each project

---

## 🧠 The Engine: Multi-Agent Orchestration

Unlike "black box" AI wrappers, this platform features:
- **Flow-Based Orchestration**: Agents run in parallel where possible, avoiding SDK turn limits
- **Live Process Stream**: Real-time visibility into agent collaboration
- **Custom Workflows**: Standardized `.agent/workflows/` for code quality
- **AI Skills**: Project knowledge stored in `.agent/skills/` for consistent expansion

---

# 🛠️ Technical Reference

## 🏗️ Architecture

```
Agent_tools/
├── backend/
│   ├── app/
│   │   ├── core/           # Shared config & model management
│   │   ├── agents/
│   │   │   ├── sales/      # 6-agent sales pipeline
│   │   │   └── research/   # 3-agent research squad
│   │   ├── api.py          # FastAPI endpoints (draft/send/research)
│   │   └── main.py         # CLI entry point
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/     # React UI components
    │   └── App.jsx         # Tab-based orchestrator
    └── package.json
```

## 🚀 Quick Start

### Setup

1. **Clone and navigate**
```bash
git clone https://github.com/Samrude1/Agentsquad.git
cd Agent_tools
```

2. **Backend Engine Setup**
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r backend/requirements.txt
cp .env.example .env  # Add your API keys here
```

3. **Frontend UI Setup**
```bash
cd frontend
npm install
```

### Running the Platform

**Production Mode (Web UI):**
- **Backend**: `uvicorn backend.app.api:app --reload` (Port 8000)
- **Frontend**: `npm run dev` (Port 5173)

**Dev Mode (CLI):**
- `python -m backend.app.main`

## 🧪 Tech Stack

- **Backend**: Python 3.10+, FastAPI, OpenAI Agents SDK (Gemini 2.0 Flash)
- **Search Engine**: Tavily AI
- **Email Delivery**: SendGrid
- **Frontend**: React 18, Vite, Vanilla CSS

## 🛠️ Development & Scalability

This platform is built for **extensibility**:
- **Modular Agents**: Add new capabilities in `backend/app/agents/`
- **Flow Orchestration**: `asyncio.gather()` for parallel agent execution
- **Visual Logs**: Frontend automatically maps to agent lifecycle steps

---

## 🤝 Contributing & License

Designed for demonstration and portfolio use. Licensed under MIT.
Built with ❤️ by Samrude1.
