from crewai import Agent, Task, Crew, LLM
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
    # Create agents
    researcher = Agent(
        role='Market Research Analyst',
        goal='Provide up-to-date market analysis of the AI industry',
        backstory='An expert analyst with a keen eye for market trends.',
        tools=[search_tool],
        verbose=True,
    )

    writer = Agent(
        role='Content Writer',
        goal='Craft engaging blog posts about the AI industry',
        backstory='A skilled writer with a passion for technology.',
        tools=[docs_tool, file_tool],
        verbose=True,
    )

    # The `# Define tasks` comment is simply providing a visual separation in the code to indicate that the following
    # code block is defining the tasks for the agents. It serves as a helpful marker for the reader to understand
    # that the tasks are being defined in that specific section of the code.
    # Define tasks
    research = Task(
        description='Research the latest trends in the AI industry and provide a summary.',
        expected_output='A summary of the top 3 trending developments in the AI industry with a unique perspective on their significance.',
        agent=researcher,
        max_iterations=2
    )

    write = Task(
        description='Write an engaging blog post about the AI industry, based on the research analyst\'s summary. Draw inspiration from the latest blog posts in the directory.',
        expected_output='A 4-paragraph blog post formatted in markdown with engaging, informative, and accessible content, avoiding complex jargon.',
        agent=writer,
        output_file='blog-posts/new_post.md'  # The final blog post will be saved here
    )
    
    return researcher, writer, research, write


def crew_run():
    researcher, writer, research, write = create_agents_and_tasks()

    # Create crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research, write],
        verbose=True
    )

    # Run crew
    crew.kickoff()

