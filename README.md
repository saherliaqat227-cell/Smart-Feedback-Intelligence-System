# Smart Feedback Intelligence System

## Project Description

Smart Feedback Intelligence System is a Python-based backend application that analyzes customer feedback and identifies its sentiment as Positive, Negative, or Neutral using Machine Learning.

The system provides REST APIs for managing customer feedback, user authentication, and sentiment classification.

## Technologies Used

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Scikit-learn
- Pandas
- Matplotlib
- TF-IDF Vectorization
- Logistic Regression
- Natural Language Processing (NLP)
- JWT Authentication
- Bcrypt Password Hashing

## Project Structure

```text
Smart-Feedback-Intelligence-System/
│
├── app/
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   ├── services/
│   └── core/
│
├── docs/
│   ├── dataset.md
│   └── model_training.md
│
├── ml/
│   ├── inspect_dataset.py
│   ├── clean_dataset.py
│   ├── prepare_data.py
│   ├── train_model.py
│   ├── sentiment_distribution.png
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── tests/
│
├── main.py
├── migrate_db.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/saherliaqat227-cell/Smart-Feedback-Intelligence-System.git
```

### 2. Navigate to Project Directory

```bash
cd Smart-Feedback-Intelligence-System
```

### 3. Create Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root and configure the required secret key.

Use `.env.example` as a reference.

## Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Open API documentation:

http://127.0.0.1:8000/docs

## Database

The project uses SQLite as its database.

Database file: `smart_feedback.db`

SQLAlchemy is used for database integration and ORM operations.

## Authentication and Access Rules

- User registration and login endpoints are publicly accessible.
- Feedback CRUD endpoints require JWT authentication.
- Users must provide a valid Bearer token to access protected feedback endpoints.
- Requests without a token or with an invalid or expired token are rejected with HTTP 401 Unauthorized.
- Passwords are securely stored as bcrypt hashes.
- JWT access tokens expire after 30 minutes.

## Machine Learning Model

### Dataset

- Dataset Name: Twitter and Reddit Sentimental Analysis Dataset
- Source: Kaggle
- Selected File: `Twitter_Data.csv`
- Original Records: 162,980
- Cleaned Records: 160,843
- Sentiment Classes: Negative, Neutral, Positive

### Data Preprocessing

- Missing values removed.
- Duplicate rows removed.
- Dataset divided into 80% training and 20% testing data.
- Stratified splitting used to maintain class distribution.
- TF-IDF vectorization implemented.
- TF-IDF fitted only on training data to prevent data leakage.

### Model Training

- Algorithm: Logistic Regression
- Maximum Features: 30,000
- N-gram Range: (1, 2)
- Maximum Iterations: 1000

### Model Evaluation

| Evaluation Metric | Score |
|---|---:|
| Accuracy | 85.24% |
| Precision | 85.63% |
| Recall | 85.24% |
| F1-Score | 85.09% |

### Saved Model Files

- `sentiment_model.pkl` — Trained Logistic Regression model.
- `tfidf_vectorizer.pkl` — Trained TF-IDF vectorizer.

### Retrain the Model

After placing `Twitter_Data_Cleaned.csv` inside the `ml` folder, run:

```bash
python ml/train_model.py
```

The script trains the model, evaluates its performance, and saves the updated model and vectorizer.

**Note:** Dataset CSV files are excluded from GitHub using `.gitignore`. Download and prepare the dataset separately before training.

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

### Day 4 — Dataset and Model Training

- Labeled sentiment dataset selected and documented.
- Dataset explored using Pandas.
- Sentiment class distribution analyzed and visualized.
- Missing values and duplicate records removed.
- Training and testing data split using an 80/20 ratio.
- Stratified sampling implemented.
- TF-IDF text preprocessing implemented.
- Logistic Regression classification model trained.
- Accuracy, Precision, Recall and F1-score calculated.
- Confusion Matrix generated.
- Trained model and TF-IDF vectorizer saved.
- Model evaluation and retraining documentation created.

## Author

**Saher Liaqat**

GitHub: https://github.com/saherliaqat227-cell

## Project Repository

https://github.com/saherliaqat227-cell/Smart-Feedback-Intelligence-System