# [MCP Clients](https://huggingface.co/learn/mcp-course/unit1/mcp-clients)
MCP Clients are the bridge between MCP Hosts & Servers. Think of each Client as a communications manager for each Server connected to the Host.

Users interact with Clients via apps like Claude Desktop or interactive development environments like VS Code.

MCP Hosts use a JSON configuration file ([mcp.json](mcp_examples_json.txt)) to manage client & server communication.

## [Tiny Agents Clients](https://huggingface.co/learn/mcp-course/unit1/mcp-clients#tiny-agents-clients)
***Explore how to use MCP Clients within code***

You can also use tiny agents as MCP Clients to connect directly to MCP servers from your code. Tiny agents provide a simple way to create AI agents that can use tools from MCP servers.

Tiny Agent can run MCP servers with a command line environment. To do this, we will need to install npm and run the server with npx. We’ll need these for both Python and JavaScript.

In this example, the tiny agent utilizes @playwright/mcp@latest which allows agentic interaction with browsers. 

Example:

> Find the top posts in reddit by hot. From the first post, provide a summary of the title and sentiments found in the comments. In natural language, the agent will perform all steps needed to provide the requested title and comments sentiments (eg navigation, filtering, summarizing).

### Setup

1. Install npx:

    `npm install -g npx`

2. Install huggingface_hub package with the MCP support. This will allow us to run MCP servers and clients:

    `pip install "huggingface_hub[mcp]>=0.32.0"`

3. Log in to the Hugging Face Hub to access the MCP servers (*requires an access token from your Hugging Face profile*):

    `hf auth login`

### Connecting to MCP Servers
4. Create an agent configuration file agent.json:
    ```json
    {
        "model": "Qwen/Qwen2.5-72B-Instruct",
        "provider": "nebius",
        "servers": [
            {
                "type": "stdio",
                "config": {
                    "command": "npx",
                    "args": ["@playwright/mcp@latest"]
                }
            }
        ]
    }
    ```
    **Above configuration returns a command key error; `command` & `args` should not be nested within `config`.**

    ***Fix***:
    ```json
    {
        "model": "Qwen/Qwen2.5-72B-Instruct",
        "provider": "nebius",
        "servers": [
            {
                "type": "stdio",
                "command": "npx",
                "args": ["@playwright/mcp@latest"]
            }
        ]
    }
    ```

In this configuration, we are using the @playwright/mcp MCP server. This is an MCP server that can control a browser with Playwright.

Now you can run the agent:

`tiny-agents run agent.json`

> The preceding cmd starts the agent and the following response is returned:  

  >  Agent loaded with 21 tools:  
    • browser_close  
    • browser_resize  
    • browser_console_messages  
    • browser_handle_dialog  
    • browser_evaluate  
    • browser_file_upload  
    • browser_fill_form  
    • browser_install  
    • browser_press_key  
    • browser_type  
    • browser_navigate  
    • browser_navigate_back  
    • browser_network_requests  
    • browser_take_screenshot  
    • browser_snapshot  
    • browser_click  
    • browser_drag  
    • browser_hover  
    • browser_select_option  
    • browser_tabs  
    • browser_wait_for  
    »

### Interact with the browser:

1. Queries for browser tasks are added after `»`. For example "Find the top headlines on CNN".
2. Agent opens browser and navigates to CNN. Then returns CNN website's HTML markup in Markdown.
3. In natural language, agent provides a list of the top headlines on CNN.