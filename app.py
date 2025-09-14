import json
import gradio as gr
from textblob import TextBlob

# sentiment_analysis function takes a text input and returns a dictionary with sentiment details
def sentiment_analysis(text: str) -> str:
  """
  Analyzes the sentiment of the input text.
  
  Parameters:
    text (str): The input text to analyze.
  Returns:
    str: A JSON string containing polarity, subjectivity, and assessment.
  """
  blob = TextBlob(text)
  sentiment = blob.sentiment

  result = {
    'polarity': round(sentiment.polarity, 2), # -1 (negative) to 1 (positive)
    'subjectivity': round(sentiment.subjectivity), # 0 (objective) to 1 (subjective)
    'assessment': 'positive' if sentiment.polarity > 0 else 'negative' if sentiment.polarity < 0 else 'neutral'
  }

  return json.dumps(result)

# Gradio interface creates both the web UI and MCP server
demo = gr.Interface(
  fn=sentiment_analysis,
  inputs=gr.Textbox(placeholder='Enter text to analyze...'),
  outputs=gr.Textbox(),
  title='Text Sentiment Analysis',
  description='Analyze the sentiment of text using TextBlob'
)

# Launch interface & MCP server
  # Web interface: http://localhost:7860
  # MCP server: http://localhost:7860/gradio_api/mcp/sse
  # MCP schema: http://localhost:7860/gradio_api/mcp/schema
    #   {
    # "predict": {
    #       "type": "object",
    #       "properties": {
    #         "text": {
    #           "type": "string",
    #           "description": "The input text to analyze."
    #         }
    #       },
    #       "description": "Analyzes the sentiment of the input text."
    #     }
    #   }
# Start server: python app.py
if __name__ == '__main__':
  demo.launch(mcp_server=True)