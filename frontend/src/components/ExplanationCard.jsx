function ExplanationCard({ explanation }) {

    return (

        <div className="ai-card">

            <h2>AI Explanation</h2>

            <hr />

            <ul>
                {explanation.explanation.map((item, index) => (
                    <li key={index}>
                        {item}
                    </li>
                ))}
            </ul>

        </div>

    );

}

export default ExplanationCard;