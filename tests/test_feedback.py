
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


def test_create_feedback_success(client):
    register = client.post(
        "/api/auth/register",
        json={
            "username": "feedbackuser",
            "email": "feedback@example.com",
            "password": "Test12345"
        }
    )

    login = client.post(
        "/api/auth/login",
        json={
            "email": "feedback@example.com",
            "password": "Test12345"
        }
    )

    token = login.json()["access_token"]

    response = client.post(
        "/api/feedback",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "customer_name": "Test Customer",
            "email": "customer@example.com",
            "feedback_text": "The service was excellent!"
        }
    )

    assert register.status_code == 200
    assert login.status_code == 200
    assert response.status_code == 200
    assert response.json()["customer_name"] == "Test Customer"
    assert response.json()["sentiment"] == "Positive"


def test_get_feedback_unauthorized(client):
    response = client.get("/api/feedback")
    assert response.status_code == 401


def test_feedback_user_isolation(client):
    client.post(
        "/api/auth/register",
        json={
            "username": "firstuser",
            "email": "first@example.com",
            "password": "Test12345"
        }
    )

    login1 = client.post(
        "/api/auth/login",
        json={
            "email": "first@example.com",
            "password": "Test12345"
        }
    )

    token1 = login1.json()["access_token"]

    created = client.post(
        "/api/feedback",
        headers={"Authorization": f"Bearer {token1}"},
        json={"feedback_text": "Excellent service!"}
    )

    feedback_id = created.json()["id"]

    client.post(
        "/api/auth/register",
        json={
            "username": "seconduser",
            "email": "second@example.com",
            "password": "Test12345"
        }
    )

    login2 = client.post(
        "/api/auth/login",
        json={
            "email": "second@example.com",
            "password": "Test12345"
        }
    )

    token2 = login2.json()["access_token"]

    response = client.get(
        f"/api/feedback/{feedback_id}",
        headers={"Authorization": f"Bearer {token2}"}
    )

    assert response.status_code == 404


def test_feedback_pagination(client):
        client.post(
            "/api/auth/register",
            json={
                "username": "pageuser",
                "email": "page@example.com",
                "password": "Test12345"
            }
        )

        login = client.post(
            "/api/auth/login",
            json={
                "email": "page@example.com",
                "password": "Test12345"
            }
        )

        token = login.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        for i in range(3):
            client.post(
                "/api/feedback",
                headers=headers,
                json={"feedback_text": f"Excellent service number {i}"}
            )

        response = client.get(
            "/api/feedback?skip=0&limit=2",
            headers=headers
        )

        assert response.status_code == 200
        assert len(response.json()) == 2

def test_feedback_search(client):
        client.post(
            "/api/auth/register",
            json={
                "username": "searchuser",
                "email": "search@example.com",
                "password": "Test12345"
            }
        )

        login = client.post(
            "/api/auth/login",
            json={
                "email": "search@example.com",
                "password": "Test12345"
            }
        )

        token = login.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        client.post(
            "/api/feedback",
            headers=headers,
            json={
                "customer_name": "Ali",
                "feedback_text": "Excellent service"
            }
        )

        client.post(
            "/api/feedback",
            headers=headers,
            json={
                "customer_name": "Sara",
                "feedback_text": "Average experience"
            }
        )

        response = client.get(
            "/api/feedback?search=Ali",
            headers=headers
        )

        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["customer_name"] == "Ali"

def test_feedback_sentiment_filter(client):
        client.post(
            "/api/auth/register",
            json={
                "username": "filteruser",
                "email": "filter@example.com",
                "password": "Test12345"
            }
        )

        login = client.post(
            "/api/auth/login",
            json={
                "email": "filter@example.com",
                "password": "Test12345"
            }
        )

        token = login.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        client.post(
            "/api/feedback",
            headers=headers,
            json={"feedback_text": "Excellent amazing wonderful service"}
        )

        client.post(
            "/api/feedback",
            headers=headers,
            json={"feedback_text": "Terrible awful disappointing service"}
        )

        response = client.get(
            "/api/feedback?sentiment=Positive",
            headers=headers
        )

        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["sentiment"] == "Positive"

def test_feedback_invalid_date_range(client):
        client.post(
            "/api/auth/register",
            json={
                "username": "dateuser",
                "email": "date@example.com",
                "password": "Test12345"
            }
        )

        login = client.post(
            "/api/auth/login",
            json={
                "email": "date@example.com",
                "password": "Test12345"
            }
        )

        token = login.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        response = client.get(
            "/api/feedback?start_date=2026-11-21T00:00:00&end_date=2026-11-01T00:00:00",
            headers=headers
        )

        assert response.status_code == 422

