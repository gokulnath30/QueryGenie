from PyPDF2 import PdfReader

class PDFTextExtractor:
    def extract_text(self, pdf_path):
        """Extract text from all pages of the PDF."""
        reader = PdfReader(pdf_path)
        texts = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                texts.append(text)
        return texts