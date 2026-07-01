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

    print("\n========== INPUT RECEIVED ==========")
    print(values)

    values = scaler.transform(values)

    print("\n========== AFTER SCALING ==========")
    print(values)

    prediction = model.predict(values)[0]
    probability = model.predict_proba(values)[0]

    print("\n========== MODEL OUTPUT ==========")
    print("Prediction:", prediction)
    print("Probability:", probability)

    approval_probability = round(float(probability[1]) * 100, 2)

    confidence = round(max(probability) * 100, 2)

    loan_status = "Approved" if prediction == 1 else "Rejected"

    # Risk Level
    if approval_probability >= 80:
        risk_level = "Low"
    elif approval_probability >= 50:
        risk_level = "Medium"
    else:
        risk_level = "High"

    # Recommended Interest Rate
    if risk_level == "Low":
        interest_rate = 8.5
    elif risk_level == "Medium":
        interest_rate = 10.5
    else:
        interest_rate = 13.5

    # Recommended Loan Limit
    income = data.ApplicantIncome + data.CoapplicantIncome

    if loan_status == "Approved":
        recommended_loan_limit = round(income * 20, 2)
    else:
        recommended_loan_limit = 0

    # Dummy Fraud Score (we'll replace this with the Fraud Agent later)
    fraud_score = round((1 - probability[1]) * 20, 2)

    # Human-in-the-loop decision
    manual_review = bool(confidence < 70)

    # AI Decision Summary
    if loan_status == "Approved":
        decision = (
            "Loan approved based on good credit history, income stability, "
            "and overall low financial risk."
        )
    else:
        decision = (
            "Loan rejected due to higher estimated credit risk. "
            "Manual review may be required."
        )

    return {
    "loan_status": str(loan_status),
    "approval_probability": float(approval_probability),
    "risk_level": str(risk_level),
    "confidence": float(confidence),
    "recommended_interest_rate": float(interest_rate),
    "recommended_loan_limit": float(recommended_loan_limit),
    "fraud_score": float(fraud_score),
    "manual_review": bool(manual_review),
    "decision": str(decision)
}