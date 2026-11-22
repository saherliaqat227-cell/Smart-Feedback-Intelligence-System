
# Machine Learning Evaluation Summary

## 1. Model Overview

The Smart Feedback Intelligence System uses a Logistic Regression classifier to predict customer feedback sentiment.

The model classifies feedback into three categories:

- Positive
- Negative
- Neutral

TF-IDF is used to convert text into numerical features before classification.

## 2. Dataset Information

- Dataset: Twitter and Reddit Sentimental Analysis Dataset
- Source: Kaggle
- Original records: 162,980
- Cleaned records: 160,843
- Train-test split: 80/20
- Maximum TF-IDF features: 30,000
- N-gram range: Unigrams and Bigrams

## 3. Model Evaluation Results

The model was evaluated using the following metrics:

| Metric | Score |
|---|---:|
| Accuracy | 85.24% |
| Weighted Precision | 85.63% |
| Weighted Recall | 85.24% |
| Weighted F1-Score | 85.09% |

## 4. Class-wise Performance

| Sentiment | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Negative | 0.86 | 0.72 | 0.79 |
| Neutral | 0.81 | 0.95 | 0.87 |
| Positive | 0.89 | 0.84 | 0.87 |

## 5. Confusion Matrix

| Actual / Predicted | Negative | Neutral | Positive |
|---|---:|---:|---:|
| Negative | 5077 | 923 | 1026 |
| Neutral | 129 | 10269 | 454 |
| Positive | 680 | 1536 | 12075 |

## 6. Evaluation Interpretation

- The model achieved 85.24% accuracy on the test dataset.
- Positive sentiment achieved an F1-score of 0.87.
- Neutral sentiment achieved an F1-score of 0.87.
- Negative sentiment achieved an F1-score of 0.79.
- The model performs better at identifying neutral feedback than negative feedback in terms of recall.

## 7. Model Limitations

- The model was trained on social-media text.
- Real customer feedback may use different language and expressions.
- Short and ambiguous feedback can be difficult to classify.
- A high confidence score does not guarantee a correct prediction.

## 8. Conclusion

The Logistic Regression model provides automated three-class sentiment classification using TF-IDF features.

The evaluation results provide a measurable overview of model performance and help identify areas for future improvement.
