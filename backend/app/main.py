import asyncio
import sys
from backend.app.core.config import setup_environment
from backend.app.agents.sales.flow import run_sales_flow
from backend.app.agents.research.flow import run_deep_research

async def main():
    print("Welcome to Smart Outreach Manager (Agent Tools)")
    print("1. Run Sales Agent (Email Draft)")
    print("2. Run Deep Research Agent")
    print("3. Exit")
    
    choice = input("Select an option (1/2/3): ")
    
    if choice == "1":
        prospect = input("Enter Prospect Name: ")
        sender = input("Enter Sender Name: ")
        await run_sales_flow(prospect, sender)
        
    elif choice == "2":
        topic = input("Enter Research Topic: ")
        await run_deep_research(topic)
        
    elif choice == "3":
        print("Exiting.")
        sys.exit(0)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    setup_environment()
    asyncio.run(main())
