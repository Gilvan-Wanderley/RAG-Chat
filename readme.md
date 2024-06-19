# RAG-Chat
> Author: Gilvan Wanderley de Farias Neto
---------------
## Solution Description
![Chat App Diagram](./docs/images/diagram.png)
The application follows these steps to provide answers to your questions:

* **PDF Loading**: The app reads multiple PDF documents and extracts their text content.

* **Text Chunking**: The extracted text is divided into smaller chunks that can be processed effectively.

* **Language Model**: The app uses a language model to generate vector representations (embeddings) of the text chunks.

* **Similarity Matching**: When you ask a question, the app compares it against the text blocks and identifies the most semantically similar ones.

* **Answer Generation**: The selected chunks are passed to the language model, which generates an answer based on the relevant content from the PDFs.

## Dependencies and Installation

### Installation Using Poetry

```
poetry shell
poetry install
```

### Installation Using Pip

```
pip install -r requirements.txt
```

## Usage
To start the Chat, follow these steps:
* Make sure your environment is activated, required dependencies are installed, and the OpenAI API key is added to the .env file.
* Run the app.py file using Streamlit. Execute the following command:
```
streamlit run app.py
```
* The app will start in your default browser, displaying the user interface.
![Chat App UI](./docs/images/chat_UI.png)
* Load one or multiple PDF documents into the app following the provided instructions.
* Ask questions about the loaded PDFs using the chat interface.
