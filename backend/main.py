from fastapi import FastAPI
from log_ingestion import ingest_log
from log_processing import process_logs
from database import get_logs

app = FastAPI()

@app.post("/logs")
async def receive_log(log: dict):
    ingest_log(log)
    return {"message": "Log received"}

@app.get("/logs")
async def fetch_logs():
    return get_logs()

@app.get("/process")
async def analyze_logs():
    process_logs()
    return {"message": "Log analysis started"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
