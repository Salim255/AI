# This file is responsible for parsing the model's output 
# to determine which tool to call and with what arguments.
def parse_tool_call(model_output: dict):
    tool_name = model_output.get("tool")
    arguments = model_output.get("arguments", {})
    return tool_name, arguments
