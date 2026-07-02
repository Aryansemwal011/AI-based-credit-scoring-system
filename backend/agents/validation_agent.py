class ValidationAgent:

    def process(self, application):

        errors = []

        if application.ApplicantIncome <= 0:
            errors.append("Applicant income must be greater than 0")

        if application.LoanAmount <= 0:
            errors.append("Loan amount must be greater than 0")

        return {
            "valid": len(errors) == 0,
            "errors": errors
        }