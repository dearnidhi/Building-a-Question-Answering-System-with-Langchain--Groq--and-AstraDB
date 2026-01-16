# RAG Pipeline with Groq, LangChain & AstraDB 🧠📚

This project demonstrates a **Retrieval-Augmented Generation (RAG)** workflow using **LangChain**, **Groq LLM (Mixtral)**, and **AstraDB (Cassandra)**.
It loads content from the web, splits it into chunks, generates embeddings, stores them in a vector database, and retrieves relevant context to answer user queries accurately.

---

## 🚀 Features

- Web document loading using BeautifulSoup
- Text chunking with overlap for better retrieval
- Vector embeddings using OpenAI Embeddings
- Vector storage with AstraDB (Cassandra)
- Context-aware question answering using Groq LLM
- Modular LangChain-based pipeline

---

## 🧠 Architecture Overview

1. **Web Loader**
   - Fetches structured content from a given URL

2. **Text Splitting**
   - Breaks large documents into manageable chunks

3. **Embeddings**
   - Converts text into vector embeddings using OpenAI

4. **Vector Store**
   - Stores embeddings in AstraDB (Cassandra)

5. **Retrieval + Generation**
   - Retrieves relevant chunks
   - Passes context to Groq LLM for answer generation

---

## 📂 Project Flow

```text
Web Page → Text Splitter → Embeddings → AstraDB
                                   ↓
                             Groq LLM (Mixtral)
                                   ↓
                              Final Answer

▶️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🔐 Environment Variables
Create a .env file in the root directory:
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
ASTRA_DB_APPLICATION_TOKEN=your_astra_token
ASTRA_DB_ID=your_database_id



▶️ Running the Project
The script initializes the vector store and retrieval chain automatically.
To query the system, uncomment and use:
astra_vector_index.query("Your question here", llm=llm)
Or integrate the retrieval chain with a frontend like Streamlit or Flask.

🛠️ Tech Stack

Python
LangChain
Groq (Mixtral-8x7B)
OpenAI Embeddings
AstraDB (Cassandra)
BeautifulSoup
dotenv

⚠️ Notes

Designed for learning and experimentation
Uses cloud-based vector storage
Requires valid API keys
Not production-hardened
