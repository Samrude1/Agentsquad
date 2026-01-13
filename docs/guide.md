# Project Blueprint: Smart Outreach Manager

## 🎯 Goal
Transform individual monolithic agent scripts (`manager.py`, `deepresearcher.py`) into a **modular, scalable, and professional** AI backend. This project serves as the engine for a generic "Agent Tools" platform.

## 🏗️ Architecture Philosophy
Incorporating lessons from `example_deep_research` and the `soloproject` workflow, we will adopt a **Task-Based Modular Architecture**.

**Core Principles:**
1.  **Single Responsibility:** Agents, Tools, and Workflows (Orchestrators) are separate files.
2.  **Shared Foundation:** Configuration, LLM setup, and Logging live in a `core/` module.
3.  **Domain Isolation:** Sales logic and Research logic live in their own packages.
4.  **Simplicity:** No over-engineering. Flat folder structures where possible.

---

## 📂 Proposed File Structure

We will restructure the root directory to separate the application logic from project metadata.

```text
Agent_tools/
├── backend/                # Mental Model: The "Brain"
│   ├── app/
│   │   ├── core/           # Shared utilities
│   │   │   ├── config.py   # Env vars, Gemini setup, Tracing disable
│   │   │   └── utils.py    # Common helpers
│   │   ├── agents/         # The "Actors"
│   │   │   ├── sales/      # Domain: Sales Outreach
│   │   │   │   ├── flow.py     # (Was manager.py) The Orchestrator
│   │   │   │   ├── personas.py # The 3 Agent definitions (Pro/Fun/Busy)
│   │   │   │   └── tools.py    # SendGrid & specialized tools
│   │   │   └── research/   # Domain: Deep Research
│   │   │   │   ├── flow.py     # (Was deepresearcher.py) The Orchestrator
│   │   │   │   ├── squad.py    # Planner, Search, Writer Agents
│   │   │   │   └── tools.py    # Tavily Search tools
│   │   └── main.py         # Application Entry Point (FastAPI or CLI)
├── frontend/               # Mental Model: The "Face" (Future)
├── .env                    # Secrets (API Keys)
├── requirements.txt        # Python Dependencies
└── guide.md                # This Blueprint
```

---

## � Refactoring Analysis

### 1. `manager.py` (Sales Agent) -> `agents/sales/`
**Current Status:** Monolithic. Mixes config, tool definitions, agent definitions, and execution flow.
**Action Plan:**
- **Extract Config:** Move `os.environ` and `trace` settings to `core/config.py`.
- **Extract Tools:** Move `send_email` and `send_html_email` to `agents/sales/tools.py`.
- **Extract Agents:** Move `sales_agent1/2/3`, `subject_writer`, `html_converter` to `agents/sales/personas.py`.
- **Clean Flow:** Keep only the `run_sales_flow` logic in `agents/sales/flow.py`.

### 2. `deepresearcher.py` (Research Agent) -> `agents/research/`
**Current Status:** Monolithic. Similar mix of responsibilities.
**Action Plan:**
- **Extract Tools:** Move `web_search` (Tavily) to `agents/research/tools.py`.
- **Extract Agents:** Move `planner_agent`, `search_agent`, `writer_agent` to `agents/research/squad.py`.
- **Clean Flow:** Keep `run_deep_research` in `agents/research/flow.py`.
- **Fix Reporting:** Separate the Markdown/HTML file writing logic into a utility or keep it as the final step of the flow.

---

## 🚀 Workflow Guide (Solo Project)

### Phase 0: Environment Setup (CRITICAL FIRST STEP)
1.  **Create Virtual Environment:**
    ```bash
    python -m venv .venv
    ```
2.  **Activate Environment:**
    *   Windows: `.\.venv\Scripts\activate`
    *   Mac/Linux: `source .venv/bin/activate`
3.  **Install Dependencies:**
    ```bash
    pip install -r backend/requirements.txt
    ```
4.  **Configure Environment:**
    *   Copy `.env.example` to `.env`
    *   Add your API keys (Gemini, Tavily, SendGrid)

### Phase 1: Restructuring (Immediate)
1.  **Create Folders:** Set up `backend/app/core`, `backend/app/agents/sales`, `backend/app/agents/research`.
2.  **Centralize Config:** Create `core/config.py` to handle `AsyncOpenAI` client creation and generic Model settings.
3.  **Slice & Dice:** Refactor `manager.py` and `deepresearcher.py` into their respective domains.

### Phase 2: Unification
1.  **Unified Entry:** Create `backend/app/main.py`.
2.  **API wrapper:** Use FastAPI to expose `run_sales_flow` and `run_deep_research` as endpoints.

### Phase 3: Frontend (React + Vite) ✅ COMPLETE
1.  Initialize `frontend/` using Vite.
2.  Build simple UI to trigger the API endpoints.
3.  **Status**: Fully implemented with TailwindCSS styling and tab-based navigation.

---

## 🎉 Project Status

**Current State**: Production-ready full-stack application
- ✅ Backend: Modular agent architecture with FastAPI
- ✅ Frontend: React + Vite with modern UI
- ✅ Documentation: Complete README and guides
- ✅ Optimization: Minimalist, Pythonic code

**Next Steps** (Optional):
- Add unit tests for agent flows
- Implement user authentication
- Deploy to production (Vercel + Render)

---

## 🛠️ Code Standards (Compact & Easy Config)

**1. Compact Agent Definitions**
Don't copy-paste `instructions`. Use string templates or a simpler configuration object if they share similarities.

**Example (Better):**
```python
# agents/sales/personas.py
def create_sales_agent(name, tone_instruction):
    return Agent(
        name=name,
        instructions=f"You are a {tone_instruction} sales agent...",
        model=default_model
    )
```

**2. Easy Usage**
Usage should look like this:
```python
from backend.app.agents.sales.flow import run_sales_flow

# One line execution
result = await run_sales_flow(prospect="Acme Corp", sender="Sam")
```

---

## ✅ Checklist for Agent Developer

- [ ] **Config:** Is `OPENAI_API_KEY` loaded once in `core`?
- [ ] **Tracing:** Is the annoying telemetry disabled centrally?
- [ ] **Imports:** Are we using relative imports or absolute imports consistently?
- [ ] **Structure:** Does every file have *one* clear purpose?
