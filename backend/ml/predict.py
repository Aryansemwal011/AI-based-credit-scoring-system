import os
import joblib
import numpy as np

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

model = joblib.load(
    os.path.join(BASE_DIR, "model", "model.pkl")
)

scaler = joblib.load(
    os.path.join(BASE_DIR, "model", "scaler.pkl")
)


def predict_loan(data):

    values = np.array([[
        data.Gender,
        data.Married,
        data.Dependents,
        data.Education,
        data.Self_Employed,
        data.ApplicantIncome,
        data.CoapplicantIncome,
        data.LoanAmount,
        data.Loan_Amount_Term,
        data.Credit_History,
        data.Property_Area
    ]])

    values = scaler.transform(values)

    prediction = model.predict(values)[0]

    probability = model.predict_proba(values)[0]

    return {
        "prediction": int(prediction),
        "approval_probability": round(float(probability[1]), 4)
    }