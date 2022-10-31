from fastapi import FastAPI
import uvicorn

from api.v1 import routes as v1_routes
from repositories import init_db

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    init_db()

app.include_router(v1_routes, prefix="/api/v1")

@app.get("/healthz")
def healthz():
    return "Service is healthy"

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080)
