# aggregator.py

from arkaine.tools.tool import Tool

def unify_responses(context, kwargs):
    """
    Expects kwargs = {
      "persona_ans": ...,
      "shadow_ans": ...,
      "anima_ans": ...
    }
    """
    persona_ans = kwargs["persona_ans"]
    shadow_ans = kwargs["shadow_ans"]
    anima_ans = kwargs["anima_ans"]

    return (
        "FINAL UNIFIED RESPONSE\n"
        "======================\n\n"
        f"Persona:\n{persona_ans}\n\n"
        f"Shadow:\n{shadow_ans}\n\n"
        f"Anima:\n{anima_ans}\n\n"
        "Self Synthesis:\n"
        "Here is where you combine insights into a single cohesive answer."
    )

# aggregator_tool is a standard Tool
aggregator_tool = Tool(
    "SelfAggregator",
    "Combines persona outputs into one final answer.",
    [],  # arguments (none needed)
    [],  # examples (none)
    unify_responses
)
