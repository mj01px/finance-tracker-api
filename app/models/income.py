"""
Income model definition

Responsibilities:
- Defines ORM model for Income entity
- Maps to PostgreSQL table using SQLAlchemy ORM
- Represents income records with source, amount, and category fields

Example:
    income = Income(source="Freelance Work", amount=1200.0, category="Extra")
"""

from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base


# Income Model
class Income(Base):
    __tablename__ = "incomes"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )  # Unique identifier

    source = Column(
        String,
        nullable=False
    )  # Income source (e.g., Salary, Freelance, Investment)

    amount = Column(
        Float,
        nullable=False
    )  # Amount received

    category = Column(
        String,
        nullable=False
    )  # Income category or type