
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.sentiment_service import predict_sentiment


router = APIRouter(
    prefix="/api/sentiment",
    tags=["Sentiment Analysis"]
)


class SentimentRequest(BaseModel):
    feedback_text: str


@router.post("/predict")
def predict_feedback_sentiment(request: SentimentRequest):

    if not request.feedback_text.strip():
        raise HTTPException(
            status_code=422,
            detail="Feedback text cannot be empty."
        )

    try:
        result = predict_sentiment(request.feedback_text)

        return {
            "feedback_text": request.feedback_text,
            "sentiment": result["sentiment"],
            "confidence_score": result["confidence_score"]
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Sentiment prediction failed: {str(e)}"
        )
