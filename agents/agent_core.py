from agents.tools.tool_registry import TOOLS
from agents.tools.tool_call_parser import parse_tool_call
from agents.tools.tool_executors import execute_tool

# This is the core agent logic that ties everything together.
# It takes a user message, asks the model what to do, executes the tool, and returns the final answer.
# The flow is:
# 1. User sends a message to the agent.
# 2. The agent asks the model what tool to call and with what arguments.
# 3. The agent executes the tool and gets the result.
# 4. The agent sends the tool result back to the model and gets the final answer
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
