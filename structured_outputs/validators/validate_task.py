from structured_outputs.schemas.task_schema import Task
from pydantic import ValidationError

def validate_task_json(data: dict):
    try:
        task = Task(**data)
        print("VALID JSON:", task)
        return task
    except ValidationError as e:
        print("INVALID JSON:", e.errors())
        return None