from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from .doc_handler import DocHandler


class RetrievalAugmentedGen:
    def __init__(self, 
                 embeddings: OpenAIEmbeddings,
                 doc_handler: DocHandler) -> None:
        self._embeddings = embeddings
        self._doc_handler = doc_handler
    
    def get_vectorstore(self, docs: list) -> FAISS:
        return FAISS.from_texts(texts=self._doc_handler.get_chunks(docs), 
                                embedding=self._embeddings)

    def get_rag_chain(self, vectorstore: FAISS):
        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm= ChatOpenAI(),
            retriever= vectorstore.as_retriever(),
            memory= ConversationBufferMemory(memory_key="chat_history", 
                                            return_messages=True)
        )
        return conversation_chain