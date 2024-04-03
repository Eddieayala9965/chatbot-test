import streamlit as st
from dotenv import load_dotenv, find_dotenv
from pypdf import PdfReader
from langchain_text_splitters import CharacterTextSplitter


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
    
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n", 
        chunk_size=1000,
        chunk_overlap=200, 
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks
    
def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDF's", page_icon=":books")
    
    st.header("chat with multiple PDF's :books:")
    st.text_input("ask a question about your documents:")
    
    with st.sidebar:
        st.subheader("your documents")
        pdf_docs = st.file_uploader("Upload you PDF's here and click on process", accept_multiple_files=True)
        if st.button("process"):
            with st.spinner("Processing"):
                raw_text = get_pdf_text(pdf_docs)
                
                text_chunks = get_text_chunks(raw_text)
                st.write(text_chunks)


if __name__ == '__main__':
    main()