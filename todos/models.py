from pydantic import BaseModel


class Item(BaseModel):
    item: str
    status: bool


class Todo(BaseModel):
    id: int
    item: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Learn FastAPI",

            }
        }


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Learn FastAPI"
            }
        }
