import { useState } from "react";
import API from "../services/api";

function LoanForm() {

   const [formData, setFormData] = useState({
    Gender: "",
    Married: "",
    Dependents: "",
    Education: "",
    Self_Employed: "",
    ApplicantIncome: "",
    CoapplicantIncome: "",
    LoanAmount: "",
    Loan_Amount_Term: "",
    Credit_History: "",
    Property_Area: ""
});

    const [result, setResult] = useState(null);

    const handleChange = (e) => {

    const { name, value } = e.target;

    setFormData({
        ...formData,
        [name]: value === "" ? "" : Number(value)
    });

};

    const handleSubmit = async (e) => {

        e.preventDefault();

        try {

            const response = await API.post("/predict", formData);

            setResult(response.data);

        } catch (error) {

    console.error(error);

    if (error.response) {
        console.log(error.response.data);
        alert(JSON.stringify(error.response.data));
    } else {
        alert("Cannot connect to backend");
    }

}
    };

    return (

        <div className="container">

            <h1>AI Credit Scoring System</h1>

            <form onSubmit={handleSubmit}>

                <label>Gender</label>

                <select
                    name="Gender"
                    value={formData.Gender}
                    onChange={handleChange}
                >   <option value="">Select</option>
                    <option value={1}>Male</option>
                    <option value={0}>Female</option>
                </select>

                <label>Married</label>

                <select
                    name="Married"
                    value={formData.Married}
                    onChange={handleChange}
                >   <option value="">Select</option>

                    <option value={1}>Yes</option>
                    <option value={0}>No</option>
                </select>

                <label>Dependents</label>

                <input
                    type="number"
                    name="Dependents"
                    value={formData.Dependents}
                    onChange={handleChange}
                    placeholder="Enter dependents" 
                    required
                />

                <label>Education</label>

                <select
                    name="Education"
                    value={formData.Education}
                    onChange={handleChange}
                >   <option value="">Select</option>

                    <option value={0}>Graduate</option>
                    <option value={1}>Not Graduate</option>
                </select>

                <label>Self Employed</label>

                <select
                    name="Self_Employed"
                    value={formData.Self_Employed}
                    onChange={handleChange}
                >   <option value="">Select</option>
                    <option value={0}>No</option>
                    <option value={1}>Yes</option>
                </select>

                <label>Applicant Income</label>

                <input
                    type="number"
                    name="ApplicantIncome"
                    value={formData.ApplicantIncome}
                    onChange={handleChange}
                    placeholder="Enter applicant income"
                    required
                />

                <label>Coapplicant Income</label>

                <input
                    type="number"
                    name="CoapplicantIncome"
                    value={formData.CoapplicantIncome}
                    onChange={handleChange}
                    placeholder="Enter coapplicant income"
                    required
                />

                <label>Loan Amount</label>

                <input
                    type="number"
                    name="LoanAmount"
                    value={formData.LoanAmount}
                    onChange={handleChange}
                    placeholder="Enter loan amount"
                    required
                />

                <label>Loan Term</label>

                <input
                    type="number"
                    name="Loan_Amount_Term"
                    value={formData.Loan_Amount_Term}
                    onChange={handleChange}
                    placeholder="Enter number of months"
                    required
                />

                <label>Credit History</label>

                <select
                    name="Credit_History"
                    value={formData.Credit_History}
                    onChange={handleChange}
                >   <option value="">Select</option>

                    <option value={1}>Good</option>
                    <option value={0}>Bad</option>
                </select>

                <label>Property Area</label>

                <select
                    name="Property_Area"
                    value={formData.Property_Area}
                    onChange={handleChange}
                >   <option value="">Select</option>

                    <option value={0}>Rural</option>
                    <option value={1}>Semiurban</option>
                    <option value={2}>Urban</option>
                </select>

                <button type="submit">
                    Predict
                </button>

            </form>

            {result && (
    <div
        style={{
            marginTop: "30px",
            padding: "20px",
            border: "1px solid #ccc",
            borderRadius: "10px"
        }}
    >
        <h2>Prediction Result</h2>

        <p>
            <strong>Loan Status:</strong> {result.loan_status}
        </p>

        <p>
            <strong>Approval Probability:</strong>{" "}
            {result.approval_probability}%
        </p>

        <p>
            <strong>Risk Level:</strong> {result.risk_level}
        </p>

        <p>
            <strong>Confidence:</strong> {result.confidence}%
        </p>

        <p>
            <strong>Interest Rate:</strong>{" "}
            {result.recommended_interest_rate}%
        </p>

        <p>
            <strong>Recommended Loan Limit:</strong> ₹
            {result.recommended_loan_limit}
        </p>

        <p>
            <strong>Fraud Score:</strong> {result.fraud_score}
        </p>

        <p>
            <strong>Manual Review:</strong>{" "}
            {result.manual_review ? "Yes" : "No"}
        </p>

        <p>
            <strong>AI Decision:</strong> {result.decision}
        </p>

    </div>
)}

        </div>

    );

}

export default LoanForm;