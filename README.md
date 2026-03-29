# 📄 Document RAG System with FAISS + ReAct Agent (Dockerized)

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

- Local vector storage using FAISS  
- Fast similarity search (ANN)  
- Optional persistence support  

---

### 🤖 ReAct Agent

- Dynamically selects tools  
- Combines reasoning + retrieval  
- Handles multi-step queries  

---

### 🧩 Modular Architecture

- Document ingestion  
- Vector store management  
- Graph-based workflow  
- Agent orchestration  

---

### 💬 Chat UI

- Built with Streamlit  
- Maintains chat history  
- Interactive Q&A  

---

## 🏗️ Project Structure

DOCUMENT_RAG/
│
├── data/
│
├── src/
│   ├── config/
│   ├── document_ingestion/
│   ├── graph_builder/
│   ├── nodes/
│   ├── state/
│   ├── vectorstore/
│
├── streamlit_app.py
├── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .env
└── README.md

---

## 🔄 How It Works

1. Document ingestion → chunking  
2. Embedding generation using OpenAI  
3. Store embeddings in FAISS  
4. Query → embedding → retrieval  
5. ReAct agent → reasoning + response  

---



---

## ⚙️ Installation & Setup (Local)

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd travel-recommendation-system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
streamlit run streamlit_app.py
```

### 5️⃣ Open in Browser

```
http://localhost:8000
```

---

## 🐳 Docker Setup

### 1️⃣ Build Docker Image

```bash
docker build -t doc-rag .
```

### 2️⃣ Run Container

```bash
docker run -d \
  -p 8501:8501 \
  --env-file .env \
  doc-rag
```

### 3️⃣ Access Application

```
http://localhost:8501
```

---


## 🚀 Future Enhancements

* Persistent FAISS storage
* Hybrid search (BM25 + vector)
* Reranking models
* Production deployment (Kubernetes)
* GPU acceleration

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Asit Kumar Sahoo**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it 🚀
