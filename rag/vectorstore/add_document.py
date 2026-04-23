import numpy as np
from rag.embeddings.embedder import embed_text

def add_document(text: str):
    """
    Add a document to the vector store.

    Parameters
    ----------
    text : str
        The raw text content to store and embed.

    Returns
    -------
    dict
        A simple status dictionary.
    """

    # Generate an embedding for the provided text.
    # embed_text() returns {"embedding": [...]}, so we extract the vector.
    emb = embed_text(text)["embedding"]

    # Store the text and its embedding in the in-memory DB.
    VECTOR_DB.append({"text": text, "embedding": emb})

    # Return a simple confirmation.
    return {"status": "ok"}