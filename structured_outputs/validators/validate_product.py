from pydantic import ValidationError
from structured_outputs.schemas.product_schema import Product

def validate_product_json(data: dict):
    try:
        product = Product(**data)
        print("VALID JSON:", product)
        return product
    except ValidationError as e:
        print("INVALID JSON:", e.errors())
        return None