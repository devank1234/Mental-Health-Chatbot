# Mental-Health-Chatbot

# 🌿 MindMate — RAG-Based Mental Wellness Assistant

MindMate is a **Retrieval-Augmented Generation (RAG)** based conversational assistant designed to provide supportive and context-aware responses using information retrieved from a curated PDF knowledge base.

The application combines **Streamlit, LangChain, ChromaDB, Hugging Face embeddings, and Ollama** to build a complete local RAG pipeline.

---

## ✨ Features

- 💬 Interactive conversational interface using Streamlit
- 📄 Loads knowledge from PDF documents
- ✂️ Splits documents into smaller chunks using Recursive Character Text Splitter
- 🧠 Generates semantic embeddings using Hugging Face
- 🔎 Performs similarity-based retrieval using ChromaDB
- 🤖 Generates responses using a locally running Ollama LLM
- 🗂️ Maintains chat history during the session
- ⚡ Uses Streamlit caching to avoid repeatedly creating the vector store
- 🔒 Runs locally without requiring the user's documents to be uploaded to a third-party application

---

## 🏗️ Architecture

```text
                 PDF Knowledge Base
                         │
                         ▼
                  PyPDFLoader
                         │
                         ▼
             Recursive Text Splitter
                         │
                         ▼
              Document Chunks
                         │
                         ▼
          Hugging Face Embeddings
                         │
                         ▼
                    ChromaDB
                  Vector Store
                         │
                         ▼
                    Retriever
                         │
                         ▼
                   RetrievalQA
                         │
                         ▼
                Ollama LLM
                Qwen2.5:1.5B
                         │
                         ▼
                  Final Response
                         │
                         ▼
                  Streamlit UI
