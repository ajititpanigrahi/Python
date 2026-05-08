import numpy as np

sentence = "I love AI"

#step-1 Tokenization
tokens = sentence.split()
#print(tokens) ['I', 'love', 'AI']

#step-2 Token IDs
vocab={
    "I":1,
    "love":2,
    "AI":3
}

token_ids =[vocab[word] for word in tokens]
#print(token_ids) [1, 2, 3]

#step-3 embedding - vector
embedding_table ={
    1:[0.1,0.5],
    2:[0.7,0.2],
    3:[0.9,0.6],
}

embeddings = np.array([embedding_table[id] for id in token_ids])
print(embeddings)
#output of embedding
# [[0.1 0.5]
#  [0.7 0.2]
#  [0.9 0.6]]