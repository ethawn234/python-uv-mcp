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
  
  1. Click on `Tools` to return available capabilities (`get_weather`, `analyze_sentiment`).
  2. Demo code returns hardcoded string with user input for `location`. 
  3. **NEW**: Sentiment analysis tool analyzes text sentiment with polarity, subjectivity, and assessment.

  - Note: The terminal will log commands that have run.

## New Features

### Sentiment Analysis Tool

The server now includes a `analyze_sentiment` tool that provides comprehensive sentiment analysis of text:

#### Usage:
- **Tool**: `analyze_sentiment(text: str)`
- **Returns**: JSON with polarity, subjectivity, assessment, and detailed analysis notes

#### Example:
```python
# Guitar review analysis
text = """Lacks a good electronic reproduction so if thats what you need then this is not for you unless you use chorus. It is light and easy to play so again its a good acoustical guitar especially in this price range. I compared it to a Taylor Baby e and Martins small guitar e. This Yamaha has fuller sound."""

# Returns:
{
  "polarity": 0.33,
  "subjectivity": 0.17,
  "assessment": "positive",
  "positive_indicators": 4,
  "negative_indicators": 2,
  "analysis_notes": [
    "Notes limitation in electronic reproduction",
    "Highlights positive physical characteristics", 
    "Emphasizes sound quality benefits",
    "Includes comparative analysis with other brands"
  ]
}
```

#### Features:
- **Polarity**: Scale from -1 (very negative) to +1 (very positive)
- **Subjectivity**: Scale from 0 (objective) to 1 (very subjective)  
- **Assessment**: Overall sentiment classification (positive/negative/neutral)
- **Analysis Notes**: Context-aware insights about the text content