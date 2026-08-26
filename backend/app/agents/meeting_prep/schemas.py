"""Pydantic schemas for structured output in Meeting Prep agent."""

from pydantic import BaseModel, Field
from typing import List
from datetime import date


class WebSearchItem(BaseModel):
    reason: str = Field(description="Why this search helps gather meeting intelligence.")
    query: str = Field(description="The surgical, focused search query.")


class MeetingSearchPlan(BaseModel):
    searches: List[WebSearchItem] = Field(
        description="3 targeted searches: 1) Company overview & business model, 2) Leadership/key people, 3) Recent news & milestones."
    )


class MeetingBriefing(BaseModel):
    """Structured output for meeting preparation briefings."""
    
    company_snapshot: str = Field(
        description="Factual overview of the company: what they do, market position, headquarters, and key services. ONLY verified facts."
    )
    key_people: List[str] = Field(
        description="List of verified key executives and leaders with their titles. If local or specific names are not verified in search results, state known organization structure or leadership without inventing names."
    )
    recent_developments: List[str] = Field(
        description="3-5 bullet points of verified recent news, mergers, partnerships, or strategic developments from the search data."
    )
    talking_points: List[str] = Field(
        description="3-5 insightful conversation starters for the meeting based strictly on their actual business and recent developments."
    )
    questions_to_consider: List[str] = Field(
        description="3-5 smart questions to ask in the meeting demonstrating deep knowledge of their actual business context."
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
        lines.append(self.company_snapshot.strip())
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
