from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from services.rag_pipeline import rag_pipeline_generate
from services.document_loader import load_pdf
from services.chunking import create_chunks_with_metadata
from services.embedding import embed_text
from services.retriever import build_index
import os, shutil


app = FastAPI()


class QueryRequest(BaseModel):
    question: str


@app.post("/ask")
def ask_question(req: QueryRequest):
    answer = rag_pipeline_generate(req.question)
    return {"answer": answer}


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error": "file extension not supported. Only PDF files are accepted."}
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # load pdf
    pages = load_pdf(file_path)

    # chunk data
    chunks= create_chunks_with_metadata(pages)

    # create embedding
    embeddings=[]
    metadata=[]

    for c in chunks:
        emb=embed_text(c["content"])
        embeddings.append(emb)
        metadata.append(c)

    #build FAISS index it will called once while uploading pdf
    build_index(embeddings, metadata)

    return {"message":"PDF uploaded and indexed successfully!,now ready for Q & A","chunks":len(chunks)}
