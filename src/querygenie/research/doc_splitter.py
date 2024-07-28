from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

class DocumentSplitter:
    def __init__(self, chunk_size=800, chunk_overlap=80, length_function=len, is_separator_regex=False):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=length_function,
            is_separator_regex=is_separator_regex,
        )

    def split_documents(self, documents: list[Document]):
        """Split documents into chunks."""
        return self.text_splitter.split_documents(documents)

if __name__ == "__main__":
    # Example usage
    documents = [Document(page_content="Example text content.")]
    splitter = DocumentSplitter()
    chunks = splitter.split_documents(documents)
    
    for chunk in chunks:
        print(chunk)