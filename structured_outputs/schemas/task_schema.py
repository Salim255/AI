from pydantic import BaseModel, Field
from typing import Optional, Literal

class Task(BaseModel):
    id: Optional[str] = Field(None, description="Unique task ID")
    title: str = Field(..., min_length=3)
    description: Optional[str] = None
    status: Literal["todo", "in_progress", "done"] = "todo"
    priority: Literal["low", "medium", "high"] = "medium"
    assignee: Optional[str] = None
    story_points: Optional[int] = None
    sprint_id: Optional[str] = None
    project_id: Optional[str] = None
