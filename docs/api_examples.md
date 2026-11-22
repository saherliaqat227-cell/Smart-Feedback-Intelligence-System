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

## 6. Get Feedback by ID

**Endpoint:** `GET /api/feedback/{feedback_id}`

**Authentication:** Required

**Example:**

```text
GET /api/feedback/1
```

Returns the feedback record with the specified ID, if it belongs to the authenticated user.

## 7. Update Feedback

**Endpoint:** `PUT /api/feedback/{feedback_id}`

**Authentication:** Required

**Example:**

```text
PUT /api/feedback/1
```

**Request Body:**

```json
{
  "feedback_text": "Updated feedback text."
}
```

Updates the selected feedback record.

## 8. Delete Feedback

**Endpoint:** `DELETE /api/feedback/{feedback_id}`

**Authentication:** Required

**Example:**

```text
DELETE /api/feedback/1
```

Deletes the selected feedback record.

## 9. Search Feedback

**Endpoint:** `GET /api/feedback?search=Ali`

**Authentication:** Required

Searches feedback records using the search keyword.

## 10. Filter Feedback by Sentiment

**Endpoint:** `GET /api/feedback?sentiment=Positive`

**Authentication:** Required

Filters feedback records by sentiment.

Supported sentiment categories:

- Positive
- Negative
- Neutral

## 11. Filter Feedback by Date

**Endpoint:** `GET /api/feedback`

**Authentication:** Required

**Query Parameters:**

- `start_date`
- `end_date`

**Example:**

```text
GET /api/feedback?start_date=2026-11-01T00:00:00&end_date=2026-11-30T23:59:59
```

Returns feedback records within the selected date range.

## 12. Feedback Pagination

**Endpoint:** `GET /api/feedback?skip=0&limit=10`

**Authentication:** Required

**Query Parameters:**

- `skip`: Number of records to skip.
- `limit`: Maximum number of records to return.

Pagination helps retrieve feedback records in smaller groups.

## 13. Predict Sentiment

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

## 14. Analytics Summary

**Endpoint:** `GET /api/analytics/summary`

**Authentication:** Required

Returns total feedback, sentiment counts, and sentiment distribution percentages.

## 15. Analytics Trends

**Endpoint:** `GET /api/analytics/trends`

**Authentication:** Required

**Query Parameters:**

- `start_date`
- `end_date`

Returns daily feedback counts and sentiment trends for the selected date range.

## 16. Health Check

**Endpoint:** `GET /health`

Checks whether the application is running.

## 17. API Documentation

Interactive API documentation is available through Swagger UI:

`http://127.0.0.1:8000/docs`
