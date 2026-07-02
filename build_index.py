from rag.vector_store import create_faiss_index

total = create_faiss_index()

print(f"FAISS Index Created Successfully!")

print(f"Total Assessments Indexed : {total}")