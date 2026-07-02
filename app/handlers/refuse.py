OFF_TOPIC_KEYWORDS = [
    "ipl",
    "cricket",
    "football",
    "movie",
    "actor",
    "actress",
    "weather",
    "bitcoin",
    "stock",
    "prime minister",
    "president",
    "politics",
    "news",
    "recipe",
    "music",
    "song",
    "youtube",
    "instagram"
]


def is_off_topic(query: str):

    query = query.lower()

    return any(word in query for word in OFF_TOPIC_KEYWORDS)


def refuse():

    return {
        "reply": (
            "I can only help with SHL assessment recommendations, "
            "assessment comparisons, and selecting assessments from the "
            "SHL catalog."
        ),
        "recommendations": [],
        "end": False
    }