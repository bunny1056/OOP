
import json
from datetime import datetime

class Transaction:
    def __init__(self, amount, category, txn_type, timestamp=None):
        self.amount = amount
        self.category = category
        self.txn_type = txn_type  # 'income' or 'expense'
        self.timestamp = timestamp if timestamp else datetime.now().isoformat()

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "type": self.txn_type,
            "timestamp": self.timestamp
        }

class Category:
    def __init__(self, name):
        self.name = name

class Wallet:
    def __init__(self):
        self.__balance = 0.0
        self.transactions = []

    def add_transaction(self, txn):
        if txn.txn_type == 'income':
            self.__balance += txn.amount
        elif txn.txn_type == 'expense':
            if txn.amount > self.__balance:
                raise ValueError("Insufficient balance")
            self.__balance -= txn.amount
        else:
            raise ValueError("Invalid transaction type")

        self.transactions.append(txn)

    def get_balance(self):
        return self.__balance

    def export_transactions(self, format='json'):
        if format == 'json':
            return json.dumps([txn.to_dict() for txn in self.transactions], indent=4)
        elif format == 'text':
            return "\n".join([f"{txn.timestamp} | {txn.txn_type.upper()} | Rs.{txn.amount} | {txn.category}" for txn in self.transactions])
        else:
            raise ValueError("Unsupported export format")

    def save_to_file(self, filename="transactions.json"):
        with open(filename, 'w') as f:
            f.write(self.export_transactions('json'))

class User:
    def __init__(self, name):
        self.name = name
        self.wallet = Wallet()

    def add_income(self, amount, category):
        txn = Transaction(amount, category, 'income')
        self.wallet.add_transaction(txn)

    def add_expense(self, amount, category):
        txn = Transaction(amount, category, 'expense')
        self.wallet.add_transaction(txn)

    def show_balance(self):
        print(f"Current Balance for {self.name}: Rs.{self.wallet.get_balance()}")

    def print_report(self, format='text'):
        print(self.wallet.export_transactions(format))

# Sample usage (uncomment to test):
# user = User("Harshith")
# user.add_income(1000, "Salary")
# user.add_expense(200, "Groceries")
# user.show_balance()
# user.print_report('text')
# user.wallet.save_to_file()
