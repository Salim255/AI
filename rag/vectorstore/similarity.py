import numpy as np
from rag.embeddings.embedder import embed_text
from rag.vectorstore.store import VECTOR_DB

def search(query: str, top_k: int = 3):
    """
    Perform semantic search over the vector store.

    Parameters
    ----------
    query : str
        The user query to embed and compare.
    top_k : int
        Number of top results to return.

    Returns
    -------
    dict
        A dictionary containing the list of retrieved texts.
    """

    # Convert the query into an embedding vector.
    q_emb = np.array(embed_text(query)["embedding"])

    # This list will store tuples of (similarity_score, document_text).
    scored = []

    # Iterate over every stored document in the vector DB.
    for doc in VECTOR_DB:
        # Convert stored embedding to NumPy array for math operations.
        d_emb = np.array(doc["embedding"])

        # Compute cosine similarity:
        # score = (q ⋅ d) / (||q|| * ||d||)
        score = np.dot(q_emb, d_emb) / (np.linalg.norm(q_emb) * np.linalg.norm(d_emb))

        # Store the score and the document text.
        scored.append((score, doc["text"]))

    # Sort results by similarity score (highest first).
    scored.sort(reverse=True)

    # Extract only the text of the top_k results.
    return {"results": [text for _, text in scored[:top_k]]}
