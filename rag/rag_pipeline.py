from rag.vectorstore.similarity import search
from rag.vectorstore.similarity import search
from rag.generator.llm_generator import LLMGenerator
from llms.client import llm   # whatever LLM client you use


def rag_answer(query: str):
    """
    Full RAG pipeline:
    1. Retrieve relevant documents (semantic search)
    2. Build RAG prompt
    3. Generate grounded answer using the LLM
    High-level RAG pipeline step:
    - Retrieve relevant documents
    - Return them as context for the LLM

    Parameters
    ----------
    query : str
        The user question.

    Returns
    -------
    dict
        Contains:
        - the original query
        - the retrieved context (list of text chunks)
    """

    # -----------------------------
    # STEP 1 — RETRIEVAL
    # -----------------------------
    # Perform semantic search using the vector store.
    retrieved = search(query)["results"]   # list of top‑K text chunks

    # If nothing relevant found → avoid hallucinations
    if not retrieved:
        return {
            "query": query,
            "context": [],
            "answer": "I don't know."
        }

    # -----------------------------
    # STEP 2 — GENERATION
    # -----------------------------
    generator = LLMGenerator(llm)  # LLM wrapper
    final_answer = generator.generate_answer(query, retrieved)

    # -----------------------------
    # STEP 3 — RETURN STRUCTURED OUTPUT
    # -----------------------------
    return {
        "query": query,
        "context": retrieved,
        "answer": final_answer
    }
