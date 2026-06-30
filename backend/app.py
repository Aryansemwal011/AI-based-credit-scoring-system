from fastapi import FastAPI

from backend.routes.predict import router as predict_router

app = FastAPI(
    title="AI Credit Scoring System",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Credit Scoring API"
    }


@app.get("/health")
def health():
    return {
        "status": "Running"
    }


app.include_router(predict_router)