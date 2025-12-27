import faiss
import numpy as np


# this function called once
def build_index(embeddings, metadata):
    global index, metadata_store
    embeddings = np.array(embeddings).astype("float32")
    if embeddings is None or len(embeddings) == 0:
        raise ValueError("No embeddings created. PDF may be empty or scanned")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    metadata_store = metadata


# used during every user questions
def retrieve(query_embedding, k=3):
    distances, indices = index.search(np.array([query_embedding]), k)
    results = []
    for i in indices[0]:
        results.append(metadata_store[i])
    return results
