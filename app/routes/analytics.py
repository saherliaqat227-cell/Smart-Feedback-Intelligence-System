
from datetime import date, datetime, time, timedelta

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError

from app.database import get_db
from app.models.feedback import Feedback
from app.core.security import get_current_user


router = APIRouter(
    prefix="/api/analytics",
    tags=["Analytics"],
    dependencies=[Depends(get_current_user)]
)


# SUMMARY STATISTICS AND SENTIMENT DISTRIBUTION
@router.get("/summary")
def get_analytics_summary(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    try:
        query = db.query(Feedback).filter(
            Feedback.user_id == current_user.id
        )

        total_feedback = query.count()

        positive_count = query.filter(
            Feedback.sentiment == "Positive"
        ).count()

        negative_count = query.filter(
            Feedback.sentiment == "Negative"
        ).count()

        neutral_count = query.filter(
            Feedback.sentiment == "Neutral"
        ).count()

        if total_feedback > 0:
            positive_percentage = round(
                positive_count / total_feedback * 100, 2
            )
            negative_percentage = round(
                negative_count / total_feedback * 100, 2
            )
            neutral_percentage = round(
                neutral_count / total_feedback * 100, 2
            )
        else:
            positive_percentage = 0
            negative_percentage = 0
            neutral_percentage = 0

        return {
            "total_feedback": total_feedback,
            "sentiment_counts": {
                "positive": positive_count,
                "negative": negative_count,
                "neutral": neutral_count
            },
            "sentiment_distribution": {
                "positive_percentage": positive_percentage,
                "negative_percentage": negative_percentage,
                "neutral_percentage": neutral_percentage
            }
        }

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Database error occurred while fetching analytics"
        )


# DAILY FEEDBACK COUNTS AND SENTIMENT TRENDS
@router.get("/trends")
def get_analytics_trends(
    start_date: date = Query(...),
    end_date: date = Query(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    try:
        if start_date > end_date:
            raise HTTPException(
                status_code=422,
                detail="Start date cannot be later than end date."
            )

        start_datetime = datetime.combine(
            start_date, time.min
        )

        end_datetime = datetime.combine(
            end_date + timedelta(days=1), time.min
        )

        results = db.query(
            func.date(Feedback.created_at).label("feedback_date"),
            Feedback.sentiment,
            func.count(Feedback.id).label("count")
        ).filter(
            Feedback.user_id == current_user.id,
            Feedback.created_at >= start_datetime,
            Feedback.created_at < end_datetime
        ).group_by(
            func.date(Feedback.created_at),
            Feedback.sentiment
        ).order_by(
            func.date(Feedback.created_at)
        ).all()

        daily_data = {}

        for row in results:
            day = str(row.feedback_date)

            if day not in daily_data:
                daily_data[day] = {
                    "date": day,
                    "total_feedback": 0,
                    "positive": 0,
                    "negative": 0,
                    "neutral": 0
                }

            daily_data[day]["total_feedback"] += row.count

            if row.sentiment == "Positive":
                daily_data[day]["positive"] += row.count

            elif row.sentiment == "Negative":
                daily_data[day]["negative"] += row.count

            elif row.sentiment == "Neutral":
                daily_data[day]["neutral"] += row.count

        return {
            "start_date": str(start_date),
            "end_date": str(end_date),
            "daily_trends": list(daily_data.values())
        }

    except HTTPException:
        raise

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Database error occurred while fetching trends"
        )
