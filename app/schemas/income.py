"""
Income schemas

Responsibilities:
- Defines Pydantic models for Income validation and serialization
- Separates models for creation (input) and response (output)
- Ensures ORM compatibility for SQLAlchemy model mapping

Example:
    {
        "id": 3,
        "source": "Freelance Project",
        "amount": 1200.0,
        "category": "Extra"
    }
"""

from pydantic import BaseModel


# Shared base schema for common Income fields
class IncomeBase(BaseModel):
    source: str       # Income source (e.g., Salary, Freelance)
    amount: float     # Amount received
    category: str     # Income category or type


# Schema for creating new incomes (inherits all fields)
class IncomeCreate(IncomeBase):
    pass


# Schema for returning income data (adds 'id' field)
class IncomeOut(IncomeBase):
    id: int

    class Config:
        from_attributes = True  # Allows ORM objects to map directly to Pydantic models