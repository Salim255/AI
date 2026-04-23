from agents.tools.tool_executors import get_user

# This file registers all the tools that the agent can call,
#  along with their schemas and executor functions.

TOOL_REGISTRY = {
    "get_user": get_user
}
