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
    base_url=os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1"),
    api_key=os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
)

# OpenAI-based models (OpenAI Agents SDK)
# Using OpenRouter free model temporarily
default_model = OpenAIChatCompletionsModel(
    model="google/gemma-4-31b-it:free", 
    openai_client=client
)

# Fallback: using the same free model
budget_model = OpenAIChatCompletionsModel(
    model="google/gemma-4-31b-it:free",
    openai_client=client
)

# LiteLLM-based models for Meeting Prep (CrewAI)
# Using the same OpenAI-compatible gateway
crew_llm = LLM(
    model="openai/google/gemma-4-31b-it:free",
    base_url=os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1"),
    api_key=os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
)

budget_crew_llm = LLM(
    model="openai/google/gemma-4-31b-it:free",
    base_url=os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1"),
    api_key=os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
)
