from sentence_transformers import SentenceTransformer

# Load embedding model only once
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


def get_embedding(text: str):
    """
    Convert text into embedding vector.
    """

    return model.encode(text)