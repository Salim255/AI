# This is the JSON schema the model uses to fill arguments.
get_user_schema = {
    "type": "function",
    "name": "get_user",
    "description": "Fetch a user by ID",
    "parameters": {
        "type": "object",
        "properties": {
             "user_id": {
                "type": "integer",
                "description": "The ID of the user to fetch"
            }
        },
        "required": ["user_id"]
    }
}