function PredictionCard({ result }) {

    const prediction = result.result;

    return (

       <div className="ai-card">

            <h2>Loan Prediction Result</h2>

            <hr />

            <p>
                <strong>Application ID:</strong>{" "}
                {result.application_id}
            </p>

           <p>

            <strong>Loan Status:</strong>

            <span
            style={{
            color:
            prediction.loan_status==="Approved"
            ? "green"
            : "red",

            fontWeight:"bold"

            }}
            >

            {prediction.loan_status}

            </span>

            </p>

            <p>
                <strong>Approval Probability:</strong>{" "}
                {prediction.approval_probability}%
            </p>

            <p>
                <strong>Confidence:</strong>{" "}
                {prediction.confidence}%
            </p>

            <p>
                <strong>Decision:</strong>{" "}
                {prediction.decision}
            </p>

            <p>
                <strong>Reason:</strong>{" "}
                {prediction.reason}
            </p>

            <p>
                <strong>Risk Level:</strong>{" "}
                {prediction.risk_level}
            </p>

            <p>
                <strong>Fraud Score:</strong>{" "}
                {prediction.fraud_score}
            </p>

            <p>
                <strong>Manual Review:</strong>{" "}
                {prediction.manual_review ? "Yes" : "No"}
            </p>

            <p>
                <strong>Recommended Interest Rate:</strong>{" "}
                {prediction.recommended_interest_rate}%
            </p>

            <p>
                <strong>Recommended Loan Limit:</strong>{" "}
                ₹{prediction.recommended_loan_limit}
            </p>

        </div>

    );

}

export default PredictionCard;