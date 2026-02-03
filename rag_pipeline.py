# rag_pipeline.py
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

# Dummy embeddings class for demo without API key
class DummyEmbeddings:
    def embed_documents(self, texts):
        return [[0.1] * 768 for _ in texts]
    def embed_query(self, text):
        return [0.1] * 768
    def __call__(self, text):
        return [0.1] * 768

# Check if API key is valid
api_key = os.getenv("GOOGLE_API_KEY", "").strip()
has_valid_key = api_key and api_key not in ["your_google_api_key_here", "your_gemini_api_key_here"]

# Load embeddings
if has_valid_key:
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
else:
    embeddings = DummyEmbeddings()

# Load FAISS vectorstore
db = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)
retriever = db.as_retriever()

# Initialize LLM
if has_valid_key:
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)
else:
    llm = None

# Simple QA function
def ask_question(query):
    """Answer questions based on retrieved documents"""
    if not has_valid_key:
        retrieved_docs = retriever.invoke(query)
        docs_text = "\n\n".join([doc.page_content for doc in retrieved_docs])
        return f"Demo Mode (no API key). Retrieved context:\n{docs_text}\n\nAdd a valid Google API key to enable LLM responses."
    
    # Retrieve relevant documents
    retrieved_docs = retriever.invoke(query)
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])
    
    # Generate answer using LLM
    prompt = f"""Based on the following context, answer the question.

Context:
{context}

Question: {query}

Answer:"""
    
    response = llm.invoke(prompt)
    return response.content if hasattr(response, 'content') else str(response)
