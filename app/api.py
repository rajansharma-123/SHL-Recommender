from fastapi import APIRouter

from app.schemas import (
    ChatRequest,
    ChatResponse,
    Recommendation
)

from app.agent import run_agent

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "ok"
    }


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    messages = [message.model_dump() for message in request.messages]

    response = run_agent(messages)

    recommendations = []

    for item in response["recommendations"]:

        recommendations.append(
            Recommendation(
                name=item["name"],
                url=item["link"],
                test_type=", ".join(item.get("keys", []))
            )
        )

    return ChatResponse(
        reply=response["reply"],
        recommendations=recommendations,
        end_of_conversation=response["end"]
    )