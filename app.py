from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import InMemoryVectorStore
import streamlit as st
from time import sleep


llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "messages" not in st.session_state:
    st.session_state.messages = []



## Document 
def document_loader(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    
    print(len(docs))

    ## Splitting
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(docs)

    print(len(docs))

    ## Embedding and Storing in Vector Store
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )
    vector_store = InMemoryVectorStore.from_documents(docs, embeddings)
    st.session_state.vector_store = vector_store   
    st.session_state.document_uploaded = True 

## User Query


# answer = llm.invoke(prompt)

### Streamlit UI
st.subheader("📝 PDF QnA Chatbot")

if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False

### Document Upload 
if not st.session_state.document_uploaded:
    file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if file:
        with open("uploaded_document.pdf", "wb") as f:
            f.write(file.getvalue())
        st.markdown("Document uploaded successfully!")   

        with st.spinner("Processing the document..."):
            document_loader("uploaded_document.pdf")
            st.session_state.document_uploaded = True
            st.success("Document processed successfully!") 
            sleep(2)
            st.rerun()


### Chatbot UI
if st.session_state.document_uploaded and st.session_state.vector_store:
    for oneMessage in st.session_state.messages:
        role = oneMessage["role"]
        content = oneMessage["content"]

        st.chat_message(role).markdown(content)
           
    
    query = st.chat_input("Ask a question about the document:")
    if query:   

        st.session_state.messages.append({"role": "user", "content": query})

        st.chat_message("User").markdown(query)

        documnents = st.session_state.vector_store.similarity_search(query, k=2)
        context = ""

        for doc in documnents:
            context += doc.page_content + "\n\n"

        prompt = f"""
            You are a PDF Question Answering assistant.

            Use only the information from the context.

            If the answer is not present, say:
            "I couldn't find this information in the document."

            Return the answer in clean Markdown.

            Context:
            {context}

            Question:
            {query}
        """

        result = llm.invoke(prompt)

        answer = ""

        if isinstance(result.content, list):
            for item in result.content:
                if item.get("type") == "text":
                    answer += item.get("text", "")
        else:
            answer = result.content

        # st.chat_message("Bot").markdown(answer)

        st.session_state.messages.append({"role": "ai", "content": answer})
        st.chat_message("Bot").markdown(answer)


     