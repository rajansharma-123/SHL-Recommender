from rag.retriever import find_assessment_by_name
from app.prompts import SYSTEM_PROMPT
from app.llm import generate_response


def compare(conversation):

    text = conversation.lower()

    if " and " not in text:
        return None

    if "difference between" in text:
        text = text.replace("difference between", "")

    elif "compare" in text:
        text = text.replace("compare", "")

    left, right = text.split(" and ", 1)

    left = left.strip()
    right = right.strip()

    assessment1 = find_assessment_by_name(left)
    assessment2 = find_assessment_by_name(right)

    if assessment1 is None or assessment2 is None:
        return None

    prompt = f"""
Compare these SHL assessments.

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

Rules:

- Compare only these assessments.
- Mention purpose.
- Mention differences.
- Do not invent any information.
- Keep answer under 120 words.
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