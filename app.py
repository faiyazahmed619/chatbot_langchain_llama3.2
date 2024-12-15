from langchain_community.llms import ollama
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

#Langsmith tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'True'
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

#Prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'you are a virtual assistant, answer questions that are asked'),
        ('user', 'question : {question}')
    ]
)

#streamlit framework

st.title("LANGCHAIN CHAT APP USING LLAMA 3.2 MODEL BY META")
input_text = st.text_input('What do you want to ask?')

#creating a chain
llm = ollama.Ollama(model='llama3.2')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser


if st.text_input:
    st.write(chain.invoke({'question' : input_text}))

