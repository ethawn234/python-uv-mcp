# [Building an End-to-End MCP Application](https://huggingface.co/learn/mcp-course/unit2/introduction)

## End-to-End Project
Build a **sentiment analysis application** that consists of three main parts: the ***server***, the ***client***, and the ***deployment***.

### Server Side
- Uses Gradio to create a web interface and MCP server via gr.Interface
- Implements a sentiment analysis tool using TextBlob
- Exposes the tool through both HTTP and MCP protocols

### Client Side
- Implements a HuggingFace.js client
- Or, creates a smolagents Python client
- Demonstrates how to use the same server with different client implementations

### Deployment
- Deploys the server to Hugging Face Spaces
- Configures the clients to work with the deployed server

### Architecture
![Architecture](arch.png)

---

## What You’ll Learn
**Objective**: A working MCP application that demonstrates the power and flexibility of the protocol

In this unit, you will:

- Create an MCP Server using Gradio’s built-in MCP support
- Build a sentiment analysis tool that can be used by AI models
- Connect to the server using different client implementations:
  - A HuggingFace.js-based client
  - A SmolAgents-based client for Python
- Deploy your MCP Server to Hugging Face Spaces
- Test and debug the complete system

## Prerequisites

Before proceeding with this unit, make sure you:

- Have completed Unit 1 or have a basic understanding of MCP concepts
- Are comfortable with both Python and JavaScript/TypeScript
- Have a basic understanding of APIs and client-server architecture
- Have a development environment with:
    - Python 3.10+
    - Node.js 18+
- A Hugging Face account (for deployment)