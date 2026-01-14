from typing import List
from pydantic import BaseModel, Field
from agents import Agent
from backend.app.core.config import default_model
from backend.app.agents.research.tools import web_search

# --- MODELS ---
class WebSearchItem(BaseModel):
    reason: str = Field(description="Why this search helps.")
    query: str = Field(description="The optimized search query.")

class WebSearchPlan(BaseModel):
    searches: List[WebSearchItem] = Field(description="3 optimized web searches.")

# --- 3 RESEARCH AGENTS ---

# Agent 1: The Planner
planner_agent = Agent(
    name="Research Planner",
    instructions="""You are a Research Strategist.
Break down the topic into 3 surgical search queries.
Target technical terms, benchmarks, and recent developments.""",
    model=default_model,
    output_type=WebSearchPlan,
)

# Agent 2: The Search Analyst (runs multiple times in parallel)
search_agent = Agent(
    name="Search Analyst",
    instructions="""You are a Research Analyst with a web search tool.
1. Execute the search using web_search tool
2. Analyze the results
3. Extract key facts, statistics, and source URLs
4. Return a structured summary of findings""",
    tools=[web_search],
    model=default_model,
)

# Agent 3: The Writer
writer_agent = Agent(
    name="Research Writer",
    instructions="""You are an expert technical writer.

STRUCTURE:
1. Start with 'Key Takeaways' bullet list (Executive Summary)
2. Use clear H2/H3 headers for sections
3. Use numbered citations like [1], [2], [3] for key facts

SOURCE MATERIAL FORMAT (CRITICAL):
At the end, create a numbered list matching your citations:
1. Source Title or Description. <URL>
2. Source Title or Description. <URL>

RULES:
- Match citation numbers to source numbers.
- NO domain name in brackets at the start.
- Wrap the URL in < > brackets.
- Only state facts found in the provided data.""",
    model=default_model,
)
