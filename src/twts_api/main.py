from fastapi import FastAPI
import uvicorn

from api.v1 import routes as v1_routes
from repositories import init_db

init_db()

app = FastAPI()

app.include_router(v1_routes, prefix="/api")

@app.get("/healthz")
def healthz():
    return "Service is healthy"


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080)
