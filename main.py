# Python
import os
from typing import Sequence, List

from setup_environment import load_environment_variables
load_environment_variables()
print("Environment variables loaded. Ready to run.")


# Langchain
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph
from chains import generate_chain, reflect_chain

from graph import TweetReflectorGraph

def main():
    # Initialize the graph
    tweet_graph = TweetReflectorGraph()
    
    # Visualize the graph structure
    print("\nGraph Structure:")
    print("-" * 50)
    tweet_graph.visualize()
    print("-" * 50)
    
    # Initial poorly written tweet about Einstein
    initial_tweet = "yo einstein was like super smart n stuff, he did that e=mc2 thing which is like energy equals mass times speed squared or whatever lol #physics #genius"
    
    # Create initial message
    messages = [HumanMessage(content=initial_tweet)]
    
    # Run the graph
    print("\nInitial Tweet:")
    print("-" * 50)
    print(initial_tweet)
    print("-" * 50)
    
    # Process through the graph
    result = tweet_graph.process(messages)
    
    # Print the conversation flow
    print("\nReflection and Generation Process:")
    print("-" * 50)
    for i, message in enumerate(result, 1):
        prefix = "🤖 Generated" if i % 2 == 0 else "🤔 Reflection"
        print(f"\n{prefix} #{i//2 + 1}:")
        print(message.content)
        print("-" * 50)

if __name__ == "__main__":
    main() 