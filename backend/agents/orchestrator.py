from backend.database.crud import save_application

from backend.agents.intake_agent import IntakeAgent
from backend.agents.validation_agent import ValidationAgent
from backend.agents.distribution_agent import DistributionAgent
from backend.agents.decision_agent import DecisionAgent
from backend.agents.explainability_agent import ExplainabilityAgent
from backend.agents.fraud_agent import FraudAgent
from backend.agents.risk_agent import RiskAnalysisAgent
from backend.agents.recommendation_agent import RecommendationAgent

from backend.ml.predict import predict_loan


class AgentOrchestrator:

    def __init__(self):
        self.intake = IntakeAgent()
        self.validation = ValidationAgent()
        self.distribution = DistributionAgent()
        self.decision = DecisionAgent()
        self.explainer = ExplainabilityAgent()
        self.fraud = FraudAgent()
        self.risk = RiskAnalysisAgent()
        self.recommendation = RecommendationAgent()

    def run(self, application):

        # ----------------------------
        # Intake Agent
        # ----------------------------
        intake_result = self.intake.process(application)

        # ----------------------------
        # Validation Agent
        # ----------------------------
        validation_result = self.validation.process(application)

        # ----------------------------
        # Distribution Agent
        # ----------------------------
        distribution_result = self.distribution.process(application)

        # Default values (prevents UnboundLocalError)
        prediction = {}
        explanation = []
        fraud = {
            "fraud_score": 0,
            "manual_review": False,
            "reasons": []
        }

        risk_result = {
            "risk_level": "Unknown",
            "risk_score": 0,
            "risk_factors": []
        }

        recommendation_result = {
            "recommendations": []
        }

        # ----------------------------
        # Run ML & AI Agents only if input is valid
        # ----------------------------
        if validation_result["valid"]:

            prediction = predict_loan(application)

            explanation = self.explainer.process(
                application,
                prediction
            )

            fraud = self.fraud.process(application)

            risk_result = self.risk.process(application)

            recommendation_result = self.recommendation.process(
                application,
                prediction,
                risk_result
            )

        # ----------------------------
        # Decision Agent
        # ----------------------------
        final_result = self.decision.process(
             validation_result,
            distribution_result,
            prediction,
            fraud,
            risk_result
)

        # ----------------------------
        # Final API Response
        # ----------------------------
        response = {
            "application_id": intake_result["application_id"],
            "timestamp": intake_result["timestamp"],

            "validation": validation_result,

            "distribution_check": distribution_result,

            "result": {

                **prediction,

                **final_result,

                "manual_review": fraud["manual_review"],
                "fraud_score": fraud["fraud_score"],

                "risk_level": risk_result["risk_level"],

                "explanation": explanation,

                "fraud_analysis": fraud,

                "risk_analysis": risk_result,

                "recommendations": recommendation_result["recommendations"]
            }
        }

        # ----------------------------
        # Save to Database
        # ----------------------------
        save_application(application, response)

        return response