from pydantic import ValidationError

def generate_correction_instructions(errors: ValidationError):
    """
    Convert Pydantic validation errors into human-readable correction instructions
    for the LLM.
    """
    print("Generating correction instructions for errors: 🔥🔥\n", errors.errors())
    instructions = ["Fix the JSON according to these rules:"]

    for error in errors.errors():
        field = ".".join(str(loc) for loc in error['loc'])
        msg = error['msg']
        input_value = error.get("input", None)
        instructions.append(
            f"- Field '{field}' is invalid: {msg}. Received: {input_value}"
        )
    instructions.append("Return ONLY corrected JSON. No explanations.")
    return "\n".join(instructions)