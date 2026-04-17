from structured_outputs.schemas.sprint_schema import Sprint
from pydantic import ValidationError

def validate_sprint_json(data: dict):
    try:
        sprint = Sprint(**data)
        print("VALID JSON:", sprint)
        return sprint
    except ValidationError as e:    
        print("INVALID JSON:", e.errors())
        return None