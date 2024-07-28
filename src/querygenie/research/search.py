from querygenie.research.faiss_store import FAISSStorage
from querygenie.research.vectorizer import Vectorizer

def search_pdfs(query, faiss_storage, vectorizer, k=5):
    """Search for similar documents in the FAISS index based on a query."""
    # Convert the query to a vector
    query_vector = vectorizer.vectorize_query(query)
    
    # Perform the search in FAISS
    distances, indices = faiss_storage.search(query_vector, k)
    
    # Retrieve the associated texts
    texts = faiss_storage.get_texts(indices)
    
    return texts

if __name__ == "__main__":
    # Example usage
    index_path = "output/vectors.index"
    
    # Initialize FAISS storage and load the index
    faiss_storage = FAISSStorage()
    faiss_storage.load_index(index_path)
    
    # Initialize the vectorizer
    vectorizer = Vectorizer()
    
    # Define a query
    query = "Title Deed card"
    
    # Perform the search
    results = search_pdfs(query, faiss_storage, vectorizer)
    
    # Print the results
    for result in results:
        print(result)