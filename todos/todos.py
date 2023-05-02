from fastapi import APIRouter

todo_router = APIRouter()

todo_list = []  # 임시 데이터베이스


@todo_router.post('/todo')
async def add_todo(todo: dict) -> dict:
    todo_list.append(todo)
    return {
        'message': '[SUCCESS] add Todo'
    }


@todo_router.get('/todo')
async def receive_todos() -> dict:
    return {
        'todos': todo_list
    }
