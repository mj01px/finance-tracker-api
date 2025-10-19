"""
Expense schemas

Responsibilities:
- Defines Pydantic models for Expense data validation and response
- Manages type safety for request (create) and response (output) models
- Integrates with TagOut schema for nested tag representation

Example:
    {
        "id": 1,
        "description": "Groceries",
        "amount": 150.0,
        "category": "Food",
        "tags": [{"id": 1, "name": "Market"}]
    }
"""

from pydantic import BaseModel, ConfigDict, Field
from typing import List
from app.schemas.tag import TagOut


# Shared base schema for common Expense fields
class ExpenseBase(BaseModel):
    description: str
    amount: float = Field(gt=0)  # Must be greater than zero
    category: str


# Schema for creating new expenses (accepts tag names as strings)
class ExpenseCreate(ExpenseBase):
    tags: List[str] = []


# Schema for returning expense data (includes full Tag objects)
class ExpenseOut(ExpenseBase):
    id: int
    tags: List[TagOut] = []

    class Config:
        from_attributes = True  # Allows ORM models to be converted to schema instances