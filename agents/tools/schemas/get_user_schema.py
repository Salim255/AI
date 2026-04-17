get_user_schema = {
    "name": "get_user",
    "description": "Fetch a user by ID",
    "parameters": {
        "type": "object",
        "properties": {
            "user_id": {"type": "integer"}
        },
        "required": ["user_id"]
    }
}