import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_crud_lifecycle():
    # 1. Create task
    new_task = {"title": "Test Task Automated", "completed": False}
    create_res = client.post("/tasks", json=new_task)
    assert create_res.status_code == 200
    data = create_res.json()
    assert "task added successfully id" in data
    task_id = data["task added successfully id"]
    assert data["data"]["title"] == "Test Task Automated"
    assert data["data"]["completed"] is False

    # 2. Read all tasks
    all_tasks_res = client.get("/tasks")
    assert all_tasks_res.status_code == 200
    all_tasks = all_tasks_res.json()
    assert str(task_id) in all_tasks or task_id in all_tasks

    # 3. Read single task by ID
    single_res = client.get(f"/tasks/{task_id}")
    assert single_res.status_code == 200
    assert single_res.json()["title"] == "Test Task Automated"

    # 4. Update task
    update_data = {"title": "Test Task Automated Updated", "completed": True}
    update_res = client.put(f"/tasks/{task_id}", json=update_data)
    assert update_res.status_code == 200
    assert update_res.json()["message"] == "Task updated successfully"
    assert update_res.json()["data"]["completed"] is True

    # 5. Delete task
    delete_res = client.delete(f"/tasks/{task_id}")
    assert delete_res.status_code == 200
    assert delete_res.json()["message"] == "Task deleted successfully"

    # 6. Verify 404 for deleted task
    not_found_res = client.get(f"/tasks/{task_id}")
    assert not_found_res.status_code == 404

def test_get_nonexistent_task():
    res = client.get("/tasks/999999")
    assert res.status_code == 404
    assert res.json()["detail"] == "Id not found"
