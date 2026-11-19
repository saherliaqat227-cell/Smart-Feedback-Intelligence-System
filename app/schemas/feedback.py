from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class FeedbackCreate(BaseModel):
    customer_name: Optional[str] = None
    feedback_text: str


class FeedbackResponse(BaseModel):
    id: int
    customer_name: Optional[str]
    feedback_text: str
    sentiment: Optional[str]
    user_id: Optional[int]
    created_at: Optional[datetime]

    class Config:
        from_attributes = True