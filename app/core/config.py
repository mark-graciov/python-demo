from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env")
    PROJECT_NAME: str = "Admin User CRUD API"
    API_V1_STR: str = "/api/v1"
    
    # DATABASE_URL: str = "sqlite:///./sql_app.db"
    # For testing/local we can use in-memory or file-based sqlite
    DATABASE_URL: Optional[str] = "sqlite:///./test.db"

settings = Settings()
