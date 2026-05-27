from fastapi import FastAPI

app = FastAPI(
    title="Analisis IO LPM",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Analisis IO LPM API is running"
    }
