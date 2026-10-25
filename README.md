# 📝 FastAPI To-Do REST API

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2.0+-e92063.svg?style=flat&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight, robust, and asynchronous RESTful To-Do application built with **FastAPI**, **Pydantic v2**, and persistent **CSV storage**. Designed with clean architecture, interactive Swagger API docs, and automated test suites.

---

## 🚀 Features

- **⚡ High Performance:** Powered by FastAPI and ASGI (Uvicorn) for lightning-fast request processing.
- **🔄 Full CRUD Operations:** Complete support to Create, Read, Update, and Delete tasks.
- **💾 Persistent CSV Storage:** Automatically saves tasks to `tasks.csv` and loads them on startup—no external database setup required!
- **🛡️ Data Validation:** Strict request payload schema validation using Pydantic v2 models.
- **📖 Interactive API Documentation:** Auto-generated interactive documentation available out of the box via Swagger UI and ReDoc.
- **🩺 Health Check:** Built-in `/health` status endpoint for monitoring and uptime checks.
- **🧪 Test Suite:** Fully covered with automated `pytest` tests using FastAPI's `TestClient`.

---

## 📂 Project Structure

```text
fastapi-todo-api/
├── main.py                 # FastAPI application and route controllers
├── test_main.py            # Automated test suite using TestClient & Pytest
├── tasks.csv               # Persistent CSV data storage for tasks
├── requirements.txt        # Production and testing dependencies
├── LICENSE                 # MIT License
├── .gitignore              # Git ignore rules for Python projects
└── README.md               # Project documentation
```

---

## 📡 API Endpoints Reference

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :---: |
| `GET` | `/` | Welcome message / root status | `200 OK` |
| `GET` | `/health` | Service health status check | `200 OK` |
| `POST` | `/tasks` | Create a new task | `200 OK` |
| `GET` | `/tasks` | Retrieve all tasks | `200 OK` |
| `GET` | `/tasks/{task_id}` | Retrieve a specific task by ID | `200 OK` / `404 Not Found` |
| `PUT` | `/tasks/{task_id}` | Update an existing task | `200 OK` / `404 Not Found` |
| `DELETE` | `/tasks/{task_id}` | Delete a task by ID | `200 OK` / `404 Not Found` |

---

## 🛠️ Prerequisites & Installation

### Requirements
- **Python 3.10+**
- `pip` package manager

### 1. Clone the repository
```bash
git clone https://github.com/Adii2610/fastapi-todo-api.git
cd fastapi-todo-api
```

### 2. Create and activate a virtual environment

**On Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**On Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🏃 Running the Application

Start the local development server with auto-reload:

```bash
uvicorn main:app --reload
```

The application will start at:
- **Base URL:** `http://127.0.0.1:8000`
- **Interactive Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative ReDoc UI:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 💻 Example API Usage (cURL)

### 1. Create a Task
```bash
curl -X POST "http://127.0.0.1:8000/tasks" \
     -H "Content-Type: application/json" \
     -d '{"title": "Learn FastAPI & Docker", "completed": false}'
```

**Response:**
```json
{
  "task added successfully id": 2,
  "data": {
    "title": "Learn FastAPI & Docker",
    "completed": false
  }
}
```

### 2. Get All Tasks
```bash
curl -X GET "http://127.0.0.1:8000/tasks"
```

### 3. Get Task by ID
```bash
curl -X GET "http://127.0.0.1:8000/tasks/2"
```

### 4. Update a Task
```bash
curl -X PUT "http://127.0.0.1:8000/tasks/2" \
     -H "Content-Type: application/json" \
     -d '{"title": "Learn FastAPI & Docker", "completed": true}'
```

### 5. Delete a Task
```bash
curl -X DELETE "http://127.0.0.1:8000/tasks/2"
```

---

## 🧪 Running Unit Tests

Execute the automated test suite with `pytest`:

```bash
pytest -v
```

---

## 📄 License

This project is open-source and licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Aditya**  
GitHub: [@Adii2610](https://github.com/Adii2610)
