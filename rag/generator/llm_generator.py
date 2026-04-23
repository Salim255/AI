# ============================================
# LLMGenerator
# --------------------------------------------
# This class is responsible ONLY for:
#   - Building the RAG prompt (context + question)
#   - Sending the prompt to the LLM
#   - Returning the final grounded answer
#
# It does NOT:
#   - Retrieve embeddings
#   - Search the vector store
#   - Chunk documents
#
# Clean separation of concerns → scalable architecture.
# ============================================

# rag/generator/llm_generator.py

class LLMGenerator:
    def __init__(self, llm):
        self.llm = llm

    def build_prompt(self, query, context_chunks):
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
        """

    def generate_raw(self, query, context_chunks):
        """
        Returns RAW LLM output (dict or string).
        No validation. No retry.
        """
        prompt = self.build_prompt(query, context_chunks)
        return self.llm.generate(prompt)
