import time

from celery.contrib.abortable import AbortableTask

from app.core.celery_app import celery_app


@celery_app.task(name="create_new_task", base=AbortableTask)
def create_new_task(task_type):
    time.sleep(int(task_type) * 10)
    return True
