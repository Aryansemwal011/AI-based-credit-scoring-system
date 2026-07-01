from fastapi import APIRouter

from backend.schemas.predict_schema import LoanApplication
from backend.agents.orchestrator import AgentOrchestrator

router = APIRouter()

orchestrator = AgentOrchestrator()


@router.post("/predict")
def predict(application: LoanApplication):

    result = orchestrator.run(application)

    return result