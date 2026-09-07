import json
import os
from datetime import datetime
import streamlit as st
import pandas as pd

DATA_FILE = "expenses.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

if "expenses" not in st.session_state:
    st.session_state.expenses = load_data()

st.set_page_config(page_title="Expense Tracker", page_icon="💸")
st.title("💸 Expense Tracker")

tab1, tab2, tab3 = st.tabs(["➕ Add Expense", "📋 All Expenses", "💰 Totals"])

# ---- Add Expense ----
with tab1:
    st.subheader("Add a new expense")
    desc = st.text_input("Description")
    amount = st.number_input("Amount", min_value=0.0, step=1.0)
    category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Other"])

    if st.button("Add Expense"):
        if not desc.strip():
            st.error("❌ Description cannot be empty!")
        elif amount <= 0:
            st.error("❌ Amount must be positive!")
        else:
            expense = {
                "description": desc.strip(),
                "amount": amount,
                "category": category,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            st.session_state.expenses.append(expense)
            save_data(st.session_state.expenses)
            st.success(f"✅ Added: ${amount:.2f} for '{desc}' ({category})")

# ---- View All ----
with tab2:
    st.subheader("All Expenses")
    if not st.session_state.expenses:
        st.info("📭 No expenses yet.")
    else:
        df = pd.DataFrame(st.session_state.expenses)
        st.dataframe(df, use_container_width=True)

# ---- Totals ----
with tab3:
    st.subheader("Totals by Category")
    if not st.session_state.expenses:
        st.info("📭 No expenses yet.")
    else:
        df = pd.DataFrame(st.session_state.expenses)
        totals = df.groupby("category")["amount"].sum()
        st.bar_chart(totals)
        for cat, total in totals.items():
            st.write(f"**{cat}:** ${total:.2f}")
        st.write(f"### 🏦 Grand Total: ${df['amount'].sum():.2f}")