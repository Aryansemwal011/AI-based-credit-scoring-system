class FraudAgent:

    def process(self, application):

        fraud_score = 0
        reasons = []

        # Income vs Loan Amount
        if application.ApplicantIncome > 0:

            ratio = application.LoanAmount / application.ApplicantIncome

            if ratio > 0.20:
                fraud_score += 40
                reasons.append(
                    "Loan amount is unusually high compared to applicant income."
                )

        # Credit History
        if application.Credit_History == 0:
            fraud_score += 30
            reasons.append(
                "Poor credit history increases fraud risk."
            )

        # Self Employment
        if application.Self_Employed == 1:
            fraud_score += 10
            reasons.append(
                "Self-employed applicants require additional verification."
            )

        # Extremely High Loan Amount
        if application.LoanAmount > 500:
            fraud_score += 20
            reasons.append(
                "Requested loan amount is unusually high."
            )

        fraud_score = min(fraud_score, 100)

        return {
            "fraud_score": fraud_score,
            "manual_review": fraud_score >= 50,
            "fraud_reasons": reasons
        }