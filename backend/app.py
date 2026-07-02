from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from backend.routes.predict import router as predict_router
from fastapi import FastAPI

from backend.database.models import create_tables
from backend.routes.history import router as history_router 




app = FastAPI(
    title="AI Credit Scoring System",
    version="1.0"
)
create_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome"}

@app.get("/health")
def health():
    return {"status": "Running"}

app.include_router(predict_router)
app.include_router(history_router)