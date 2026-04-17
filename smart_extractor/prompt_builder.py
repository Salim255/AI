def build_task_description(schema_name: str, schema: dict) -> str:
    properties = schema.get("properties", {})
    fields = ", ".join(
        f"{name} ({details.get('type', 'unknown')})"
        for name, details in properties.items()
    )

    return f"""Your task is to extract information and return it as a JSON object that matches this schema: {schema_name} {{ {fields} }}            """

def build_prompt(schema_name: str, schema: dict, text: str) -> str:
    properties = schema.get("properties", {})
    fields = ", ".join(
        f"{name}: {details.get('type', 'unknown')}"
        for name, details in properties.items()
    )

    return f"""
You MUST extract exactly ONE JSON object that matches this schema:

{schema_name} {{ {fields} }}

STRICT RULES:
- Return ONLY one JSON object.
- Do NOT return a list.
- Do NOT return multiple options.
- Do NOT add explanations, comments, or text.
- Do NOT add emojis.
- Field names must match the schema exactly.
- Types must match the schema exactly.
- All required fields must be present.

Text to extract from:
{text}

Return ONLY valid JSON.
"""