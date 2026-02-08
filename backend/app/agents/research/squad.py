from typing import List
from datetime import date
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

# --- Helper to get current date ---
def get_current_date_str():
    return date.today().strftime("%B %Y")  # e.g., "February 2026"

def get_current_year():
    return date.today().year

# --- 3 RESEARCH AGENTS ---

# Agent 1: The Planner (with dynamic date)
def create_planner_agent():
    current_date = get_current_date_str()
    current_year = get_current_year()
    return Agent(
        name="Research Planner",
        instructions=f"""You are a Research Strategist.
TODAY'S DATE: {current_date}. Always search for CURRENT information.

Break down the topic into 3 surgical search queries.
Target technical terms, benchmarks, and recent developments from {current_year-1}-{current_year}.
IMPORTANT: Add "{current_year-1}" or "{current_year}" to queries when searching for current data.""",
        model=default_model,
        output_type=WebSearchPlan,
    )

# Keep backward compatibility
planner_agent = create_planner_agent()

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
1. [Source Name/Title] - Brief description (URL)
2. [Source Name/Title] - Brief description (URL)

EXAMPLE:
"AI adoption increased 40% in 2024 [1]..."

Sources:
1. McKinsey AI Report - 2024 Global Survey (https://mckinsey.com/...)
2. Gartner Analysis - Enterprise Trends (https://gartner.com/...)

RULES:
- Match citation numbers to source numbers
- Use the article TITLE as source name, not raw URL
- Keep URLs short if possible (main domain + path)
- Only state facts found in the provided data""",
    model=default_model,
)
