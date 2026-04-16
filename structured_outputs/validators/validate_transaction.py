from pydantic import ValidationError
from schemas.transaction_schema import Transaction


def validate_transaction_json(data: dict):
    try:
        transaction = Transaction(**data)
        print("VALID JSON:", transaction)
        return transaction
    except ValidationError as e:
        print("INVALID JSON:", e.errors())
        return None
