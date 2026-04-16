from pydantic import ValidationError
from structured_outputs.schemas.user_schema import User

def validate_user_json(data: dict):
    try:
        user = User(**data)
        print("VALID JSON:", user)
        return user
    except ValidationError as e:
        print("INVALID JSON:", e.errors())
        return None