from sentence_transformers import SentenceTransformer

_model = None


def get_model():
    """
    Lazy-load the embedding model.
    The model is loaded only on the first request.
    """

    global _model

    if _model is None:
        _model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    return _model


def get_embedding(text: str):

    model = get_model()

    embedding = model.encode(
        text,
        normalize_embeddings=True
    )

    return embedding