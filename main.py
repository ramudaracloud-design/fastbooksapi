from fastapi import FastAPI

app = FastAPI(
    title="My EC2 FastAPI Application",
    version="1.0.0",
)

@app.get("/")
def home():
    return {
        "message": "Hello from FastAPI on Amazon EC2! Built By Ramu, using Shell Scripts",
        "status": "success",
    }

@app.get("/health")
def health():
    return {"status": "healthy"}


