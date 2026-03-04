# Development Guide

This document provides a detailed overview of the project structure, module responsibilities, and the recommended development workflow.

## Project Structure Overview

The project is structured following industry-standard FastAPI best practices, emphasizing clean architecture and separation of concerns.

```text
.
├── app/                    # Main application package
│   ├── api/                # API layer (v1 versioning)
│   │   └── v1/             # Version 1 of the API
│   │       ├── endpoints/  # Specific endpoint handlers (e.g., users)
│   │       └── api.py      # Main router combining all endpoints
│   ├── core/               # Core configuration and security
│   │   ├── config.py       # Pydantic settings and environment management
│   │   └── security.py     # Password hashing and authentication utilities
│   ├── db/                 # Database layer
│   │   └── session.py      # Engine setup, sessionmaker, and Base model
│   ├── models/             # SQLAlchemy ORM models (Database entities)
│   ├── schemas/            # Pydantic schemas (Data validation/API models)
│   ├── services/           # Service layer (Business logic)
│   └── main.py             # FastAPI entry point
├── tests/                  # Automated test suite
│   ├── api/                # API integration tests
│   └── conftest.py         # Pytest fixtures and configuration
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Multi-container orchestration (API + PostgreSQL)
└── requirements.txt        # Python dependencies
```

---

## Module Responsibilities

### `app/api/`
Handles HTTP requests and responses. It defines the routing logic and maps HTTP verbs to service methods.
- **`v1/endpoints/`**: Contains the actual route handlers. They should be thin and delegate business logic to the services layer.
- **`api_router`**: Combines all sub-routers into a single entry point for the application.

### `app/core/`
Centralized configuration and cross-cutting concerns.
- **`config.py`**: Uses `pydantic-settings` to manage environment variables (`.env`).
- **`security.py`**: Handles password hashing using `bcrypt` directly to ensure security.

### `app/db/`
Encapsulates all database-related setup.
- **`session.py`**: Configures the SQLAlchemy engine and provides the `get_db` dependency for FastAPI's dependency injection system.
- **`Base`**: The declarative base for all ORM models.

### `app/models/`
Defines the database schema using SQLAlchemy. These classes represent the physical tables in the database.

### `app/schemas/`
Defines the data structures for input validation and output serialization using Pydantic. These are used to generate the OpenAPI documentation automatically.
- `UserCreate`: Validation for registration/creation.
- `UserUpdate`: Validation for partial updates.
- `User`: The response model (serializes database objects).

### `app/services/`
The "brain" of the application. All business logic, database queries, and data manipulation should reside here. This makes the code more testable and reusable.

### `app/main.py`
The main entry point of the FastAPI application. It initializes the app, includes routers, and handles the initial database table creation (for local/simple setups).

---

## Development Workflow

### 1. Local Environment Setup
It is recommended to use a virtual environment.
```bash
# Create a virtual environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate
# Activate it (Unix)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Running the Application
For local development with auto-reload:
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.
Swagger Documentation: `http://127.0.0.1:8000/docs`

### 3. Docker Workflow
To run the application with a PostgreSQL database:
```bash
# Build and start services
docker-compose up --build

# Run in background
docker-compose up -d

# Stop services
docker-compose down
```

### 4. Testing
The project uses `pytest` for automated testing.
```bash
# Run all tests
pytest

# Run tests and show output
pytest -s
```
Tests use a separate temporary SQLite database (`test_temp.db`) to ensure isolation and reproducibility. Fixtures are defined in `tests/conftest.py`.

---

## Best Practices Followed

- **Clean Imports**: Using `__init__.py` files to export key symbols allows for concise imports like `from app.models import User`.
- **Dependency Injection**: Database sessions are injected into endpoints, making them easy to mock during testing.
- **Separation of Concerns**: API routes don't know about database details, and models don't know about HTTP.
- **Input Validation**: Strong typing ensures that only valid data reaches the service layer.
- **Security**: Never stores plain-text passwords; uses `bcrypt` directly for hashing.
