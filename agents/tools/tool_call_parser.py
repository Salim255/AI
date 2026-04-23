# This file is responsible for parsing the model's output 
# to determine which tool to call and with what arguments.
import json


def parse_tool_call(model_output: dict):
    print("\n=== MODEL RESPONSE ===")
    print(json.dumps(model_output, indent=2, default=str))
    
    tool_name = model_output.get("tool")
    arguments = model_output.get("arguments", {})
    return tool_name, arguments


def parse_tool_call_groq(model_output: dict):
    print("\n=== MODEL RESPONSE ===")
    print(json.dumps(model_output, indent=2, default=str))

    tool_calls = model_output.get("tool_calls")
    if not tool_calls:
        return None, None

    # Groq returns objects, not dicts → convert to string then parse manually
    call = tool_calls[0]

    print("\n=== MODEL RESPONSE ===👹", call)
    # Convert the tool call object to a dict-like structure
    # Groq objects behave like: ChatCompletionMessageToolCall(...)
    # So we extract fields manually
     # Extract name + arguments from Groq tool call object
    tool_call_id =  call.id
    tool_name = call.function.name
    arguments = json.loads(call.function.arguments)
    print("\n=== MODEL RESPONSE ===👹👹", tool_call_id, tool_name, arguments)
    return  tool_call_id, tool_name, arguments