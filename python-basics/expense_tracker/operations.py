"""Core business operations for the Smart Expense Tracker."""

from collections import defaultdict
from expense_tracker.storage import save_json
from expense_tracker.models import make_expense


DATA_FILE = "expenses.json"
BUDGET_FILE = "budgets.json"


def _to_positive_float(value):
    """Convert *value* to a positive float, raising ValueError otherwise."""
    amount = float(value)
    if amount <= 0:
        raise ValueError("Amount must be positive")
    return amount


def add_expense(expenses, budgets, description, category, amount):
    """Add a new expense and persist it, then show budget warnings if any."""
    try:
        amount = _to_positive_float(amount)
    except ValueError as e:
        print(f"Invalid amount: {e}")
        return

    expense = make_expense(description, category, amount, existing=expenses)
    expenses.append(expense)
    save_json(DATA_FILE, expenses)

    budget = budgets.get(category)
    if budget:
        spent = sum(e["amount"] for e in expenses if e["category"] == category)
        percent = spent / budget * 100
        if spent > budget:
            print(f"⚠️  Over budget for {category}! Spent ${spent:.2f} / ${budget:.2f}")
        elif percent >= 80:
            print(f"⚠️  You have used {percent:.1f}% of your {category} budget.")

    print(f"Added expense #{expense['id']}: {description} (${amount:.2f}) [{category}]")


def list_expenses(expenses, category=None):
    """Print expenses as a table, optionally filtered by category."""
    filtered = [e for e in expenses if category is None or e["category"] == category]
    if not filtered:
        print("No expenses found.")
        return

    print(f"\n{'ID':<5}{'Date':<12}{'Category':<15}{'Description':<25}{'Amount':<10}")
    print("-" * 70)
    for e in filtered:
        print(f"{e['id']:<5}{e['date']:<12}{e['category']:<15}{e['description']:<25}${e['amount']:<9.2f}")
    print("-" * 70)
    print(f"Total: ${sum(e['amount'] for e in filtered):.2f}\n")


def update_expense(expenses, expense_id, **changes):
    """Update one or more fields of the expense with the given ID."""
    for e in expenses:
        if e["id"] == expense_id:
            for key, value in changes.items():
                if value is None:
                    continue
                if key == "amount":
                    value = _to_positive_float(value)
                e[key] = value
            save_json(DATA_FILE, expenses)
            print(f"Updated expense #{expense_id}")
            return
    print(f"Expense #{expense_id} not found.")


def delete_expense(expenses, expense_id):
    """Remove the expense with the given ID if it exists."""
    original_len = len(expenses)
    expenses[:] = [e for e in expenses if e["id"] != expense_id]
    if len(expenses) < original_len:
        save_json(DATA_FILE, expenses)
        print(f"Deleted expense #{expense_id}")
    else:
        print(f"Expense #{expense_id} not found.")


def summarize(expenses, budgets):
    """Show total spending, category totals, and remaining budgets."""
    if not expenses:
        print("No expenses to summarize.")
        return

    print("\n--- Spending Summary ---")
    total = sum(e["amount"] for e in expenses)
    print(f"Total spending: ${total:.2f}")

    by_category = defaultdict(float)
    for e in expenses:
        by_category[e["category"]] += e["amount"]

    print("\nBy category:")
    for category, spent in sorted(by_category.items()):
        budget = budgets.get(category)
        line = f"  {category}: ${spent:.2f}"
        if budget is not None:
            remaining = budget - spent
            line += f" (budget ${budget:.2f}, remaining ${remaining:.2f})"
        print(line)
    print()


def set_budget(budgets, category, amount):
    """Set a monthly budget for a category and persist it."""
    try:
        amount = _to_positive_float(amount)
    except ValueError:
        print("Budget must be a positive number.")
        return
    budgets[category] = round(amount, 2)
    save_json(BUDGET_FILE, budgets)
    print(f"Budget for {category} set to ${amount:.2f}")
