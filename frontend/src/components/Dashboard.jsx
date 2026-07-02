import PredictionCard from "./PredictionCard";
import RiskCard from "./RiskCard";
import FraudCard from "./FraudCard";
import ExplanationCard from "./ExplanationCard";
import RecommendationCard from "./RecommendationCard";

function Dashboard({ result }) {

    return (

        <div className="dashboard">

            <PredictionCard result={result} />

            <div className="dashboard-grid">

                <RiskCard
                    riskAnalysis={result.result.risk_analysis}
                />

                <FraudCard
                    fraudAnalysis={result.result.fraud_analysis}
                />

            </div>

            <ExplanationCard
                explanation={result.result.explanation}
            />

            <RecommendationCard
                recommendations={result.result.recommendations}
            />

        </div>

    );

}

export default Dashboard;