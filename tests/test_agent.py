import os
from dotenv import load_dotenv
from arkaine.llms.openai import OpenAI
from arkaine.tools.agent import SimpleAgent
from arkaine.tools.tool import Argument

# 1. Load environment variables from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 2. Initialize the LLM
llm = OpenAI(api_key=api_key)

# 3. Create a single SimpleAgent
agent = SimpleAgent(
    name="my_agent",
    description="A simple test agent",
    args=[Argument("task", "Describe a task", "str", required=True)],
    llm=llm,
    prepare_prompt=lambda context, **kwargs: f"Please perform this task: {kwargs['task']}",
    extract_result=lambda context, output: output.strip()
)

# ---------------------------
# Multiple Calls in One Script
# ---------------------------

# A) Greeting
greeting_result = agent(task="Greet John")
print("\n[GREETING]")
print(greeting_result)

# B) Summarizer
text_to_summarize = (
    "Arkaine is a framework that simplifies building AI-based agents "
    "with tool integration, making development faster and more organized."
)
summary_result = agent(task=f"Summarize the following text:\n{text_to_summarize}")
print("\n[SUMMARY]")
print(summary_result)

# C) Q&A Helper
question = "What is the capital of France?"
qa_result = agent(task=f"Answer this question: {question}")
print("\n[Q&A]")
print(qa_result)

# D) Creative Writer
story_result = agent(task="Write a short story about a robot learning to cook")
print("\n[CREATIVE WRITING]")
print(story_result)

# E) Instruction Generator
instructions_result = agent(task="Give me a step-by-step guide on how to change a tire")
print("\n[INSTRUCTIONS]")
print(instructions_result)
