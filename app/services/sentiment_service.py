
from pathlib import Path
import joblib


# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Saved ML model and TF-IDF vectorizer paths
MODEL_PATH = BASE_DIR / "ml" / "sentiment_model.pkl"
VECTORIZER_PATH = BASE_DIR / "ml" / "tfidf_vectorizer.pkl"


# Load trained model and vectorizer
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


def predict_sentiment(feedback_text: str):
    if not feedback_text or not feedback_text.strip():
        raise ValueError("Feedback text cannot be empty.")

    # Convert text into TF-IDF features
    text_vector = vectorizer.transform([feedback_text.strip()])

    # Predict sentiment
    prediction = model.predict(text_vector)[0]

    # Get prediction probabilities
    probabilities = model.predict_proba(text_vector)[0]

    # Convert numeric labels into readable labels
    sentiment_labels = {
        -1: "Negative",
        0: "Neutral",
        1: "Positive"
    }

    sentiment = sentiment_labels[int(prediction)]

    # Highest probability as confidence percentage
    confidence_score = float(max(probabilities) * 100)

    return {
        "sentiment": sentiment,
        "confidence_score": round(confidence_score, 2)
    }
