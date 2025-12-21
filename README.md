# [Tiny Agents Clients](https://huggingface.co/learn/mcp-course/unit1/mcp-clients?env-variables=python#tiny-agents-clients)

You can also use tiny agents as MCP Clients to connect directly to MCP servers from your code. Tiny agents provide a simple way to create AI agents that can use tools from MCP servers.

Tiny Agent can run MCP servers with a command line environment. 

## Quickstart

- Need Hugging Face access. Use `hf auth whoami` to check login status.

- Run the Tiny Agent MCP Client: `tiny-agents run .\agent.json`.
  * Currently fails due to invalid `model` selection in `agent.json`.