# Smart Feedback Intelligence System

A machine learning-based customer feedback management system built with **Python, FastAPI, SQLAlchemy, SQLite, and Scikit-learn**. The system allows authenticated users to manage customer feedback and automatically analyze its sentiment as Positive, Negative, or Neutral.

## 1. Project Overview

The Smart Feedback Intelligence System is a backend application that combines REST APIs with machine learning to analyze customer feedback.

It uses a trained Logistic Regression model with TF-IDF text vectorization to predict the sentiment of customer feedback.

### Main Features

- User registration and login
- Password hashing
- JWT-based authentication
- Customer feedback management (CRUD)
- Automatic sentiment prediction
- Confidence score calculation
- Search and sentiment filtering
- Date-based filtering
- Pagination
- SQLite database integration
- Machine learning model integration

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
| Joblib | Saving and loading ML models |
| Pytest | Automated testing |

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
│   │   └── sentiment.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   └── sentiment_service.py
│   │
│   └── database.py
│
├── docs/
│   ├── dataset.md
│   ├── model_training.md
│   └── day5_sentiment_integration.md
│
├── ml/
│   ├── inspect_dataset.py
│   ├── clean_dataset.py
│   ├── prepare_data.py
│   ├── train_model.py
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebooks/
├── tests/
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── smart_feedback.db
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

FastAPI automatically generates interactive API documentation.

**Swagger UI:**

`http://127.0.0.1:8000/docs`

### Authentication APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register` | Register a new user |
| POST | `/api/auth/login` | Login and receive an access token |

### Feedback APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/feedback/` | Create feedback |
| GET | `/feedback/` | Get all feedback |
| GET | `/feedback/{feedback_id}` | Get feedback by ID |
| PUT | `/feedback/{feedback_id}` | Update feedback |
| DELETE | `/feedback/{feedback_id}` | Delete feedback |

Feedback routes require authentication.

### Sentiment Analysis API

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/sentiment/predict` | Predict feedback sentiment |

## 6. Sentiment Analysis Model

The system uses a Logistic Regression machine learning model trained on customer sentiment data.

### Dataset

- Dataset: Twitter and Reddit Sentimental Analysis Dataset
- Selected file: `Twitter_Data.csv`
- Cleaned records: 160,843
- Sentiment classes: Negative, Neutral, Positive

### Data Preprocessing

- Removed missing values.
- Removed duplicate records.
- Applied TF-IDF vectorization.
- Used 30,000 maximum features.
- Used unigram and bigram features.
- Applied stratified 80/20 train-test split.

### Model Configuration

- Algorithm: Logistic Regression
- Maximum iterations: 1000
- Vectorizer: TF-IDF

### Model Evaluation

| Metric | Score |
|---|---:|
| Accuracy | 85.24% |
| Precision | 85.63% |
| Recall | 85.24% |
| F1-Score | 85.09% |

### Class-wise Performance

| Sentiment | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Negative | 0.86 | 0.72 | 0.79 |
| Neutral | 0.81 | 0.95 | 0.87 |
| Positive | 0.89 | 0.84 | 0.87 |

## 7. Model Files

The trained model artifacts are saved in the `ml/` directory:

- `sentiment_model.pkl`
- `tfidf_vectorizer.pkl`

The backend loads these files to predict the sentiment of submitted feedback.

The original and cleaned CSV datasets are not included in GitHub because they are excluded through `.gitignore`.

## 8. Feedback Prediction Workflow

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

## 9. Confidence Score and Limitations

The confidence score represents the highest probability returned by the model for its predicted sentiment class, expressed as a percentage.

It does not guarantee that the prediction is correct.

The model may misclassify some feedback, especially short, ambiguous, neutral, or unusual text.

## 10. Model Training

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

## 11. Project Progress

| Day | Completed Work |
|---|---|
| Day 1 | Project setup, FastAPI application, database setup and GitHub repository |
| Day 2 | Database models, feedback CRUD APIs, validation, search and pagination |
| Day 3 | User registration, login, password hashing and JWT authentication |
| Day 4 | Dataset preparation, cleaning, TF-IDF, model training and evaluation |
| Day 5 | ML model integration, sentiment prediction API and automatic feedback prediction storage |

## 12. Documentation

Additional project documentation is available in the `docs/` directory:

- `dataset.md` – Dataset information and exploration
- `model_training.md` – Model training and evaluation report
- `day5_sentiment_integration.md` – Sentiment integration and testing report

## 13. Future Improvements

- Implement analytics and sentiment distribution dashboards.
- Add daily sentiment trend analysis.
- Improve neutral sentiment classification.
- Expand automated test coverage.
- Add more advanced machine learning models.
- Improve logging and error monitoring.

## 14. Author

**Saher Liaqat**

BS Information Technology Student

GitHub: [saherliaqat227-cell](https://github.com/saherliaqat227-cell)

---

**Project:** Smart Feedback Intelligence System

**Version:** 1.0.0