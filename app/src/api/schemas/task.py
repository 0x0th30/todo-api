from pydantic import BaseModel

class TaskModel(BaseModel):
    name: str
    status: str
