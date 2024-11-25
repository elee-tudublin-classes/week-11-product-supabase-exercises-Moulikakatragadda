from pydantic import BaseModel, ValidationInfo, field_validator
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None  # Use 'id' instead of '_id'
    category_id: int
    title: str
    description: str
    price: float
    stock: int
    thumbnail: str = ""

    @field_validator('thumbnail')
    def default_image(cls, v: str, info: ValidationInfo) -> str:
        if not v:
            return "/static/images/product/placeholder.webp"
        return v
