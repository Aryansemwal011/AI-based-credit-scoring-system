import { useState } from "react";

function LoanForm() {

    const [formData, setFormData] = useState({
        Gender: "",
        Married: "",
        ApplicantIncome: ""
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        console.log(formData);
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
                >
                    <option value="">Select</option>
                    <option>Male</option>
                    <option>Female</option>
                </select>

                <label>Married</label>

                <select
                    name="Married"
                    value={formData.Married}
                    onChange={handleChange}
                >
                    <option value="">Select</option>
                    <option>Yes</option>
                    <option>No</option>
                </select>

                <label>Applicant Income</label>

                <input
                    type="number"
                    name="ApplicantIncome"
                    value={formData.ApplicantIncome}
                    onChange={handleChange}
                />

                <button type="submit">
                    Predict
                </button>

            </form>

        </div>
    );
}

export default LoanForm;