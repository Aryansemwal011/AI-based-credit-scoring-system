import { useState } from "react";
import API from "../services/api";
import Dashboard from "./Dashboard";
import "../styles/form.css";

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

            <div className="hero">

                <h1>AI Loan Approval System</h1>

                <p>
                    Intelligent Multi-Agent Loan Approval Platform
                </p>

            </div>

            <form onSubmit={handleSubmit}>

                <div className="form-grid">

                    <div className="form-group">

                        <label>Gender</label>

                        <select
                            name="Gender"
                            value={formData.Gender}
                            onChange={handleChange}
                            required
                        >
                            <option value="">Select</option>
                            <option value={1}>Male</option>
                            <option value={0}>Female</option>
                        </select>

                    </div>

                    <div className="form-group">

                        <label>Married</label>

                        <select
                            name="Married"
                            value={formData.Married}
                            onChange={handleChange}
                            required
                        >
                            <option value="">Select</option>
                            <option value={1}>Yes</option>
                            <option value={0}>No</option>
                        </select>

                    </div>

                    <div className="form-group">

                        <label>Dependents</label>

                        <input
                            type="number"
                            name="Dependents"
                            value={formData.Dependents}
                            onChange={handleChange}
                            placeholder="Enter dependents"
                            required
                        />

                    </div>

                    <div className="form-group">

                        <label>Education</label>

                        <select
                            name="Education"
                            value={formData.Education}
                            onChange={handleChange}
                            required
                        >
                            <option value="">Select</option>
                            <option value={0}>Graduate</option>
                            <option value={1}>Not Graduate</option>
                        </select>

                    </div>

                    <div className="form-group">

                        <label>Self Employed</label>

                        <select
                            name="Self_Employed"
                            value={formData.Self_Employed}
                            onChange={handleChange}
                            required
                        >
                            <option value="">Select</option>
                            <option value={0}>No</option>
                            <option value={1}>Yes</option>
                        </select>

                    </div>

                    <div className="form-group">

                        <label>Applicant Income</label>

                        <input
                            type="number"
                            name="ApplicantIncome"
                            value={formData.ApplicantIncome}
                            onChange={handleChange}
                            placeholder="Enter applicant income"
                            required
                        />

                    </div>

                    <div className="form-group">

                        <label>Coapplicant Income</label>

                        <input
                            type="number"
                            name="CoapplicantIncome"
                            value={formData.CoapplicantIncome}
                            onChange={handleChange}
                            placeholder="Enter coapplicant income"
                            required
                        />

                    </div>

                    <div className="form-group">

                        <label>Loan Amount</label>

                        <input
                            type="number"
                            name="LoanAmount"
                            value={formData.LoanAmount}
                            onChange={handleChange}
                            placeholder="Enter loan amount"
                            required
                        />

                    </div>

                    <div className="form-group">

                        <label>Loan Amount Term</label>

                        <input
                            type="number"
                            name="Loan_Amount_Term"
                            value={formData.Loan_Amount_Term}
                            onChange={handleChange}
                            placeholder="Enter loan term (months)"
                            required
                        />

                    </div>

                    <div className="form-group">

                        <label>Credit History</label>

                        <select
                            name="Credit_History"
                            value={formData.Credit_History}
                            onChange={handleChange}
                            required
                        >
                            <option value="">Select</option>
                            <option value={1}>Good</option>
                            <option value={0}>Bad</option>
                        </select>

                    </div>

                    <div className="form-group">

                        <label>Property Area</label>

                        <select
                            name="Property_Area"
                            value={formData.Property_Area}
                            onChange={handleChange}
                            required
                        >
                            <option value="">Select</option>
                            <option value={0}>Rural</option>
                            <option value={1}>Semiurban</option>
                            <option value={2}>Urban</option>
                        </select>

                    </div>

                </div>

                <button
                    type="submit"
                    className="predict-btn"
                >
                    Predict Loan
                </button>

            </form>

            {result && (

                <Dashboard result={result} />

            )}

        </div>

    );

}

export default LoanForm;