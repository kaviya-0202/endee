def get_embedding(texts):
    embeddings = []
    MAX_LEN = 10
    
    for text in texts:
        text = text.lower()
        words = text.split()
        
        # simple hashing embedding
        vector = [hash(word) % 100 for word in words]
        
        # padding
        if len(vector) < MAX_LEN:
            vector += [0] * (MAX_LEN - len(vector))
        
        # trimming
        vector = vector[:MAX_LEN]
        
        embeddings.append(vector)
    
    return embeddings