class DistributionAgent:

    def process(self, application):

        warnings = []

        if application.ApplicantIncome > 50000:
            warnings.append("Applicant income is outside training distribution.")

        if application.LoanAmount > 700:
            warnings.append("Loan amount is outside training distribution.")

        return {
            "in_distribution": len(warnings) == 0,
            "warnings": warnings
        }