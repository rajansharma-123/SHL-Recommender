from rag.retriever import find_assessment_by_name
from app.prompts import SYSTEM_PROMPT
from app.llm import generate_response


def compare_assessments(query: str):

    query_lower = query.lower()

    # Example:
    # Difference between OPQ and GSA

    if " and " not in query_lower:
        return None

    left, right = query_lower.split(" and ", 1)

    left = left.replace("difference between", "").strip()
    right = right.strip()

    assessment1 = find_assessment_by_name(left)
    assessment2 = find_assessment_by_name(right)

    if not assessment1 or not assessment2:
        return None

    prompt = f"""
Compare these two SHL assessments.

Assessment 1

Name:
{assessment1["name"]}

Description:
{assessment1["description"]}


Assessment 2

Name:
{assessment2["name"]}

Description:
{assessment2["description"]}

Only compare these two assessments.
Do not invent any information.
"""

    reply = generate_response(
        SYSTEM_PROMPT,
        prompt
    )

    return {
        "reply": reply,
        "recommendations": [
            assessment1,
            assessment2
        ],
        "end": True
    }