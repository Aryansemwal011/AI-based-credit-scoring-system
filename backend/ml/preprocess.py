#print("HELLO FROM PREPROCESS")
import os
import pandas as pd

# -------------------------------
# Load Dataset
# -------------------------------

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

train_path = os.path.join(BASE_DIR, "dataset", "train.csv")

df = pd.read_csv(train_path)

# -------------------------------
# Dataset Overview
# -------------------------------

print("="*70)
print("DATASET OVERVIEW")
print("="*70)

print("\nShape of Dataset:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
df.info()

# -------------------------------
# Missing Values
# -------------------------------

print("\n" + "="*70)
print("MISSING VALUES")
print("="*70)

print(df.isnull().sum())

# -------------------------------
# Duplicate Rows
# -------------------------------

print("\n" + "="*70)
print("DUPLICATE ROWS")
print("="*70)

print("Total Duplicate Rows:", df.duplicated().sum())

# -------------------------------
# Statistical Summary
# -------------------------------

print("\n" + "="*70)
print("STATISTICAL SUMMARY")
print("="*70)

print(df.describe())

# -------------------------------
# Target Variable
# -------------------------------

print("\n" + "="*70)
print("TARGET VARIABLE")
print("="*70)

print(df["Loan_Status"].value_counts())

print("\nTarget Percentage")

print(df["Loan_Status"].value_counts(normalize=True)*100)