from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    completed: bool

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    owner_id: int  

    class Config:
        from_attributes = True  
