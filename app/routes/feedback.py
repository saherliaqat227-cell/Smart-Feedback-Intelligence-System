from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User

from app.core.security import get_current_user

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Optional
from datetime import datetime


from app.database import get_db
from app.models.feedback import Feedback
from app.schemas.feedback import FeedbackCreate, FeedbackResponse, FeedbackUpdate

router = APIRouter(
    prefix="/feedback",
    tags=["Feedback"],
    dependencies=[Depends(get_current_user)]
)


# CREATE FEEDBACK
@router.post("/", response_model=FeedbackResponse)
def create_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    try:

        new_feedback = Feedback(
            customer_name=feedback.customer_name,
            email=feedback.email,
            feedback_text=feedback.feedback_text
        )

        db.add(new_feedback)
        db.commit()
        db.refresh(new_feedback)

        return new_feedback

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Database error occurred while creating feedback"
        )


# GET ALL FEEDBACK WITH SEARCH, FILTERS AND PAGINATION
@router.get("/", response_model=List[FeedbackResponse])
def get_all_feedback(
    search: Optional[str] = None,
    sentiment: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    try:
        query = db.query(Feedback)

        if search:
            query = query.filter(
                (Feedback.customer_name.ilike(f"%{search}%")) |
                (Feedback.feedback_text.ilike(f"%{search}%"))
            )

        if sentiment:
            query = query.filter(Feedback.sentiment == sentiment)

        if start_date:
            query = query.filter(Feedback.created_at >= start_date)

        if end_date:
            query = query.filter(Feedback.created_at <= end_date)

        return query.order_by(Feedback.id).offset(skip).limit(limit).all()

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Database error occurred while fetching feedback"
        )


# GET FEEDBACK BY ID
@router.get("/{feedback_id}", response_model=FeedbackResponse)
def get_feedback(feedback_id: int, db: Session = Depends(get_db)):
    try:
        feedback = db.query(Feedback).filter(
            Feedback.id == feedback_id
        ).first()

        if feedback is None:
            raise HTTPException(
                status_code=404,
                detail="Feedback not found"
            )

        return feedback

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Database error occurred while fetching feedback"
        )


# UPDATE FEEDBACK
@router.put("/{feedback_id}", response_model=FeedbackResponse)
def update_feedback(
    feedback_id: int,
    updated_data: FeedbackUpdate,
    db: Session = Depends(get_db)
):
    try:
        feedback = db.query(Feedback).filter(
            Feedback.id == feedback_id
        ).first()

        if feedback is None:
            raise HTTPException(
                status_code=404,
                detail="Feedback not found"
            )

        data = updated_data.model_dump(exclude_unset=True)

        for key, value in data.items():
            if value is not None:
                setattr(feedback, key, value)

        db.commit()
        db.refresh(feedback)

        return feedback

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Database error occurred while updating feedback"
        )


# DELETE FEEDBACK
@router.delete("/{feedback_id}")
def delete_feedback(feedback_id: int, db: Session = Depends(get_db)):
    try:
        feedback = db.query(Feedback).filter(
            Feedback.id == feedback_id
        ).first()

        if feedback is None:
            raise HTTPException(
                status_code=404,
                detail="Feedback not found"
            )

        db.delete(feedback)
        db.commit()

        return {"message": "Feedback deleted successfully"}

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Database error occurred while deleting feedback"
        )

    security = HTTPBearer(auto_error=False)

    def get_current_user(
            credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
            db: Session = Depends(get_db)
    ):
        if credentials is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
                headers={"WWW-Authenticate": "Bearer"}
            )

        token_data = verify_token(credentials.credentials)

        if token_data is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token",
                headers={"WWW-Authenticate": "Bearer"}
            )

        user_id = token_data.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

        user = db.query(User).filter(User.id == int(user_id)).first()

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )

        return user



