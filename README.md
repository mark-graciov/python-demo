# Admin User CRUD API

This is an industry-standard FastAPI-based Admin CRUD API for managing users.

## Features

- **FastAPI**: High performance, easy to use, and automatic interactive documentation.
- **SQLAlchemy**: ORM for database interactions.
- **Pydantic**: Data validation and settings management.
- **SQLite**: Local/testing database.
- **PostgreSQL**: Production-ready database (via Docker).
- **Docker**: Containerized environment for easy deployment.
- **Testing**: Comprehensive tests using `pytest`.

## Project Structure

- `app/api`: API routes and versioning.
- `app/core`: Configuration and settings.
- `app/services`: Business logic and services.
- `app/db`: Database session and base model.
- `app/models`: SQLAlchemy models.
- `app/schemas`: Pydantic schemas.
- `tests`: Unit and integration tests.

## Local Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```
3. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Running with Docker

1. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

## Running Tests

```bash
pytest
```

## Best Practices Followed

- **Project Structure**: Clear separation of concerns (Models, Schemas, Services, API).
- **Dependency Injection**: Used for database sessions.
- **Environment Variables**: Managed with Pydantic Settings.
- **Input Validation**: Strong typing and validation using Pydantic.
- **API Versioning**: Included `/api/v1` prefix.
- **Automatic Documentation**: OpenAPI/Swagger docs enabled.
- **Containerization**: Docker and Docker Compose support.
- **Testing**: Automated tests included.

For more details on the project structure and development workflow, see [DEVELOPMENT.md](DEVELOPMENT.md).
