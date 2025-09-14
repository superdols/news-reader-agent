import dotenv

dotenv.load_dotenv()

from crewai import Crew, Agent, Task
from crewai.project import CrewBase, agent, task, crew

@CrewBase
class TranslaterCrew:
    @agent
    def translator_agent(self):
        return Agent(
            config=self.agents_config["translator_agent"],
        )

    @task
    def translate_task(self):
        return Task(
            config=self.tasks_config["translate_task"],
        )
    
    @task
    def retranslate_task(self):
        return Task(
            config=self.tasks_config["retranslate_task"],
        )
    
    @crew
    def assemble_crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )
    
TranslaterCrew().assemble_crew().kickoff(inputs={"sentence": "I'm Kihun and I like studying AI Agents"})