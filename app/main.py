from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .config import settings

from .worker import celery_app, create_new_task

from .schemas import Task

# FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.post("/tasks")
async def create_task(task: Task):
    task = create_new_task.apply_async(args=[task.task_type], eta=task.started_at)
    return JSONResponse({"task_id": task.id})


@app.get("/tasks/{task_id}")
def get_status(task_id):
    task_result = celery_app.AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
    return JSONResponse(result)


@app.delete("/tasks/{task_id}")
def delete_task(task_id):
    task_result = celery_app.AsyncResult(task_id).revoke(terminate=True)
    return JSONResponse(task_result)
