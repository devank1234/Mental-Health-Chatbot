from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
import streamlit as st

def load_pdf_files():
    loader = DirectoryLoader("raw_pdf/",
                             glob = "*.pdf",
                             loader_cls = PyPDFLoader)
    documents = loader.load()
    return documents

def create_chunks():
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500,
                                                   chunk_overlap = 50)
    text_chunks = text_splitter.split_documents(load_pdf_files())
    return text_chunks

def get_embedding_model():
    embedding_model = HuggingFaceEmbeddings(
        model = "sentence-transformers/all-MiniLM-L6-v2")
    return embedding_model

@st.cache_resource
def get_vectorstore():
    db = FAISS.from_documents(create_chunks(), 
                              get_embedding_model())
    db_path = "vectorstore/db_faiss"
    db.save_local(folder_path =db_path, 
                  index_name = "index")
    return db

def load_llm():

    llm = OllamaLLM(model="mistral:7b")
    return llm

def get_prompt(prompt_template,input_variables):
    prompt = PromptTemplate(template = prompt_template,
                            input_variables = input_variables)
    return prompt

