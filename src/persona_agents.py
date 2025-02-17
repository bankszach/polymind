# persona_agents.py

import os
from dotenv import load_dotenv
from arkaine.llms.openai import OpenAI
from arkaine.tools.agent import SimpleAgent
from arkaine.tools.tool import Argument

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the LLM
llm = OpenAI(api_key=api_key)

# Persona Agent
persona_agent = SimpleAgent(
    "PersonaAgent",
    "Provides a direct, factual answer.",
    [Argument("question", "User question", "str", True)],
    llm,
    prepare_prompt=lambda ctx, **kw: (
        "You are the Persona, providing a straightforward response.\n\n"
        f"User question: {kw['question']}"
    ),
    extract_result=lambda ctx, output: output.strip()
)

# Shadow Agent
shadow_agent = SimpleAgent(
    "ShadowAgent",
    "Critical viewpoint that questions assumptions.",
    [Argument("question", "User question", "str", True)],
    llm,
    prepare_prompt=lambda ctx, **kw: (
        "You are the Shadow, playing devil's advocate.\n\n"
        f"User question: {kw['question']}"
    ),
    extract_result=lambda ctx, output: output.strip()
)

# Anima Agent
anima_agent = SimpleAgent(
    "AnimaAgent",
    "Creative, big-picture perspective.",
    [Argument("question", "User question", "str", True)],
    llm,
    prepare_prompt=lambda ctx, **kw: (
        "You are the Anima, offering imaginative or empathic insights.\n\n"
        f"User question: {kw['question']}"
    ),
    extract_result=lambda ctx, output: output.strip()
)
