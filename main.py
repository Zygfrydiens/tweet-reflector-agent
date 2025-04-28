# Python
import os

# Environment variables
os.environ["OPENAI_API_KEY"] = os.getenv('TWEET-REFLECTOR-AGENT-OPENAI')
os.environ["LANGCHAIN_API_KEY"] = os.getenv('TWEET-REFLECTOR-AGENT-LANGCHAIN')
os.environ["LANGSMITH_PROJECT"] = "tweet_reflector_agent"
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "reflector agent"


from typing import Sequence, List
# Langchain
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph
from chains import generate_chain, reflect_chain



# Nodes
REFLECT = "reflect"
GENERATE = "generate"


def generation_node(state: Sequence[BaseMessage]):
    return generate_chain.invoke({"messages": state})


def reflection_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    res = reflect_chain.invoke({"messages": messages})
    return [HumanMessage(content=res.content)]

def should_continue(state: List[BaseMessage]) -> bool:
    # Return True to continue to REFLECT, False to END, implement logic as needed
    return len(state) <= 6

# Graph
builder = MessageGraph()
builder.add_node(GENERATE, generation_node)
builder.add_node(REFLECT, reflection_node)
builder.set_entry_point(GENERATE)

builder.add_conditional_edges(
    GENERATE,
    should_continue,
    {
        True: REFLECT,
        False: END
    }
)
builder.add_edge(REFLECT, GENERATE)

graph = builder.compile()
print(graph.get_graph().draw_mermaid())
graph.get_graph().print_ascii()

def main():
    print("Environment variables loaded. Ready to run.")
    
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
    result = graph.invoke(messages)
    
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