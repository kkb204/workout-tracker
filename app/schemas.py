from pydantic import BaseModel
from typing import Optional

class WorkoutBase(BaseModel):
    name: str
    duration: int
    date: str
    description: Optional[str] = None


class WorkoutCreate(WorkoutBase):
    pass

class WorkoutResponse(WorkoutBase):
    id: int
    class Config:
        from_attributes = True

