
import pandas as pd
from pathlib import Path

# Load original dataset
file_path = Path(__file__).with_name("Twitter_Data.csv")
df = pd.read_csv(file_path)

print("DATA CLEANING")
print("-------------")

print("Original Dataset Shape:", df.shape)

# Convert category into numeric format
df["category"] = pd.to_numeric(
    df["category"],
    errors="coerce"
)

# Remove extra spaces from text
df["clean_text"] = df["clean_text"].astype("string").str.strip()

# Convert empty text into missing values
df["clean_text"] = df["clean_text"].replace("", pd.NA)

# Remove missing values
df = df.dropna(subset=["clean_text", "category"])

print("\nDataset Shape After Removing Missing Values:", df.shape)

# Remove duplicate rows
df = df.drop_duplicates()

print("Dataset Shape After Removing Duplicates:", df.shape)

# Save cleaned dataset
output_path = Path(__file__).with_name("Twitter_Data_Cleaned.csv")
df.to_csv(output_path, index=False)

print("\nCleaned Dataset Saved Successfully!")
print("Final Dataset Shape:", df.shape)

print("\nFinal Sentiment Distribution:")
print(df["category"].value_counts().sort_index())
