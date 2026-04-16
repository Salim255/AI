from llms.groq_llm import groq_llm_call
from smart_extractor.extractor import smart_json_extractor
from structured_outputs.schemas.user_schema import User


if __name__ == "__main__":
    prompt = (
        "Extract a JSON object matching this schema: "
        "User { fullName: string, age: integer, country: string } "
        "from the text: 'John Doe, 27, France'. "
        "Return ONLY JSON."
    )
    result = smart_json_extractor(
        schema=User,
        llm_call=lambda p: groq_llm_call(p, debug=True),
        prompt=prompt,
        max_retries=3,
    )

    print("\nFinal result:", result)