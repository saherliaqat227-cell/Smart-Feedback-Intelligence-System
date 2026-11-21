
import logging

from fastapi import FastAPI

from app.database import engine, Base
from app.models.user import User
from app.models.feedback import Feedback
from app.routes.feedback import router as feedback_router
from app.routes.auth import router as auth_router
from app.routes.sentiment import router as sentiment_router
from app.routes.analytics import router as analytics_router


# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


app = FastAPI(
    title="Smart Feedback Intelligence System",
    description="Customer Feedback Sentiment Analysis API",
    version="1.0.0"
)


# Create Database Tables
Base.metadata.create_all(bind=engine)


# Register API Routers
app.include_router(feedback_router)
app.include_router(auth_router)
app.include_router(sentiment_router)
app.include_router(analytics_router)


@app.on_event("startup")
def startup_event():
    logger.info("Smart Feedback Intelligence System started successfully")


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
