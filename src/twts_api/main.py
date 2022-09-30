from fastapi import FastAPI
from api.v1 import routes as v1_routes
import uvicorn

app = FastAPI()

app.include_router(v1_routes, prefix="/api")


@app.get("/healthz")
def healthz():
    return "Service is healthy"


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080)
