# In-memory vector database.
# Each entry is a dictionary:
# {
#   "text": "original text chunk",
#   "embedding": [float, float, ...]
# }
#
# This is intentionally simple for learning and debugging.
# Later, you can replace it with FAISS, Chroma, Pinecone, etc.
VECTOR_DB = []
