import asyncio
from agents import Runner
from backend.app.agents.sales.personas import sales_manager

async def run_sales_flow(prospect_name: str, sender_name: str):
    print(f"\n>> Myyntiprosessi: {prospect_name}...")
    
    query = f"Send a cold sales email addressed to '{prospect_name}' from {sender_name}"
    result = await Runner.run(sales_manager, query)
    
    print(f">> Valmis: {prospect_name}\n")
    return result.final_output

if __name__ == "__main__":
    from backend.app.core.config import setup_environment
    asyncio.run(run_sales_flow("Dear CEO", "Alice"))
