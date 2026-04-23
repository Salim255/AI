from agents.tools.tool_registry import TOOL_REGISTRY
from agents.tools.tool_schemas_list import TOOLSGROQ
from agents.tools.tool_call_parser import parse_tool_call_groq
from smart_extractor.prompt_builder import build_prompt
from structured_outputs.schemas.user_schema import User
from smart_extractor.extractor import  smart_json_extractor
import json

# FIRST CALL — model must decide which tool to call
TOOL_CALL_SYSTEM_PROMPT = """
You are a tool-calling agent.

You MUST ALWAYS call a tool when responding.
You MUST NOT answer in natural language.
You MUST NOT output anything except a tool call.
You MUST NOT explain your reasoning.
You MUST NOT return content.
Your ONLY valid output is a tool call in the correct JSON format.

If the user asks for a user profile, call get_user with the correct user_id.
"""

# SECOND CALL — tool already executed, answer directly
text="""
You already executed the tool. 
Now answer the user directly using the tool result. 
Do NOT call any tools again.
Do NOT return tool_calls.
Do NOT return JSON.
Answer in natural language only.
"""
schema_dict = User.model_json_schema()
NO_TOOL_CALL_SYSTEM_PROMPT = build_prompt('user', schema_dict ,text)


def run_agent(llm, user_message: str):
    """
    Core agent loop:
    1. Ask the model which tool to call and with what arguments.
    2. Execute the tool.
    3. Send the tool result back to the model to get the final answer.
    """

    tool_schemas = TOOLSGROQ

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
    
    #
    # 2. Parse tool call
    #
    tool_call_id, tool_name, arguments = parse_tool_call_groq(model_response)

    if tool_name is None or arguments is None:
        return {
            "content": "I could not determine which tool to call from the model response.",
            "tool_calls": None
        }

    #
    # 3. Execute the tool
    #
    if tool_name == "get_user":
        tool_result = TOOL_REGISTRY[tool_name](arguments["user_id"])
    else:
        tool_result = {"error": f"Unknown tool: {tool_name}"}

    print("\n=== TOOL RESULT ===", tool_result)

    #
    # 4. SECOND CALL — give tool result to model, force natural-language answer
    #
    tool_message = {
        "role": "tool",
        "tool_call_id": tool_call_id,
        "name": tool_name,
        "content": json.dumps(tool_result)
    }

    messages_second_call = [
        {
            "role": "system",
            "content": NO_TOOL_CALL_SYSTEM_PROMPT
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
                    "id": tool_call_id,
                    "type": "function",
                    "function": {
                        "name": tool_name,
                        "arguments": json.dumps(arguments)
                    }
                }
            ]
        },
        tool_message
    ]

    final_answer = llm(
        messages=messages_second_call
    )

    return final_answer
