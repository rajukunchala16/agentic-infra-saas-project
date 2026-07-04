from dotenv import load_dotenv

from langchain.agents import create_agent
from langgraph.prebuilt import create_react_agent

from config import config
from llm.factory import get_llm
from memory.short_term_memory import get_summarization_middleware
from observability import logger

#from tools import tools

load_dotenv()


async def build_agent(checkpoint):
    """
    Build and return a LangGraph ReAct agent with
    summarization middleware.
    """

    logger.info("Loading configuration...")

    _ = config

    logger.info("Initializing LLM...")

    llm = get_llm()

    logger.info("Creating summarization middleware...")

    middleware = get_summarization_middleware(llm)

    logger.info("Building LangGraph agent...")

    agent = create_agent(
        model=llm,
        middleware=[middleware],
        checkpointer=checkpoint,
    )

    logger.info("LangGraph agent initialized successfully.")

    return agent