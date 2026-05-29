from fastapi import FastAPI

app = FastAPI()

todos = [
    {"id": 1, "title": "Learn Fast api"},
    {"id": 2, "title": "Learn CI/CD"},
]

@app.get("/")
def home():
    return {"message": "FastApi CI/CD app"}

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def create_todos(todo: dict):
        todos.append(todo)
        return {
             "message": "Todo Created",
             "data": todo
        }

    