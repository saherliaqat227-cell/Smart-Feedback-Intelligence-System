
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class FeedbackCreate(BaseModel):
    customer_name: Optional[str] = None
    email: Optional[EmailStr] = None
    feedback_text: str


class FeedbackResponse(BaseModel):
    id: int
    customer_name: Optional[str]
    email: Optional[str]
    feedback_text: str
    sentiment: Optional[str]
    confidence_score: Optional[float]
    user_id: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class FeedbackUpdate(BaseModel):
    customer_name: Optional[str] = None
    email: Optional[EmailStr] = None
    feedback_text: Optional[str] = None
    sentiment: Optional[str] = None
    confidence_score: Optional[float] = None
