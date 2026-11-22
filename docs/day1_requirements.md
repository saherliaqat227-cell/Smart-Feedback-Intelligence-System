# Day 1 – Requirements, Assumptions and Project Understanding

## 1. Project Understanding

The Smart Feedback Intelligence System is a backend application designed to manage customer feedback and analyze its sentiment using Machine Learning.

The system allows users to submit feedback, stores feedback records in a database, and predicts whether the feedback is Positive, Negative, or Neutral.

The project uses FastAPI for API development, SQLAlchemy for database management, SQLite for data storage, and a Machine Learning model for sentiment analysis.

## 2. Key Requirements

- Create a FastAPI application.
- Set up a Python virtual environment and install dependencies.
- Create a proper project folder structure.
- Implement a working health-check endpoint.
- Design User and Feedback database entities.
- Create a GitHub repository.
- Prepare a README file with setup and running instructions.

## 3. Project Assumptions

- SQLite will be used as the initial database.
- SQLAlchemy will be used as the ORM.
- FastAPI will handle backend API requests.
- Users will need to register and log in to access protected features.
- Customer feedback will be classified into Positive, Negative, or Neutral sentiment.
- Feedback records will be stored in the database.
- A pre-trained Machine Learning model will be used for sentiment prediction.

## 4. Initial Questions and Considerations

- Which database should be used for the project?
- Which Machine Learning model is suitable for sentiment analysis?
- Should feedback submission require user authentication?
- How should prediction results be stored and displayed?

These questions were considered during the initial planning and design of the project.

## 5. Initial Technology Stack

- Programming Language: Python
- Backend Framework: FastAPI
- Database: SQLite
- ORM: SQLAlchemy
- API Documentation: Swagger UI
- Version Control: Git and GitHub
- Machine Learning: Scikit-learn

## 6. Day 1 Outcome

The initial project structure and development environment were established. FastAPI was configured with a working health-check endpoint. The initial database schema was designed, and the GitHub repository and README documentation were created.