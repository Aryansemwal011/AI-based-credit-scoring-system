import { useEffect, useState } from "react";
import axios from "axios";
import "../styles/history.css";

function HistoryPage() {

    const [history, setHistory] = useState([]);
    const [search, setSearch] = useState("");

    useEffect(() => {
        fetchHistory();
    }, []);

    const fetchHistory = async () => {

        try {

            const response = await axios.get(
                "http://127.0.0.1:8000/history"
            );

            setHistory(response.data);

        } catch (error) {
            console.error(error);
        }

    };

    return (

        <div className="history-container">

            <h1 className="history-title">
                Loan Application History
            </h1>
            <input
                className="search-box"
                type="text"
                placeholder="Search Application ID..."
                value={search}
            onChange={(e) => setSearch(e.target.value)}
           
        />

            <table
                className="history-table"
                style={{
                    width: "100%",
                    borderCollapse: "collapse",
                    boxShadow: "0 5px 15px rgba(0,0,0,.15)"
                }}
            >

                <thead
                    style={{
                        background: "#1f2937",
                        color: "white"
                    }}
                >

                    <tr>

                        <th style={styles.th}>Application ID</th>

                        <th style={styles.th}>Loan Status</th>

                        <th style={styles.th}>Probability</th>

                        <th style={styles.th}>Risk</th>

                        <th style={styles.th}>Fraud Score</th>

                        <th style={styles.th}>Manual Review</th>

                        <th style={styles.th}>Date</th>

                    </tr>

                </thead>

                <tbody>

                    {history
                         .filter(item =>
                            item.application_id
                                .toLowerCase()
                                .includes(search.toLowerCase())
                         )
                        .map((item) => (

                        <tr key={item.id}>

                            <td style={styles.td}>
                                {item.application_id}
                            </td>

                            <td> <span
                                className={
                                item.loan_status==="Approved"
                                ?
                                "badge-approved"
                                :
                                "badge-rejected"
                                }
                                >   

                                {item.loan_status}

                                </span>

                            </td>

                            <td style={styles.td}>
                                {item.approval_probability}%
                            </td>

                            <td> <span
                                className={
                                item.risk_level==="Low"
                                ?
                                "low"
                                :
                                item.risk_level==="Medium"
                                ?
                                "medium"
                                :
                                "high"
                                }
                                >

                                {item.risk_level}

                                </span>

                            </td>

                            <td style={styles.td}>
                                {item.fraud_score}
                            </td>

                            <td style={styles.td}>
                                {item.manual_review ? "Yes" : "No"}
                            </td>

                            <td style={styles.td}>
                                {item.created_at}
                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}

const styles = {

    th: {

        padding: "12px"

    },

    td: {

        padding: "12px",

        textAlign: "center",

        borderBottom: "1px solid #ddd"

    }

};

export default HistoryPage;