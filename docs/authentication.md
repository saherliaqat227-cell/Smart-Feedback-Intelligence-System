# Authentication and Access Rules

## 1. Authentication Overview

The Smart Feedback Intelligence System uses JWT (JSON Web Token) authentication to secure private API endpoints.

Users must register and log in before accessing protected feedback resources.

## 2. User Registration

- Endpoint: `POST /api/auth/register`
- Users can register with a username, email, and password.
- Passwords are hashed using bcrypt before being stored in the database.
- Duplicate email addresses are not allowed.

## 3. User Login

- Endpoint: `POST /api/auth/login`
- Users log in using their email and password.
- The system verifies the password against its stored hash.
- After successful login, the system generates a JWT access token.

## 4. JWT Token Security

- JWT uses the HS256 algorithm.
- Access tokens expire after 30 minutes.
- The token contains the user's ID.
- Protected endpoints require a valid Bearer token.
- Missing, invalid, or expired tokens are rejected.

## 5. Protected Endpoints

The following feedback endpoints require JWT authentication:

- `GET /api/feedback`
- `POST /api/feedback`
- `GET /api/feedback/{id}`
- `PUT /api/feedback/{id}`
- `DELETE /api/feedback/{id}`

## 6. User Access Rules

- Each authenticated user can access only their own feedback records.
- Users cannot view, update, or delete another user's feedback.
- The system checks the authenticated user's ID when accessing feedback records.
- Unauthorized requests return HTTP 401.
- Feedback records that do not belong to the current user return HTTP 404.

## 7. Public Sentiment Prediction

- Endpoint: `POST /api/sentiment/predict`
- This endpoint is public and does not require authentication.
- Users can submit text for sentiment prediction.

## 8. Security Summary

JWT authentication protects private feedback resources, bcrypt protects user passwords, and user-level access control prevents unauthorized access to other users' data.