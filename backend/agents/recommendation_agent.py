class RecommendationAgent:

    def process(self, application, prediction, risk):

        recommendations = []

        # Credit history
        if application.Credit_History == 0:
            recommendations.append(
                "Improve your credit history before applying again."
            )

        # Income
        if application.ApplicantIncome < 3000:
            recommendations.append(
                "Increase your monthly income or add a co-applicant."
            )

        # Loan amount
        if application.LoanAmount > 300:
            recommendations.append(
                "Consider requesting a lower loan amount."
            )

        # Self-employed
        if application.Self_Employed == 1:
            recommendations.append(
                "Provide additional proof of stable business income."
            )

        # Dependents
        if application.Dependents >= 3:
            recommendations.append(
                "A higher number of dependents may affect repayment capacity."
            )

        # General advice
        if prediction["loan_status"] == "Approved":
            recommendations.append(
                "Maintain your current financial profile for future borrowing."
            )
        else:
            recommendations.append(
                "Improve your financial profile and apply again after a few months."
            )

        return {
            "recommendations": recommendations
        }