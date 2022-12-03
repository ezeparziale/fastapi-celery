import time

from celery import Celery

from config import settings

celery_app = Celery(
    __name__, backend=settings.CELERY_RESULT_BACKEND, broker=settings.CELERY_BROKER_URL
)


@celery_app.task(name="create_task")
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True
