"""Flow adapter for Meeting Prep CrewAI agent."""

import sys
import asyncio
from pathlib import Path
from datetime import date
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

# Add the meeting_prep src to path
current_dir = Path(__file__).parent
src_dir = current_dir / "src"
if str(src_dir) not in sys.path:
    sys.path.append(str(src_dir))

from meeting_prep.crew import MeetingPrepCrew
from meeting_prep.schemas import MeetingBriefing
from backend.app.core.utils import save_markdown_report, convert_to_html


async def run_meeting_prep(topic: str) -> str:
    """
    Run the Meeting Prep CrewAI workflow.
    
    Args:
        topic: Company name to prepare for
        
    Returns:
        Markdown-formatted meeting briefing
    """
    print(f"\n=== MEETING PREP: {topic} ===\n")
    
    # Dynamic date injection
    current_year = date.today().year
    inputs = {
        'topic': topic,
        'current_date': date.today().strftime("%B %Y"),  # e.g., "February 2026"
        'current_year': str(current_year),
        'last_year': str(current_year - 1),
    }

    try:
        crew_instance = MeetingPrepCrew().crew()
        result = await crew_instance.kickoff_async(inputs=inputs)
        
        # With output_pydantic, result.pydantic gives us the structured data
        if hasattr(result, 'pydantic') and result.pydantic:
            briefing: MeetingBriefing = result.pydantic
            clean_output = briefing.to_markdown(company_name=topic)
        else:
            # Fallback: use raw output if pydantic parsing failed
            clean_output = str(result)
        
        print("\n=== MEETING PREP COMPLETE ===\n")
        
        # Save to Reports folder
        if md_file := save_markdown_report(clean_output, topic):
            convert_to_html(clean_output, topic, md_file)
            
        return clean_output
        
    except Exception as e:
        print(f"Error in Meeting Prep Flow: {e}")
        raise


if __name__ == "__main__":
    import dotenv
    dotenv.load_dotenv()
    asyncio.run(run_meeting_prep("Nokia"))
