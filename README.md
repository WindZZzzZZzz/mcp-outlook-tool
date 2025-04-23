# MCP Outlook Tool

The MCP Outlook Tool is a project that consists of two main components: a client and a server. These components work together to interact with Microsoft Outlook and other tools via the MCP (Modular Command Protocol) framework.

## Project Structure

### Components

#### 1. **Client**
The client is responsible for interacting with the server and processing user queries. It uses the Anthropic API and MCP framework to process queries and execute tools.

- **Main File**: [outlook-mcp-client/src/main.py](outlook-mcp-client/src/main.py)
- **Core Logic**: [outlook-mcp-client/src/mcp_client.py](outlook-mcp-client/src/mcp_client.py)

#### 2. **Server**
The server provides tools and resources for interacting with Microsoft Graph API to manage Outlook data such as emails, users, and more.

- **Main File**: [outlook-mcp-server/main.py](outlook-mcp-server/main.py)
- **Core Logic**: [outlook-mcp-server/src/mcp_server.py](outlook-mcp-server/src/mcp_server.py)
- **Graph API Integration**: [outlook-mcp-server/src/graph.py](outlook-mcp-server/src/graph.py)

## Prerequisites

- Python 3.12 or higher
- Required dependencies listed in `pyproject.toml` for both client and server
- Microsoft Azure credentials for Graph API integration

## Setup

### 1. Set Env
#### Copy .env.template and name the new file ".env
#### Set LLM API keys and Graph API access keys
### 2. Activate uv environment
#### On Windows:
.venv\Scripts\activate
#### On Unix or MacOS:
source .venv/bin/activate
#### Install required packages
```bash
uv add mcp anthropic python-dotenv
```
### 3. Run the client
```bash
uv run .\outlook-mcp-client\src\main.py .\outlook-mcp-server\src\mcp-server.py
```

## Features
### Client:

- Connects to the MCP server.
- Processes user queries using Anthropic's Claude API.
- Executes tools provided by the server.

### Server:

- Integrates with Microsoft Graph API for managing Outlook data.
- Provides tools for sending emails, retrieving inbox messages, and more.