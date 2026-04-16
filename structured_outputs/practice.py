from structured_outputs.validators.validate_user import validate_user_json
from structured_outputs.validators.validate_transaction import validate_transaction_json
from structured_outputs.validators.validate_product import validate_product_json
from smart_extractor.retry_loop import retry_until_valid
from structured_outputs.schemas.user_schema import User
from smart_extractor.extractor import smart_json_extractor
# Example of validating a product JSON output from a model
product_model_output = {
    "id": "abc123",
    "name": "Smartphone",
    "price": 299.99,
    "features": [
        {"name": "Screen Size", "value": "6.5 inches"},
        {"name": "Battery Life", "value": "24 hours"}
    ]
}
# Validate the product model output
validated_product = validate_product_json(product_model_output)


# Example of validating a user JSON output from a model
transaction_model_output = {
    "id": "12345",
    "amount": 100.0,
    "currency": "USD",
    "status": "pending",
    "timestamp": "2023-01-01T00:00:00Z"
}
# Validate the transaction model output
validated_transaction = validate_transaction_json(transaction_model_output)

# Fake model output (tu peux le casser pour tester)
model_output = {
    "fullName": "John Doe",
    "age": "do@e",  # string instead of int
    "city": "Berlin"
}
# Validate the model output
validated_user = validate_user_json(model_output)

def fake_model_output():
    return {
        "fullName": "John Doe",
        "age": "27dsdsds",  # string instead of int
        "city": "Berlin"
    }

result = retry_until_valid(User, fake_model_output)
#print("Result:", result)

def fake_llm_correction(instructions):
    print("\nLLM received correction instructions:")
    print(instructions)

    # Simulate corrected JSON
    return {
        "fullName": "John Doe",
        "age": "27",
        "city": "Berlin"
    }
result_with_correction = retry_until_valid(User, fake_model_output, llm_fn=fake_llm_correction)
#print("Final result:", result_with_correction)

def fake_llm(prompt: str):
    print("\nLLM PROMPT:")
    print(prompt)

    # First call: return invalid JSON
    if "Fix the JSON" not in prompt:
        return {
            "fullName": "John Doe",
            "age": "27dsdsds",
            "city": "Berlin",
        }

    # Correction call: return valid JSON
    return {
        "fullName": "John Doe",
        "age": 27,
        "city": "Berlin",
    }

if __name__ == "__main__":
    prompt = "Extract a User object with fullName, age, city from: 'John Doe, 27, Berlin'"
    result = smart_json_extractor(User, fake_llm, prompt, max_retries=3)
    print("\nFinal result:", result)