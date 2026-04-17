def build_task_description(schema_name: str, schema: dict) -> str:
    properties = schema.get("properties", {})
    fields = ", ".join(
        f"{name} ({details.get('type', 'unknown')})"
        for name, details in properties.items()
    )

    return f"""
You MUST extract exactly ONE JSON object that matches this schema:

{schema_name} {{ {fields} }}

### REQUIRED FIELDS (always generate them)
- title: generate a short, clear title summarizing the task.
- description: generate a concise description (1–2 sentences).
- story_points: generate a reasonable integer estimate (1–13).
- status: default to "todo" unless the text explicitly indicates progress.

### OPTIONAL FIELDS (do NOT guess)
If the text does NOT explicitly provide these fields, set them to null:
- id
- assignee
- sprint_id
- project_id

### STRICT RULES
- Return ONLY one JSON object.
- Do NOT return a list.
- Do NOT return multiple options.
- Do NOT add explanations, comments, or text.
- Do NOT add emojis.
- Field names must match the schema exactly.
- Types must match the schema exactly.
- Do NOT infer optional fields.
- Only infer the required fields listed above.

### TEXT TO EXTRACT FROM
{text}

Return ONLY valid JSON.
"""

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