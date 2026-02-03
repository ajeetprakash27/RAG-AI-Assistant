# RAG AI Assistant

A Retrieval Augmented Generation (RAG) system that combines document embeddings with Google Generative AI for intelligent Q&A.

## Project Structure

```
RAG-AI-Assistant/
├── app.py              # FastAPI application
├── ingest.py           # Document ingestion and vectorization
├── rag_pipeline.py     # RAG pipeline for Q&A
├── requirements.txt    # Python dependencies
├── .env               # Environment configuration (API keys)
├── data/              # Document storage
│   └── sample.txt     # Sample document for testing
└── vectorstore/       # FAISS vector database
```

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Key (Optional)
Edit `.env` file:
```
GOOGLE_API_KEY=your_actual_google_api_key_here
```

Get your API key from: https://ai.google.dev/

### 3. Ingest Documents
```bash
python ingest.py
```

This creates embeddings and stores them in the FAISS vectorstore.

## Usage

### Run FastAPI Server
```bash
uvicorn app:app --reload
```

API endpoint: `http://127.0.0.1:8000/ask?q=your_question`

### Example Request
```bash
curl "http://127.0.0.1:8000/ask?q=What%20is%20RAG?"
```

## Features

- **Document Processing**: Supports PDF and text files
- **Vector Embeddings**: Uses Google Generative AI embeddings
- **FAISS Database**: Efficient similarity search
- **FastAPI Server**: RESTful API endpoint
- **Demo Mode**: Works without API key using dummy embeddings

## Demo Mode

If `GOOGLE_API_KEY` is not set or invalid, the system runs in demo mode:
- ✅ Document ingestion works
- ✅ Retrieval works
- ❌ LLM responses are limited (returns retrieved context only)

## Technologies Used

- **LangChain**: Framework for building LLM applications
- **FAISS**: Facebook AI Similarity Search
- **FastAPI**: Modern Python web framework
- **Google Generative AI**: LLM and embedding models

## Troubleshooting

### Import Errors
Make sure all packages are installed:
```bash
pip install langchain langchain-community langchain-google-genai faiss-cpu fastapi uvicorn pypdf python-dotenv google-generativeai
```

### API Key Invalid
Add a valid Google API key to `.env` or use demo mode.

### Vectorstore Not Found
Run `python ingest.py` first to create the vectorstore.

## Notes

- Demo mode uses dummy embeddings (768-dim vectors of 0.1)
- For production use, add a valid Google API key
- The system is designed for CPU-based inference (faiss-cpu)
