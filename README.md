# Smart Feedback Intelligence System

A machine learning-based customer feedback management system built with Python, FastAPI, SQLAlchemy, SQLite, and Scikit-learn. The system allows authenticated users to manage customer feedback and automatically analyze its sentiment as Positive, Negative, or Neutral.

## 1. Project Overview

The Smart Feedback Intelligence System is a backend application that combines REST APIs with machine learning to analyze customer feedback.

It uses a trained Logistic Regression model with TF-IDF text vectorization to predict the sentiment of customer feedback.

### Main Features

- User registration and login
- Secure password hashing
- JWT-based authentication
- Customer feedback management (CRUD)
- Automatic sentiment prediction
- Confidence score calculation
- Search and sentiment filtering
- Date-based filtering
- Pagination
- User-specific feedback access
- SQLite database integration
- Machine learning model integration
- Analytics and sentiment distribution
- Daily feedback and sentiment trends
- Input validation and error handling
- Automated testing with Pytest

## 2. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API development |
| SQLAlchemy | Database ORM |
| SQLite | Database |
| Pydantic | Data validation |
| JWT | Authentication |
| Bcrypt | Password hashing |
| Scikit-learn | Machine learning |
| TF-IDF | Text feature extraction |
| Logistic Regression | Sentiment classification |
| Pandas | Dataset processing |
| NumPy | Numerical operations |
| Joblib | Saving and loading ML models |
| Pytest | Automated testing |
| Matplotlib | Data visualization |

TF-IDF was selected for text feature extraction because it integrates directly with the Scikit-learn machine learning pipeline.

## 3. Project Structure

```text
Smart-Feedback-Intelligence-System/
│
├── app/
│   ├── core/
│   │   └── security.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── feedback.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   └── feedback.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── feedback.py
│   │   ├── sentiment.py
│   │   └── analytics.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   └── sentiment_service.py
│   │
│   └── database.py
│
├── docs/
│   ├── database_schema.md
│   ├── dataset.md
│   ├── model_training.md
│   ├── day5_sentiment_integration.md
│   └── day6_test_results.md
│
├── ml/
│   ├── inspect_dataset.py
│   ├── clean_dataset.py
│   ├── prepare_data.py
│   ├── train_model.py
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_feedback.py
│   ├── test_sentiment.py
│   └── test_analytics.py
│
├── main.py
├── migrate_db.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 4. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/saherliaqat227-cell/Smart-Feedback-Intelligence-System.git
```

### Step 2: Open Project Folder

```bash
cd Smart-Feedback-Intelligence-System
```

### Step 3: Create Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Configure Environment Variables

Create a `.env` file in the project root directory.

Add the following configuration:

```env
SECRET_KEY=your_secret_key
```

Use a strong secret key for your local environment. Never share your actual secret key or commit the `.env` file to GitHub.

### Step 7: Run the Application

```bash
uvicorn main:app --reload
```

The application will run at:

`http://127.0.0.1:8000`

## 5. API Documentation

FastAPI automatically generates interactive API documentation using Swagger UI and OpenAPI.

Swagger UI:

`http://127.0.0.1:8000/docs`

### Authentication APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register` | Register a new user |
| POST | `/api/auth/login` | Login and receive an access token |

### Feedback APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/feedback` | Create feedback with automatic sentiment prediction |
| GET | `/api/feedback` | Get feedback with search, filters and pagination |
| GET | `/api/feedback/{feedback_id}` | Get feedback by ID |
| PUT | `/api/feedback/{feedback_id}` | Update feedback |
| DELETE | `/api/feedback/{feedback_id}` | Delete feedback |

### Feedback API Features

- Search feedback by customer name or feedback text.
- Filter feedback by sentiment.
- Filter feedback by start date and end date.
- Pagination using `skip` and `limit`.
- Each authenticated user can access only their own feedback.
- Feedback endpoints require JWT authentication.
- Invalid requests return validation errors.
- Missing feedback records return HTTP 404.
- Database errors are handled with appropriate HTTP responses.

