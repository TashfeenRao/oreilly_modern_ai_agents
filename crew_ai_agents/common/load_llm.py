from crewai import LLM
from crew_ai_agents.config.settings import settings

def load_llm():
    """Load and return the LLM instance based on configuration settings."""

    return LLM(
        model='gpt-4.1',
        api_key=settings.OPENAI_API_KEY,
        temperature=0.7
    )