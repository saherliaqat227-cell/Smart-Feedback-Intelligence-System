from fastapi import FastAPI
from app.database import engine, Base
from app.models.user import User
from app.models.feedback import Feedback

app = FastAPI(
    title="Smart Feedback Intelligence System",
    description="Customer Feedback Sentiment Analysis API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Smart Feedback Intelligence System is running!",
        "status": "Success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "Healthy"
    }