import streamlit as st
from langchain_helper import create_vector_db, get_qa_chain

st.title('Q&A ❓❓ (By Aritra Ganguly)')

btn = st.button("Create Knowledgebase")
if btn:
    # Implement your knowledgebase creation logic here
    pass

question = st.text_input("Enter the question: ")

if question:
    chain = get_qa_chain()
    try:
        response = chain(question)
        st.header("Answer: ")
        st.write(response["result"])
    except IndexError:
        st.header("Answer: ")
        st.write("I don't know ")
