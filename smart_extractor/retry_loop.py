from pydantic import ValidationError

def retry_until_valid(schema, model_fn, max_retries=3):
    for attempt in range(max_retries):
        output = model_fn()
        try:
            return schema(**output)
        except ValidationError as e:
            print(f"Attempt {attempt+1} failed:", e.errors())
    return None
