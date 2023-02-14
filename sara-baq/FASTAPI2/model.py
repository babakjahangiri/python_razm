from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str

class TodoItem(BaseModel):
    class Config:
        schema_extra={
            "example":{
                "item":"read the next chapter of book"
            }
            }