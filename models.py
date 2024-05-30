from pydantic import BaseModel
from typing import Optional



class Task(BaseModel):
    name: str
    description: Optional[str] = None
    completed: bool = False

class UpdateTask(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    completed: bool = False