### Sentiment Analysis API

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/sentiment/predict` | Predict feedback sentiment using the trained ML model |

The sentiment prediction endpoint is public and does not require authentication.

### Analytics APIs

The system provides authenticated analytics endpoints to monitor customer feedback and sentiment distribution.

**1. GET `/api/analytics/summary`**

Returns:

- Total feedback count.
- Positive feedback count.
- Negative feedback count.
- Neutral feedback count.
- Sentiment distribution percentages.

**2. GET `/api/analytics/trends`**

Required query parameters:

- `start_date`
- `end_date`

Returns daily feedback counts and sentiment trends for the requested date range.

Both analytics endpoints require a valid JWT access token.

### Authentication and Access Rules

- Registration and login endpoints are public.
- Sentiment prediction endpoint is public.
- Feedback management endpoints require JWT authentication.
- Analytics endpoints require JWT authentication.
- Private endpoints validate the access token before processing requests.
- Users can access their own feedback records.

## 6. Sentiment Analysis Model

The system uses a Logistic Regression machine learning model trained on sentiment data.

### Dataset Information

- Dataset: Twitter and Reddit Sentimental Analysis Dataset
- Source: Kaggle
- Selected file: `Twitter_Data.csv`
- Original records: 162,980
- Cleaned records: 160,843
- Sentiment classes: Negative, Neutral, Positive

### Data Preprocessing

- Removed missing values.
- Removed duplicate records.
- Applied text cleaning.
- Applied TF-IDF vectorization.
- Used 30,000 maximum features.
- Used unigram and bigram features.
- Applied stratified 80/20 train-test split.

### Model Configuration

- Algorithm: Logistic Regression
- Maximum iterations: 1000
- Vectorizer: TF-IDF
- Train-test split: 80/20

### Model Evaluation

| Metric | Score |
|---|---:|
| Accuracy | 85.24% |
| Weighted Precision | 85.63% |
| Weighted Recall | 85.24% |
| Weighted F1-Score | 85.09% |

### Class-wise Performance

| Sentiment | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Negative | 0.86 | 0.72 | 0.79 |
| Neutral | 0.81 | 0.95 | 0.87 |
| Positive | 0.89 | 0.84 | 0.87 |

### Confusion Matrix

| Actual / Predicted | Negative | Neutral | Positive |
|---|---:|---:|---:|
| Negative | 5077 | 923 | 1026 |
| Neutral | 129 | 10269 | 454 |
| Positive | 680 | 1536 | 12075 |

## 7. Dataset Source and License

The project uses the Twitter and Reddit Sentimental Analysis Dataset available on Kaggle.

Dataset source:

https://www.kaggle.com/datasets/cosmos98/twitter-and-reddit-sentimental-analysis-dataset

The dataset is distributed under the CC BY-NC-SA 4.0 license.

This license requires appropriate attribution, restricts commercial use, and requires adaptations to be shared under the same license.

The dataset contains social-media text and may not fully represent real customer feedback. This limitation is considered when interpreting model predictions.

The original and cleaned CSV datasets are not included in GitHub because they are excluded through `.gitignore`.

## 8. Model Files

The trained model artifacts are saved in the `ml/` directory:

- `sentiment_model.pkl`
- `tfidf_vectorizer.pkl`

The backend loads these files to predict the sentiment of submitted feedback.

The trained model and vectorizer are loaded by the sentiment prediction service.

## 9. Feedback Prediction Workflow

When a customer submits feedback:

1. The API receives the feedback text.
2. The text is passed to the sentiment prediction service.
3. The TF-IDF vectorizer converts the text into numerical features.
4. The Logistic Regression model predicts the sentiment.
5. The confidence score is calculated.
6. The feedback, predicted sentiment, and confidence score are stored in the database.

### Example Prediction Response

```json
{
  "feedback_text": "The service was excellent and amazing.",
  "sentiment": "Positive",
  "confidence_score": 99.97
}
```

## 10. Confidence Score and Limitations

The confidence score represents the highest probability returned by the model for its predicted sentiment class, expressed as a percentage.

It does not guarantee that the prediction is correct.

The model may misclassify some feedback, especially short, ambiguous, neutral, or unusual text.

The model was trained on social-media data, so its performance may differ when analyzing actual customer feedback.

## 11. Model Training

The reproducible training script is:

`ml/train_model.py`

To train the model again:

```bash
python ml/train_model.py
```

Make sure the cleaned dataset is available at:

`ml/Twitter_Data_Cleaned.csv`

The training script saves the updated model and vectorizer artifacts.

For more details, see:

`docs/model_training.md`

## 12. Automated Testing

Pytest is used for automated testing.

The project includes automated tests for:

- User registration and authentication.
- Feedback CRUD operations.
- Sentiment prediction behavior.
- Analytics summary and trends.
- Invalid credentials and unauthorized access.
- Input validation and error handling.
- Pagination and filtering.
- Analytics date validation.

### Test Execution

Run the complete test suite using:

```bash
python -m pytest tests/ -v
```

### Test Results

The complete test suite was executed successfully.

- Total passed tests: 23
- Warnings: 4
- Failed tests: 0

The warnings are related to Pydantic deprecations and do not indicate test failures.

## 13. Project Progress

| Day | Work Completed |
|---|---|
| Day 1 | Project setup, FastAPI application, database setup, health-check route and GitHub repository |
| Day 2 | Database models, feedback CRUD APIs, validation, search, filters and pagination |
| Day 3 | User registration, login, password hashing and JWT authentication |
| Day 4 | Dataset preparation, cleaning, TF-IDF, model training and evaluation |
| Day 5 | ML model integration, sentiment prediction API and automatic feedback prediction storage |
| Day 6 | Analytics endpoints, automated testing, logging, code review and bug fixing |
| Day 7 | Pending |

## 14. Documentation

Additional project documentation is available in the `docs/` directory:

- `database_schema.md` – Database tables and relationships.
- `dataset.md` – Dataset information and exploration.
- `model_training.md` – Model training and evaluation report.
- `day5_sentiment_integration.md` – Sentiment integration and testing report.
- `day6_test_results.md` – Analytics, automated testing and code review results.

## 15. Future Improvements

- Improve neutral sentiment classification.
- Expand automated test coverage.
- Add more advanced machine learning models.
- Improve logging and error monitoring.
- Consider PostgreSQL for production database requirements.
- Develop a user-friendly dashboard for analytics visualization.

## 16. AI Assistance Disclosure

AI coding assistance was used for guidance, code explanations, debugging, and documentation support during development. The project code, implementation decisions, testing, and final submission are reviewed and understood by the developer.

## 17. Author

**Saher Liaqat**

GitHub: https://github.com/saherliaqat227-cell

---

Project: Smart Feedback Intelligence System

Version: 1.0.0