from fastapi import FastAPI, HTTPException
from app.models import AnalyzePRRequest
from app.tasks import analyze_code_task
from celery.result import AsyncResult

app = FastAPI()

@app.post("/analyze-pr")
def analyze_pr(request: AnalyzePRRequest):
    task = analyze_code_task.apply_async(args=[request.model_dump()])
    return {"task_id": task.id, "status": "submitted"}

@app.get("/status/{task_id}")
def get_status(task_id: str):
    task_result = AsyncResult(task_id)
    if task_result.state == "PENDING":
        return {"task_id": task_id, "status": "pending"}
    elif task_result.state == "SUCCESS":
        return {"task_id": task_id, "status": "completed", "result": task_result.result}
    elif task_result.state == "FAILURE":
        return {"task_id": task_id, "status": "failed", "error": str(task_result.info)}
    else:
        return {"task_id": task_id, "status": task_result.state}