### Q&A Chatbot
import os
from constants import openai_key 
from langchain_openai import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

### Function to load open AI model and get responses

def get_openai_responses(question):
    llm = OpenAI(temperature=0.5)
    response = llm(question)
    return response

### initialize our streamlit

st.set_page_config(page_title="Q&A Chatbot")

st.header("Langchain application")

input = st.text_input("Input: " ,key="input")
response = get_openai_responses(input)

submit = st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The response is")
    st.write(response)