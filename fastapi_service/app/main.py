from fastapi import FastAPI
from app.routers import health

app = FastAPI()
app.include_router(health.router)

@app.get("/")
def read_root():
    return {"message": "FastAPI Microservice Running"}