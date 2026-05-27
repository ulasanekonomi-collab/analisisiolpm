from fastapi import FastAPI
from app.routers import upload

app = FastAPI(
    title="Analisis IO LPM",
    version="0.1.0"
)

app.include_router(upload.router)

@app.get("/")
def root():
    return {
        "message": "Analisis IO LPM API is running"
    }
