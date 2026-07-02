from groq import Groq

from app.config import GROQ_API_KEY

client = None
if GROQ_API_KEY:
    client = Groq(api_key=GROQ_API_KEY)


def generate_response(system_prompt: str, user_prompt: str):
    if client is None:
        return "The Groq API key is not configured yet. Please set the GROQ_API_KEY environment variable before using the recommender."

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content