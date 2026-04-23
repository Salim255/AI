from rag.vectorstore.store import add_document, VECTOR_DB
from rag.vectorstore.similarity import search
from rag.rag_pipeline import rag_answer

print("\n=== STEP 1: Add documents ===")
add_document("Paris is the capital of France.")
add_document("The Eiffel Tower is located in Paris.")
add_document("Tokyo is the capital of Japan.")
print(f"Vector DB size: {len(VECTOR_DB)}")

print("\n=== STEP 2: Test semantic search ===")
results = search("capital of France")
print("Search results:", results)

print("\n=== STEP 3: Test full RAG pipeline ===")
rag = rag_answer("What is the capital of France?")
print("RAG answer:", rag)


