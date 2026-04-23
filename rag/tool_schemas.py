embed_tool_schema={
    "type": "function",
    "function": {
        "name": "embed_text",
        "description": "Generate an embedding vector for a given text.",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {"type": "string"}
            },
            "required": ["text"]
        }
    }
}
