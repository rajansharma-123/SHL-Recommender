from rag.embeddings import get_embedding

vector = get_embedding("Java Developer")

print(len(vector))
print(vector[:10])