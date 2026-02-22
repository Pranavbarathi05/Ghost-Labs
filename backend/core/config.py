"""
Configuration settings for Ghost Labs
"""
from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    """Application settings"""
    
    # Application
    APP_NAME: str = "Ghost Labs"
    DEBUG: bool = True
    API_V1_PREFIX: str = "/api/v1"
    
    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@db:5432/ghostlabs"
    )
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://frontend:3000"
    ]
    
    # Docker & Workspaces
    DOCKER_SOCKET: str = "/var/run/docker.sock"
    WORKSPACE_IMAGE: str = "ubuntu:22.04"
    WORKSPACE_SNAPSHOT_PATH: str = "/app/snapshots"
    
    # Cloudflare Tunnel
    CLOUDFLARE_TUNNEL_TOKEN: str = os.getenv("CLOUDFLARE_TUNNEL_TOKEN", "")
    
    # AI Service
    AI_SERVICE_URL: str = os.getenv("AI_SERVICE_URL", "http://ai-service:8001")
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
