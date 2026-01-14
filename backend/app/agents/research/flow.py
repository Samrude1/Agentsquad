import asyncio
from agents import Runner
from backend.app.agents.research.squad import planner_agent, search_agent, writer_agent
from backend.app.core.utils import save_markdown_report, convert_to_html

async def run_deep_research(topic: str):
    print(f"\n=== TUTKIMUS: {topic} ===\n")

    # Step 1: PLANNER creates search strategy
    print(">> Agent 1: Research Planner creating strategy...")
    plan = (await Runner.run(planner_agent, f"Topic: {topic}")).final_output

    # Step 2: SEARCH ANALYSTS run in PARALLEL (3 instances of same agent)
    print(">> Agent 2: Search Analysts executing parallel searches...")
    search_results = await asyncio.gather(*[
        Runner.run(search_agent, f"Search and analyze: {item.query}")
        for item in plan.searches
    ])
    
    # Combine all analyst findings
    combined_data = "\n\n---\n\n".join([
        f"SEARCH {i+1}: {item.query}\nFINDINGS:\n{result.final_output}"
        for i, (item, result) in enumerate(zip(plan.searches, search_results))
    ])

    # Step 3: WRITER synthesizes into final report
    print(">> Agent 3: Research Writer synthesizing report...")
    final_report = (await Runner.run(
        writer_agent, 
        f"Topic: {topic}\n\nResearch Data:\n{combined_data}"
    )).final_output

    print("\n=== VALMIS ===\n")
    
    # Save to unique folder
    if md_file := save_markdown_report(final_report, topic):
        convert_to_html(final_report, topic, md_file)

    return final_report

if __name__ == "__main__":
    from backend.app.core.config import setup_environment
    asyncio.run(run_deep_research("AI agents 2026"))
