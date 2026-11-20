
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

# Load cleaned dataset
file_path = Path(__file__).with_name("Twitter_Data_Cleaned.csv")
df = pd.read_csv(file_path)

print("TRAIN TEST DATA SPLITTING")
print("-------------------------")

# Separate features and target
X = df["clean_text"]
y = df["category"]

# Split dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Display dataset sizes
print("\nTotal Records:", len(df))
print("Training Records:", len(X_train))
print("Testing Records:", len(X_test))

# Display class distribution
print("\nTraining Class Distribution:")
print(y_train.value_counts().sort_index())

print("\nTesting Class Distribution:")
print(y_test.value_counts().sort_index())

print("\nTraining and Testing Split Completed Successfully!")
