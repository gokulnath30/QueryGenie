import os
import numpy as np
from querygenie.research.extractpdf import PDFTextExtractor
from querygenie.research.faiss_store import FAISSStorage
from querygenie.research.vectorizer import Vectorizer
from langchain.schema.document import Document
from querygenie.research.doc_splitter import DocumentSplitter

def process_pdfs(pdf_directory, output_dir):
    """Process PDF files in a directory to extract text, split into chunks, vectorize, and store in FAISS."""
    # Initialize components
    text_extractor = PDFTextExtractor(pdf_directory)
    splitter = DocumentSplitter()
    vectorizer = Vectorizer()
    faiss_storage = FAISSStorage()
    
    # Extract text from PDFs
    texts = text_extractor.extract_text()
    
    # Split texts into chunks
    documents = [Document(page_content=text) for text in texts]
    chunks = splitter.split_documents(documents)
    
    # Vectorize text chunks
    chunk_texts = [chunk.page_content for chunk in chunks]
    vectors = vectorizer.vectorize_text(chunk_texts)
    
    # Convert list to numpy array
    vectors = np.array(vectors)
    
    # Initialize and store vectors and texts in FAISS index
    faiss_storage.initialize_index(vectors.shape[1])
    faiss_storage.add_vectors(vectors, chunk_texts)
    faiss_storage.save_index(os.path.join(output_dir, "vectors.index"))

if __name__ == "__main__":
    # Example usage
    pdf_directory = "dataset/sample"
    output_dir = "models"
    process_pdfs(pdf_directory, output_dir)