"""Flow for Meeting Prep agent squad using OpenAI Agents SDK."""

import asyncio
from datetime import date
from agents import Runner  # type: ignore[import-untyped]
from backend.app.agents.meeting_prep.squad import (
    planner_agent,
    search_agent,
    analyst_agent,
    briefing_agent,
)
from backend.app.agents.meeting_prep.schemas import MeetingBriefing
from backend.app.core.utils import agent_run_with_retry, save_markdown_report, convert_to_html


async def run_meeting_prep(topic: str) -> str:
    """
    Run the Meeting Prep multi-agent workflow with real-time web search.
    
    Args:
        topic: Target company or organization name
        
    Returns:
        Markdown-formatted verified meeting briefing
    """
    print(f"\n=== MEETING PREP: {topic} ===\n")
    
    # Step 1: PLANNER creates 3 targeted search queries
    print(">> Agent 1: Meeting Intelligence Planner generating search strategy...")
    plan_result = await agent_run_with_retry(
        Runner, 
        planner_agent, 
        f"Target Company / Organization: {topic}"
    )
    plan = plan_result.final_output
    
    # Step 2: SEARCH ANALYSTS execute real-time searches in parallel
    print(f">> Agent 2: Search Analysts executing {len(plan.searches)} real-time searches...")
    
    async def staggered_search(query: str, index: int):
        if index > 0:
            await asyncio.sleep(index * 2)
        return await agent_run_with_retry(
            Runner, 
            search_agent, 
            f"Search and extract verified company intelligence for: {query}"
        )
    
    search_results = await asyncio.gather(*[
        staggered_search(item.query, i)
        for i, item in enumerate(plan.searches)
    ])
    
    combined_research = "\n\n---\n\n".join([
        f"SEARCH {i+1} ({item.reason}): {item.query}\nFINDINGS:\n{result.final_output}"
        for i, (item, result) in enumerate(zip(plan.searches, search_results))
    ])
    
    # Step 3: STRATEGY ANALYST formulates talking points & high-impact questions
    print(">> Agent 3: Meeting Strategy Analyst formulating talking points & questions...")
    strategy_result = await agent_run_with_retry(
        Runner,
        analyst_agent,
        f"Company: {topic}\n\nVerified Research Data:\n{combined_research}"
    )
    strategy_output = strategy_result.final_output
    
    # Step 4: BRIEFING SPECIALIST produces structured, 100% grounded briefing
    print(">> Agent 4: Executive Briefing Specialist compiling final dossier...")
    briefing_input = (
        f"Target Company: {topic}\n\n"
        f"Verified Research Findings:\n{combined_research}\n\n"
        f"Strategy & Questions:\n{strategy_output}"
    )
    
    briefing_result = await agent_run_with_retry(
        Runner,
        briefing_agent,
        briefing_input
    )
    
    final_data = briefing_result.final_output
    if isinstance(final_data, MeetingBriefing):
        clean_markdown = final_data.to_markdown(company_name=topic)
    else:
        # Fallback if raw text
        clean_markdown = str(final_data)
    
    # Step 5: Save report to Reports directory
    try:
        md_file = save_markdown_report(clean_markdown, f"Meeting_Prep_{topic}")
        convert_to_html(clean_markdown, f"Meeting Prep: {topic}", md_file)
    except Exception as save_err:
        print(f"[Meeting Prep] Note: Could not save report file locally: {save_err}")
        
    print("\n=== MEETING PREP COMPLETE ===\n")
    return clean_markdown


if __name__ == "__main__":
    from backend.app.core.config import setup_environment
    setup_environment()
    asyncio.run(run_meeting_prep("DNV cyber finland"))
