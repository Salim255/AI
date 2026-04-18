from agents.tools.tool_schemas import get_user_schema
from agents.tools.tool_schemas import get_user_groq_schema
from agents.tools.tool_executors import get_user

# This file registers all the tools that the agent can call,
#  along with their schemas and executor functions.
TOOLS = {
    "get_user": {
        "schema": get_user_schema,
        "function": get_user
    }
}

TOOLSGROQ = {
    "get_user": {
        "schema": get_user_groq_schema,
        "function": get_user
    }
}