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
default_model = OpenAIChatCompletionsModel(
    model="anthropic/claude-3.5-sonnet", 
    openai_client=client
)

# Fallback model
budget_model = OpenAIChatCompletionsModel(
    model="meta-llama/llama-3.3-70b-instruct",
    openai_client=client
)

# Litellm / CrewAI wrapper models
# Note: LiteLLM requires the "openai/" prefix when using custom base_url to pass the exact model string to OpenRouter
crew_llm = LLM(
    model="openai/openai/gpt-4o",
    base_url=os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1"),
    api_key=os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
)

budget_crew_llm = LLM(
    base_url=os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1"),
    api_key=os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
)
