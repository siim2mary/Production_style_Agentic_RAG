"""
ARCHITECTURE: Agentic RAG Knowledge System

FLOW:

1. USER → FastAPI (/ask endpoint)
2. REQUEST → LangGraph Agent

3. SUPERVISOR NODE:
   - Decides:
     → vector_store (RAG)
     → web_search (Tavily)
     → direct_answer (LLM)

4. TOOL EXECUTION:
   A. Vector Store:
      - FAISS similarity search
      - Retrieve top-k chunks
      - Return context + metadata

   B. Web Search:
      - Tavily API call
      - Extract content + URLs

5. GENERATION NODE:
   - Combine:
     → Context
     → Chat history
   - LLM generates grounded answer

6. MEMORY:
   - Thread-based conversation store
   - Maintains last N interactions

7. RESPONSE:
   - Answer
   - Sources
   - Decision path

----------------------------------------

KEY COMPONENTS:

- FastAPI → API layer
- LangGraph → Agent orchestration
- FAISS → Vector DB
- HuggingFace → Embeddings
- OpenAI GPT → Reasoning
- Tavily → Web search tool

----------------------------------------

SCALABILITY (Production Plan):

- Replace FAISS → Pinecone / Weaviate
- Replace memory → Redis
- Add → Authentication
- Add → Logging (LangSmith)
- Deploy → Docker + AWS

----------------------------------------
"""