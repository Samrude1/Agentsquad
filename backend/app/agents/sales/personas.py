from pydantic import BaseModel, Field
from agents import Agent
from backend.app.core.config import default_model

# --- MODELS ---
class EmailDraft(BaseModel):
    to_email: str = Field(description="The recipient email address")
    subject: str = Field(description="A catchy subject line")
    html_body: str = Field(description="Professional HTML email body")

# --- 3 COMPETING PERSONAS ---
professional_agent = Agent(
    name="Professional Sales Agent",
    instructions="""Write a professional sales email using PAS (Problem-Agitation-Solution).
GREETING: Use greeting hint provided. NO PLACEHOLDERS.
SIGNATURE: Sign with sender name.""",
    model=default_model
)

engaging_agent = Agent(
    name="Engaging Sales Agent", 
    instructions="""Write an engaging sales email using AIDA (Attention-Interest-Desire-Action).
Be memorable and punchy. Use vivid analogies.
GREETING: Use greeting hint provided. NO PLACEHOLDERS.
SIGNATURE: Sign with sender name.""",
    model=default_model
)

busy_agent = Agent(
    name="Busy Executive Agent",
    instructions="""Write a concise email using BLUF (Bottom Line Up Front).
STRICT: Under 75 words. No fluff. Go straight to value.
GREETING: Use greeting hint provided. NO PLACEHOLDERS.
SIGNATURE: Sign with sender name.""",
    model=default_model
)

# --- MANAGER (Evaluator) ---
sales_manager = Agent(
    name="Sales Manager",
    instructions="""You are given 3 email drafts from different writers.

TASK: Evaluate all 3 and pick the SINGLE BEST one for the prospect.
OUTPUT: Return ONLY the winning email text (body only, no subject).
Explain briefly why you chose it.""",
    model=default_model
)

# --- SPECIALIST AGENTS ---
subject_writer = Agent(
    name="Subject Line Specialist",
    instructions="""You write catchy, high-conversion email subject lines.
RULES:
- Under 50 characters
- Create curiosity or urgency
- No clickbait
OUTPUT: Return ONLY the subject line, nothing else.""",
    model=default_model
)

html_formatter = Agent(
    name="HTML Formatter",
    instructions="""Convert the email text to clean, professional HTML.
RULES:
- Use simple tags: <p>, <strong>, <br>
- No inline styles
- Keep it clean and readable
- Preserve the original content exactly
- DO NOT include markdown code fences (no \`\`\`html or \`\`\`)
OUTPUT: Return ONLY raw HTML tags, nothing else.""",
    model=default_model
)

# Export for flow.py
persona_agents = [professional_agent, engaging_agent, busy_agent]
