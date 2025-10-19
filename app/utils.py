"""
Utility functions for Finance Tracker

Responsibilities:
- Provides helper functions used across the application
- Handles financial calculations such as total balance

Example:
    balance = get_balance(db)
    print(balance)  # → net balance (incomes - expenses)
"""

from sqlalchemy.orm import Session
from app.models.expense import Expense
from app.models.income import Income


def get_balance(db: Session):
    """
    Calculates the user's total financial balance.

    Args:
        db (Session): Active SQLAlchemy session.

    Returns:
        float: Net balance (total incomes minus total expenses).
    """
    # Fetch all income and expense records
    total_income = db.query(Income).all()
    total_expense = db.query(Expense).all()

    # Compute sums for each category
    income_sum = sum(i.amount for i in total_income)
    expense_sum = sum(e.amount for e in total_expense)

    # Return the net result
    return income_sum - expense_sum