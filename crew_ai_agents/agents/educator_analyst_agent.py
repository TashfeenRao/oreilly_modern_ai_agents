from crewai import Agent, Task, Crew, Process
# Importing crewAI tools
from crew_ai_agents.config import settings
from crew_ai_agents.common.load_llm import load_llm

from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    WebsiteSearchTool,
    SerperDevTool
)


docs_tool = DirectoryReadTool(directory='./')
file_tool = FileReadTool()
search_tool = SerperDevTool()


def create_agents_and_tasks():
    llm = load_llm()
    
    data_analyst = Agent(
        role='educator',
        goal='based on the context provide, answer the question.',
        backstory='you are a data expert',
        allow_delegation=False,
        tools=[search_tool],
        verbose=True)
    
    nlp_task = Task(
        description='understand the topic of natuaral language processing and summarize it for me',
        agent=data_analyst,
        expected_output='i want response to be short as much as possible',
    )
    
    calculator_agent = Agent(
        role='calculator',
        goal='you calculate things',
        backstory='you are a math expert',
        allow_delegation=False,
        tools=[],
        verbose=True)
    
    math_task = Task(
        description='tell me what is 2*24*432',
        agent=calculator_agent,
        expected_output='calculate this',
    )
    
    
    crew = Crew(
        agents=[ calculator_agent, data_analyst],
        process=Process.hierarchical,
        tasks=[math_task,nlp_task],
        manager_llm=llm,
        verbose=True
    )
    output = crew.kickoff()
    print("Final Output:\n", output.raw)
    
    
    
    
    
if __name__ == '__main__':
    create_agents_and_tasks()