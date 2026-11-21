
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)

    customer_name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    feedback_text = Column(Text, nullable=False)

    sentiment = Column(String, nullable=True)
    confidence_score = Column(Float, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True),
        default=func.now(),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    user = relationship("User", back_populates="feedbacks")
