"""
GitHub MCP Client

Creates a reusable MultiServerMCPClient instance that can be used
by LangGraph agents.
"""

import os
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient

from observability import logger

load_dotenv()


def get_mcp_client() -> MultiServerMCPClient:
    """
    Creates and returns a MultiServerMCPClient configured
    with the GitHub MCP server.

    Returns:
        MultiServerMCPClient
    """

    logger.info("Initializing GitHub MCP client...")

    github_token = os.getenv("GITHUB_TOKEN")

    if not github_token:
        logger.error("GITHUB_TOKEN not found in environment.")
        raise ValueError("Missing GITHUB_TOKEN in .env")

    try:
        client = MultiServerMCPClient(
            {
                "github": {
                    "command": "npx",
                    "args": [
                        "-y",
                        "@modelcontextprotocol/server-github",
                    ],
                    "env": {
                        "GITHUB_PERSONAL_ACCESS_TOKEN": github_token
                    },
                    "transport": "stdio",
                }
            }
        )

        logger.info("GitHub MCP client initialized successfully.")

        return client

    except Exception as ex:
        logger.exception("Failed to initialize GitHub MCP client.")
        raise ex