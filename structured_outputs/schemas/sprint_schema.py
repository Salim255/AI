from pydantic import BaseModel
from typing import Optional

class Sprint(BaseModel):
    id: Optional[str] = None
    name: str
    goal: Optional[str] = None
    start_date: Optional[str] = None  # ISO date
    end_date: Optional[str] = None
    project_id: Optional[str] = None
