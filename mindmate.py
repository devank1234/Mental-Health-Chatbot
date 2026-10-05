from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings


def load_pdf_files():
    loader=DirectoryLoader(
    path= r'pro1\fol1',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)
    documnets=loader.load()
    return documnets

def create_chunks():
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=80
    )
    text_chunks=text_splitter.split_documents(load_pdf_files())
    return text_chunks


def get_embedding_model():
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embedding_model  


@st.cache_resource
def get_vectorstore():
    db = Chroma.from_documents(
        create_chunks(),
        get_embedding_model(),
        persist_directory="pro1"
    )
    return db

def load_llm():

    llm=OllamaLLM(model="Qwen2.5:1.5b")
    return llm

def get_prompt(prompt_template,input_variables):
    prompt = PromptTemplate(template = prompt_template,
                            input_variables = input_variables)
    return prompt








