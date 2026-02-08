"""Pydantic schemas for structured output in Meeting Prep agent."""

from pydantic import BaseModel, Field
from typing import List
from datetime import date


class MeetingBriefing(BaseModel):
    """Structured output for meeting preparation briefings."""
    
    company_snapshot: str = Field(
        description="Brief overview of the company: what they do, size, headquarters"
    )
    key_people: List[str] = Field(
        description="List of key executives with their titles (e.g., 'John Doe - CEO')"
    )
    recent_developments: List[str] = Field(
        description="3-5 bullet points of recent news and developments"
    )
    talking_points: List[str] = Field(
        description="3-5 conversation starters for the meeting"
    )
    questions_to_consider: List[str] = Field(
        description="3-5 smart questions to ask in the meeting"
    )
    
    def to_markdown(self, company_name: str = "") -> str:
        """Convert the structured output to markdown format."""
        lines = []
        
        # Header with date
        today = date.today().strftime("%B %d, %Y")
        if company_name:
            lines.append(f"# Meeting Prep: {company_name}")
        lines.append(f"*Report generated: {today}*")
        lines.append("")
        
        lines.append("## Company Snapshot")
        lines.append(self.company_snapshot)
        lines.append("")
        
        lines.append("## Key People")
        for person in self.key_people:
            lines.append(f"- {person}")
        lines.append("")
        
        lines.append("## Recent Developments")
        for development in self.recent_developments:
            lines.append(f"- {development}")
        lines.append("")
        
        lines.append("## Talking Points")
        for point in self.talking_points:
            lines.append(f"- {point}")
        lines.append("")
        
        lines.append("## Questions to Consider")
        for question in self.questions_to_consider:
            lines.append(f"- {question}")
        
        return "\n".join(lines)
