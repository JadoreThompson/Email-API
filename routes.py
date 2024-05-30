from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from models import Task

app = FastAPI()

tasks = {
    1: Task(name="Cook", description="Jerk Chicken"),
    2: Task(name="Clean", description="Kitchen"),
    3: Task(name="Study", description="FastAPI", completed=True),
}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/tasks/")
def get_all_tasks(title: str = None):
    incomplete_tasks = {task_id: task.dict() for task_id, task in tasks.items() if not task.completed}
    if title:
        return {task_id: task.dict() for task_id, task in tasks.items() if task.name == title}

    return incomplete_tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return tasks[task_id]

@app.post("/tasks/{task_id}")
def create_task(task: Task):
    tasks[len(tasks) + 1] = task
    return task

@app.put("/tasks/{task_id}/update")
def update_task(task_id: int, task: Task):
    update_task_encoded = jsonable_encoder(task)
    tasks[task_id] = update_task_encoded

    return update_task_encoded
