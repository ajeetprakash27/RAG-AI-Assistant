# 🚀 QUICK REFERENCE GUIDE

## Start the Application

### Windows Quick Start
```batch
run.bat
```

### Manual Start (All Platforms)
```bash
python ingest.py
uvicorn app:app --reload
```

## Test the API

### curl (Command Line)
```bash
curl "http://127.0.0.1:8000/ask?q=What%20is%20RAG?"
```

### Python Code
```python
from rag_pipeline import ask_question
result = ask_question("What is Retrieval Augmented Generation?")
print(result)
```

### Browser
Open: `http://127.0.0.1:8000/ask?q=Your%20Question%20Here`

## Configuration

### Add Google API Key
Edit `.env`:
```env
GOOGLE_API_KEY=your_key_from_https://ai.google.dev/
```

### Add Documents
1. Place PDF or TXT files in `data/` folder
2. Run `python ingest.py`
3. Server uses updated vectorstore automatically

### Change Settings
Edit `config.py`:
- `CHUNK_SIZE` - Document chunk size
- `CHUNK_OVERLAP` - Overlap between chunks
- `RETRIEVER_K` - Number of documents to retrieve
- `API_PORT` - Server port

## Troubleshooting

### Port 8000 Already in Use
```bash
uvicorn app:app --port 8001 --reload
```

### Missing Vectorstore
```bash
python ingest.py
```

### Installation Issues
```bash
pip install -r requirements.txt --upgrade
```

### Module Not Found
```bash
pip install langchain langchain-community langchain-google-genai google-generativeai
```

## File Locations

| File | Purpose |
|------|---------|
| `app.py` | FastAPI server |
| `ingest.py` | Document processing |
| `rag_pipeline.py` | RAG logic |
| `config.py` | Settings |
| `.env` | API keys |
| `data/` | Documents folder |
| `vectorstore/` | Vector database |

## API Endpoint

- **URL**: `http://127.0.0.1:8000/ask`
- **Method**: GET
- **Parameter**: `q` (question)
- **Response**: JSON with "answer" field

## Example Requests

```bash
# Simple question
curl "http://127.0.0.1:8000/ask?q=How%20does%20RAG%20work?"

# Complex question
curl "http://127.0.0.1:8000/ask?q=What%20are%20the%20advantages%20of%20RAG%20systems?"

# With spaces (URL encoded)
curl "http://127.0.0.1:8000/ask?q=Explain%20Retrieval%20Augmented%20Generation%20in%20detail"
```

## Environment Variables

```env
GOOGLE_API_KEY         # Google Generative AI API key
PYTHONUNBUFFERED=1     # Real-time output (optional)
```

## Common Commands

```bash
# Show project structure
tree /F

# Check dependencies
pip list | findstr langchain

# Update packages
pip install -r requirements.txt --upgrade

# Run tests
python -c "from rag_pipeline import ask_question; print(ask_question('test'))"

# Check server
curl -s http://127.0.0.1:8000/ask?q=hello | findstr answer
```

## Performance Tips

1. **Faster Retrieval**: Reduce `RETRIEVER_K` in `config.py`
2. **Better Quality**: Increase `CHUNK_SIZE` for longer contexts
3. **Faster Ingestion**: Reduce `CHUNK_OVERLAP`
4. **Lower Memory**: Use smaller embedding models

## Deployment Options

- **Local**: `uvicorn app:app --host 127.0.0.1 --port 8000`
- **Production**: Use Gunicorn: `gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app`
- **Docker**: Create Dockerfile and deploy to containers
- **Cloud**: Deploy to Google Cloud, AWS, or Azure

## Documentation

- `README.md` - Full documentation
- `SETUP_SUMMARY.md` - Error resolution details
- `COMPLETION_REPORT.md` - Session completion report
- `config.py` - Configuration options

---

**Need more help?** Check `README.md` for detailed documentation.
