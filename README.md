# 📚 Smart Study Assistant using RAG (Endee-Based)

## 🚀 Project Overview

This project is a simple AI-powered Smart Study Assistant built using a Retrieval Augmented Generation (RAG) approach. It allows users to ask questions and retrieves relevant information from a dataset using vector similarity.

The project is built on top of the Endee repository and demonstrates how vector databases can be used in real-world AI applications.

---

## 🎯 Objective

* To implement a basic RAG pipeline
* To demonstrate vector-based semantic search
* To simulate how Endee can be used as a vector database for AI systems

---

## 🧠 Key Concepts Used

* Vector Embeddings
* Cosine Similarity
* Semantic Search
* Retrieval Augmented Generation (RAG)

---

## ⚙️ System Design

### Workflow:

1. Input text data is converted into embeddings
2. Embeddings are stored in a vector database (Endee-inspired structure)
3. User enters a query
4. Query is converted into embedding
5. Similar vectors are retrieved using cosine similarity
6. Relevant data is returned as the answer

---

## 🗂️ Project Structure

```
study-assistant/
│── app.py          # Streamlit UI
│── rag.py          # Retrieval and logic
│── embed.py        # Embedding generation
│── data.txt        # Dataset
```

---

## 📊 Dataset

The dataset used in this project consists of curated content related to:

* Vector databases
* Machine learning
* RAG systems
* Artificial intelligence concepts

This dataset is designed to demonstrate semantic search and retrieval effectively.

---

## 🧩 Use of Endee

This project is built using the Endee repository as the base.

Endee is a vector database designed for storing and searching embeddings efficiently. In this project, we implement a simplified vector storage and retrieval mechanism inspired by Endee’s architecture.

The workflow aligns with Endee’s core principles:

* Data is converted into embeddings
* Embeddings are stored as vectors
* Similarity search is used for retrieval

---

## 🛠️ Technologies Used

* Python
* Streamlit
* NumPy

---

## ▶️ How to Run

1. Clone the repository:

```
git clone <your-repo-link>
cd study-assistant
```

2. Install dependencies:

```
pip install streamlit numpy
```

3. Run the application:

```
python -m streamlit run app.py
```

4. Open browser:

```
http://localhost:8501
```

---

## 🧪 Example Queries

* What is machine learning?
* Explain RAG
* What is a vector database?
* What is overfitting?

---

## ✅ Features

* Simple and interactive UI
* Semantic search using vector similarity
* Lightweight implementation (no heavy ML dependencies)
* Demonstrates real-world RAG pipeline

---

## 🔮 Future Improvements

* Integrate real embedding models (BERT, Sentence Transformers)
* Connect with full Endee backend
* Improve dataset and accuracy
* Add chatbot-style responses

---

## 📌 Conclusion

This project demonstrates how vector databases like Endee can be used to build AI applications such as RAG systems. It highlights the importance of embeddings, similarity search, and structured data retrieval in modern AI systems.

---
