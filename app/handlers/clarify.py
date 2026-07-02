VAGUE_WORDS = {
    "assessment",
    "assessments",
    "test",
    "tests",
    "hire",
    "hiring",
    "job",
    "candidate",
    "need"
}


def is_vague(query: str):

    query = query.lower().strip()

    words = query.split()

    if len(words) <= 2:
        return True

    if all(word in VAGUE_WORDS for word in words):
        return True

    return False


def clarify():

    return {
        "reply": (
            "I'd be happy to help. "
            "What role are you hiring for? "
            "Please also mention the experience level if possible."
        ),
        "recommendations": [],
        "end": False
    }