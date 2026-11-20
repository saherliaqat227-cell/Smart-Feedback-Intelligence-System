# Dataset Documentation

## 1. Dataset Name
Twitter and Reddit Sentimental Analysis Dataset

## 2. Dataset Source
- Platform: Kaggle
- Dataset Link: https://www.kaggle.com/datasets/cosmos98/twitter-and-reddit-sentimental-analysis-dataset
- Selected File: Twitter_Data.csv

## 3. Dataset Description
This dataset contains Twitter text data with sentiment labels. It is used for sentiment analysis and machine learning classification.

The dataset contains two columns:
- `clean_text`: Contains the text of tweets.
- `category`: Contains the sentiment label.

## 4. Dataset Size
- Total Records: 162,980
- Total Columns: 2

## 5. Sentiment Classes

| Label | Sentiment | Records |
|---|---|---:|
| -1 | Negative | 35,510 |
| 0 | Neutral | 55,213 |
| 1 | Positive | 72,250 |

## 6. Data Quality Observations
Initial dataset inspection identified:
- 4 missing values in the `clean_text` column.
- 7 missing values in the `category` column.
- 1 duplicate row.

These issues will be handled during data preprocessing.

## 7. Project Usage
This dataset will be used to train a machine learning classification model for the Smart Feedback Intelligence System.

The model will classify text into three sentiment categories:
- Positive
- Negative
- Neutral

## 8. License
The Kaggle dataset is listed under the CC BY-NC-SA 4.0 license. Its terms must be followed when using or sharing the dataset.