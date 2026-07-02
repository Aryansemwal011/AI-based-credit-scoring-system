class ExplainabilityAgent:

    def process(self, application, prediction):

        explanations = []

        # Credit History
        if application.Credit_History == 1:
            explanations.append(
                "Good credit history increased approval chances."
            )
        else:
            explanations.append(
                "Poor credit history reduced approval chances."
            )

        # Income
        if application.ApplicantIncome >= 5000:
            explanations.append(
                "Applicant income is sufficient."
            )
        else:
            explanations.append(
                "Applicant income is relatively low."
            )

        # Loan Amount
        if application.LoanAmount <= 200:
            explanations.append(
                "Requested loan amount is within acceptable range."
            )
        else:
            explanations.append(
                "Requested loan amount is relatively high."
            )

        # Property Area
        if application.Property_Area == 2:
            explanations.append(
                "Urban property area generally has favorable approval trends."
            )

        return {
            "explanation": explanations
        }