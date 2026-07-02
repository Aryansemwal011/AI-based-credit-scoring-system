function RiskCard({ riskAnalysis }) {

    return (

        <div className="ai-card">

            <h2>Risk Analysis</h2>

            <hr />

            <p>
                <strong>Risk Score:</strong>{" "}
                {riskAnalysis.risk_score}
            </p>
            

           <span
            style={{

            color:

            riskAnalysis.risk_level==="Low"

            ? "green"

            : riskAnalysis.risk_level==="Medium"

            ? "orange"

            : "red",

            fontWeight:"bold"

            }}

            >

            {riskAnalysis.risk_level}

            </span>

            <h3>Risk Reasons</h3>

            <ul>
                {riskAnalysis.risk_reasons.map((reason, index) => (
                    <li key={index}>{reason}</li>
                ))}
            </ul>

        </div>

    );

}

export default RiskCard;