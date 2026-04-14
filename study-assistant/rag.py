import numpy as np
from embed import get_embedding

# -----------------------------
# Cosine Similarity Function
# -----------------------------
def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    
    if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
        return 0.0
    
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# -----------------------------
# Simple Vector Database
# -----------------------------
class EndeeDB:
    def __init__(self):
        self.data = []

    def insert(self, text, vector):
        self.data.append({
            "text": text,
            "vector": vector
        })

    def search(self, query_vector, top_k=3):
        results = []

        for item in self.data:
            score = cosine_similarity(query_vector, item["vector"])
            results.append((score, item["text"]))

        # Sort by similarity score (highest first)
        results.sort(key=lambda x: x[0], reverse=True)

        # Debug (VERY IMPORTANT)
        print("\n--- Retrieval Debug ---")
        for score, text in results[:5]:
            print(f"Score: {score:.3f} | Text: {text}")
        print("-----------------------\n")

        # Filter low-quality matches
        filtered = [item for item in results if item[0] > 0.1]

        return filtered[:top_k]


# -----------------------------
# Initialize Database
# -----------------------------
db = EndeeDB()


# -----------------------------
# Store Data into DB
# -----------------------------
def store(texts):
    embeddings = get_embedding(texts)

    for i in range(len(texts)):
        db.insert(texts[i], embeddings[i])


# -----------------------------
# Answer Function (RAG)
# -----------------------------
def answer(query):
    query_lower = query.lower()

    # -------------------------
    # Rule-based answers (fast)
    # -------------------------
    if "machine learning" in query_lower:
        return "Machine learning is a method of data analysis that allows systems to learn automatically from data."

    elif "overfitting" in query_lower:
        return "Overfitting happens when a model memorizes training data instead of learning general patterns."

    elif "batch normalization" in query_lower:
        return "Batch normalization improves the speed, performance, and stability of neural networks."

    elif "neural network" in query_lower:
        return "Neural networks are systems of interconnected nodes that process information similar to the human brain."

    # -------------------------
    # Retrieval-based fallback
    # -------------------------
    query_vec = get_embedding([query])[0]
    results = db.search(query_vec)

    if not results:
        return "Sorry, I couldn't find relevant information in the dataset."

    # Extract top texts
    top_texts = [text for _, text in results]

    # Combine into answer
    final_answer = " ".join(top_texts)

    return final_answer