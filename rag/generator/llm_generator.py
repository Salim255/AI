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

class LLMGenerator:
    def __init__(self, llm):
        """
        Constructor receives an LLM client instance.
        
        The LLM must expose a `.generate(prompt)` method.
        This keeps the generator independent of the LLM provider
        (OpenAI, Groq, Anthropic, local model, etc.).
        """
        self.llm = llm

    # --------------------------------------------------------
    # Build the RAG prompt
    # --------------------------------------------------------
    def build_prompt(self, query, context_chunks):
        """
        Build a structured, deterministic RAG prompt.

        WHY this format?
        - Forces the LLM to use ONLY the retrieved context.
        - Prevents hallucinations.
        - Makes the system predictable and testable.
        - Industry-standard RAG prompt structure.
        """

        # Format the context as a numbered list for clarity.
        context_text = "\n".join(
            [f"{i+1}. {chunk}" for i, chunk in enumerate(context_chunks)]
        )

        # Final RAG prompt template.
        return f"""
            Use ONLY the context below to answer the question.

            Context:
            {context_text}

            Question:
            {query}

            If the answer is not in the context, say: "I don't know."
            Answer:
            """

    # --------------------------------------------------------
    # Generate the final answer using the LLM
    # --------------------------------------------------------
    def generate_answer(self, query, context_chunks):
        """
        Build the prompt → send to LLM → return final answer.

        This is the GENERATION phase of RAG.
        Retrieval happens earlier in rag_pipeline.py.
        """
        prompt = self.build_prompt(query, context_chunks)
        return self.llm.generate(prompt)
