from fastapi import APIRouter, Path, Query

from todos.models import Todo, TodoItem

todo_router = APIRouter()

todo_list = []


@todo_router.post('/todo')
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        'message': '[SUCCESS] add Todo'
    }


@todo_router.get('/todo')
async def receive_todos() -> dict:
    return {
        'todos': todo_list
    }


@todo_router.get('/todo/{todo_id}')
async def get_single_todo(todo_id: int = Path(...,
                                              title='The ID of the todo to retrieve.')) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                'todo': todo
            }
    return {
        'message': "Todo with supplied ID doesn't exist."
    }


@todo_router.put('/todo/{todo_id}')
async def update_todo(todo_data: TodoItem, todo_id: int = Path(...,
                                                               title='The ID of the todo to be updated.')) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data
            return {
                'todo': '[SUCCESS] update Todo'
            }
    return {
        'message': "Todo with supplied ID doesn't exist."
    }


async def query_route(query: str = Query(None)):
    return query
