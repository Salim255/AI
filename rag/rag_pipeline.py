from rag.vectorstore.similarity import search

def rag_answer(query: str):
    """
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

    # Perform semantic search using the vector store.
    retrieved = search(query)["results"]

    # Return both the query and the retrieved context.
    # The LLM will use this context to generate a grounded answer.
    return {
        "query": query,
        "context": retrieved
    }
