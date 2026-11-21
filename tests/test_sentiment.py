def test_positive_sentiment(client):
    response = client.post(
        "/api/sentiment/predict",
        json={"feedback_text": "The service was excellent and amazing!"}
    )

    assert response.status_code == 200
    assert response.json()["sentiment"] == "Positive"
    assert response.json()["confidence_score"] > 0


def test_negative_sentiment(client):
    response = client.post(
        "/api/sentiment/predict",
        json={"feedback_text": "The service was terrible and disappointing."}
    )

    assert response.status_code == 200
    assert response.json()["sentiment"] == "Negative"
    assert response.json()["confidence_score"] > 0


def test_neutral_sentiment(client):
    response = client.post(
        "/api/sentiment/predict",
        json={"feedback_text": "The product arrived today."}
    )

    assert response.status_code == 200
    assert response.json()["sentiment"] == "Neutral"
    assert response.json()["confidence_score"] > 0


def test_empty_feedback(client):
    response = client.post(
        "/api/sentiment/predict",
        json={"feedback_text": ""}
    )

    assert response.status_code == 422