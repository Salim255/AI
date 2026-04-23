from pydantic import ValidationError
from smart_extractor.corrector import generate_correction_instructions

def retry_first_tool_call_until_valid(llm_fn, messages, tools, max_retries=3):
    """
    Retries the FIRST model call until a valid tool call is returned.
    
    llm_fn: the LLM function (e.g., client.chat.completions.create)
    messages: list of messages for the first call
    tools: list of tool schemas
    """
    last_error = None

    for attempt in range(max_retries):
        print(f"🔁 First-call attempt {attempt+1}/{max_retries}")

        try:
            response = llm_fn(messages=messages, tools=tools)
        except Exception as e:
            last_error = e
            print("❌ LLM error:", e)
            continue

        tool_calls = response.get("tool_calls")

        if tool_calls:
            # SUCCESS
            return response

        print("⚠️ Model did not return a tool call. Retrying...")

    # FAILED AFTER RETRIES
    print("❌ Model failed to return a tool call after retries.")
    return None


def retry_until_valid(schema, model_fn, llm_fn=None, max_retries=3):
    """
    schema: Pydantic model
    model_fn: function that generates JSON (LLM or fake)
    llm_fn: optional function that takes correction instructions and returns corrected JSON
    """
    for attempt in range(max_retries):
        output = model_fn()
        try:
            return schema(**output)
        except ValidationError as e:
            print(f"Attempt {attempt+1} failed:", e.errors(), "👹👹", llm_fn)

            if llm_fn is None:
                continue  # fallback: retry without correction

            # Generate correction instructions
            instructions = generate_correction_instructions(e)

            # Ask the LLM to correct the JSON
            corrected = llm_fn(instructions)

            # VALIDATE THE CORRECTED JSON IMMEDIATELY
            try:
                return schema(**corrected)
            except ValidationError as e2:
                print("Corrected JSON still invalid:", e2.errors())
    return None
