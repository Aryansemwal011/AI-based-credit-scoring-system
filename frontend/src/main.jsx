import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

import { BrowserRouter } from "react-router-dom";

import "./styles/dashboard.css";
import "./styles/cards.css";
import "./styles/app.css";
import "./styles/history.css";
import "./styles/form.css";
import "./styles/navbar.css";
import "./styles/footer.css";

ReactDOM.createRoot(document.getElementById("root")).render(

    <BrowserRouter>

        <App />

    </BrowserRouter>

);