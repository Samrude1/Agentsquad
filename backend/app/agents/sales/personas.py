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
STRICT RULES:
- NO LABELS like 'Problem:', 'Agitation:', or 'Solution:' in the output.
- NO PLACEHOLDERS like [Brand Name], [Link], or [Insert info]. 
- Use ONLY the info provided. If details are missing, write around them naturally.
GREETING: Use greeting hint provided.
SIGNATURE: Use 'Best regards, {sender_name}'.""",
    model=default_model
)

engaging_agent = Agent(
    name="Engaging Sales Agent", 
    instructions="""Write an engaging sales email using AIDA (Attention-Interest-Desire-Action).
STRICT RULES:
- NO LABELS like 'Attention:', 'Interest:', etc. in the output.
- NO PLACEHOLDERS like [Brand Name], [Link], or [Insert info]. 
- Use ONLY the info provided.
GREETING: Use greeting hint provided.
SIGNATURE: Use 'Best regards, {sender_name}'.""",
    model=default_model
)

busy_agent = Agent(
    name="Busy Executive Agent",
    instructions="""Write a concise email using BLUF (Bottom Line Up Front).
STRICT RULES:
- Under 75 words. No fluff. Go straight to value.
- NO labels like 'BLUF:' or 'Note:'.
- NO PLACEHOLDERS.
- Use ONLY the info provided.
GREETING: Use greeting hint provided.
SIGNATURE: Use 'Best regards, {sender_name}'.""",
    model=default_model
)

# --- MANAGER (Evaluator) ---
sales_manager = Agent(
    name="Sales Manager",
    instructions="""You are given 3 email drafts from different writers.

TASK: Evaluate all 3 and pick the SINGLE BEST one for the prospect.
OUTPUT: Return ONLY the winning email text. nothing else. No explanation, no reasoning, no "Reason:" section.""",
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
    instructions="""Convert the email text to high-end, professional HTML.
ESTHETIC GOAL: Clean, modern, "Fortune 500" tech style. 

RULES:
- Use a clean hierarchy with <p>, <strong>, and <ul>/<li> if relevant.
- Use minimal inline styles for professional spacing:
  - Paragraphs should have: style="line-height: 1.6; margin-bottom: 16px; font-family: sans-serif; color: #333;"
  - Strong text should have: style="color: #000;"
- Ensure the layout feels spacious and easy to read.
- DO NOT use amateurish colors or fonts. 
- DO NOT include markdown code fences (no ```html or ```).
- Preserve the original message exactly.
OUTPUT: Return ONLY the raw HTML body content.""",
    model=default_model
)

# Export for flow.py
persona_agents = [professional_agent, engaging_agent, busy_agent]
