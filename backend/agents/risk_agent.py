class RiskAnalysisAgent:

    def process(self, application):

        score = 0
        reasons = []

        # Credit history
        if application.Credit_History == 0:
            score += 40
            reasons.append("Poor credit history.")

        # Income
        if application.ApplicantIncome < 3000:
            score += 20
            reasons.append("Low applicant income.")

        # Loan amount
        if application.LoanAmount > 300:
            score += 20
            reasons.append("High requested loan amount.")

        # Self employed
        if application.Self_Employed == 1:
            score += 10
            reasons.append("Self-employed applicant.")

        # Dependents
        if application.Dependents >= 3:
            score += 10
            reasons.append("Large number of dependents.")

        # Risk level
        if score >= 60:
            level = "High"
        elif score >= 30:
            level = "Medium"
        else:
            level = "Low"

        return {
            "risk_score": score,
            "risk_level": level,
            "risk_reasons": reasons
        }