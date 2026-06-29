import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

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


# ==========================================
# ENCODING CATEGORICAL FEATURES
# ==========================================

print("\n" + "=" * 60)
print("ENCODING CATEGORICAL FEATURES")
print("=" * 60)

# Manual Encoding

df["Gender"] = df["Gender"].map({
    "Male": 1,
    "Female": 0
})

df["Married"] = df["Married"].map({
    "Yes": 1,
    "No": 0
})

df["Education"] = df["Education"].map({
    "Graduate": 1,
    "Not Graduate": 0
})

df["Self_Employed"] = df["Self_Employed"].map({
    "Yes": 1,
    "No": 0
})

df["Loan_Status"] = df["Loan_Status"].map({
    "Y": 1,
    "N": 0
})

df["Property_Area"] = df["Property_Area"].map({
    "Rural": 0,
    "Semiurban": 1,
    "Urban": 2
})

df["Dependents"] = df["Dependents"].map({
    "0": 0,
    "1": 1,
    "2": 2,
    "3+": 3
})

print("\nEncoding Completed Successfully!")

print("\nFirst 5 Rows After Encoding\n")

print(df.head())

# ==========================================
# FEATURES AND TARGET
# ==========================================

print("\n" + "=" * 60)
print("FEATURES & TARGET")
print("=" * 60)

X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"]

print("Feature Shape :", X.shape)
print("Target Shape  :", y.shape)

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTrain Shape :", X_train.shape)
print("Test Shape  :", X_test.shape)

# ==========================================
# FEATURE SCALING
# ==========================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

print("\nScaling Completed Successfully!")

# Save scaler
joblib.dump(scaler, "model/scaler.pkl")

print("\nScaler Saved Successfully!")