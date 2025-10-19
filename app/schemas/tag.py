"""
Tag schemas

Responsibilities:
- Defines Pydantic models for Tag entity validation and serialization
- Separates input (create) and output (response) models
- Ensures ORM compatibility for automatic data conversion

Example:
    {
        "id": 1,
        "name": "Utilities"
    }
"""

from pydantic import BaseModel, ConfigDict


# Shared base schema for common Tag fields
class TagBase(BaseModel):
    name: str  # Tag name (must be unique)


# Schema for creating new tags (inherits all fields)
class TagCreate(TagBase):
    pass

# Schema for returning tag data (includes ID)
class TagOut(TagBase):
    id: int

    class Config:
        from_attributes = True  # Allows ORM models to map directly to Pydantic objects
