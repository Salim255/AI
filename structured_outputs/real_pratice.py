from llms.groq_llm import groq_llm_call
from smart_extractor.extractor import smart_json_extractor
from structured_outputs.schemas.task_schema import Task
from structured_outputs.schemas.task_schema import Task
from structured_outputs.schemas.user_schema import User
from smart_extractor.prompt_builder import build_prompt

schema_dict = Task.model_json_schema()

if __name__ == "__main__":
    prompt = build_prompt("Task", schema_dict, "Create me task id:456 for project with id 123 to complete the project documentation by next week")
    result = smart_json_extractor(
        schema=Task,
        llm_call=lambda p: groq_llm_call(p, debug=True),
        prompt=prompt,
        max_retries=3,
    )

    print("\nFinal result:", result)