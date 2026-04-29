import asyncio
from datetime import date
from agents import Runner
from backend.app.agents.research.squad import planner_agent, search_agent, writer_agent
from backend.app.core.utils import save_markdown_report, convert_to_html, agent_run_with_retry

async def run_deep_research(topic: str):
    print(f"\n=== TUTKIMUS: {topic} ===\n")

    # Step 1: PLANNER creates search strategy
    print(">> Agent 1: Research Planner creating strategy...")
    plan_result = await agent_run_with_retry(Runner, planner_agent, f"Topic: {topic}")
    plan = plan_result.final_output

    # Step 2: SEARCH ANALYSTS run in PARALLEL with staggered starts
    print(">> Agent 2: Search Analysts executing parallel searches...")
    
    async def staggered_search(query, index):
        # Stagger starts to avoid hitting 15 RPM limit instantly
        if index > 0:
            await asyncio.sleep(index * 3) 
        return await agent_run_with_retry(Runner, search_agent, f"Search and analyze: {query}")

    search_results = await asyncio.gather(*[
        staggered_search(item.query, i)
        for i, item in enumerate(plan.searches)
    ])

    
    # Combine all analyst findings
    combined_data = "\n\n---\n\n".join([
        f"SEARCH {i+1}: {item.query}\nFINDINGS:\n{result.final_output}"
        for i, (item, result) in enumerate(zip(plan.searches, search_results))
    ])

    # Step 3: WRITER synthesizes into final report
    print(">> Agent 3: Research Writer synthesizing report...")
    writer_result = await agent_run_with_retry(
        Runner,
        writer_agent, 
        f"Topic: {topic}\n\nResearch Data:\n{combined_data}"
    )
    final_report = writer_result.final_output



    # Add date header
    today = date.today().strftime("%B %d, %Y")
    final_report = f"# Research Report: {topic}\n*Report generated: {today}*\n\n{final_report}"

    print("\n=== VALMIS ===\n")
    
    # Local saving disabled for cloud deployment
    # if md_file := save_markdown_report(final_report, topic):
    #     convert_to_html(final_report, topic, md_file)

    return final_report

if __name__ == "__main__":
    from backend.app.core.config import setup_environment
    asyncio.run(run_deep_research("AI agents 2026"))
