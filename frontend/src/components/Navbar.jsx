import { Link } from "react-router-dom";

function Navbar() {

    return (

        <nav
            style={{
                background: "#1f2937",
                padding: "15px",
                display: "flex",
                gap: "20px"
            }}
        >

            <Link
                to="/"
                style={{
                    color: "white",
                    textDecoration: "none"
                }}
            >
                Loan Prediction
            </Link>

            <Link
                to="/history"
                style={{
                    color: "white",
                    textDecoration: "none"
                }}
            >
                History
            </Link>

        </nav>

    );

}

export default Navbar;