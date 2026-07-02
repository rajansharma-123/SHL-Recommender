from app.handlers.compare import compare
from app.handlers.refine import (
    refine,
    is_refinement
)
from app.handlers.clarify import (
    clarify,
    is_vague
)

from app.handlers.refuse import (
    refuse,
    is_off_topic
)

from app.handlers.recommend import recommend


def build_conversation_context(messages):

    history = []

    for message in messages:

        if message["role"] == "user":
            history.append(message["content"])

    return "\n".join(history)


def run_agent(messages):

    conversation = build_conversation_context(messages)

    # Clarification
    if is_vague(conversation):
        return clarify()
    
    # Off-topic detection
    if is_off_topic(conversation):
        return refuse()

    # Refinement
    if is_refinement(conversation):
        return refine(conversation)

    # Recommendation
    return recommend(conversation)

