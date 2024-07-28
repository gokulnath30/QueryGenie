# QueryGenie

This open-source application allows users to ask questions to various models (like ChatGPT, Ollama, Gemini) and receive answers. It also provides the functionality to upload documents and get answers based on the content of these documents. Users have the freedom to customize the processing pipeline by selecting different options for models,text extraction, splitting, embedding generation, and storage thus providing one single platform leveraging all the capabilities.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Configuration](#configuration)
5. [Contributing](#contributing)
6. [License](#license)

## Features

- **Model Selection:** Users can choose from various models (ChatGPT, Ollama, Gemini etc.) to answer their queries.
- **Document Upload:** Supports uploading documents in various formats (PDF, text, Excel etc.).
- **Text Extraction:** Users can select different text extractors for extracting text from documents.
- **Text Splitting:** Provides multiple options for splitting the text into chunks (Langchain RecursiveCharacterTextSplitter, etc.).
- **Embedding Generation:** Users can choose from several transformers (SentenceTransformer, etc.) for generating embeddings.
- **Storage Options:** Supports multiple storage options for embeddings (Faiss, etc.).
- **Customizable Pipeline:** The platform allows users to customize each step of the processing pipeline to suit their needs.
- **Local and Cloud Deployment:** The application can run both locally and on cloud platforms, ensuring data privacy when run locally.

## Installation

### Prerequisites

- Python 3.8+
- PDM (Python Dependency Manager)
- Docker

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/gokulnath30/QueryGenie.git
   cd QueryGenie
   ```

2. Build the Docker container:
   ```bash
   docker build -t QueryGenie .
   ```

3. Install the dependencies using PDM:
   ```bash
   pdm install
   ```

4. Run the application locally:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Launching the Application:**
   Open your browser and go to `http://localhost:8501` to access the Streamlit UI.

2. **Uploading a Document:**
   - Click on the upload button and select your document (PDF, text, Excel).
   - Choose the text extractor from the provided options.

3. **Customizing the Processing Pipeline:**
   - Select the text splitter to chunk the document.
   - Choose the transformer to generate embeddings.
   - Pick the storage option to store embeddings.

4. **Asking Questions:**
   - Select the model you want to use (ChatGPT, Ollama, Gemini).
   - Enter your question in the input box and submit.
   - View the answer generated based on the selected options and document content.

## Configuration

The application allows for easy customization through the Streamlit UI. Here are the configurable components:

1. **Text Extractors:** Choose from a variety of text extraction methods.
2. **Text Splitters:** Options for splitting the text into manageable chunks.
3. **Transformers:** Select from different transformers for embedding generation.
4. **Storage Options:** Pick the preferred storage for embeddings.

## Contributing

Contributions are welcome! If you have any suggestions or find any bugs, please open an issue or submit a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

This README provides a comprehensive guide to installing, configuring, and using the application, with updated instructions for using PDM and Docker, and highlights the open-source and privacy-maintaining aspects of the application. Adjust the content as necessary to fit the specifics of your project.