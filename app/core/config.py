
from pydantic_settings import BaseSettings
from pathlib import Path
from typing import List

class Settings(BaseSettings):
    
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "PDF Analysis API"
    VERSION: str = "0.1.0"
    
    
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    
    
    UPLOAD_DIR: Path = Path("uploads")
    MAX_UPLOAD_SIZE: int = 50 * 1024 * 1024  
    
    class Config:
        env_file = ".env"

settings = Settings()