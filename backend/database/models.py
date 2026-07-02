from backend.database.database import get_connection


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS loan_applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    application_id TEXT,

    gender INTEGER,
    married INTEGER,
    dependents INTEGER,
    education INTEGER,
    self_employed INTEGER,

    applicant_income REAL,
    coapplicant_income REAL,
    loan_amount REAL,
    loan_amount_term REAL,
    credit_history INTEGER,
    property_area INTEGER,

    loan_status TEXT,
    approval_probability REAL,
    risk_level TEXT,
    fraud_score REAL,
    manual_review INTEGER,

    response_json TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
    
    """)

    conn.commit()
    conn.close()