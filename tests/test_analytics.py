
from datetime import date


def register_and_login(client):
    client.post(
        "/api/auth/register",
        json={
            "username": "analytics_user",
            "email": "analytics@example.com",
            "password": "Test12345"
        }
    )

    response = client.post(
        "/api/auth/login",
        json={
            "email": "analytics@example.com",
            "password": "Test12345"
        }
    )

    assert response.status_code == 200

    return {
        "Authorization": f"Bearer {response.json()['access_token']}"
    }


# TEST 1: Analytics summary
def test_analytics_summary(client):
    headers = register_and_login(client)

    response = client.get(
        "/api/analytics/summary",
        headers=headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total_feedback"] == 0
    assert data["sentiment_counts"]["positive"] == 0
    assert data["sentiment_counts"]["negative"] == 0
    assert data["sentiment_counts"]["neutral"] == 0


# TEST 2: Analytics without login
def test_analytics_summary_unauthorized(client):
    response = client.get("/api/analytics/summary")

    assert response.status_code == 401


# TEST 3: Analytics trends
def test_analytics_trends(client):
    headers = register_and_login(client)

    response = client.get(
        f"/api/analytics/trends?start_date={date.today()}&end_date={date.today()}",
        headers=headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["start_date"] == str(date.today())
    assert data["end_date"] == str(date.today())
    assert "daily_trends" in data


# TEST 4: Invalid date range
def test_analytics_trends_invalid_date(client):
    headers = register_and_login(client)

    response = client.get(
        "/api/analytics/trends?start_date=2026-11-21&end_date=2026-11-01",
        headers=headers
    )

    assert response.status_code == 422


# TEST 5: Missing dates
def test_analytics_trends_missing_dates(client):
    headers = register_and_login(client)

    response = client.get(
        "/api/analytics/trends",
        headers=headers
    )

    assert response.status_code == 422
