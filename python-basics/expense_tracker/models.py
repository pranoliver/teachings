"""Data models and helpers for the Smart Expense Tracker."""

from datetime import datetime


def next_id(items):
    """Return the next available integer ID for a list of dict items."""
    if not items:
        return 1
    return max(item["id"] for item in items) + 1


def make_expense(description, category, amount, date=None, expense_id=None, existing=None):
    """Create a validated expense dictionary.

    Parameters
    ----------
    description : str
        What the expense was for.
    category : str
        Budget category, e.g. "Food" or "Transport".
    amount : float or str
        Positive amount spent.
    date : str, optional
        ISO date string. Defaults to today.
    expense_id : int, optional
        Specific ID to use. Auto-generated if not supplied.
    existing : list, optional
        List of existing expenses used to auto-generate a new ID.
    """
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    return {
        "id": expense_id if expense_id is not None else next_id(existing or []),
        "date": date,
        "description": description,
        "category": category,
        "amount": round(float(amount), 2),
    }
