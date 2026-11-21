
# Model Training and Evaluation Report

## 1. Dataset
- Dataset: Twitter and Reddit Sentimental Analysis Dataset
- Selected File: Twitter_Data.csv
- Cleaned Records: 160,843
- Sentiment Classes: Negative, Neutral, Positive

## 2. Data Preparation
- Missing values were removed.
- Duplicate rows were removed.
- Dataset was divided into 80% training and 20% testing data.
- Stratified splitting was used to maintain class distribution.

## 3. Text Preprocessing
- Technique: TF-IDF Vectorization
- Maximum Features: 30,000
- N-gram Range: (1, 2)
- Stop Words: English
- TF-IDF was fitted only on training data to prevent data leakage.

## 4. Machine Learning Model
- Algorithm: Logistic Regression
- Maximum Iterations: 1000

## 5. Model Evaluation

| Metric | Score |
|---|---:|
| Accuracy | 85.24% |
| Precision | 85.63% |
| Recall | 85.24% |
| F1-Score | 85.09% |

## 6. Class-wise Performance

| Sentiment | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Negative | 0.86 | 0.72 | 0.79 |
| Neutral | 0.81 | 0.95 | 0.87 |
| Positive | 0.89 | 0.84 | 0.87 |


## 7. Confusion Matrix

The confusion matrix shows the actual and predicted sentiment classes.

| Actual / Predicted | Negative | Neutral | Positive |
|---|---:|---:|---:|
| Negative | 5077 | 923 | 1026 |
| Neutral | 129 | 10269 | 454 |
| Positive | 680 | 1536 | 12075 |

Rows represent actual sentiment classes, while columns represent predicted sentiment classes.

The diagonal values represent correctly classified records. The model correctly classified 5,077 Negative, 10,269 Neutral, and 12,075 Positive records.

## 8. Preprocessing Library Justification

Scikit-learn's TfidfVectorizer was used for text preprocessing and feature extraction instead of NLTK.

It converts text into numerical TF-IDF features and supports English stop-word removal and unigram/bigram extraction. This provides the preprocessing functionality required for this classification project.

## 9. Saved Model Artifacts

- sentiment_model.pkl
- tfidf_vectorizer.pkl

## 10. Saved Model Artifacts
- sentiment_model.pkl
- tfidf_vectorizer.pkl

## 11. Training Script
The reproducible training script is:
ml/train_model.py

## 12. How to Retrain the Model

1. Install project dependencies:
   pip install -r requirements.txt

2. Make sure Twitter_Data_Cleaned.csv is available inside the ml folder.

3. Run the training script:
   python ml/train_model.py

4. The script will train the Logistic Regression model and save:
   - sentiment_model.pkl
   - tfidf_vectorizer.pkl

## 13. Conclusion
The Logistic Regression model achieved 85.24% accuracy on the test dataset. The trained model and TF-IDF vectorizer were successfully saved for future use.
