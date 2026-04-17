from typing import Optional
from pydantic import BaseModel

class Project(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    owner_id: Optional[str] = None