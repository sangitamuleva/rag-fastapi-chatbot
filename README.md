# rag-fastapi-chatbot

📄 Document-Based Chatbot using RAG (FastAPI + FAISS)
A Retrieval-Augmented Generation (RAG) based document chatbot built using FastAPI, FAISS, and local embedding models.
This application allows users to upload PDF documents and ask natural language questions, with answers generated from document content.


✅ Note: Embeddings are generated locally (no paid GenAI embedding APIs used).

🚀 Features
📄 Upload PDF documents
✂️ Text chunking for large documents
🔍 Vector search using FAISS
🧠 Local embedding generation (free & offline)
🤖 LLM-based answer generation
⚡ FastAPI backend
📘 Interactive Swagger UI
🏗️ Tech Stack

Backend: FastAPI
Vector Store: FAISS
Embeddings: Local embedding model (SentenceTransformers)
LLM: Gemini / any compatible LLM
PDF Processing: pdfplumber
Language: Python 3.11+


🧠 How RAG Works (Local Embeddings)
PDF is uploaded
Text is extracted
Text is split into chunks
Embeddings are generated locally
Stored in FAISS vector index
User query is embedded locally
Relevant chunks retrieved
LLM generates final answer using retrieved context

💡 Why Local Embeddings?
✅ Free (no API cost)
✅ No rate limits
✅ Privacy-friendly
✅ Suitable for production
✅ Faster local development

🛡️ Security Notes
.env is ignored in Git
Uploaded files are not committed
FAISS index files are ignored
No paid embedding APIs used

📈 Future Enhancements
Multi-document chat
Persistent FAISS storage
Chat memory
Authentication
UI frontend
Streaming responses

🧑‍💻 Author
Sangi
Software Developer | FastAPI | RAG | FAISS | Generative AI

⭐ Support
If you find this project useful:
⭐ Star the repo
🍴 Fork it
💼 Use it for learning & interviews