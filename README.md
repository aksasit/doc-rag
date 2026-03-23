# 📄 Document RAG System with FAISS + ReAct Agent

## 🚀 Overview

This project is a **Retrieval-Augmented Generation (RAG) system** that enables intelligent question answering over multiple document sources.

It combines:
- **FAISS** for fast vector similarity search
- **OpenAI Embeddings** for semantic understanding
- **ReAct Agent** for tool-based reasoning
- **Streamlit UI** for interactive chat experience

---

## 🧠 Features

### 🔍 Multi-Source Retrieval
Supports ingestion from:
- 📄 PDFs  
- 🌐 URLs  
- 📝 `.txt` files  
- 📁 Directories  
- 📚 Wikipedia  

---

### ⚡ Vector Store (FAISS)
- Local vector storage
- Fast similarity search (ANN)
- Optional persistence support

---

### 🤖 ReAct Agent
- Dynamically selects tools
- Performs reasoning + retrieval
- Handles multi-step queries

---

### 💬 Chat UI with History
- Built using Streamlit
- Maintains previous responses
- Interactive Q&A interface

---

## 🏗️ Project Structure
DOCUMENT_RAG/
│
├── data/ # Input documents
│
├── src/
│ ├── config/ # Configurations
│ ├── document_ingestion/ # Loading & chunking
│ ├── graph_builder/ # Workflow construction
│ ├── nodes/ # Agent/tools logic
│ ├── state/ # RAG state management
│ ├── vectorstore/ # FAISS logic
│
├── streamlit_app.py # UI
├── main.py # Entry point
├── requirements.txt
├── .env # API keys
└── README.md

---

## 🔄 How It Works

1. **Document Ingestion**
   - Load and split documents into chunks

2. **Embedding Generation**
   - Convert chunks into embeddings using OpenAI

3. **Vector Storage**
   - Store embeddings in FAISS

4. **Query Flow**
   - User query → embedding
   - FAISS retrieves relevant chunks

5. **ReAct Agent**
   - Decides which tool to use
   - Generates final answer

---

## 🛠️ Installation

```bash
git clone <your-repo-url>
cd DOCUMENT_RAG

pip install -r requirements.txt