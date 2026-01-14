---
name: agent-architect
description: Deep expertise in designing, building, and orchestrating AI agents using the project's custom Runner and Agent classes.
---

# Agent Architect Skill

This skill defines the structural and intellectual standards for building autonomous agents within this platform. Use this skill whenever adding new agent capabilities.

## 🏗️ Structural Standards

### 1. Domain Separation
Every new agent domain must live in `backend/app/agents/[domain]/` and contain:
- `__init__.py`: Package initialization.
- `tools.py`: Specialized `@function_tool` definitions.
- `squad.py` or `personas.py`: `Agent` definitions using `backend.app.core.config.default_model`.
- `flow.py`: Orchestration logic using `async asyncio.run_flow(...)` and `Runner.run()`.

### 2. Structured Planning
Always use Pydantic models with the `output_type` parameter for "Planner" agents. This ensures the output is a valid object rather than raw text.

## 🧠 Brain Design (Prompt Engineering)

### 1. Frameworks
Do not use generic tone descriptions. Use proven frameworks:
- **Sales:** Use **PAS** (Problem-Agitation-Solution) or **AIDA** (Attention-Interest-Desire-Action).
- **Executive:** Use **BLUF** (Bottom Line Up Front).
- **Research:** Use the **Executive Summary -> Deep Dive -> Citations** structure.

### 2. Personas
When creating multiple personas for a single task, use the **Factory Pattern** in `personas.py` to keep the code DRY (Don't Repeat Yourself).

## 📡 Flow Orchestration
- Use `asyncio.gather()` for parallel tool calling or search tasks.
- The `Sales Manager` pattern (Generate -> Evaluate -> Quality Control) is the standard for high-stakes outputs (emails, contracts).
- Always include a "Live Process" log entry for every major step.

## 🛠️ Tool Usage
- Tools should be stateless.
- Never hardcode recipients or sensitive data in tools; always pass them as arguments.
- Document every tool with a clear docstring so the AI understands its purpose.

## 📚 Reference Materials
- See `backend/app/agents/research/flow.py` for parallel searching examples.
- See `backend/app/agents/sales/personas.py` for agent factory examples.
