from llms.openai_llm import openai_llm_call
from smart_extractor.extractor import smart_json_extractor
from structured_outputs.schemas.user_schema import User


if __name__ == "__main__":
    prompt = (
        "Extract a JSON object matching this schema: "
        "User { fullName: string, age: integer, city: string } "
        "from the text: 'John Doe, 27, Berlin'. "
        "Return ONLY JSON."
    )
    result = smart_json_extractor(
        schema=User,
        llm_call=openai_llm_call,
        prompt=prompt,
        max_retries=3,
    )

    print("\nFinal result:", result)