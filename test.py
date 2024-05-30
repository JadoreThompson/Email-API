from models import Task

tasks = {
    1: Task(name="Cook", description="Jerk Chicken"),
    2: Task(name="Clean", description="Kitchen"),
    3: Task(name="Study", description="FastAPI", completed=True),
}


new_name = str(input("Name:"))
new_desc = str(input("Desc:"))
new_comp = bool(input("Comp:"))
task_id = int(input("ID:"))

if new_name != '':
    tasks[task_id].name = new_name
if new_desc != '':
    tasks[task_id].description = new_desc
if new_comp:
    tasks[task_id].completed = new_comp

print(tasks[task_id])




