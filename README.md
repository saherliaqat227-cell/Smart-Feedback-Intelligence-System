# Smart Feedback Intelligence System

## Project Description

Smart Feedback Intelligence System is a Python-based backend application that analyzes customer feedback and identifies its sentiment as Positive, Negative, or Neutral using Machine Learning.

## Technologies Used

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Scikit-learn
- Machine Learning
- Natural Language Processing (NLP)

## Project Structure

- `app/` - Main application
- `app/models/` - Database models
- `app/schemas/` - Pydantic schemas
- `app/routes/` - API routes
- `app/services/` - Business logic
- `app/core/` - Security configuration
- `ml/` - Machine Learning files
- `tests/` - Testing files
- `docs/` - Project documentation

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

## API Documentation

After starting the server, open:

http://127.0.0.1:8000/docs

## Database

The project uses SQLite database named `smart_feedback.db`.

## Current Progress

### Day 1 — Requirements, Setup and Design

- FastAPI application setup completed.
- Python virtual environment configured.
- Health check API created.
- SQLite database configured.
- Initial project structure created.
- Database schema documented.

### Day 2 — Database and Feedback CRUD

- SQLAlchemy database integration completed.
- User and Feedback models created.
- Pydantic input and output schemas implemented.
- Feedback Create, Read, Update and Delete (CRUD) APIs implemented.
- Keyword search and sentiment filtering added.
- Date range filtering implemented.
- Pagination implemented.
- Input validation and missing-record handling added.
- Database error handling implemented and tested.
- Database migration script created.

### Day 3 — Authentication and Security

- User registration and login APIs implemented.
- Secure password hashing using bcrypt.
- JWT access token generation with 30-minute expiry.
- Protected feedback endpoints implemented.
- Token validation and authenticated user verification.
- Unauthorized access and invalid token handling tested.
- Environment variables configured for secret key.

## Author

Saher Liaqat