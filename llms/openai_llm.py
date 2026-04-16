import json
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def openai_llm_call(prompt: str) -> dict:
    """
    Calls an OpenAI model and expects pure JSON in the response.
    """
    response = client.chat.completions.create(
        model="gpt-4.1-mini",  # or another model
        messages=[
             {
                "role": "system",
                "content": (
                    "You are a strict JSON generator. "
                    "You ONLY respond with valid JSON, no explanations, no extra text."
                ),
            },
            {
                "role": "user", 
                "content": prompt,
            }
        ],
        response_format={"type": "json_object"}
    )
    content =  response.choices[0].message.content
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        # Fallback: try to extract JSON or raise
        print("LLM returned invalid JSON:", content)
        raise ValueError(f"Model did not return valid JSON: {content}")
