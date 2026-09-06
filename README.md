# 💰 Terminal Expense Tracker

A command-line interface (CLI) application built in Python that helps users record, categorize, track, and analyze personal expenses. Designed for simplicity and speed, the tracker stores data locally using JSON format, ensuring persistent records between sessions without requiring complex database setups.

---

## 📋 Table of Contents

1. [Overview](#-overview)
2. [Key Features](#-key-features)
3. [Architecture & How It Works](#-architecture--how-it-works)
4. [Prerequisites](#-prerequisites)
5. [Installation & Setup](#-installation--setup)
6. [Usage Guide](#-usage-guide)
   - [Adding an Expense](#1-adding-an-expense)
   - [Viewing All Expenses](#2-viewing-all-expenses)
   - [Categorized Summaries](#3-viewing-totals-by-category)
7. [Data Storage Format](#-data-storage-format)
8. [Error Handling & Input Validation](#-error-handling--input-validation)
9. [Future Roadmap](#-future-roadmap)
10. [License](#-license)

---

## 🎯 Overview

Managing day-to-day spending should be effortless. The **Terminal Expense Tracker** provides a lightweight, distraction-free environment to log purchases instantly from your command prompt or terminal. It automatically timestamps every transaction and presents clear financial summaries broken down by spending categories.

Whether you want to track daily coffee runs, utility bills, or monthly entertainment budgets, this tool keeps your data local, transparent, and easy to inspect.

---

## ✨ Key Features

- **Interactive CLI Menu:** Intuitive text-based interface with simple numeric choices.
- **Robust Validation:** Prevents blank descriptions, invalid characters, zero amounts, or negative numbers.
- **Categorization Engine:** Built-in category selection mapping (Food, Transportation, Entertainment, Utilities, Other).
- **Automated Timestamps:** Records exact dates and times (`YYYY-MM-DD HH:MM`) for every transaction using Python's standard `datetime` module.
- **Persistent Local Storage:** Saves transactions automatically to `expenses.json` so your data persists across restarts.
- **Financial Insights:** Real-time summary views calculating total expenditure per category.

---

## 🏗️ Architecture & How It Works

The project is structured within a modular, single-file Python script (`expense_tracker.py`):

- **`load_expenses()`**: Checks for the existence of `expenses.json`. If present, reads and parses the JSON array; otherwise, initializes a fresh list.
- **`save_data(expenses)`**: Serializes the current Python dictionary structure into human-readable, formatted JSON back to disk.
- **`add_expense(expenses)`**: Handles interactive prompts for description, numeric validation for amounts, category mapping, and appending formatted records.
- **`view_all(expenses)`**: Formats stored records into a clean, tabulated terminal list.
- **`view_total(expenses)`**: Aggregates expenditure totals per category using hash maps (dictionaries).
- **`main()`**: The event loop driving menu selection and program state execution.

---

## 💻 Prerequisites

This application runs natively on any system supporting Python 3:

* **Python version:** `Python 3.6` or higher
* **Dependencies:** None! Built strictly with Python Standard Library packages (`json`, `os`, `datetime`).

---

## 🚀 Installation & Setup

### Step 1: Clone the Repository

Clone this repository to your local machine using `git`:

```bash
git clone [https://github.com/infiniteLoopx-299792458/Expense-Tracker.git](https://github.com/infiniteLoopx-299792458/Expense-Tracker.git)
cd Expense-Tracker
