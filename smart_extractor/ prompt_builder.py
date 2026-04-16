def build_prompt(schema_name: str, schema: dict, text: str) -> str:
    fields = ", ".join(f"{k}: {v.__name__}" for k, v in schema.items())
    return f"""
Extract a JSON object matching this schema:

{schema_name} {{ {fields} }}

From this text:
{text}

Return ONLY valid JSON.
"""