
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# Load dataset
file_path = Path(__file__).with_name("Twitter_Data.csv")
df = pd.read_csv(file_path)

# Dataset information
print("DATASET EXPLORATION")
print("-------------------")

print("Dataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Convert category into numeric format
df["category"] = pd.to_numeric(
    df["category"],
    errors="coerce"
)

# Sentiment distribution
print("\nSentiment Class Distribution:")
print(df["category"].value_counts().sort_index())

# Class percentages
print("\nClass Distribution Percentage:")
print(
    (df["category"].value_counts(normalize=True).sort_index() * 100)
    .round(2)
)

# Calculate sentiment counts for graph
sentiment_counts = (
    df["category"]
    .dropna()
    .value_counts()
    .reindex([-1.0, 0.0, 1.0], fill_value=0)
)

# Create sentiment distribution graph
plt.figure(figsize=(8, 5))

plt.bar(
    ["Negative", "Neutral", "Positive"],
    sentiment_counts.values
)

plt.title("Sentiment Class Distribution")
plt.xlabel("Sentiment Category")
plt.ylabel("Number of Records")

plt.tight_layout()

# Save graph
output_path = Path(__file__).with_name("sentiment_distribution.png")
plt.savefig(output_path, dpi=300)

# Display graph
plt.show()
