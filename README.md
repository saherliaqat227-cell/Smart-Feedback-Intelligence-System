
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
- app/ - Main application
- app/models/ - Database models
- app/schemas/ - Pydantic schemas
- app/routes/ - API routes
- app/services/ - Business logic
- app/core/ - Security configuration
- ml/ - Machine Learning files
- tests/ - Testing files
- docs/ - Project documentation

## Installation

Install the required dependencies:

```bash
pip install fastapi uvicorn sqlalchemy pydantic python-dotenv
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
The project uses SQLite database named smart_feedback.db.

## Current Progress
- FastAPI application setup completed.
- Health check API created.
- SQLite database configured.
- User and Feedback models created.
- Pydantic schemas created.
- Database schema documented.

## Author
Saher Liaqat
