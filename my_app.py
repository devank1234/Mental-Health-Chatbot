import streamlit as st
from Mindmate import get_vectorstore, get_prompt, load_llm
from langchain.chains import RetrievalQA

# Streamlit UI
st.markdown("""
# 🌿 Welcome to **MindMate**
### Your personal companion for mental well-being.

### 💖 _I'm here to listen, support, and guide you._

---

### How can I assist you today?
""")

# Store chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

prompt = st.chat_input("What’s on your mind?")

if prompt and prompt.strip():
    st.chat_message('user').markdown(prompt)
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    prompt_template = """
    Use the pieces of information provided in the context to answer user's question.
    If you don’t know the answer, just say that you don’t know. Don’t try to make up an answer. 
    Don’t provide anything outside the given context.

    Context: {context}
    Question: {question}

    Start the answer directly. No small talk please.
    """

    try:
        vectorstore = get_vectorstore()
        if vectorstore is None:
            st.error("Failed to load the vector store")

        qa_chain = RetrievalQA.from_chain_type(
            llm=load_llm(),
            chain_type="stuff",
            retriever=vectorstore.as_retriever(search_kwargs={'k': 3}),
            return_source_documents=True,
            chain_type_kwargs={'prompt': get_prompt(prompt_template, input_variables=["context", "question"])}
        )

        response = qa_chain.invoke({'query': prompt})
        result = response["result"]
        st.chat_message('assistant').markdown(result)
        st.session_state.messages.append({'role': 'assistant', 'content': result})

    except Exception as e:
        import traceback
        st.error(f"Error: {str(e)}")
        st.text(traceback.format_exc())

# Clear chat button
if st.button("🗑️ Clear Chat History"):
    st.session_state.messages = []
    st.rerun()