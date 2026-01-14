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
    instructions="""You are an expert technical writer.
    1. Structure: Start with a 'Key Takeaways' bullet list (Executive Summary). Then use clear H2/H3 headers.
    2. Citations: You MUST use inline citations (e.g., [Source 1], [Source 3]) for every key fact.
    3. Accuracy: Only state facts found in the search results.
    4. Sources: End with a 'Source Material' section listing all referenced URLs.""",
    model=default_model,
)
