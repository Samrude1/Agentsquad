from agents import Agent
from backend.app.core.config import default_model
from backend.app.agents.sales.tools import send_email, return_draft

# --- CONFIG ---
PERSONAS = [
    # (Name, Tone_Description) -> Now includes framework instructions implicitly in prompt construction
    ("Professional", "Use the PAS (Problem-Agitation-Solution) framework. Identify a pain point, agitate it slightly, then offer the solution. Be strategic and advisory"),
    ("Engaging", "Use the AIDA (Attention-Interest-Desire-Action) framework. Use vivid analogies and storytelling elements. Be memorable and punchy"),
    ("Busy", "Use the BLUF (Bottom Line Up Front) method. STRICT CONSTRAINT: Must be under 75 words. No fluff greetings like 'Hope you are well'. Go straight to value"),
]

# --- AGENT FACTORY ---
sales_agents_tools = []
for name, tone in PERSONAS:
    agent = Agent(
        name=f"{name} Sales Agent",
        instructions=f"You are a {tone} sales agent writing high-converting emails. GREETING RULE: If the prospect name is a person, use 'Dear [Name]'. If it is a company (e.g., McDonald's), use 'To the team at [Company]' or 'Dear [Company] Management'. ALWAYS sign off with the provided sender name and ensure ZERO placeholders remain.",
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
    instructions="Format the email (subject + HTML). Then, look at the original user request to find the 'to_email' (prospect email). Finally, call return_draft(to_email, subject, html_body).",
    tools=[
        subject_writer.as_tool(tool_name="subject_writer", tool_description="Write a subject line"),
        html_converter.as_tool(tool_name="html_converter", tool_description="Convert to HTML"),
        return_draft
    ],
    model=default_model,
    handoff_description="Format and send a final sales email"
)

sales_manager = Agent(
    name="Sales Manager",
    instructions="""You are an expert Sales Manager.
1. Generate Drafts: Use all 3 sales agent tools to generate drafts for the user's product/service.
2. Evaluate: Choose the single best email based on the prospect's profile.
3. QUALITY CONTROL: Ensure the selected draft:
   - Uses the EXACT prospect name provided.
   - Signs off with the EXACT sender name provided.
   - Contains ZERO placeholders (like [Name], [Company]).
4. Handoff: Pass ONLY the final, polished draft to the 'Email Manager'.""",
    tools=sales_agents_tools,
    handoffs=[emailer_agent],
    model=default_model,
)
