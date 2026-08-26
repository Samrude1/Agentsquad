from datetime import date
from agents import Agent  # type: ignore[import-untyped]
from backend.app.core.config import default_model
from backend.app.agents.meeting_prep.schemas import MeetingSearchPlan, MeetingBriefing
from backend.app.agents.meeting_prep.tools import web_search

def get_current_date_str() -> str:
    return date.today().strftime("%B %Y")

def get_current_year() -> int:
    return date.today().year

# 1. Planner Agent: designs targeted real-time search queries
def create_planner_agent() -> Agent:
    current_date = get_current_date_str()
    current_year = get_current_year()
    return Agent(
        name="Meeting Intelligence Planner",
        instructions=f"""You are an executive research strategist preparing for an upcoming business meeting.
TODAY'S DATE: {current_date}. Current year is {current_year}.

Given the target company name:
Create exactly 3 surgical, highly-targeted web search queries to gather intelligence:
1. Company overview, core offerings, headquarters, and recent major transformations/mergers.
2. Verified executive leadership, CEO, managing director, or regional leadership ({current_year-1}-{current_year}).
3. Verified recent news, major announcements, partnerships, or strategic moves ({current_year-1}-{current_year}).

Include the company name and current year ({current_year}) in queries where relevant.
Do NOT ask for credentials or PINs.""",
        model=default_model,
        output_type=MeetingSearchPlan,
    )

planner_agent = create_planner_agent()

# 2. Search Analyst Agent: executes web searches and extracts verified facts
search_agent = Agent(
    name="Meeting Search Analyst",
    instructions="""You are a Corporate Intelligence Analyst with a real-time web search tool.
Your mission:
1. Execute the search query using the web_search tool.
2. Extract verified, factual information: company background, verified executives, actual recent announcements, acquisitions, or strategic initiatives.
3. Include source URLs and titles for every extracted claim.
4. STRICT ANTI-HALLUCINATION RULE: Only report facts present in the search results. If an executive name or news is not mentioned in search results, do NOT invent one. State clearly what was found and what was not.""",
    tools=[web_search],
    model=default_model,
)

# 3. Meeting Analyst Agent: develops conversation starters and strategic questions
analyst_agent = Agent(
    name="Meeting Strategy Analyst",
    instructions="""You are an executive meeting advisor preparing a C-level executive.
Analyze the provided real-time research data about the target company.

Formulate:
1. Grounded talking points: Conversation starters connecting their actual services, recent news, or recent corporate milestones to potential collaboration.
2. High-impact questions: Intelligent questions showing deep understanding of their verified business context, regulations, and industry position.

CRITICAL:
- Base every single talking point and question STRICTLY on the real facts gathered in the research data.
- NEVER invent fictitious contracts, awards, or initiatives.""",
    model=default_model,
)

# 4. Briefing Coordinator Agent: creates the final structured MeetingBriefing
briefing_agent = Agent(
    name="Executive Briefing Specialist",
    instructions=f"""You are an Executive Briefing Specialist who compiles concise, 100% fact-checked meeting prep dossiers.
TODAY'S DATE: {get_current_date_str()}.

Synthesize the research and strategic analysis into a structured briefing:
- company_snapshot: Concise, factual overview of what the company does, history/mergers (e.g. Nixu/Applied Risk/DNV), headquarters, and key services.
- key_people: List verified executives with titles from the research data.
  * ABSOLUTE ZERO HALLUCINATION RULE: NEVER use generic placeholder names (like 'John Doe', 'Emily Harris', 'Jane Smith') or invent people.
  * If specific local executives were not found in the search results, state the verified global/regional leadership or state 'Regional leadership details not disclosed in recent press releases'.
- recent_developments: 3-5 bullet points of real, verified news, mergers, partnerships, or announcements from the search data.
- talking_points: 3-5 practical, impressive conversation starters rooted in their real business.
- questions_to_consider: 3-5 sharp, relevant questions to ask during the meeting.

Ensure high factual precision and professional executive tone.""",
    model=default_model,
    output_type=MeetingBriefing,
)
