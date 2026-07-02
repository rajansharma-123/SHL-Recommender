from rag.retriever import search_assessments

results = search_assessments(
    "Java Backend Developer"
)

print()

print("Top Results")

print("=" * 50)

for item in results:

    print(item["name"])

    print(item["link"])

    print(item["score"])

    print("-" * 50)