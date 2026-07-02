from app.llm import generate_response

response = generate_response(
    "You are a helpful assistant.",
    "Say Hello in one sentence."
)

print(response)