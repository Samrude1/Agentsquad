from agents import Agent
from backend.app.core.config import default_model
from backend.app.agents.sales.tools import send_email, send_html_email

# --- CONFIG ---
PERSONAS = [
    ("Professional", "professional, serious"),
    ("Engaging", "humorous, engaging"),
    ("Busy", "busy, concise"),
]

# --- AGENT FACTORY ---
sales_agents_tools = []
for name, tone in PERSONAS:
    agent = Agent(
        name=f"{name} Sales Agent",
        instructions=f"You are a {tone} sales agent. You write high-converting cold outreach emails. ALWAYS use the provided prospect name for the greeting and sign off with the provided sender name. DO NOT use placeholders like [Your Name] or [Firm Name].",
        model=default_model
    )
    # Create tool dynamically
    tool = agent.as_tool(
        tool_name=f"sales_agent_{name.lower()}",
        tool_description=f"Write a {name.lower()} sales email"
    )
    sales_agents_tools.append(tool)

# --- HELPER AGENTS ---
subject_writer = Agent(
    name="Email subject writer",
    instructions="You write catchy, high-conversion subject lines for cold sales emails based on the provided body text.",
    model=default_model
)

html_converter = Agent(
    name="HTML email body converter",
    instructions="You convert plain text email bodies into clean, professional HTML emails with logical layout and simple design.",
    model=default_model
)

# --- COORDINATORS ---
emailer_agent = Agent(
    name="Email Manager",
    instructions="Format the email (subject + HTML) then send it using send_html_email.",
    tools=[
        subject_writer.as_tool(tool_name="subject_writer", tool_description="Write a subject line"),
        html_converter.as_tool(tool_name="html_converter", tool_description="Convert to HTML"),
        send_html_email
    ],
    model=default_model,
    handoff_description="Format and send a final sales email"
)

sales_manager = Agent(
    name="Sales Manager",
    instructions="""You are an expert Sales Manager.
1. Generate Drafts: Use all 3 sales agent tools to generate drafts for the user's product/service.
2. Evaluate: Choose the single best email. Ensure it uses the correct prospect and sender names provided in the query and contains NO placeholders like [Name].
3. Handoff: Pass ONLY the winning draft to the 'Email Manager'.""",
    tools=sales_agents_tools,
    handoffs=[emailer_agent],
    model=default_model,
)
