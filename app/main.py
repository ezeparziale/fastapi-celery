from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


from .worker import celery_app, create_task


@app.get("/")
async def root(task_type: int):
    task = create_task.delay(task_type)
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
