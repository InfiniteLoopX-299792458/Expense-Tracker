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
