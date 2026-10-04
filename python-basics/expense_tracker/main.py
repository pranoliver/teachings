"""Entry point for the Smart Expense Tracker.

Run with:
    python -m expense_tracker.main

Or from the project directory:
    python main.py
"""

from expense_tracker.storage import load_json
from expense_tracker.operations import (
    add_expense,
    list_expenses,
    update_expense,
    delete_expense,
    summarize,
    set_budget,
    DATA_FILE,
    BUDGET_FILE,
)
from expense_tracker.reports import export_csv


def show_menu():
    print("\n=== Smart Expense Tracker ===")
    print("1. Add expense")
    print("2. List expenses")
    print("3. Update expense")
    print("4. Delete expense")
    print("5. Set category budget")
    print("6. Show summary")
    print("7. Export to CSV")
    print("8. Quit")


def get_input(prompt, required=True):
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
        print("This field is required.")


def main():
    expenses = load_json(DATA_FILE, [])
    budgets = load_json(BUDGET_FILE, {})

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            description = get_input("Description: ")
            category = get_input("Category: ")
            amount = get_input("Amount: ")
            add_expense(expenses, budgets, description, category, amount)

        elif choice == "2":
            category = input("Filter by category (press Enter for all): ").strip() or None
            list_expenses(expenses, category)

        elif choice == "3":
            try:
                expense_id = int(input("Expense ID to update: "))
            except ValueError:
                print("ID must be a number.")
                continue
            description = input("New description (press Enter to keep): ").strip() or None
            category = input("New category (press Enter to keep): ").strip() or None
            amount = input("New amount (press Enter to keep): ").strip() or None
            update_expense(
                expenses,
                expense_id,
                description=description,
                category=category,
                amount=amount,
            )

        elif choice == "4":
            try:
                expense_id = int(input("Expense ID to delete: "))
            except ValueError:
                print("ID must be a number.")
                continue
            delete_expense(expenses, expense_id)

        elif choice == "5":
            category = get_input("Category: ")
            amount = get_input("Budget amount: ")
            set_budget(budgets, category, amount)

        elif choice == "6":
            summarize(expenses, budgets)

        elif choice == "7":
            filename = input("Export filename (default report.csv): ").strip() or "report.csv"
            export_csv(expenses, filename)

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
