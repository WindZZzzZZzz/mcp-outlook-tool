from typing import Any
from .graph import Graph
from .mcp import MCPServer, MCPTool, MCPResource, MCPPrompt, MCPPromptArgument
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("outlook")



if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')