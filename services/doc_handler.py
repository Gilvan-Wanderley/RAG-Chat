from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter


class DocHandler:
     def __init__(self, chunk_size: int, chunk_overlap: int) -> None:
         self._chunk_size = chunk_size
         self._chunk_overlap = chunk_overlap
     
     def _get_text(self, docs: list) -> str:
        text = ""
        for doc in docs:
            doc_reader = PdfReader(doc)
            for page in doc_reader.pages:
                text += page.extract_text()
        return text
     
     def get_chunks(self, docs: list) -> list[str]:
        text_splitter= CharacterTextSplitter(separator="\n",
                                            chunk_size= self._chunk_size,
                                            chunk_overlap= self._chunk_overlap,
                                            length_function=len)
        chunks = text_splitter.split_text(self._get_text(docs))
        return chunks