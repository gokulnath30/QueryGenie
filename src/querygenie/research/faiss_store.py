import faiss
import numpy as np

class FAISSStorage:
    def __init__(self):
        self.index = None
        self.texts = []  # To store the texts associated with each vector

    def initialize_index(self, dim):
        """Initialize a FAISS index with the given dimension."""
        self.index = faiss.IndexFlatL2(dim)

    def add_vectors(self, vectors, texts):
        """Add vectors to the FAISS index and store associated texts."""
        if self.index is None:
            raise ValueError("FAISS index is not initialized.")
        self.index.add(vectors)
        self.texts.extend(texts)

    def save_index(self, file_path):
        """Save the FAISS index to a file."""
        faiss.write_index(self.index, file_path)
        # Save texts separately
        with open(file_path + ".texts", "w") as f:
            for text in self.texts:
                f.write(text + "\n")

    def load_index(self, file_path):
        """Load a FAISS index from a file."""
        self.index = faiss.read_index(file_path)
        # Load texts from file
        with open(file_path + ".texts", "r") as f:
            self.texts = [line.strip() for line in f]

    def search(self, query_vector, k=5):
        """Search for the k nearest neighbors of the query vector."""
        if self.index is None:
            raise ValueError("FAISS index is not initialized.")
        distances, indices = self.index.search(query_vector, k)
        return distances, indices

    def get_texts(self, indices):
        """Retrieve the texts associated with the indices."""
        return [self.texts[i] for i in indices[0]]
