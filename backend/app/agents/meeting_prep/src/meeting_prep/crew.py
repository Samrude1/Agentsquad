from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import TavilySearchTool
from meeting_prep.schemas import MeetingBriefing
from backend.app.core.config import crew_llm

@CrewBase
class MeetingPrepCrew():
    """Meeting Prep crew for preparing business meeting briefings"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self, llm=None):
        self.llm = llm or crew_llm

    @agent
    def lead_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['lead_researcher'],
            verbose=True,
            tools=[TavilySearchTool()],
            llm=self.llm
        )

    @agent
    def meeting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['meeting_analyst'],
            verbose=True,
            llm=self.llm
        )

    @agent
    def briefing_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config['briefing_coordinator'],
            verbose=True,
            llm=self.llm
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task'],
        )

    @task
    def briefing_task(self) -> Task:
        return Task(
            config=self.tasks_config['briefing_task'],
            output_pydantic=MeetingBriefing,  # Forces structured output
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=False, # DISABLED for Render Free Tier (saves RAM)
        )
