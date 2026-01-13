import asyncio
from agents import Runner
from backend.app.agents.research.squad import planner_agent, search_agent, writer_agent
from backend.app.core.utils import save_markdown_report, convert_to_html

async def run_deep_research(topic: str):
    print(f"\n=== TUTKIMUS: {topic} ===\n")

    # 1. PLAN
    print(">> Suunnitellaan...")
    plan = (await Runner.run(planner_agent, f"Topic: {topic}")).final_output

    # 2. SEARHC (Parallel)
    print(">> Haetaan tietoa...")
    search_tasks = [Runner.run(search_agent, f"Search: {item.query}") for item in plan.searches]
    results = await asyncio.gather(*search_tasks)
    
    # Combine results
    combined_summaries = "\n\n".join([r.final_output for r in results])

    # 3. WRITE
    print(">> Kirjoitetaan raporttia...")
    final_report = (await Runner.run(writer_agent, f"Topic: {topic}\n\nData:\n{combined_summaries}")).final_output

    print("\n=== VALMIS ===\n")
    
    # Save
    if md_file := save_markdown_report(final_report, topic):
        convert_to_html(final_report, topic, md_file)

    return final_report

if __name__ == "__main__":
    from backend.app.core.config import setup_environment
    asyncio.run(run_deep_research("AI agents 2026"))
