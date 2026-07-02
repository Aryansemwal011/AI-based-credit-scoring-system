import { Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";

import LoanForm from "./components/LoanForm";
import HistoryPage from "./pages/HistoryPage";
import Footer from "./components/Footer";

function App() {

    return (

        <>

            <Navbar />

            <Routes>

                <Route
                    path="/"
                    element={<LoanForm />}
                />

                <Route
                    path="/history"
                    element={<HistoryPage />}
                />

            </Routes>
            <Footer />

        </>

    );

}

export default App;