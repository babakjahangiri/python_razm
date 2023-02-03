from pydantic import BaseModel

class ProductSchema(BaseModel):
    company: str
    name: str
    model: str
    is_available: bool