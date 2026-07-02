from app.handlers.recommend import recommend


REFINE_WORDS = [
    "actually",
    "also",
    "add",
    "include",
    "instead",
    "change",
    "remove",
    "update"
]


def is_refinement(conversation: str):

    text = conversation.lower()

    return any(word in text for word in REFINE_WORDS)


def refine(conversation):

    # Current implementation:
    # Simply re-run recommendation using the full conversation.
    # Because conversation contains previous user messages,
    # the retriever sees the updated requirement.

    return recommend(conversation)