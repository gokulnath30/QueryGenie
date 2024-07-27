import os
import numpy as np

from faiss_store import FAISSStorage
from vectorizer import Vectorizer

def search_pdfs(query, faiss_storage, vectorizer, k=5):
    """Search for similar documents in the FAISS index based on a query."""
    # Convert the query to a vector
    query_vector = vectorizer.vectorize_query(query)
    
    # Perform the search in FAISS
    distances, indices = faiss_storage.search(query_vector, k)
    
    # Retrieve the associated texts
    texts = faiss_storage.get_texts(indices)
    
    return distances, indices, texts


if __name__ == "__main__":
    output_dir = "output"
    
    # Load the FAISS index for searching
    faiss_storage = FAISSStorage()
    faiss_storage.load_index(os.path.join(output_dir, "vectors.index"))
    
    # Initialize the vectorizer
    vectorizer = Vectorizer()
    
    query = "sample search query"
    distances, indices, texts = search_pdfs(query, faiss_storage, vectorizer, k=5)
    
    print("Distances:", distances)
    print("Indices:", indices)
    print("Texts:", texts)

