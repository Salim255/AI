import os
import json
from groq import Groq

client = Groq(api_key=os.getenv("GROAI_API_KEY"))

def groq_llm_tools(
    message: str,
    tools: list = None,
    conversation_id: str = None,
    debug: bool = False
) -> dict:
    """
    Tool-calling mode — for agents.
    """

    messages = [
        {
            "role": "system",
            "content": "You are an AI agent. Use tools when needed."
        },
        {
            "role": "user",
            "content": message
        }
    ]

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        tools=tools if tools else None,
        tool_choice="auto" if tools else None
    )

    msg = response.choices[0].message

    if debug:
        print("RAW TOOL RESPONSE:", msg)

    return {
        "content": msg.content,
        "tool_calls": msg.tool_calls,
        "conversation_id": response.id
    }
