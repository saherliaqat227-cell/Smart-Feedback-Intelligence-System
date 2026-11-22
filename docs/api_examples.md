
# API Examples

## 1. API Base URL

```text
http://127.0.0.1:8000
```

## 2. User Registration

**Endpoint:** `POST /api/auth/register`

**Request Body:**

```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "StrongPassword123"
}
```

## 3. User Login

**Endpoint:** `POST /api/auth/login`

**Request Body:**

```json
{
  "email": "test@example.com",
  "password": "StrongPassword123"
}
```

**Response:** A successful login returns a JWT access token.

Use this token as a Bearer token for protected endpoints.

## 4. Create Customer Feedback

**Endpoint:** `POST /api/feedback`

**Authentication:** Required

**Request Body:**

```json
{
  "customer_name": "Test Customer",
  "email": "test@example.com",
  "feedback_text": "The service was excellent and amazing."
}
```

The system automatically predicts sentiment and stores the feedback.

## 5. Get All Feedback

**Endpoint:** `GET /api/feedback`

**Authentication:** Required

Returns feedback records belonging to the authenticated user.

## 6. Predict Sentiment

**Endpoint:** `POST /api/sentiment/predict`

**Authentication:** Not Required

**Request Body:**

```json
{
  "feedback_text": "The service was excellent and amazing."
}
```

**Example Response:**

```json
{
  "sentiment": "Positive",
  "confidence_score": 99.97
}
```

Note: The confidence score above is illustrative. Actual results depend on the model prediction.

## 7. Analytics Summary

**Endpoint:** `GET /api/analytics/summary`

**Authentication:** Required

Returns total feedback, sentiment counts, and sentiment distribution percentages.

## 8. Analytics Trends

**Endpoint:** `GET /api/analytics/trends`

**Authentication:** Required

**Query Parameters:**

- `start_date`
- `end_date`

Returns daily feedback counts and sentiment trends for the selected date range.

## 9. Health Check

**Endpoint:** `GET /health`

Checks whether the application is running.

## 10. API Documentation

Interactive API documentation is available through Swagger UI:

`http://127.0.0.1:8000/docs`
