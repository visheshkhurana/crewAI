"""
Cleya.ai Growth & Viral Marketing Crew
=======================================
A multi-agent system for running Cleya.ai's growth marketing operations.

5 specialized agents work in sequence:
  1. Market Intelligence Analyst → ecosystem intel
  2. Growth Strategist → strategy & funnels  
  3. Viral Content Architect → content engine
  4. Community Growth Hacker → partnerships & community
  5. PLG Engineer → referral & viral mechanics

Each agent builds on the previous agent's output, creating a comprehensive
marketing operations playbook.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
    SerperDevTool,
    ScrapeWebsiteTool,
    FileWriterTool,
    FileReadTool,
)
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


# ── Tool Instances ───────────────────────────────────────────────────────
# Shared across agents that need web research capabilities
serper_search = SerperDevTool()
web_scraper = ScrapeWebsiteTool()
file_writer = FileWriterTool()
file_reader = FileReadTool()


@CrewBase
class CleyaMarketingCrew:
    """Cleya.ai Growth & Viral Marketing Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # ── AGENTS ───────────────────────────────────────────────────────────

    @agent
    def market_intelligence_analyst(self) -> Agent:
        """Ecosystem intelligence & competitive analysis specialist."""
        return Agent(
            config=self.agents_config["market_intelligence_analyst"],
            tools=[serper_search, web_scraper, file_reader],
            verbose=True,
        )

    @agent
    def growth_strategist(self) -> Agent:
        """Head of Growth — designs funnels, loops, and acquisition strategy."""
        return Agent(
            config=self.agents_config["growth_strategist"],
            tools=[serper_search, file_reader],
            verbose=True,
            allow_delegation=True,
        )

    @agent
    def viral_content_architect(self) -> Agent:
        """Creates viral content for LinkedIn, Twitter/X, and WhatsApp."""
        return Agent(
            config=self.agents_config["viral_content_architect"],
            tools=[serper_search, web_scraper],
            verbose=True,
        )

    @agent
    def community_growth_hacker(self) -> Agent:
        """Builds partnerships, ambassador programs, and community flywheels."""
        return Agent(
            config=self.agents_config["community_growth_hacker"],
            tools=[serper_search, web_scraper],
            verbose=True,
        )

    @agent
    def product_led_growth_engineer(self) -> Agent:
        """Designs referral systems, viral mechanics, and PLG features."""
        return Agent(
            config=self.agents_config["product_led_growth_engineer"],
            tools=[file_reader],
            verbose=True,
        )

    # ── TASKS ────────────────────────────────────────────────────────────

    @task
    def ecosystem_intelligence_task(self) -> Task:
        """Compile real-time ecosystem intelligence brief."""
        return Task(
            config=self.tasks_config["ecosystem_intelligence_task"],
            output_file="output/01_ecosystem_intelligence.md",
        )

    @task
    def growth_strategy_task(self) -> Task:
        """Design comprehensive growth strategy with funnels and loops."""
        return Task(
            config=self.tasks_config["growth_strategy_task"],
            output_file="output/02_growth_strategy.md",
        )

    @task
    def viral_content_task(self) -> Task:
        """Create viral content calendar and assets."""
        return Task(
            config=self.tasks_config["viral_content_task"],
            output_file="output/03_viral_content_calendar.md",
        )

    @task
    def community_partnerships_task(self) -> Task:
        """Design community partnerships and ambassador program."""
        return Task(
            config=self.tasks_config["community_partnerships_task"],
            output_file="output/04_community_partnerships.md",
        )

    @task
    def product_led_growth_task(self) -> Task:
        """Design product-led growth mechanics and referral system."""
        return Task(
            config=self.tasks_config["product_led_growth_task"],
            output_file="output/05_product_led_growth.md",
        )

    # ── CREW ─────────────────────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """
        Assembles the Cleya.ai Marketing Crew.
        
        Process: Sequential
        - Each task builds on the previous agent's output
        - Intelligence → Strategy → Content → Community → PLG
        
        Memory: Enabled for cross-task context retention
        """
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=True,
            output_log_file="output/crew_execution.log",
        )
