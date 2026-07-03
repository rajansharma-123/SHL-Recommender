from sklearn.metrics.pairwise import cosine_similarity

from rag.vector_store import (
    load_vectorizer,
    load_matrix,
    load_metadata
)


def search_assessments(query: str, top_k: int = 5):

    vectorizer = load_vectorizer()
    matrix = load_matrix()
    metadata = load_metadata()

    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        matrix
    )[0]

    ranked = similarities.argsort()[::-1][:top_k]

    results = []

    for idx in ranked:

        item = metadata[idx].copy()

        item["score"] = float(similarities[idx])

        results.append(item)

    return results


def find_assessment_by_name(name: str):

    metadata = load_metadata()

    name = name.lower()

    for item in metadata:

        if name in item["name"].lower():

            return item

    return None