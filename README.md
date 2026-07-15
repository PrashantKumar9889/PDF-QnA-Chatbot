# 📄 PDF QnA Chatbot

An AI-powered chatbot that lets users upload any PDF and ask questions in natural language.

The application uses **Retrieval-Augmented Generation (RAG)** with **LangChain**, **HuggingFace Embeddings**, and **Google Gemini** to answer questions based only on the uploaded document.

---

## 🚀 Features

- Upload any PDF
- Semantic search using vector embeddings
- AI-powered question answering
- Chat interface built with Streamlit
- Conversation history
- Uses only document context
- Clean Markdown responses

---

## 🛠 Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini API
- HuggingFace Embeddings (BAAI/bge-small-en-v1.5)
- InMemoryVectorStore
- PyPDFLoader

---

## 📂 Project Structure

```
PDF-QnA-Chatbot/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── uploaded_document.pdf
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/PrashantKumar9889/PDF-QnA-Chatbot.git

cd PDF-QnA-Chatbot
```

Create a virtual environment

```bash
python -m venv env
```

Activate it

Windows

```bash
env\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file

```text
GOOGLE_API_KEY=your_google_api_key
```

For Streamlit Cloud, add the same key inside

```
Settings
→ Secrets
```

```toml
GOOGLE_API_KEY="your_google_api_key"
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

---

## 💬 Example Workflow

1. Upload a PDF
2. Wait for indexing
3. Ask questions like

```
Tell me about the candidate.

What projects has the candidate worked on?

Summarize the document.

What skills are mentioned?
```

---

## 🧠 How It Works

```
PDF
   │
PyPDFLoader
   │
Text Splitter
   │
Embeddings
   │
Vector Store
   │
Similarity Search
   │
Relevant Context
   │
Gemini LLM
   │
Answer
```

---

## 📸 Demo

(![Home](images/home.png)

 ![Chat](images/chat.png))

---

## 📌 Future Improvements

- FAISS Vector Database
- Multiple PDF upload
- Source citations
- Chat memory
- Download conversation
- Streaming responses
- Dark mode
- Docker support

---

## 👨‍💻 Author

**Prashant Kumar**

GitHub:
https://github.com/PrashantKumar9889

LinkedIn:
https://www.linkedin.com/in/prashant-kumar-64101b304/
