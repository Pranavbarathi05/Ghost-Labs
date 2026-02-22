"""
Database connection and session management
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

from core.config import settings

logger = logging.getLogger(__name__)

# Create Base class for models (always needed)
Base = declarative_base()

# Try to create database engine (may fail if PostgreSQL not available)
try:
    engine = create_engine(settings.DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    logger.info("Database engine created successfully")
except Exception as e:
    logger.warning(f"Could not create database engine: {e}")
    logger.warning("Database operations will not work until PostgreSQL is configured")
    engine = None
    SessionLocal = None


# Dependency to get database session
def get_db():
    """Get database session"""
    if SessionLocal is None:
        raise RuntimeError("Database not configured. Please set up PostgreSQL.")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
