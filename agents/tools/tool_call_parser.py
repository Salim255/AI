def parse_tool_call(model_output: dict):
    tool_name = model_output.get("tool")
    arguments = model_output.get("arguments", {})
    return tool_name, arguments
