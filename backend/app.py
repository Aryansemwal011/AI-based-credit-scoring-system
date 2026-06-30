from fastapi import FastAPI

app = FastAPI(
    title="AI Credit Scoring System",
    version="1.0.0",
    description="AI Powered Credit Scoring Platform"
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