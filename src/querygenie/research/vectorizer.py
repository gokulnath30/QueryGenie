from sentence_transformers import SentenceTransformer

class Vectorizer:
    def __init__(self):
        self.text_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    def vectorize_text(self, texts):
        """Convert a list of texts to vectors."""
        return self.text_model.encode(texts)
    
    def vectorize_query(self, query):
        """Convert a query text to a vector."""
        return self.text_model.encode([query])
