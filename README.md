# Tweet Reflector Agent

A Python-based AI agent that analyzes, reflects on, and generates improved versions of tweets, particularly focusing on scientific content. The agent uses a graph-based workflow to iteratively improve tweet quality through reflection and regeneration.

## Features

- Tweet analysis and reflection
- Intelligent tweet regeneration based on reflections
- Graph-based workflow visualization
- Support for scientific content improvement
- Hashtag optimization

## Project Structure

The project follows a graph-based workflow:
```
__start__ -> generate -> reflect -> generate [repeats given amount of times...]-> __end__
```

## Setup

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
```
3. Activate the virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies:
```bash
pip install -r requirements.txt
```
5. Set up environment variables as needed - OpenAI API and LangChain API. You can edit them in setup_enviroment.py
6. Run the project:
```bash
python main.py
```

## Example

The agent can take casual scientific tweets like:
```
yo einstein was like super smart n stuff, he did that e=mc2 thing which is like energy equals mass times speed squared or whatever lol #physics
```

And transform them into more professional and engaging content:
```
Unraveling the mysteries of the universe, one equation at a time. #Einstein, the maestro of relativity, gave us E=mc², proving that energy and mass are interchangeable. A testament to the power of intellect! #PhysicsGenius #RelativityRules
```
