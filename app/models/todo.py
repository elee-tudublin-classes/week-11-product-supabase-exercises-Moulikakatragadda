from pydantic import BaseModel

class ToDo(BaseModel):
    id: int
    details: str
    completed: bool = False
    userId: int = 0
