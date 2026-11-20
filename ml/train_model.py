
import pandas as pd
from pathlib import Path
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# Load cleaned dataset
file_path = Path(__file__).with_name("Twitter_Data_Cleaned.csv")
df = pd.read_csv(file_path)

print("SMART FEEDBACK INTELLIGENCE SYSTEM")
print("----------------------------------")

# Separate input text and target labels
X = df["clean_text"].astype(str)
y = df["category"].astype(int)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))

# TF-IDF preprocessing
# Fit only on training data to avoid data leakage
vectorizer = TfidfVectorizer(
    max_features=30000,
    ngram_range=(1, 2),
    stop_words="english"
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print("\nTF-IDF Preprocessing Completed!")

# Train Logistic Regression model
model = LogisticRegression(max_iter=1000)

print("\nTraining Model...")
model.fit(X_train_tfidf, y_train)

print("Model Training Completed!")

# Make predictions
y_pred = model.predict(X_test_tfidf)

# Model evaluation
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="weighted")
recall = recall_score(y_test, y_pred, average="weighted")
f1 = f1_score(y_test, y_pred, average="weighted")

print("\nMODEL EVALUATION")
print("----------------")

print("Accuracy:", round(accuracy, 4))
print("Precision:", round(precision, 4))
print("Recall:", round(recall, 4))
print("F1-Score:", round(f1, 4))

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Negative", "Neutral", "Positive"]
    )
)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save trained model and TF-IDF vectorizer
output_dir = Path(__file__).parent

joblib.dump(model, output_dir / "sentiment_model.pkl")
joblib.dump(vectorizer, output_dir / "tfidf_vectorizer.pkl")

print("\nModel and TF-IDF Vectorizer Saved Successfully!")
