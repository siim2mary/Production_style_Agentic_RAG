import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# ================================
# API KEYS & SERVER
# ================================
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
PORT = int(os.getenv("PORT", 8000))

# ================================
# PATHS & DIRECTORIES
# ================================
DB_PATH = "faiss_index"
TEMP_DIR = "temp_uploads"

# ================================
# MODEL SETTINGS
# ================================
# The LLM "Brain"
LLM_MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"
# The Embedding "Translator"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ================================
# RAG PARAMETERS
# ================================
TOP_K = 3            # How many PDF chunks to read per question
CHUNK_SIZE = 800      # Size of each text piece
CHUNK_OVERLAP = 80    # Overlap to keep context between pieces