from validators.validate_user import validate_user_json
from validators.validate_transaction import validate_transaction_json


# Example of validating a user JSON output from a model
transaction_model_output = {
    "transactionId": "12345",
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
    "age": 27,
    "city": "Berlin"
}
# Validate the model output
validated_user = validate_user_json(model_output)
