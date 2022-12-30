from celery import Celery

from app.core.config import settings

celery_app = Celery(
    __name__, backend=settings.CELERY_RESULT_BACKEND, broker=settings.CELERY_BROKER_URL
)
