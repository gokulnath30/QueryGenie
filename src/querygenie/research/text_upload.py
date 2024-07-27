import os
import numpy as np

from extractpdf import PDFTextExtractor
from faiss_store import FAISSStorage
from vectorizer import Vectorizer

def process_pdfs(pdf_paths, output_dir):
    """Process a list of PDF files to extract text and store vectors in FAISS."""
    text_extractor = PDFTextExtractor()
    vectorizer = Vectorizer()
    faiss_storage = FAISSStorage()
    
    text_vectors = []
    all_texts = []

    for pdf_path in pdf_paths:
        # Extract text and convert to vectors
        texts = text_extractor.extract_text(pdf_path)
        vectors = vectorizer.vectorize_text(texts)
        text_vectors.extend(vectors)
        all_texts.extend(texts)

    # Convert list to numpy array
    vectors = np.array(text_vectors)
    
    # Initialize and store vectors and texts in FAISS index
    faiss_storage.initialize_index(vectors.shape[1])
    faiss_storage.add_vectors(vectors, all_texts)
    faiss_storage.save_index(os.path.join(output_dir, "vectors.index"))


if __name__ == "__main__":
    pdf_paths = ["static/sample1.pdf"] 
    output_dir = "output" 
    os.makedirs(output_dir, exist_ok=True)

    process_pdfs(pdf_paths, output_dir)
