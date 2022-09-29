from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/healthz')
def healthz():
    return "Service is healthy"

if __name__ == '__main__':
    uvicorn.run('main:app', port=8080)
