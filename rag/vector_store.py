import json
import pickle
from pathlib import Path

import faiss
import numpy as np

from rag.embeddings import get_embedding

# -----------------------------
# Paths
# -----------------------------

CATALOG_PATH = Path("data/catalog.json")

INDEX_PATH = Path("data/faiss.index")

METADATA_PATH = Path("data/metadata.pkl")


# -----------------------------
# Load Catalog
# -----------------------------

def load_catalog():

    with open(CATALOG_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


# -----------------------------
# Build FAISS Index
# -----------------------------

def create_faiss_index():

    catalog = load_catalog()

    documents = []

    for item in catalog:

        text = f"""
        Name: {item.get("name", "")}

        Description:
        {item.get("description", "")}

        Skills:
        {", ".join(item.get("keys", []))}

        Job Levels:
        {", ".join(item.get("job_levels", []))}
        """

        documents.append(text)

    embeddings = np.array(
        [get_embedding(doc) for doc in documents],
        dtype="float32"
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    # Save FAISS index
    faiss.write_index(index, str(INDEX_PATH))

    # Save Metadata
    with open(METADATA_PATH, "wb") as file:
        pickle.dump(catalog, file)

    return len(catalog)


# -----------------------------
# Load FAISS Index
# -----------------------------

def load_faiss_index():

    return faiss.read_index(str(INDEX_PATH))


# -----------------------------
# Load Metadata
# -----------------------------

def load_metadata():

    with open(METADATA_PATH, "rb") as file:
        return pickle.load(file)
    
_index = None
_metadata = None


def load_faiss_index():

    global _index

    if _index is None:
        _index = faiss.read_index(str(INDEX_PATH))

    return _index


def load_metadata():

    global _metadata

    if _metadata is None:

        with open(METADATA_PATH, "rb") as file:
            _metadata = pickle.load(file)

    return _metadata