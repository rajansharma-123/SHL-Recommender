from rag.vector_store import create_index

total = create_index()

print("=" * 50)
print("TF-IDF Index Created Successfully")
print(f"Total Assessments Indexed: {total}")
print("=" * 50)