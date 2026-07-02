from app.llm import generate_response


INTENT_PROMPT = """
You are an intent classifier.

Classify the user's latest request into exactly ONE of these intents:

- clarify
- recommend
- refine
- compare
- off_topic

Rules:

clarify
The user has not provided enough information.

recommend
The user is asking for assessment recommendations.

refine
The user wants to modify previous recommendations.

compare
The user wants to compare assessments.

off_topic
The user is asking something unrelated to SHL assessments.

Return ONLY one word.
"""


def detect_intent(conversation: str):

    response = generate_response(
        INTENT_PROMPT,
        conversation
    )

    return response.strip().lower()