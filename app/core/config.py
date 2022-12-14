from pydantic import BaseSettings


class Settings(BaseSettings):
    # FastAPI
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI + Celery"

    # Redis
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/0"

    class Config:
        env_file = [".env"]


settings = Settings()
