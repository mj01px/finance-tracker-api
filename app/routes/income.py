"""
Income routes

Responsibilities:
- Handles CRUD operations for income records
- Maps endpoints for creating, listing, and deleting incomes
- Uses SQLAlchemy ORM with Pydantic schemas for validation

Example:
    POST /incomes
    {
        "source": "Salary",
        "amount": 3500.0,
        "category": "Job"
    }
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.core.database import get_db
from app.schemas.income import IncomeCreate, IncomeOut
import app


# Router configuration
router = APIRouter(prefix="/incomes", tags=["Incomes"])


@router.post("/", response_model=schemas.income.IncomeOut)
def create_income(data: schemas.income.IncomeCreate, db: Session = Depends(get_db)):
    """
    Creates a new income record.

    Args:
        data (IncomeCreate): Validated Pydantic schema with income data.
        db (Session): Active SQLAlchemy session.

    Returns:
        IncomeOut: The created income object.
    """
    income = app.models.income.Income(**data.model_dump())  # Unpack schema into model
    db.add(income)
    db.commit()
    db.refresh(income)
    return income


@router.get("/", response_model=list[schemas.income.IncomeOut])
def list_incomes(db: Session = Depends(get_db)):
    """
    Returns a list of all income records.
    """
    return db.query(app.models.income.Income).all()


@router.delete("/{income_id}")
def delete_income(income_id: int, db: Session = Depends(get_db)):
    """
    Deletes an income by its ID.

    Returns:
        dict: A message confirming the deletion or not found.
    """
    income = db.query(app.models.income.Income).get(income_id)
    if not income:
        return {"message": "Income not found"}

    db.delete(income)
    db.commit()
    return {"message": "Income deleted"}