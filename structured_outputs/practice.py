from validators.validate_user import validate_user_json

# Fake model output (tu peux le casser pour tester)
model_output = {
    "fullName": "John Doe",
    "age": 27,
    "city": "Berlin"
}
# Validate the model output
validated_user = validate_user_json(model_output)
