from fastapi import FastAPI
from pydantic import BaseModel
from .worker import start_worker, push

app = FastAPI(title="Notification Service")

@app.on_event("startup")
def startup(): start_worker()

class Job(BaseModel):
    channel: str  # "email" | "sms"
    to: str
    message: str

@app.post("/notify", status_code=202)
def notify(job: Job):
    push(job.dict())
    return {"accepted": True}
