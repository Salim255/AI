from agents.tools.tool_registry import TOOLS
from agents.tools.tool_call_parser import parse_tool_call
from agents.tools.tool_executor import execute_tool

def run_agent(llm, user_message: str):
    # 1. Ask the model what to do
    model_response = llm.chat(
        message=user_message,
        tools=[tool["schema"] for tool in TOOLS.values()]
    )

    # 2. Parse tool call
    tool_name, arguments = parse_tool_call(model_response)

    # 3. Execute the tool
    tool_result = execute_tool(tool_name, arguments)

    # 4. Send the result back to the model
    final_answer = llm.chat(
        message=f"Tool result: {tool_result}",
        conversation_id=model_response["conversation_id"]
    )

    return final_answer
