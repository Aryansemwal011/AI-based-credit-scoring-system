function FraudCard({ fraudAnalysis }) {

    return (

       <div className="ai-card">

            <h2>Fraud Analysis</h2>

            <hr />

            <p>
                <strong>Fraud Score:</strong>{" "}
                {fraudAnalysis.fraud_score}
            </p>

            <p>
                <strong>Manual Review:</strong>{" "}
                {fraudAnalysis.manual_review ? "Yes" : "No"}
            </p>

            <h3>Fraud Reasons</h3>

            <ul>
                {fraudAnalysis.fraud_reasons.map((reason, index) => (
                    <li key={index}>{reason}</li>
                ))}
            </ul>

        </div>

    );

}

export default FraudCard;