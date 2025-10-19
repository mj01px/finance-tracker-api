"""
Expense routes

Responsibilities:
- Handles CRUD operations for expenses
- Supports tag association (many-to-many via expense_tag)
- Automatically creates missing tags during expense creation
- Returns expense data including related tags

Example:
    POST /expenses
    {
        "description": "Groceries",
        "amount": 150.0,
        "category": "Food",
        "tags": ["Market", "Monthly"]
    }
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from app.core.database import get_db
from app.models.expense import Expense
from app.models.tag import Tag
from app.schemas.expense import ExpenseCreate, ExpenseOut
from pydantic import BaseModel


# Router configuration
router = APIRouter(prefix="/expenses", tags=["Expenses"])


# Pydantic model for delete confirmation response
class MessageOut(BaseModel):
    message: str
    id: int


@router.post("/", response_model=ExpenseOut, status_code=201)
def create_expense(payload: ExpenseCreate, db: Session = Depends(get_db)):
    """
    Creates a new expense record.
    - Inserts new expense with provided fields
    - Performs tag upsert (creates tags if they don't exist)
    - Establishes many-to-many relationships
    """
    # Create expense entity
    expense = Expense(
        description=payload.description,
        amount=payload.amount,
        category=payload.category,
    )

    # Normalize and deduplicate tag names
    tag_names = {t.strip() for t in payload.tags if t.strip()}
    if tag_names:
        # Fetch existing tags from DB
        existing_tags = db.query(Tag).filter(Tag.name.in_(tag_names)).all()
        existing_names = {t.name for t in existing_tags}

        # Create missing tags
        new_tags = [Tag(name=name) for name in tag_names - existing_names]
        for t in new_tags:
            db.add(t)

        # Flush to assign IDs to new tags (no commit yet)
        if new_tags:
            db.flush()

        # Attach both existing and new tags to the expense
        expense.tags.extend(existing_tags + new_tags)

    # Persist expense and its relationships
    db.add(expense)
    db.commit()
    db.refresh(expense)

    return expense


@router.get("/", response_model=list[ExpenseOut])
def list_expenses(db: Session = Depends(get_db)):
    """
    Returns all registered expenses including their tags.
    """
    items = db.query(Expense).options(joinedload(Expense.tags)).all()
    return items


@router.get("/{expense_id}", response_model=ExpenseOut)
def get_expense(expense_id: int, db: Session = Depends(get_db)):
    """
    Retrieves a single expense by its ID.
    Returns 404 if the expense does not exist.
    """
    expense = (
        db.query(Expense)
        .options(joinedload(Expense.tags))
        .filter(Expense.id == expense_id)
        .first()
    )

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    return expense


@router.delete("/{expense_id}", response_model=MessageOut, status_code=200)
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    """
    Deletes an expense by its ID.
    Returns a message confirming successful deletion.
    """
    exp = db.get(Expense, expense_id)
    if not exp:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(exp)
    db.commit()

    return {"message": "Expense deleted", "id": expense_id}