# Day 5 – Sentiment Analysis Integration

## 1. Objective

The objective of Day 5 was to integrate the trained machine learning sentiment analysis model into the FastAPI backend.

## 2. Model Integration

The trained Logistic Regression model and TF-IDF vectorizer were loaded from the following files:

- `ml/sentiment_model.pkl`
- `ml/tfidf_vectorizer.pkl`

A sentiment prediction service was created in:

`app/services/sentiment_service.py`

The service converts feedback text into TF-IDF features and predicts its sentiment.

## 3. Sentiment Prediction API

The following endpoint was implemented:

**POST `/api/sentiment/predict`**

It accepts feedback text and returns:

- Original feedback text
- Predicted sentiment
- Confidence score

**Authentication:** The sentiment prediction endpoint is public and does not require JWT authentication. This allows users to test sentiment predictions without creating an account. Feedback management endpoints remain protected and require a valid JWT access token.

## 4. Feedback Submission Integration

The feedback submission endpoint was connected to the sentiment prediction service.

When a customer submits feedback:

1. The feedback text is received.
2. The sentiment model predicts its sentiment.
3. The confidence score is calculated.
4. The feedback and prediction results are saved in the database.

The predicted sentiment and confidence score are stored with the feedback record.

## 5. Earlier Testing Results

| Test Case | Result | Confidence Score |
|---|---|---:|
| Positive | Positive | 99.97% |
| Negative | Negative | 99.98% |
| Neutral example | Positive (misclassified) | 87.91% |
| Empty | HTTP 422 – Validation Error | N/A |
| Unusual text | Neutral | 83.34% |

Additional neutral examples were also tested. Some were classified as Neutral, while others received a different prediction.

## 6. Latest API Verification Results

The following tests were performed on the running FastAPI application:

| Test Case | Predicted Result | Confidence Score | HTTP Status |
|---|---|---:|---:|
| Positive | Positive | 95.18% | 200 |
| Negative | Negative | 99.99% | 200 |
| Neutral | Neutral | 59.27% | 200 |
| Empty Feedback | Validation Error | N/A | 422 |

## 7. Automatic Feedback Submission Test

The protected feedback creation endpoint was also tested using JWT authentication.

**Endpoint:** `POST /api/feedback`

The system successfully:

- Authenticated the user using a JWT access token.
- Created a new feedback record.
- Automatically predicted its sentiment.
- Calculated the confidence score.
- Saved the feedback and prediction results in the database.

**Verified Response:**

| Field | Result |
|---|---|
| HTTP Status | 200 OK |
| Feedback ID | 14 |
| Sentiment | Positive |
| Confidence Score | 99.85% |
| User ID | 2 |

## 8. Confidence Score Explanation

The confidence score represents the highest probability returned by the model for its predicted sentiment class, multiplied by 100.

It indicates how strongly the model favours its predicted class. It does not guarantee that the prediction is correct.

## 9. Model Limitations

- The model may misclassify some neutral feedback.
- Predictions depend on patterns learned from the training dataset.
- Unusual text, short sentences and ambiguous wording may affect predictions.
- Confidence scores should not be treated as guaranteed accuracy.

## 10. Files Created or Updated

- `app/services/sentiment_service.py`
- `app/routes/sentiment.py`
- `app/routes/feedback.py`
- `main.py`
- `docs/day5_sentiment_integration.md`

## 11. Conclusion

The trained machine learning model was successfully integrated with the FastAPI backend. The sentiment prediction endpoint was implemented and tested with positive, negative, neutral and empty feedback inputs.

Feedback submissions now automatically receive sentiment predictions, and the predicted sentiment and confidence score are stored in the database. The integration and practical API tests were successfully completed.