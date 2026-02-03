from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
import sys


load_dotenv()

# Check if API key is set
api_key = os.getenv("GOOGLE_API_KEY", "").strip()
has_valid_key = api_key and api_key != "your_google_api_key_here" and api_key != "your_gemini_api_key_here"

if not has_valid_key:
    print("⚠️  WARNING: Google API key not set in .env file")
    print("To use real embeddings, set GOOGLE_API_KEY in .env")
    print("Get your API key from: https://ai.google.dev/")
    print("\n📝 Creating demo vectorstore with dummy embeddings...\n")
    
    # Create dummy embeddings for demo
    class DummyEmbeddings:
        def embed_documents(self, texts):
            return [[0.1] * 768 for _ in texts]
        def embed_query(self, text):
            return [0.1] * 768
    
    txt_path = "data/sample.txt"
    if not os.path.exists(txt_path):
        print(f"❌ {txt_path} not found!")
        sys.exit(1)
    
    loader = TextLoader(txt_path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    embeddings = DummyEmbeddings()
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local("vectorstore")
    print("✅ Demo vectorstore created successfully!")
    print("⚠️  Note: Using dummy embeddings. Add valid API key for real embeddings.\n")
