from typing import Callable, Any, Optional, Type, Dict
from pydantic import BaseModel

from smart_extractor.retry_loop import retry_until_valid
from llms.groq_llm import groq_llm_call

def smart_json_extractor(
    schema: Type[BaseModel],
    llm_call: groq_llm_call,
    prompt: str,
    max_retries: int = 3,
) -> Optional[BaseModel]:
    """
    Orchestrates:
    - LLM call
    - validation
    - correction
    - retry
    Returns a validated Pydantic model instance or None.

    schema: Pydantic model class
    llm_fn: function that takes a prompt and returns JSON output
    prompt: the prompt to send to the LLM
    max_retries: how many times to retry if validation fails
    """
    def model_fn():
        # 1) Call the LLM with the original prompt
        return llm_call(prompt)

    def llm_correction_fn(instructions: str):
        # 2) Ask the LLM to correct its previous answer
        #    by sending the correction instructions as a new prompt
        return llm_call(instructions)

    # 3) Use the retry loop to validate and correct until valid or max retries reached
    return retry_until_valid(
        schema, 
        model_fn, 
        llm_fn=llm_correction_fn, 
        max_retries=max_retries
    )
