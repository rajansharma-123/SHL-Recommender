import json
import pickle
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer

# -----------------------------
# Paths
# -----------------------------

CATALOG_PATH = Path("data/catalog.json")
VECTORIZER_PATH = Path("data/vectorizer.pkl")
MATRIX_PATH = Path("data/tfidf_matrix.pkl")
METADATA_PATH = Path("data/metadata.pkl")

_vectorizer = None
_matrix = None
_metadata = None


# -----------------------------
# Load Catalog
# -----------------------------

def load_catalog():

    with open(CATALOG_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


# -----------------------------
# Build TF-IDF Index
# -----------------------------

def create_index():

    catalog = load_catalog()

    documents = []

    for item in catalog:

        text = f"""
        {item.get("name", "")}

        {item.get("description", "")}

        {" ".join(item.get("keys", []))}

        {" ".join(item.get("job_levels", []))}
        """

        documents.append(text)

    vectorizer = TfidfVectorizer(stop_words="english")

    matrix = vectorizer.fit_transform(documents)

    with open(VECTORIZER_PATH, "wb") as file:
        pickle.dump(vectorizer, file)

    with open(MATRIX_PATH, "wb") as file:
        pickle.dump(matrix, file)

    with open(METADATA_PATH, "wb") as file:
        pickle.dump(catalog, file)

    return len(catalog)


# -----------------------------
# Load Vectorizer
# -----------------------------

def load_vectorizer():

    global _vectorizer

    if _vectorizer is None:

        with open(VECTORIZER_PATH, "rb") as file:

            _vectorizer = pickle.load(file)

    return _vectorizer


# -----------------------------
# Load Matrix
# -----------------------------

def load_matrix():

    global _matrix

    if _matrix is None:

        with open(MATRIX_PATH, "rb") as file:

            _matrix = pickle.load(file)

    return _matrix


# -----------------------------
# Load Metadata
# -----------------------------

def load_metadata():

    global _metadata

    if _metadata is None:

        with open(METADATA_PATH, "rb") as file:

            _metadata = pickle.load(file)

    return _metadata