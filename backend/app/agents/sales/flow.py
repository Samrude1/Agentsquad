import asyncio
from agents import Runner
from backend.app.agents.sales.personas import sales_manager

async def run_sales_flow(prospect_name: str, sender_name: str, product_description: str, prospect_email: str):
    print(f"\n>> Myyntiprosessi: {prospect_name} ({prospect_email})...")
    
    query = f"Write a cold sales email for '{product_description}' addressed to '{prospect_name}' ({prospect_email}) from {sender_name}."
    result = await Runner.run(sales_manager, query)
    
    print(f">> Valmis: {prospect_name}\n")
    return result.final_output

if __name__ == "__main__":
    from backend.app.core.config import setup_environment
    asyncio.run(run_sales_flow("Dear CEO", "Alice"))
