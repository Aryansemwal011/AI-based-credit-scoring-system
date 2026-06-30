from fastapi import APIRouter

from backend.schemas.predict_schema import LoanApplication

from backend.ml.predict import predict_loan

router = APIRouter()


@router.post("/predict")

def predict(application: LoanApplication):

    result = predict_loan(application)

    return result