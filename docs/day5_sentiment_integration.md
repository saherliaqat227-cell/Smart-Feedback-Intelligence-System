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

## 5. Testing Results

| Test Case | Input | Result | Confidence Score |
|---|---|---|---:|
| Positive | The service was excellent and amazing. | Positive | 99.97% |
| Negative | The service was very poor and disappointing. | Negative | 99.98% |
| Neutral | The product arrived yesterday. It is available in three different colors. | Positive (misclassified) | 87.91% |
| Empty | Blank spaces | HTTP 422 – Validation Error | N/A |
| Unusual | 12345 !!! @@@ 😊 | Neutral | 83.34% |

Additional neutral examples were also tested. Some were classified as Neutral, while others received a different prediction.


## 6. Confidence Score Explanation
The confidence score represents the highest probability returned by the model for its predicted sentiment class, multiplied by 100.

It indicates how strongly the model favours its predicted class. It does not guarantee that the prediction is correct.

## 7. Model Limitations
- The model may misclassify some neutral feedback.
- Predictions depend on patterns learned from the training dataset.
- Unusual text, short sentences and ambiguous wording may affect predictions.
- Confidence scores should not be treated as guaranteed accuracy.

## 8. Files Created or Updated
- `app/services/sentiment_service.py`
- `app/routes/sentiment.py`
- `app/routes/feedback.py`
- `main.py`
- `docs/day5_sentiment_integration.md`

## 9. Conclusion
The trained machine learning model was successfully integrated with the FastAPI backend. The sentiment prediction endpoint was implemented and tested. Feedback submissions now automatically receive sentiment predictions, and the predicted sentiment and confidence score are stored in the database.