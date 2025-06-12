
# 💸 Expense Tracker (Python · OOP Based)

A command-line Expense Tracker built using Python's Object-Oriented Programming concepts. This project allows users to track income and expenses, categorize transactions, and generate reports in multiple formats.

## 🚀 Features

- Add income and expenses
- Track current balance
- Categorize each transaction
- Generate transaction reports (Text / JSON)
- Save data to JSON file

## 🧠 OOP Concepts Used

- **Encapsulation**: Wallet balance protected and accessed via methods
- **Polymorphism**: Report generation supported in multiple formats
- **Abstraction**: User class abstracts internal Wallet mechanics
- **Inheritance-ready** design

## 🏗️ Class Overview

| Class        | Responsibility                                       |
|--------------|------------------------------------------------------|
| `Transaction`| Stores individual transaction data                  |
| `Wallet`     | Handles balance and transaction list                |
| `User`       | Interface to interact with the wallet               |
| `Category`   | Represents categories of income/expense (optional)  |

## 📂 File Structure

```bash
expense_tracker.py
README.md
transactions.json  # (Generated upon save)
```

## 🧪 Sample Usage

```python
user = User("Harshith")
user.add_income(1000, "Salary")
user.add_expense(200, "Groceries")
user.show_balance()
user.print_report('text')
user.wallet.save_to_file()
```

## 📦 Requirements

- Python 3.6+
- No external libraries (uses built-in `json`, `datetime`)

## 📜 Output Sample

```
2025-06-11T22:31:00 | INCOME | Rs.1000 | Salary
2025-06-11T22:32:00 | EXPENSE | Rs.200 | Groceries
```
