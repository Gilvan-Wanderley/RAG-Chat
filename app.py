import streamlit as st
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from services import Writer, RetrievalAugmentedGen, DocHandler


def handle_user_input(user_question):
    response = st.session_state.conversation({"question": user_question})
    st.session_state.chat_history = response['chat_history']
    for message in st.session_state.chat_history:
        if message.type == "human":
            st.markdown(Writer.human_msg(message.content), unsafe_allow_html=True)
        else:
            st.markdown(Writer.ai_msg(message.content), unsafe_allow_html=True)

def set_session_state() -> None:
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

def chat():
    st.header(":robot_face: Chat")
    if user_question := st.chat_input("Qual sua dúvida em relação ao conteúdo dos documentos?"):
        handle_user_input(user_question)

def sidebar_docs():
    with st.sidebar:
        st.subheader("Documentos")
        docs = st.file_uploader("Carrege os documentos e clique em Processar'", 
                                accept_multiple_files=True)
        
        rag= RetrievalAugmentedGen(OpenAIEmbeddings(),
                           DocHandler(1000, 200))
        
        if st.button("Processar"):
            with st.spinner("Processando.."):
                vectorstore = rag.get_vectorstore(docs)
                st.session_state.conversation = rag.get_rag_chain(vectorstore)

def main():
    load_dotenv()
    st.set_page_config(page_title="Desafio IEL", page_icon=":robot_face:")
    set_session_state()
    chat()
    sidebar_docs()
    
    
if __name__ == "__main__":
    main()