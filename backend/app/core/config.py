import os
import logging
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel
from crewai import LLM

# 1. Environment & Logging Setup
def setup_environment():
    """Load env vars and suppress annoying logs"""
    load_dotenv(override=True)
    
    # Disable automatic tracing to prevent 401 errors
    os.environ["OPENAI_TRACING_ENABLED"] = "false"
    os.environ["AGENT_TRACING_ENABLED"] = "false"
    os.environ["OTEL_SDK_DISABLED"] = "true"
    os.environ["PHOENIX_COLLECTOR_ENDPOINT"] = ""

    # Suppress libraries
    logging.getLogger("openai").setLevel(logging.CRITICAL)
    logging.getLogger("agents").setLevel(logging.CRITICAL)
    logging.getLogger("httpx").setLevel(logging.CRITICAL)
    logging.getLogger("httpcore").setLevel(logging.CRITICAL)

# Initialize immediately
setup_environment()

# 2. Shared Client & Model
client = AsyncOpenAI(
    base_url=os.getenv("OPENAI_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/"),
    api_key=os.getenv("OPENAI_API_KEY")
)

# OpenAI-based models (OpenAI Agents SDK)
default_model = OpenAIChatCompletionsModel(
    model="gemini-3-flash", 
    openai_client=client
)

budget_model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=client
)

# LiteLLM-based models for Meeting Prep (CrewAI)
# Using the same OpenAI-compatible gateway
crew_llm = LLM(
    model="openai/gemini-3-flash",
    base_url=os.getenv("OPENAI_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/"),
    api_key=os.getenv("OPENAI_API_KEY")
)

budget_crew_llm = LLM(
    model="openai/gemini-1.5-flash",
    base_url=os.getenv("OPENAI_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/"),
    api_key=os.getenv("OPENAI_API_KEY")
)
