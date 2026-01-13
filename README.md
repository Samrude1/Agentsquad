# Smart Outreach Manager

A modern full-stack application for AI-powered sales outreach and deep research, built with Python agents and React.

## 🎯 Features

- **Sales Agent**: Generate personalized cold sales emails using AI
- **Research Agent**: Conduct deep research on any topic with automated web searches
- **Modern UI**: Clean React interface with real-time results
- **Modular Architecture**: Scalable backend with domain-separated agents

## 🏗️ Architecture

```
Agent_tools/
├── backend/
│   ├── app/
│   │   ├── core/           # Shared config & utilities
│   │   ├── agents/
│   │   │   ├── sales/      # Sales email generation
│   │   │   └── research/   # Deep research automation
│   │   ├── api.py          # FastAPI endpoints
│   │   └── main.py         # CLI interface
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/     # React components
    │   └── App.jsx
    └── package.json
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- API Keys: Gemini, Tavily, SendGrid

### Setup

1. **Clone and navigate to project**
```bash
cd Agent_tools
```

2. **Backend Setup**
```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.\.venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys
```

3. **Frontend Setup**
```bash
cd frontend
npm install
```

### Running the Application

**Option 1: Web Interface**

Terminal 1 (Backend):
```bash
.\.venv\Scripts\activate
uvicorn backend.app.api:app --reload
```

Terminal 2 (Frontend):
```bash
cd frontend
npm run dev
```

Visit: `http://localhost:5173`

**Option 2: CLI**
```bash
.\.venv\Scripts\activate
python -m backend.app.main
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_gemini_api_key
OPENAI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
TAVILY_API_KEY=your_tavily_api_key
SENDGRID_API_KEY=your_sendgrid_api_key
```

## 📚 Tech Stack

### Backend
- **Framework**: FastAPI
- **AI Agents**: OpenAI Agents SDK
- **LLM**: Google Gemini 2.0 Flash
- **Search**: Tavily API
- **Email**: SendGrid

### Frontend
- **Framework**: React 18
- **Build Tool**: Vite
- **Styling**: TailwindCSS
- **HTTP Client**: Axios

## 🧪 Usage Examples

### Sales Agent
Generates three different email drafts (professional, engaging, concise), selects the best one, and formats it as HTML before sending.

### Research Agent
1. Plans 3 optimized search queries
2. Executes searches in parallel using Tavily
3. Synthesizes results into a comprehensive markdown report
4. Saves both markdown and HTML versions

## 📖 Documentation

- [`docs/guide.md`](docs/guide.md) - Development guide and architecture
- [`docs/plans.md`](docs/plans.md) - Original project plans
- [`.env.example`](.env.example) - Environment configuration template

## 🛠️ Development

### Code Structure
- **Modular Agents**: Each agent domain (sales/research) is self-contained
- **Factory Pattern**: Dynamic agent generation reduces code duplication
- **Async-First**: Uses `asyncio.gather` for parallel operations
- **Type Safety**: Pydantic models for data validation

### Adding New Agents
1. Create new folder in `backend/app/agents/`
2. Define tools in `tools.py`
3. Define agents in `squad.py` or `personas.py`
4. Create flow orchestration in `flow.py`
5. Add API endpoint in `api.py`

## 📝 License

MIT

## 🤝 Contributing

This is a learning/portfolio project. Feel free to fork and adapt for your needs.
