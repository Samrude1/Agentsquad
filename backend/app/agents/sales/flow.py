import asyncio
from agents import Runner
from backend.app.agents.sales.personas import (
    persona_agents, sales_manager, subject_writer, html_formatter, EmailDraft
)

async def run_sales_flow(contact_name: str, company_name: str, sender_name: str, product_description: str, prospect_email: str):
    # Build recipient string for AI
    if contact_name:
        recipient = f"{contact_name} at {company_name}"
        greeting_hint = f"Use 'Dear {contact_name}'"
    else:
        recipient = company_name
        greeting_hint = f"Use 'To the team at {company_name}'"

    print(f"\n>> Myyntiprosessi: {recipient} ({prospect_email})...")
    
    query = f"""Write a sales email.
Product: {product_description}
Recipient: {recipient}
Sender: {sender_name}
GREETING: {greeting_hint}"""

    # Step 1: 3 Personas generate drafts in PARALLEL
    print(">> Step 1: 3 Personas generating competing drafts...")
    draft_results = await asyncio.gather(*[
        Runner.run(agent, query) for agent in persona_agents
    ])
    
    drafts_text = "\n\n---\n\n".join([
        f"DRAFT {i+1} ({agent.name}):\n{result.final_output}"
        for i, (agent, result) in enumerate(zip(persona_agents, draft_results))
    ])
    
    # Step 2: Sales Manager evaluates and picks best
    print(">> Step 2: Sales Manager evaluating drafts...")
    manager_result = await Runner.run(sales_manager, f"""
Recipient: {recipient}
Sender: {sender_name}

{drafts_text}

Pick the BEST draft and return it.""")
    
    winning_draft = manager_result.final_output
    
    # Step 3: Subject Writer creates subject line
    print(">> Step 3: Subject Specialist writing subject line...")
    subject_result = await Runner.run(subject_writer, f"""
Create a subject line for this email:

{winning_draft}

Product: {product_description}
Company: {company_name}""")
    
    subject_line = subject_result.final_output.strip().strip('"').strip("'")
    
    # Step 4: HTML Formatter converts to professional HTML
    print(">> Step 4: HTML Formatter styling email...")
    html_result = await Runner.run(html_formatter, f"""
Convert this email to clean HTML:

{winning_draft}""")
    
    html_body = html_result.final_output
    
    # Clean up any code fences the AI might have added
    html_body = html_body.replace("```html", "").replace("```", "")
    html_body = html_body.replace("'''html", "").replace("'''", "")
    html_body = html_body.replace("``", "").replace("''", "")
    html_body = html_body.strip()
    
    print(f">> Valmis: {recipient}")
    
    # Return structured EmailDraft
    return EmailDraft(
        to_email=prospect_email,
        subject=subject_line,
        html_body=html_body
    ).model_dump()

if __name__ == "__main__":
    from backend.app.core.config import setup_environment
    asyncio.run(run_sales_flow("", "Sony", "Sami", "AI gaming services", "test@test.com"))
