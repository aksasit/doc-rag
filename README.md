# 📄 Document RAG System with FAISS + ReAct Agent

## 🚀 Overview

This project is a **production-style Retrieval-Augmented Generation (RAG) system** that enables intelligent question answering over multiple document sources.

It combines:

* **FAISS** for fast vector similarity search
* **OpenAI Embeddings** for semantic understanding
* **ReAct Agent** for tool-based reasoning
* **Streamlit UI** for interactive user experience

The system can ingest and query data from:

* 📄 PDFs
* 🌐 URLs
* 📝 `.txt` files
* 📁 Directories
* 📚 Wikipedia

---

## 🧠 Key Features

### 🔍 Multi-Source Retrieval

Supports ingestion from multiple data sources:

* PDF documents
* Web URLs
* Local text files
* Entire directories
* Wikipedia search

---

### ⚡ FAISS Vector Store

* Local vector storage using FAISS
* Fast similarity search (ANN)
* Persistent storage support (if saved)

---

### 🤖 ReAct Agent (Reason + Act)

* Dynamically decides which tool to use
* Combines retrieval + reasoning
* Handles multi-step queries intelligently

---

### 🧩 Modular Architecture

Clean separation of concerns:

* Document ingestion
* Vector store management
* Graph-based workflow
* Agent orchestration

---

### 💬 Chat UI with History

* Built using Streamlit
* Displays previous responses
* Interactive chat experience

---

## 🏗️ Project Structure

```
DOCUMENT_RAG/
│
├── data/                     # Input documents (PDF, txt, etc.)
│
├── src/
│   ├── config/              # Configuration files
│   ├── document_ingestion/  # Document loading & chunking
│   ├── graph_builder/       # LangGraph workflow construction
│   ├── nodes/               # Agent & tool nodes
│   ├── state/               # RAG state management
│   ├── vectorstore/         # FAISS handling logic
│
├── streamlit_app.py         # UI application
├── main.py                  # Entry point
├── requirements.txt         # Dependencies
├── .env                     # API keys (not committed)
└── README.md                # Project documentation
```

---

## 🔄 How It Works

### 1️⃣ Document Ingestion

* Documents are loaded and split into chunks

### 2️⃣ Embedding Generation

* Each chunk is converted into vector embeddings using OpenAI

### 3️⃣ Vector Storage

* Embeddings are stored in FAISS (locally)

### 4️⃣ Query Processing

* User query → converted to embedding
* FAISS retrieves relevant chunks

### 5️⃣ ReAct Agent Execution

* Agent decides:

  * Retrieve from vector store
  * Call tools (Wikipedia, URL, etc.)
* Generates final response

---

## 🛠️ Installation

```bash
git clone <your-repo-url>
cd DOCUMENT_RAG

pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application

### Run backend / main logic:

```bash
python main.py
```

### Run UI:

```bash
streamlit run streamlit_app.py
```

---

## 💡 Usage

1. Upload or provide data sources (PDF, URL, etc.)
2. Ask questions in the UI
3. System retrieves relevant context
4. Agent reasons and responds
5. Chat history is maintained in UI

---

## ⚠️ Important Notes

* FAISS is stored **locally in memory** unless explicitly persisted
* Embeddings are generated using OpenAI API (cost involved)
* On restart, embeddings must be reloaded or recreated if not saved

---

## 🔮 Future Improvements

* Persistent FAISS storage with versioning
* Hybrid search (keyword + vector)
* Reranking for better retrieval accuracy
* Deployment using FastAPI + Docker
* Integration with production vector databases

---

## 🤝 Contributing

Feel free to fork and improve the project. Contributions are welcome!

---

## 📜 License

This project is for learning and experimentation purposes.
