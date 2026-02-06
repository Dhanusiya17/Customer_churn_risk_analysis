# LLM Project – Intelligent Data Query & Analysis System

## 📌 Project Overview
This project is a **modular LLM-based application** built using **LangChain**.
It ingests structured data, stores it in a database, and allows intelligent querying
using Large Language Models (LLMs).

The architecture is designed for **scalability, clarity, and maintainability**.

---

## 🧠 System Architecture & Workflow

### 1️⃣ Data Layer
**Location:** `data/`

- `raw/` → Original datasets
- `processed/` → Cleaned and transformed datasets

Raw data is first processed and prepared before ingestion.

---

### 2️⃣ Data Ingestion
**Location:** `ingestion/`

- `ingest_to_sqlite.py`  
  Reads processed data and stores it into a SQLite database.

This enables structured storage and fast retrieval for LLM-based querying.

---

### 3️⃣ LangChain Intelligence Layer
**Location:** `langchain_layer/`

This layer manages all LLM-related logic.

- `agent/` → Decision-making agents
- `chains/` → LangChain chains (prompt → model → output)
- `intent/` → User intent detection
- `orchestration/` → Controls interaction between agents and chains
- `db/` → Database retrieval logic

This layer converts user input into meaningful, context-aware responses.

---

### 4️⃣ LLM Configuration
**Location:** `llm/`

Handles:
- LLM initialization
- Model configuration (Groq / OpenAI-compatible)

Keeps model logic separated from business logic.

---

### 5️⃣ Application Execution
**Root Files:**

- `main.py` → Main application logic
- `run.py` → Entry point to run the full pipeline
- `demo.py` → Demonstration script
- `.env` → API keys and environment variables
- `requirements.txt` → Project dependencies

---

## 🛠️ Technologies Used
- Python
- LangChain
- Groq LLM
- OpenAI-compatible APIs
- SQLite
- Pandas
- Pydantic
- DuckDuckGo Search (ddgs)
- Wikipedia API

---

## ⚙️ Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/your-username/llm_project.git
