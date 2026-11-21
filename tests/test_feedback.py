
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

from app.routes.feedback import get_all_feedback


def test_get_all_feedback_database_error():
    db = MagicMock()

    db.query.side_effect = SQLAlchemyError(
        "Simulated database failure"
    )

    current_user = SimpleNamespace(id=2)

    with pytest.raises(HTTPException) as exc_info:
        get_all_feedback(
            search=None,
            sentiment=None,
            start_date=None,
            end_date=None,
            skip=0,
            limit=10,
            db=db,
            current_user=current_user
        )

    assert exc_info.value.status_code == 500

    assert exc_info.value.detail == (
        "Database error occurred while fetching feedback"
    )
