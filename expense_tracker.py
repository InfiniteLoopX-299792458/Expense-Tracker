import json
import os
from datetime import datetime

from matplotlib import category

Data_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(Data_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(expenses):
    desc = input("Description:").strip()
    if not desc:
        print("❌ Sorry, description cannot be empty !")
        return

    try:
        amount = float(input("Amount: "))
        if amount <= 0:
            print("❌ Sorry, amount must be greater than zero !")
            return
    except ValueError:
        print("❌ Sorry, amount must be a number !")
        return

    print("Categories: 1-Food, 2-Transportation, 3-Entertainment, 4-Utilities, 5-Other")
    cat_choice = input("Choose a category (1-5): ").strip()
    cat_map = {
        "1": "Food",
        "2": "Transportation",
        "3": "Entertainment",
        "4": "Utilities",
        "5": "Other"
    }
    category = cat_map.get(cat_choice, "Other")

    expense = {
        "description": desc,
        "amount": amount,
        "catagory": category,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    expenses.append(expense)
    save_data(expenses)
    print(f"✅ Added: ${amount:.2f} for '{desc}' ({category})")

def view_all(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    print("\nAll Expenses:")
    print("-" * 50)
    for i, e in enumerate(expenses, 1):
        print(f"{e['date']} | {e['description']} | ${e['amount']:.2f} | [{e['category']}]")
    print("-" * 50)

def view_total(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    totals = {}
    for e in expenses:
        totals[e['category']] = totals.get(e['category'], 0) + e['amount']

    print("\nTotal Expenses by Category:")
    print("-" * 30)
    for cat, total in totals.items():
        print(f"{cat}: ${total:.2f}")
    print("-" * 30)

def main():
    expenses = load_data()
    while True:
        print("\n" + "="*40)
        print("Expense Tracker")
        print("="*40)
        print("1. Add expenses")
        print("2. View all expenses")
        print("3. View total expenses by category")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_all(expenses)
        elif choice == "3":
            view_total(expenses)
        elif choice == "4":
            print("Bye! Your data is saved.")
            break
        else:
            print("❌ Invalid choice. Please choose 1-4.")

if __name__ == "__main__":
    main()