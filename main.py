from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import csv
import os

app = FastAPI(
    title="To-Do REST API",
    description="A lightweight, robust RESTful To-Do API built with FastAPI and persistent CSV storage.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

class Task(BaseModel):
    title: str
    completed: bool

tasks = {}
next_id = 1


def load_tasks():
    global next_id

    if os.path.exists("tasks.csv"):
        with open("tasks.csv", "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                task_id = int(row["id"])

                if task_id >= next_id:
                    next_id = task_id + 1
                
                completed = (row["completed"] == "True")
                tasks[task_id] = {
                    "title": row["title"],
                    "completed": completed
                }

    else:
        pass

def save_tasks():
    with open("tasks.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id","title", "completed"])
        writer.writeheader()
        for task_id, task_data in tasks.items():
            writer.writerow({
                "id": task_id,
                "title": task_data["title"],
                "completed": task_data["completed"]
            })


load_tasks()

@app.get("/", tags=["General"])
def index():
    """Welcome endpoint returning API status message."""
    return {"message": "Hello World"}

@app.get("/health", tags=["General"])
def health_check():
    """Health check endpoint to verify service uptime."""
    return {"status": "healthy"}

@app.post("/tasks", tags=["Tasks"])
def task(task: Task):
    """Create a new to-do task and persist to CSV."""
    global next_id
    task_id = next_id
    tasks[task_id] = task.model_dump()
    save_tasks()
    next_id = next_id + 1

    return {"task added successfully id": task_id, "data": tasks[task_id]}

@app.get("/tasks", tags=["Tasks"])
def get_task():
    """Retrieve all to-do tasks."""
    return tasks

@app.get("/tasks/{task_id}", tags=["Tasks"])
def get_by_id(task_id: int):
    """Retrieve a specific to-do task by ID."""
    if task_id in tasks:
        return tasks[task_id]
    else:
        raise HTTPException(status_code=404, detail="Id not found")

@app.put("/tasks/{task_id}", tags=["Tasks"])
def update_task(task_id: int, task: Task):
    """Update an existing to-do task by ID."""
    if task_id in tasks:
        tasks[task_id] = task.model_dump()
        save_tasks()
        return {
            "message": "Task updated successfully",
            "data": tasks[task_id]
        }
    else:
        raise HTTPException(status_code=404, detail="Id not found")

@app.delete("/tasks/{task_id}", tags=["Tasks"])
def del_task(task_id: int):
    """Delete a to-do task by ID."""
    if task_id in tasks:
        tasks.pop(task_id)
        save_tasks()
        return {"message": "Task deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Id not found")