import time

from celery import Celery


celery_app = Celery(
    __name__, 
    backend="redis://localhost:6379", 
    broker="redis://localhost:6379"
    )

@celery_app.task(name="create_task")
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True