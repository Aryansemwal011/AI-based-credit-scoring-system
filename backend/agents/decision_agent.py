class DecisionAgent:

    def process(
        self,
        validation_result,
        distribution_result,
        prediction,
        fraud_result,
        risk_result
    ):

        # Validation failed
        if not validation_result["valid"]:
            return {
                "decision": "Rejected",
                "reason": "Invalid application data."
            }

        # Out of training distribution
        if not distribution_result["in_distribution"]:
            return {
                "decision": "Manual Review",
                "reason": "Application is outside the training distribution."
            }

        # Fraud detected
        if fraud_result["manual_review"]:
            return {
                "decision": "Manual Review",
                "reason": "High fraud risk detected."
            }

        # High financial risk
        if risk_result["risk_level"] == "High":
            return {
                "decision": "Manual Review",
                "reason": "High financial risk."
            }

        # ML prediction
        if prediction["loan_status"] == "Approved":
            return {
                "decision": "Approved",
                "reason": "Application satisfies approval criteria."
            }

        return {
            "decision": "Rejected",
            "reason": "Loan eligibility criteria not satisfied."
        }