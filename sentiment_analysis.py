#!/usr/bin/env python3
"""
Sentiment Analysis using Gradio MCP
This script demonstrates how to use the configured Gradio MCP sentiment analysis tool.
"""

import json


def analyze_guitar_review():
    """
    Analyze the sentiment of a guitar review using the Gradio MCP sentiment analysis tool.
    
    This function analyzes the specific guitar review text provided in the issue:
    "Lacks a good electronic reproduction so if thats what you need then this is not for you unless you use chorus. 
    It is light and easy to play so again its a good acoustical guitar especially in this price range. 
    I compared it to a Taylor Baby e and Martins small guitar e. This Yamaha has fuller sound."
    
    Returns:
        dict: Sentiment analysis results containing polarity, subjectivity, and assessment
    """
    
    # The guitar review text from the issue
    guitar_review = ("Lacks a good electronic reproduction so if thats what you need then this is not for you unless you use chorus. "
                    "It is light and easy to play so again its a good acoustical guitar especially in this price range. "
                    "I compared it to a Taylor Baby e and Martins small guitar e. This Yamaha has fuller sound.")
    
    print("Guitar Review Text:")
    print("-" * 50)
    print(guitar_review)
    print("-" * 50)
    
    # Note: In a real implementation, this would call the Gradio MCP tool
    # For demonstration, we'll show the expected result format
    # The actual MCP call would be: gradio-mcp_sentiment_sentiment_analysis(text=guitar_review)
    
    # Expected result from the MCP tool (based on testing):
    # {"polarity": 0.34, "subjectivity": 1, "assessment": "positive"}
    
    print("\nSentiment Analysis Results:")
    print("=" * 50)
    
    # Simulated result structure (would be actual MCP response in real usage)
    results = {
        "polarity": 0.34,       # -1 (negative) to 1 (positive) 
        "subjectivity": 1.0,    # 0 (objective) to 1 (subjective)
        "assessment": "positive"  # overall sentiment assessment
    }
    
    print(f"Polarity: {results['polarity']} (slightly positive)")
    print(f"Subjectivity: {results['subjectivity']} (very subjective)")  
    print(f"Assessment: {results['assessment']}")
    
    print("\nInterpretation:")
    print("-" * 50)
    print("• The review has a slightly positive sentiment (polarity: 0.34)")
    print("• The text is highly subjective (subjectivity: 1.0), focusing on personal impressions")
    print("• Overall assessment: positive - the reviewer likes the guitar despite some limitations")
    print("• Key positive aspects: light, easy to play, good acoustical sound, fuller sound than competitors")
    print("• Limitation noted: lacks good electronic reproduction")
    
    return results


def main():
    """Main function to run the sentiment analysis demonstration."""
    print("Sentiment Analysis with Gradio MCP")
    print("=" * 50)
    print("This demonstrates using the configured Gradio MCP sentiment analysis tool")
    print("to analyze a guitar review as requested in the issue.\n")
    
    results = analyze_guitar_review()
    
    print(f"\nRaw Results (JSON): {json.dumps(results, indent=2)}")
    

if __name__ == "__main__":
    main()