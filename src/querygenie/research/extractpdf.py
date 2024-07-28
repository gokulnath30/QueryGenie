from langchain_community.document_loaders import PyPDFDirectoryLoader

class PDFTextExtractor:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.loader = PyPDFDirectoryLoader(directory_path)

    def extract_text(self):
        """Extract text from all PDF files in the directory."""
        documents = self.loader.load()
        texts = [doc.page_content for doc in documents]
        return texts

