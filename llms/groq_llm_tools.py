import os
from groq import Groq

client = Groq(api_key=os.getenv("GROAI_API_KEY"))


def groq_llm_tools(
    messages: list,
    tools: list = None,
    debug: bool = False,
) -> dict:
    """
    Groq tool-calling wrapper.
    Expects:
        messages = [
            {"role": "system", "content": "..."},
            {"role": "user", "content": "..."},
            ...
        ]
    """

    # Groq requires explicit tool_choice
    tool_choice = "auto" if tools else "none"

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        tools=tools if tools else None,
        tool_choice=tool_choice
    )

    msg = response.choices[0].message

    if debug:
        print("\n=== RAW GROQ RESPONSE ===")
        print(msg)

    return {
        "content": msg.content,
        "tool_calls": msg.tool_calls
    }
