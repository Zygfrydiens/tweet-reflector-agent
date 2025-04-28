from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

# Define the reflection prompt template
reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twitter influencer grading a tweet. Generate critique and recommendations for the user's tweet. "
            "Always provide detailed analysis covering: "
            "1. Content Quality (clarity, effectiveness, value) "
            "2. Style (tone, language, hashtags) "
            "3. Technical aspects (length, format, media usage) "
            "4. Virality potential (engagement, shareability) "
            "5. Specific improvements with detailed recommendations"
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# Define the generation prompt template
generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a twitter techie influencer assistant tasked with writing excellent twitter posts. "
            "Generate the best twitter post possible for the user's request. "
            "Focus on creating viral, engaging content with perfect length, strong hooks, strategic hashtags, and compelling messaging. "
            "If the user provides critique, respond with a revised version of your previous attempts."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# Initialize the ChatOpenAI model
llm = ChatOpenAI(
    model_name="gpt-4",
    temperature=0.7
)

generate_chain = generation_prompt | llm
reflect_chain = reflection_prompt | llm 