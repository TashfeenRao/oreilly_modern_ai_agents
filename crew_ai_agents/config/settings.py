from dotenv import load_dotenv

load_dotenv()



class Settings:
    """Configuration settings for Crew AI Agents."""

    # API Keys
    OPENAI_API_KEY: str = None
    SERPER_API_KEY: str = None
    HUGGINGFACEHUB_API_TOKEN: str = None
    GROQ_API_KEY: str = None
    

    def __init__(self):
        import os

        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.SERPER_API_KEY = os.getenv("SERPER_API_KEY")
        self.HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        self.GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        
        
settings = Settings()