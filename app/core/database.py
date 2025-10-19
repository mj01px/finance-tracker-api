"""
Core database configuration module

Responsibilities:
- Loads environment variables from `.env`
- Defines PostgreSQL connection URL via SQLAlchemy
- Initializes database engine, ORM base, and session factory
- Provides `get_db()` dependency for FastAPI routes

Example:
    Used in routes as:
        db: Session = Depends(get_db)
"""

from __future__ import annotations

import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base

# Environment & Path Setup

BASE_DIR = Path(__file__).resolve().parents[2]   # Root project path
ENV_PATH = BASE_DIR / ".env"                     # .env file path

load_dotenv(dotenv_path=ENV_PATH)                # Load environment variables


# Database Credentials (.env)

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

#  SQLAlchemy Configuration
# Build connection URL for PostgreSQL using psycopg2 driver
url = URL.create(
    "postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
)

# Initialize SQLAlchemy engine (manages database connections)
engine = create_engine(url, pool_pre_ping=True)  # pool_pre_ping checks stale connections

# Create session factory for DB operations
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base class for all ORM models (used by declarative mapping)
Base = declarative_base()


# Database Session Dependency (FastAPI)
def get_db():
    """
    Creates a new SQLAlchemy session.

    Yields:
        db (Session): active session for database operations.
    Ensures proper cleanup by closing the session automatically.
    """
    db = SessionLocal()
    try:
        yield db  # Provide session to FastAPI route handlers
    finally:
        db.close()  # Always close after request is handled
        