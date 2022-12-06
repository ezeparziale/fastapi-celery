from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas import Task
from app.worker import celery_app, create_new_task

router = APIRouter()


@router.post("/")
async def create_task(task: Task):
    task = create_new_task.apply_async(args=[task.task_type], eta=task.started_at)
    return JSONResponse({"task_id": task.id})


@router.get("/{task_id}")
def get_status(task_id):
    task_result = celery_app.AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
    return JSONResponse(result)


@router.delete("/{task_id}")
def delete_task(task_id):
    task_result = celery_app.AsyncResult(task_id).revoke(terminate=True)
    return JSONResponse(task_result)
