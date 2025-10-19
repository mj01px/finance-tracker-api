"""
Tag model definition

Responsibilities:
- Defines ORM model for Tag entity
- Maps to PostgreSQL table using SQLAlchemy ORM
- Represents tag names used to categorize expenses

Example:
    tag = Tag(name="Food")
"""

from sqlalchemy import Column, Integer, String
from app.core.database import Base


# Tag Model
class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)  # Unique identifier
    name = Column(String(50), unique=True, nullable=False)  # Tag name (must be unique)

    def __repr__(self):
        # Returns a readable string representation of the Tag instance
        return f"<Tag(name='{self.name}')>"