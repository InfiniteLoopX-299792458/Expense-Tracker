import json
import os
from datetime import datetime

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