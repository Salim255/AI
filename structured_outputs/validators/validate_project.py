from structured_outputs.schemas.project_schema import Project
from pydantic import ValidationError

def validate_project_json(data: dict):
    try:
        project = Project(**data)
        print("VALID JSON:", project)
        return project
    except ValidationError as e:
        print("INVALID JSON:", e.errors())
        return None 