from rag.vector_store import load_catalog

catalog = load_catalog()

print(f"Total Assessments: {len(catalog)}")

print(catalog[0]["name"])