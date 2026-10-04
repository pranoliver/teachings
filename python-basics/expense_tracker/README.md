# Smart Expense Tracker

A complete, modular command-line expense tracker built as the capstone project for the **Python Fundamentals** tutorial.

## What it does

- Add, list, update, and delete expenses.
- Categorize expenses and set monthly budgets per category.
- Warn when spending reaches 80% of a budget and alert when it exceeds 100%.
- Show totals by category and overall spending.
- Export expenses to a CSV file.

## Files

```
expense_tracker/
├── __init__.py      # marks this folder as a Python package
├── main.py          # entry point and interactive menu loop
├── storage.py       # JSON load / save helpers
├── models.py        # expense data builders
├── operations.py    # business logic (add, list, update, delete, summarize)
└── reports.py       # CSV export and report helpers
```

## Run it

From inside this folder:

```bash
cd expense_tracker
python main.py
```

Or as a module from the `python-basics` directory:

```bash
python -m expense_tracker.main
```

## Data files

The tracker creates two JSON files in the directory where you run it:

- `expenses.json` — saved expenses.
- `budgets.json` — category budgets.

## Example session

```text
=== Smart Expense Tracker ===
1. Add expense
2. List expenses
...
Choose an option: 1
Description: Coffee
Category: Food
Amount: 4.50
Added expense #1: Coffee ($4.50) [Food]

Choose an option: 6

--- Spending Summary ---
Total spending: $4.50

By category:
  Food: $4.50
```

## Next steps

Try extending the tracker:

- Search expenses by keyword.
- Group spending by month.
- Import expenses from a CSV file.
- Add a simple text or `matplotlib` spending chart.
