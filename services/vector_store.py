import faiss
import numpy as np

class FaissStore:
    def _init_(self, dimension: int):
        self.index = faiss.IndexFlatIP(dimension)
        self.metadata = []

    def add_documents(self, embeddings, metadata):
        self.index.add(np.array(embeddings))
        self.metadata.extend(metadata)

    def search(self, query_embedding, k=5):
        scores, indices = self.index.search(
            np.array([query_embedding]), k
        )
        return [self.metadata[i] for i in indices[0] if i != -1]