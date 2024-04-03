import streamlit as st
from dotenv import load_dotenv, find_dotenv



def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDF's", page_icon=":books")
    
    st.header("chat with multiple PDF's :books:")
    st.text_input("ask a question about your documents:")
    
    with st.sidebar:
        st.subheader("your documents")
        st.file_uploader("Upload you PDF's here and click on process")
        st.button("process")
        


if __name__ == '__main__':
    main()