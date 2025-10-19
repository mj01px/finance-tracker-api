"""
Expense model definition

Responsibilities:
- Defines ORM models for Expense and many-to-many relationship with Tag
- Maps to PostgreSQL tables using SQLAlchemy ORM
- Uses association table `expense_tag` to link expenses ↔ tags

Example:
    expense = Expense(description="Groceries", amount=150.0, category="Food")
    expense.tags = [Tag(name="Market"), Tag(name="Monthly")]
"""

from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


# Association Table (Many-to-Many: Expense ↔ Tag)
expense_tag_table = Table(
    "expense_tag",
    Base.metadata,
    Column("expense_id", ForeignKey("expenses.id"), primary_key=True),  # FK to Expense
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),          # FK to Tag
)


# Expense Model
class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)     # Unique identifier
    description = Column(String, nullable=False)           # Expense description
    amount = Column(Float, nullable=False)                 # Expense amount
    category = Column(String, nullable=False)              # Expense category

    # Many-to-many relationship with Tag via expense_tag_table
    tags = relationship("Tag", secondary=expense_tag_table, backref="expenses")