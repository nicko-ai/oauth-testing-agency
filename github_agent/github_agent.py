import os

from agency_swarm import Agent
from agency_swarm.mcp import MCPServerOAuth

GITHUB_MCP_URL = os.getenv("GITHUB_MCP_URL", "http://localhost:8001/mcp")
GITHUB_MCP_URL_SOURCE = "env" if os.getenv("GITHUB_MCP_URL") else "default"
# Space-separated OAuth scopes; set it empty for servers that pick their own scopes (e.g. Notion).
_SCOPES = os.getenv("GITHUB_MCP_SCOPES")
GITHUB_MCP_SCOPES = _SCOPES.split() if _SCOPES is not None else ["repo", "user"]

github = MCPServerOAuth(
    url=GITHUB_MCP_URL,
    name="github",
    scopes=GITHUB_MCP_SCOPES,
)

github_agent = Agent(
    name="GitHubAgent",
    description="Helps with GitHub repositories using OAuth-enabled MCP tools.",
    instructions="./instructions.md",
    files_folder="./files",
    tools_folder="./tools",
    mcp_servers=[github],
    model="gpt-5.2",
)

