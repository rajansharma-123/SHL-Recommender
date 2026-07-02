from rag.retriever import search_assessments
from app.prompts import SYSTEM_PROMPT
from app.llm import generate_response


def build_context(results):

    context = ""

    for item in results:

        context += f"""
Assessment

Name:
{item["name"]}

Description:
{item["description"]}

Skills:
{", ".join(item["keys"])}

URL:
{item["link"]}

------------------------
"""

    return context


def recommend(conversation):

    results = search_assessments(
        conversation,
        top_k=5
    )

    context = build_context(results)

    prompt = f"""
User Requirement

{conversation}

Available SHL Assessments

{context}

Recommend only these assessments.

Never invent assessments.

Explain briefly.
"""

    reply = generate_response(
        SYSTEM_PROMPT,
        prompt
    )

    return {
        "reply": reply,
        "recommendations": results,
        "end": True
    }