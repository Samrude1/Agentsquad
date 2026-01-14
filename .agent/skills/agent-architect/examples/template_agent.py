from agents import Agent, Runner
from backend.app.core.config import default_model

# Standardized Template for a New Agent Domain

# 1. Define specific agents
agent_a = Agent(
    name="Specialist Agent",
    instructions="Focus on [Specific Task] using [Specific Framework].",
    model=default_model
)

# 2. Define the Manager (Quality Gate)
manager_agent = Agent(
    name="Domain Manager",
    instructions="""1. Coordinate: Use Specialist Agent to generate drafts.
2. Evaluate: Choose best version.
3. Quality Control: Remove placeholders and ensure [Specific Rule] is met.""",
    tools=[agent_a.as_tool()],
    model=default_model
)

# 3. Define the Flow
async def run_example_flow(input_data: str):
    # Log the step for the frontend ProcessLog
    print(">> Initializing [Domain] protocol...")
    
    query = f"Execute [Task] based on: {input_data}"
    result = await Runner.run(manager_agent, query)
    
    print(">> Task Complete.")
    return result.final_output
