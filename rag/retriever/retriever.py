# rag/retriever/retriever.py
from rag.vectorstore.similarity import search

class Retriever:
    def retrieve(self, query: str):
        """
        Returns top‑K text chunks (strings only).
        No LLM. No validation. No retry.
        """
        return search(query)["results"]
