# rag/validator/rag_validator.py
from pydantic import BaseModel
from smart_extractor.retry_loop import retry_until_valid

class RAGAnswer(BaseModel):
    answer: str

class RAGValidator:
    def __init__(self, llm):
        self.llm = llm

    def validate(self, raw_output_fn):
        """
        raw_output_fn: function that calls the LLM and returns raw JSON
        """
        def model_fn():
            return raw_output_fn()

        def llm_correction_fn(instructions: str):
            return self.llm.generate(
                "Fix the JSON according to these instructions:\n" + instructions
            )

        validated = retry_until_valid(
            schema=RAGAnswer,
            model_fn=model_fn,
            llm_fn=llm_correction_fn,
            max_retries=4
        )

        return validated.answer if validated else "I don't know."
