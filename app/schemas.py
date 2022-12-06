from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    task_type: int = 1
    started_at: Optional[datetime]