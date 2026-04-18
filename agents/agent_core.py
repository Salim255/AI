from agents.tools.tool_registry import TOOLSGROQ
from agents.tools.tool_call_parser import parse_tool_call_groq
from agents.tools.tool_executors import get_user
import json

# FIRST CALL — model must decide which tool to call
TOOL_CALL_SYSTEM_PROMPT = """
You are an AI agent that uses tools to answer user questions.

You have access to the following tools:
- get_user(user_id: integer): returns user data.

When the user asks for information that requires a tool, you MUST call the tool using the correct JSON arguments.
You MUST NOT answer the question directly before the tool is executed.
You MUST NOT invent arguments.
You MUST return a tool call in the correct format:
{
  "tool_calls": [
    {
      "type": "function",
      "function": {
        "name": "<tool_name>",
        "arguments": "<json string>"
      }
    }
  ]
}

If the user asks for a user profile, ALWAYS call get_user with the correct user_id.
Do not answer in natural language until the tool result is provided.
"""

# SECOND CALL — tool already executed, answer directly
NO_TOOL_CALL_SYSTEM_PROMPT = """
You already executed the tool. 
Now answer the user directly using the tool result. 
Do NOT call any tools again.
Do NOT return tool_calls.
Do NOT return JSON.
Answer in natural language only.
"""


def run_agent(llm, user_message: str):
    """
    Core agent loop:
    1. Ask the model which tool to call and with what arguments.
    2. Execute the tool.
    3. Send the tool result back to the model to get the final answer.
    """

    tool_schemas = [tool["schema"] for tool in TOOLSGROQ.values()]

    print(tool_schemas)
    #
    # 1. FIRST CALL — model decides which tool to call
    #
    messages_first_call = [
        {"role": "system", "content": TOOL_CALL_SYSTEM_PROMPT},
        {"role": "user", "content": user_message}
    ]

    model_response = llm(
        messages=messages_first_call,
        tools=tool_schemas
    )

    # ConversationId object
    tool_calls = model_response["tool_calls"]
   
    if not tool_calls:
        print("❌ No tool calls returned by model")
        return {
            "content": "I could not determine which tool to call from the model response.",
            "tool_calls": None
        }
    
    tool_call_id =  tool_calls[0]
    #
    # 2. Parse tool call
    #
    tool_name, arguments = parse_tool_call_groq(model_response)

    if tool_name is None or arguments is None:
        return {
            "content": "I could not determine which tool to call from the model response.",
            "tool_calls": None
        }

    #
    # 3. Execute the tool
    #
    if tool_name == "get_user":
        tool_result = get_user(arguments["user_id"])
    else:
        tool_result = {"error": f"Unknown tool: {tool_name}"}

    print("\n=== TOOL RESULT ===", tool_result)

    #
    # 4. SECOND CALL — give tool result to model, force natural-language answer
    #
    tool_message = {
        "role": "tool",
        "tool_call_id": tool_call_id.id,
        "name": "get_user",
        "content": json.dumps(tool_result)
    }

    messages_second_call = [
        {
            "role": "system",
            "content": "You have already executed the tool. Answer the user directly using the tool result. Do not call any tools again."
        },
        {
            "role": "user",
            "content": user_message
        },
        {
            "role": "assistant",
            "content": None,
            "tool_calls": [
                {
                    "id": tool_call_id.id,
                    "type": "function",
                    "function": {
                        "name": "get_user",
                        "arguments": json.dumps(arguments)
                    }
                }
            ]
        },
        tool_message
    ]

    final_answer = llm(
        messages=messages_second_call,
        tools=tool_schemas
    )

    return final_answer
