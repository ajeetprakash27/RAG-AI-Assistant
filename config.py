"""Configuration for RAG AI Assistant"""
import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "").strip()
HAS_VALID_API_KEY = (
    GOOGLE_API_KEY 
    and GOOGLE_API_KEY not in ["your_google_api_key_here", "your_gemini_api_key_here"]
)

# Model Configuration
EMBEDDING_MODEL = "models/embedding-001"
LLM_MODEL = "gemini-pro"
LLM_TEMPERATURE = 0

# Vector Store Configuration
VECTORSTORE_PATH = "vectorstore"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# API Configuration
API_HOST = "127.0.0.1"
API_PORT = 8000

# Document paths
DATA_DIR = "data"
SAMPLE_PDF_PATH = os.path.join(DATA_DIR, "sample.pdf")
SAMPLE_TXT_PATH = os.path.join(DATA_DIR, "sample.txt")

# Retriever configuration
RETRIEVER_K = 3  # Number of documents to retrieve
