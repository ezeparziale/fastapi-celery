from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Task(BaseModel):
    task_type: int = 1
    started_at: Optional[datetime]
