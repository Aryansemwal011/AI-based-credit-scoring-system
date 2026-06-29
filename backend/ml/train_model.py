import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

# =====================================
# LOAD DATASET
# =====================================

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

train_path = os.path.join(BASE_DIR, "dataset", "train.csv")

df = pd.read_csv(train_path)

#remove Loan_ID column

df.drop("Loan_ID", axis=1, inplace=True)

#fill missing values for numerical columns with median

numerical_columns = [
    "LoanAmount",
    "Loan_Amount_Term",
    "Credit_History"
]

for column in numerical_columns:
    df[column] = df[column].fillna(df[column].median())

categorical_columns = [
    "Gender",
    "Married",
    "Dependents",
    "Self_Employed"
]

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

df["Gender"] = df["Gender"].map({"Male":1,"Female":0})

df["Married"] = df["Married"].map({"Yes":1,"No":0})

df["Education"] = df["Education"].map({"Graduate":1,"Not Graduate":0})

df["Self_Employed"] = df["Self_Employed"].map({"Yes":1,"No":0})

df["Loan_Status"] = df["Loan_Status"].map({"Y":1,"N":0})

df["Property_Area"] = df["Property_Area"].map({
    "Rural":0,
    "Semiurban":1,
    "Urban":2
})

df["Dependents"] = df["Dependents"].map({
    "0":0,
    "1":1,
    "2":2,
    "3+":3
})

#split the dataset into features and target variable

X = df.drop("Loan_Status", axis=1)

y = df["Loan_Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

#log reg_model = LogisticRegression()

log_model = LogisticRegression(max_iter=1000)

log_model.fit(X_train, y_train)

log_pred = log_model.predict(X_test)

log_acc = accuracy_score(y_test, log_pred)

#design tree model

tree = DecisionTreeClassifier(random_state=42)

tree.fit(X_train, y_train)

tree_pred = tree.predict(X_test)

tree_acc = accuracy_score(y_test, tree_pred)

#random forest model

forest = RandomForestClassifier(random_state=42)

forest.fit(X_train, y_train)

forest_pred = forest.predict(X_test)

forest_acc = accuracy_score(y_test, forest_pred)

#compare the accuracy of the models

print("\n==============================")

print("MODEL ACCURACY")

print("==============================")

print(f"Logistic Regression : {log_acc:.4f}")

print(f"Decision Tree       : {tree_acc:.4f}")

print(f"Random Forest       : {forest_acc:.4f}")

#select the best model based on accuracy

models = {
    "Logistic Regression": (log_model, log_acc),
    "Decision Tree": (tree, tree_acc),
    "Random Forest": (forest, forest_acc)
}

best_model_name = max(models, key=lambda x: models[x][1])

best_model = models[best_model_name][0]

best_accuracy = models[best_model_name][1]

#save the best model

model_path = os.path.join(BASE_DIR, "model", "model.pkl")

scaler_path = os.path.join(BASE_DIR, "model", "scaler.pkl")

joblib.dump(best_model, model_path)

joblib.dump(scaler, scaler_path)

print("\n==============================")

print("BEST MODEL")

print("==============================")

print(best_model_name)

print(f"Accuracy : {best_accuracy:.4f}")

print("\nModel Saved Successfully!")

print("Scaler Saved Successfully!")
