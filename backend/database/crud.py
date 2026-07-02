import json
from backend.database.database import get_connection


def save_application(application, response):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO loan_applications (
            application_id,
            gender,
            married,
            dependents,
            education,
            self_employed,
            applicant_income,
            coapplicant_income,
            loan_amount,
            loan_amount_term,
            credit_history,
            property_area,
            loan_status,
            approval_probability,
            risk_level,
            fraud_score,
            manual_review,
            response_json
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            response["application_id"],

            application.Gender,
            application.Married,
            application.Dependents,
            application.Education,
            application.Self_Employed,
            application.ApplicantIncome,
            application.CoapplicantIncome,
            application.LoanAmount,
            application.Loan_Amount_Term,
            application.Credit_History,
            application.Property_Area,

            response["result"].get("loan_status"),
            response["result"].get("approval_probability"),
            response["result"].get("risk_level"),
            response["result"].get("fraud_score"),
            response["result"].get("manual_review"),

            json.dumps(response)
        )
    )

    conn.commit()
    conn.close()