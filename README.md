![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Docker](https://img.shields.io/badge/Docker-Containerization-lightblue)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)


📝 TO-DO APP
FastAPI + PostgreSQL + Docker

A backend application for managing tasks (To-Do) built with FastAPI, PostgreSQL, and Docker. Includes JWT authentication, full CRUD operations, API documentation with Swagger & Redoc, and quick deployment using Docker Compose.


Features
🔑 User registration and login with JWT authentication

✅ Full CRUD operations for tasks

📖 Interactive API documentation with Swagger and Redoc

🐳 Quick setup and run with Docker & Docker Compose

🧪 Seed data for testing


🛠️ Technologies
Backend: FastAPI, SQLAlchemy, Pydantic

Database: PostgreSQL

Authentication: JWT (OAuth2 Password Flow)

Containerization: Docker, Docker Compose

⚙️ Installation & Run

1️⃣ Clone the repository

```bash
git clone https://github.com/fargolazadi/todo-app-fastapi.git
cd todo-app-fastapi
```
2️⃣ Environment variables

Create a .env file in the project root and add:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=todo_db
DATABASE_URL=postgresql+psycopg2://postgres:postgres@db:5432/todo_db
```
3️⃣ Run with Docker Compose

‍‍‍‍‍‍```bash
docker-compose up --build
```

4️⃣ Access services

🌐 FastAPI: http://localhost:8000

📑 Swagger UI: http://localhost:8000/docs

📘 Redoc: http://localhost:8000/redoc

🗄️ PostgreSQL: available on port 5432

## Screenshots

### Swagger UI
![Swagger](screenshots/swagger.png)

### Redoc
![Redoc](screenshots/redoc.png)

### JSON
![Json](screenshots/json.png)

### Docker 
![Docker](screenshots/docker.png)
