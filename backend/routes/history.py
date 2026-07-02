from fastapi import APIRouter
from backend.database.database import get_connection

router = APIRouter()


@router.get("/history")
def get_history():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM loan_applications
        ORDER BY rowid DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]