import json
import os
from datetime import datetime

# FIXED: Using all caps standard naming (consistent everywhere)
DATA_FILE = "expenses.json"

def load_data():
    """Load expenses from JSON file. Returns empty list if file doesn't exist."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(expenses):
    """Save expenses list to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(expenses):
    """Add a new expense with description, amount, and category."""
    desc = input("Description: ").strip()
    if not desc:
        print("❌ Sorry, description cannot be empty!")
        return

    try:
        amount = float(input("Amount: "))
        if amount <= 0:
            print("❌ Amount must be positive!")
            return
    except ValueError:
        print("❌ Enter a valid number!")
        return

    print("Categories: 1-Food  2-Transport  3-Shopping  4-Bills  5-Other")
    cat_choice = input("Choose category (1-5): ").strip()
    cat_map = {"1": "Food", "2": "Transport", "3": "Shopping", "4": "Bills", "5": "Other"}
    category = cat_map.get(cat_choice, "Other")

    expense = {
        "description": desc,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    expenses.append(expense)
    save_data(expenses)
    print(f"✅ Added: ${amount:.2f} for '{desc}' ({category})")

def view_all(expenses):
    """Display all expenses in a clean list."""
    if not expenses:
        print("📭 No expenses yet.")
        return
    print("\n📋 All Expenses:")
    print("-" * 50)
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['date']} | {e['description']} | ${e['amount']:.2f} | [{e['category']}]")
    print("-" * 50)

def view_totals(expenses):
    """Show totals broken down by category and grand total."""
    if not expenses:
        print("📭 No expenses yet.")
        return

    totals = {}
    for e in expenses:
        totals[e['category']] = totals.get(e['category'], 0) + e['amount']

    print("\n💰 Totals by Category:")
    print("-" * 30)
    for cat, total in totals.items():
        print(f"{cat}: ${total:.2f}")
    print(f"\n🏦 GRAND TOTAL: ${sum(e['amount'] for e in expenses):.2f}")
    print("-" * 30)

def main():
    """Main menu loop."""
    expenses = load_data()
    while True:
        print("\n" + "=" * 40)
        print("   💸 EXPENSE TRACKER")
        print("=" * 40)
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View totals by category")
        print("4. Exit")
        choice = input("Choose (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_all(expenses)
        elif choice == "3":
            view_totals(expenses)
        elif choice == "4":
            print("👋 Bye! Your data is saved.")
            break
        else:
            print("❌ Invalid choice. Pick 1-4.")

if __name__ == "__main__":
    main()