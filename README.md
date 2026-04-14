# 📚 AI Study Assistant using RAG and Endee

## 📌 Overview

This project is an AI-powered Study Assistant that uses Retrieval Augmented Generation (RAG) to answer user queries based on a given dataset. It demonstrates semantic search using embeddings and vector similarity.

## 🚀 Features

* Semantic search using embeddings
* RAG-based answer retrieval
* Interactive UI using Streamlit
* Fast and simple vector search system

## 🧠 Technologies Used

* Python
* NumPy
* Streamlit
* Vector Database Concepts (Endee)

## ⚙️ System Design

1. The dataset is converted into embeddings
2. User query is converted into embedding
3. Cosine similarity is used to compare vectors
4. Top relevant results are retrieved
5. Final answer is generated and displayed

## 📂 Dataset

The dataset contains AI/ML related concepts such as:

* Machine Learning
* RAG (Retrieval Augmented Generation)
* Neural Networks
* Embeddings
* NLP

## 🔗 Endee Integration

This project is inspired by the Endee Vector Database architecture.
A lightweight in-memory vector store is implemented to simulate Endee's functionality, including vector storage and semantic search.

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📌 Example Queries

* What is RAG?
* What is machine learning?
* Explain embeddings
* What is cosine similarity?

## 📌 Future Improvements

* Full integration with Endee vector database
* Better natural language response generation
* Support for larger datasets
