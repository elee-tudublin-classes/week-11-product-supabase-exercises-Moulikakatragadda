from pydantic import BaseModel
from typing import Optional

class Category(BaseModel):
    id: Optional[int] = 0
    name: str
    description: str
