import faiss
import numpy as np


# this function called once
def build_index(embeddings,metadata):
    global index,metadata_store
    dimension=embeddings.shape[1]
    index=faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype("float32"))
    metadata_store=metadata

# used during every user questions
def retrieve(query_embedding,k=3):
    distances, indices = index.search(np.array([query_embedding]),k)
    results=[]
    for i in indices[0]:
        results.append(metadata_store[i])
    return results