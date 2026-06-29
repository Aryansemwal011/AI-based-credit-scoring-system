import os
import pandas as pd

# ==========================================
# Load Dataset
# ==========================================

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

train_path = os.path.join(BASE_DIR, "dataset", "train.csv")

df = pd.read_csv(train_path)

# ==========================================
# ORIGINAL DATASET
# ==========================================

print("=" * 60)
print("ORIGINAL DATASET")
print("=" * 60)

print(df.head())

# ==========================================
# REMOVE Loan_ID
# ==========================================

df.drop("Loan_ID", axis=1, inplace=True)

print("\nLoan_ID column removed successfully!")

# ==========================================
# MISSING VALUES BEFORE CLEANING
# ==========================================

print("\n" + "=" * 60)
print("MISSING VALUES BEFORE CLEANING")
print("=" * 60)

print(df.isnull().sum())

# ==========================================
# HANDLE NUMERICAL MISSING VALUES
# ==========================================

numerical_columns = [
    "LoanAmount",
    "Loan_Amount_Term",
    "Credit_History"
]

for column in numerical_columns:
    median = df[column].median()
    df[column] = df[column].fillna(median)

# ==========================================
# HANDLE CATEGORICAL MISSING VALUES
# ==========================================

categorical_columns = [
    "Gender",
    "Married",
    "Dependents",
    "Self_Employed"
]

for column in categorical_columns:
    mode = df[column].mode()[0]
    df[column] = df[column].fillna(mode)

# ==========================================
# MISSING VALUES AFTER CLEANING
# ==========================================

print("\n" + "=" * 60)
print("MISSING VALUES AFTER CLEANING")
print("=" * 60)

print(df.isnull().sum())

# ==========================================
# DATASET AFTER CLEANING
# ==========================================

print("\n" + "=" * 60)
print("FIRST 5 ROWS AFTER CLEANING")
print("=" * 60)

print(df.head())