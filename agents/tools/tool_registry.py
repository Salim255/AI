from agents.tools.schemas import get_user_schema
from agents.tools.tool_executor import get_user


TOOLS = {
    "get_user": {
        "schema": get_user_schema,
        "function": get_user
    }
}