import numpy as np

from rag.vector_store import load_metadata


def _get_index_and_metadata():
    from rag.embeddings import get_embedding
    from rag.vector_store import load_faiss_index

    index = load_faiss_index()
    metadata = load_metadata()
    return index, metadata, get_embedding


def search_assessments(query: str, top_k: int = 10):
    try:
        index, metadata, get_embedding = _get_index_and_metadata()
    except Exception:
        return []

    query_embedding = np.array(
        [get_embedding(query)],
        dtype="float32"
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx, distance in zip(indices[0], distances[0]):
        assessment = metadata[idx].copy()
        assessment["score"] = float(distance)
        results.append(assessment)

    return results


def find_assessment_by_name(name: str):
    """Find assessment by partial name."""

    name = name.lower().strip()
    metadata = load_metadata()

    for item in metadata:
        if name in item["name"].lower():
            return item

    return None