"""Report generators for the Smart Expense Tracker."""

import csv


def export_csv(expenses, filename="report.csv"):
    """Export *expenses* to a CSV file with the given *filename*."""
    if not expenses:
        print("No expenses to export.")
        return
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["id", "date", "category", "description", "amount"]
        )
        writer.writeheader()
        writer.writerows(expenses)
    print(f"Exported {len(expenses)} expenses to {filename}")


def monthly_summary(expenses):
    """Return a dictionary of {month: total} for all expenses."""
    totals = {}
    for e in expenses:
        month = e["date"][:7]  # YYYY-MM
        totals[month] = totals.get(month, 0.0) + e["amount"]
    return totals
