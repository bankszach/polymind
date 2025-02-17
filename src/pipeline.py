# pipeline.py

from arkaine.tools.tool import Tool, Argument
from persona_agents import persona_agent, shadow_agent, anima_agent
from aggregator import aggregator_tool

def pipeline_func(context, kwargs):
    """
    1) Calls Persona, Shadow, Anima individually with the same 'question'.
    2) Then calls aggregator_tool to unify the results.
    """
    # Step 1: Each persona agent
    persona_ans = persona_agent.invoke(context, kwargs)
    shadow_ans = shadow_agent.invoke(context, kwargs)
    anima_ans = anima_agent.invoke(context, kwargs)

    # Step 2: Pass them to aggregator
    aggregator_input = {
        "persona_ans": persona_ans,
        "shadow_ans": shadow_ans,
        "anima_ans": anima_ans
    }
    final_result = aggregator_tool.invoke(context, aggregator_input)

    return final_result

# This pipeline tool has a single argument, "question".
multi_persona_pipeline = Tool(
    "MultiPersonaPipeline", 
    "Manually calls Persona, Shadow, Anima, then unifies via aggregator.",
    [Argument("question", "User question", "str", True)],  # Must match what we pass in main.py
    [],  # examples
    pipeline_func
)
