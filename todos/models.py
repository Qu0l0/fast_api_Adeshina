from pydantic import BaseModel


# class Item(BaseModel):
#     item: str
#     status: bool


class Todo(BaseModel):
    id: int
    item: str
