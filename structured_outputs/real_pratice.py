from llms.groq_llm import groq_llm_call
from smart_extractor.extractor import smart_json_extractor
from structured_outputs.schemas.user_schema import User
from smart_extractor.prompt_builder import build_prompt

schema_dict = User.model_json_schema()

if __name__ == "__main__":
    prompt = build_prompt("User", schema_dict, "John Doe, 27, Lille")
    result = smart_json_extractor(
        schema=User,
        llm_call=lambda p: groq_llm_call(p, debug=True),
        prompt=prompt,
        max_retries=3,
    )

    print("\nFinal result:", result)