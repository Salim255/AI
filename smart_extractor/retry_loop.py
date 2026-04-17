from pydantic import ValidationError
from smart_extractor.corrector import generate_correction_instructions

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
