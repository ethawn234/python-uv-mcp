# [Demo MCP SDK](https://huggingface.co/learn/mcp-course/unit1/sdk)

## Quickstart (python)

1. Install ***uv*** package manager.

2. Install dependencies with uv:

      `uv add "mcp[cli]"`

3. Start the server (filename must be exact):

    `mcp dev server.py`


### Explore Quickstart MCP Server
- Ignore error output (not significant)
- Bottom Center Panel: lists history of commands (eg connection initialization, resource list, etc)
- Top Menu Bar (`Resources`, `Prompts`, `Tools`, etc):
  
  1. Click on `Tools` to return available capabilities (`get_weather`).
  2. Demo code returns hardcoded string with user input for `location`. 

  - Note: The terminal will log commands that have run.

### Deploy your mcp server
In order to enable others to use your MCP server, it must be deployed somewhere like **[Hugging Face Spaces](https://huggingface.co/learn/mcp-course/unit2/gradio-server#deploying-to-hugging-face-spaces)**.

