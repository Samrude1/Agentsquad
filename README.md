# AI Agent Platform

> **The next generation of autonomous workforce.** A professional-grade, full-stack platform for building, orchestrating, and visualizing intelligent AI agents.

## 🎬 Live Demo

![AI Agent Platform Demo](demo_assets/frontpage.gif)

*Watch the Research Agent in action: planning multi-stage strategies, executing parallel searches, and generating executive reports.*

---

## 🤖 Meet the Agents

### 📧 The Sales Intelligence Specialist
*Specialized in high-conversion outreach and relationship building.*

- **Strategic Personalization**: Operates with a "Zero-Placeholder" policy. Generates 100% finished emails using **PAS** and **AIDA** psychology frameworks.
- **Smart Recipient Handling**: Intelligently adapts greetings for both individual prospects ("Dear [Name]") and corporate entities ("To the team at [Company]").
- **Human-in-the-Loop**: Features a "Draft Mode" allowing users to preview, edit, or discard emails before they are sent.
- **Tone Adaptation**: Dynamically switches between **Professional**, **Engaging**, and **Busy** personas.

### 🔍 The Deep Research Architect
*A master researcher capable of synthesizing the entire web into actionable insights.*

- **Autonomous Planning**: Breaks down complex topics into multi-stage search strategies.
- **Parallel Intelligence**: Executes high-speed, multi-source searches simultaneously using the Tavily AI Search grid.
- **Executive Synthesis**: Processes 15+ sources into comprehensive reports with **inline citations** and **Executive Summaries**.
- **Organized Outputs**: Automatically generates unique, timestamped folders for every research project.

---

## 🧠 The Engine: Thinking & Governance

 Unlike "black box" AI wrappers, this platform features:
- **Live Process Stream**: Observe the agent's internal monologue and state transitions in real-time.
- **Custom Workflows**: Standardized `.agent/workflows/` for consistent code optimization and quality review.
- **AI Skills**: Project-specific "Permanent Memory" in `.agent/skills/` (e.g., `agent-architect`) that teaches the AI how to expand the platform.

---

# 🛠️ Technical Reference

## 🏗️ Architecture

```
Agent_tools/
├── backend/
│   ├── app/
│   │   ├── core/           # Shared config & dynamic model management
│   │   ├── agents/
│   │   │   ├── sales/      # Dynamic sales personas & orchestration
│   │   │   └── research/   # Deep research flows & search logic
│   │   ├── api.py          # Minimalist FastAPI endpoints
│   │   └── main.py         # Advanced CLI entry point
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/     # Modular React UI components
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
- **Backend**: `uvicorn backend.app.api:app --reload` (Runs on port 8000)
- **Frontend**: `npm run dev` (Runs on port 5173)

**Dev Mode (CLI):**
- `python -m backend.app.main`

## 🧪 Tech Stack

- **Backend**: Python 3.10+, FastAPI, OpenAI Agents SDK (Gemini 2.0 Flash)
- **Search Engine**: Tavily AI
- **Frontend**: React 18, Vite, Vanilla CSS (Modern Corporate UI)

## 🛠️ Development & Scalability

This platform is built for **extensibility**:
- **Modular Agents**: Add new "skills" by creating a new agent folder in `backend/app/agents/`.
- **Factory Pattern**: Agents are generated dynamically, allowing for hundreds of unique personas with minimal code.
- **Visual Logs**: The frontend automatically maps to agent lifecycle steps.

---

## 🤝 Contributing & License

Designed for demonstration and portfolio use. Licensed under MIT.
Built with ❤️ by Samrude1.
