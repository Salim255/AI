# rag/prompt/rag_prompt_builder.py
# ----------------------------------------------------
# Single responsibility:
# Build the RAG prompt using the query + top chunks.
# No LLM. No retry. No validation.
# ----------------------------------------------------

class RAGPromptBuilder:
    @staticmethod
    def build(query: str, context_chunks: list[str]) -> str:
        """
        Build a clean, deterministic RAG prompt.
        """
        context_text = "\n".join(
            f"{i+1}. {chunk}" for i, chunk in enumerate(context_chunks)
        )

        return f"""
Use ONLY the context below to answer the question.

Context:
{context_text}

Question:
{query}

Return JSON:
{{
  "answer": "<your answer>"
}}

If the answer is not in the context, return:
{{
  "answer": "I don't know."
}}
"""
