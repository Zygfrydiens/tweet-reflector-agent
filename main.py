import os

os.environ["OPENAI_API_KEY"] = os.getenv('TWEET-REFLECTOR-AGENT-OPENAI')
os.environ["LANGCHAIN_API_KEY"] = os.getenv('TWEET-REFLECTOR-AGENT-LANGCHAIN')
LANGCHAIN_TRACING_V2 = True
LANGCHAIN_PROJECT = "reflector agent"

def main():
    print("Environment variables loaded and LangChain Tracer initialized. Ready to run.")

if __name__ == "__main__":
    main() 