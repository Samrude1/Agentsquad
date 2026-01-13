from typing import List
from pydantic import BaseModel, Field
from agents import Agent, ModelSettings
from backend.app.core.config import default_model
from backend.app.agents.research.tools import web_search

# --- MODELS ---
class WebSearchItem(BaseModel):
    reason: str = Field(description="Why this specific search helps.")
    query: str = Field(description="The optimized search query.")

class WebSearchPlan(BaseModel):
    searches: List[WebSearchItem] = Field(description="3 optimized web searches.")

# --- AGENTS ---
planner_agent = Agent(
    name="PlannerAgent",
    instructions="You are a skilled Research Planner. Break down the topic into 3 surgical search queries. Target technical terms & benchmarks.",
    model=default_model,
    output_type=WebSearchPlan,
)

search_agent = Agent(
    name="Search agent",
    instructions="Review search results and isolate technical facts, library names, and version numbers.",
    tools=[web_search],
    model=default_model,
    model_settings=ModelSettings(tool_choice="required"),
)

writer_agent = Agent(
    name="WriterAgent",
    instructions="Write a 1000+ word deep-dive report in Markdown. Use professional technical language, headers (H1, H2), lists, and bold text.",
    model=default_model,
)
