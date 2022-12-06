import time

from celery import Celery
from celery.contrib.abortable import AbortableTask

from .config import settings

celery_app = Celery(
    __name__, backend=settings.CELERY_RESULT_BACKEND, broker=settings.CELERY_BROKER_URL
)


@celery_app.task(name="create_new_task", base=AbortableTask)
def create_new_task(task_type):
    time.sleep(int(task_type) * 10)
    return True
