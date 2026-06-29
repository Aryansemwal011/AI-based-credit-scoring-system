import os
import pandas as pd

# Find the project root directory
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

# Path to the dataset
train_path = os.path.join(BASE_DIR, "dataset", "train.csv")

# Load the dataset
df = pd.read_csv(train_path)

print("\n===== First 5 Rows =====")
print(df.head())

print("\n===== Shape =====")
print(df.shape)

print("\n===== Columns =====")
print(df.columns)

print("\n===== Information =====")
print(df.info())