"""
Reports routes

Responsibilities:
- Provides endpoints for financial reporting and summaries
- Calculates total income, total expenses, and net balance
- Uses SQLAlchemy ORM and aggregate functions (SUM)

Example:
    GET /balance
    → {
        "income": 5000.0,
        "expense": 3200.0,
        "balance": 1800.0
      }
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import get_db
from app.models.income import Income
from app.models.expense import Expense


# Router configuration
router = APIRouter(prefix="", tags=["Reports"])


@router.get("/balance")
def get_balance(db: Session = Depends(get_db)):
    """
    Calculates the user's overall financial balance.

    Returns:
        dict: A summary with total income, total expense, and current balance.
    """
    # Aggregate total income and expenses; coalesce handles null sums as 0.0
    income_sum = db.query(func.coalesce(func.sum(Income.amount), 0.0)).scalar() or 0.0
    expense_sum = db.query(func.coalesce(func.sum(Expense.amount), 0.0)).scalar() or 0.0

    # Return summarized balance report
    return {
        "income": float(income_sum),
        "expense": float(expense_sum),
        "balance": float(income_sum - expense_sum)
    }