from fastapi import APIRouter, Path
from models import Todo, TodoItem

todo_router = APIRouter()
todo_list = []


@todo_router.post("/todo")
async def add_todo (todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}


@todo_router.get("/todo")
async def retrieve_todos () -> dict:
    """

    :return:
    """
    return {"todos": todo_list}


@todo_router.get("/todo/{todo_id}")
async def get_signale_todo (todo_id: int = Path(..., title = 'Todo not found for retrieve.')) -> dict:
    """

    :param todo_id:
    """

    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Todo not found for retrieve"}


@todo_router.put("/todo/{todo_id}")
async def update_todo (todo_data: TodoItem,
                       todo_id: int = Path(..., title = "Todo not found for update")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Todo updated successfully"}
    return {"message": "Todo not found for update"}
