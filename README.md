# [Demo MCP SDK](https://huggingface.co/learn/mcp-course/unit1/sdk)

## Sentiment Analysis with Gradio MCP

This repository demonstrates using a Gradio MCP sentiment analysis tool to analyze text sentiment. The implementation includes:

- **Real MCP Integration**: Uses the configured Gradio sentiment analysis MCP
- **Guitar Review Analysis**: Analyzes the specific review text from Issue #7
- **Comprehensive Results**: Provides polarity, subjectivity, and overall assessment

### Usage

Run the sentiment analysis for the guitar review (Issue #7):

```bash
python real_mcp_analysis.py
```

Or run the demo scripts:

```bash
python sentiment_analysis.py      # Demo with interpretation
python mcp_sentiment_demo.py      # MCP usage pattern demo
```

### Results

The Gradio MCP sentiment analysis tool analyzed the guitar review:

> "Lacks a good electronic reproduction so if thats what you need then this is not for you unless you use chorus. It is light and easy to play so again its a good acoustical guitar especially in this price range. I compared it to a Taylor Baby e and Martins small guitar e. This Yamaha has fuller sound."

**MCP Results:**
- **Polarity**: 0.34 (slightly positive)
- **Subjectivity**: 1.0 (very subjective) 
- **Assessment**: positive

**Interpretation**: This is a positive, highly subjective review that recommends the Yamaha guitar for acoustic use, noting its superior sound compared to competitors while acknowledging limitations in electronic reproduction.

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