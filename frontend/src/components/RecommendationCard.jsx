function RecommendationCard({ recommendations }) {

    return (

       <div className="ai-card">

            <h2>Recommendations</h2>

            <hr />

            <ul>
                {recommendations.map((recommendation, index) => (
                    <li key={index}>
                        {recommendation}
                    </li>
                ))}
            </ul>

        </div>

    );

}

export default RecommendationCard;