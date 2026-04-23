# This schema defines the "search_documents" tool.
# The LLM uses this tool when it needs to retrieve relevant documents
# from the vector store.

retriever_tool_schema = {
    "type": "function",
    "function": {
        "name": "search_documents",  # Tool name exposed to the LLM
        "description": "Retrieve the most relevant documents for a query.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},   # The search query
                "top_k": {"type": "integer"}   # Optional: number of results
            },
            "required": ["query"]  # Only "query" is mandatory
        }
    }
}
