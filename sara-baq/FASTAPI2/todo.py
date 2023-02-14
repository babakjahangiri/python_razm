from fastapi import APIRouter
from model import Todo,TodoItem

todo_router = APIRouter()

todo_list=[]

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message":"todo added successfully"}


@todo_router.get("/todo")
async def retrieve_todos() ->dict:
    return{"todos":todo_list}

@todo_router.get("/todo/{id}")
async def find_by_id(id:int):
    for todo in todo_list:
        if todo.id==id:
            return {"todo":todo}

        return {"message":"todo with this id not found"}

@todo_router.put("todo/{id}")
async def update_todo(todo_data:TodoItem,id :int) -> dict:
    for todo in todo_list:
        if todo.id==id:
            todo.item=todo_data.item
            return {"message":"todo data updated successfully."}
        return {"message":"Todo with supplied ID doesn't exist"}