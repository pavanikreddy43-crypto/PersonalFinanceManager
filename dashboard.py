import json

from transaction import Transaction
from utils import (display_menu,get_valid_amount,get_valid_description,)


class FinanceDashboard:

    def __init__(self):
        self.transactions = self.load_transactions()

    def load_transactions(self):
        try:
            with open("transactions.json", "r") as file:
                data = json.load(file)
                return [Transaction.from_dict(item) for item in data]

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            return []

    def save_transactions(self):
        with open("transactions.json", "w") as file:
            json.dump(
                [transaction.to_dict() for transaction in self.transactions],
                file,
                indent=4
            )
    
    def add_income(self):
        amount = get_valid_amount()
        description = get_valid_description("Income Source: ")

        transaction = Transaction(
            "income",
            amount,
            description
        )

        self.transactions.append(transaction)
        self.save_transactions()

        print("\nIncome added successfully!")


    def add_expense(self):
        amount = get_valid_amount()
        description = get_valid_description("Expense Category: ")

        transaction = Transaction(
            "expense",
            amount,
            description
        )

        self.transactions.append(transaction)
        self.save_transactions()

        print("\nExpense added successfully!")

    def display_transaction_list(self):
        if not self.transactions:
            print("\nNo transactions found.")
            return

        print("\nTransactions")
        print("-" * 40)

        for i, transaction in enumerate(self.transactions, start=1):
            print(f"{i}.")
            print(transaction)
            print("-" * 40)


    def view_transactions(self):
        self.display_transaction_list()


    def select_transaction(self):
        if not self.transactions:
            print("\nNo transactions found.")
            return None

        self.display_transaction_list()

        while True:
            try:
                choice = int(input("Select transaction number: "))

                if 1 <= choice <= len(self.transactions):
                    return choice - 1

                print("Invalid transaction number.")

            except ValueError:
                print("Please enter a valid number.")
    def edit_transaction(self):
        index = self.select_transaction()

        if index is None:
            return

        transaction = self.transactions[index]

        print("\nEditing Transaction")

        transaction.amount = get_valid_amount()

        if transaction.type == "income":
            transaction.description = get_valid_description("Income Source: ")
        else:
            transaction.description = get_valid_description("Expense Category: ")

        self.save_transactions()

        print("Transaction updated successfully!")

    def delete_transaction(self):
        index = self.select_transaction()

        if index is None:
            return

        deleted = self.transactions.pop(index)

        self.save_transactions()

        print(f"\nDeleted: {deleted}")

    def view_dashboard(self):
        total_income = sum(
            transaction.amount
            for transaction in self.transactions
            if transaction.type == "income"
        )

        total_expense = sum(
            transaction.amount
            for transaction in self.transactions
            if transaction.type == "expense"
        )

        balance = total_income - total_expense

        print("\n===== Dashboard =====")
        print(f"Total Income      : ₹{total_income:.2f}")
        print(f"Total Expense     : ₹{total_expense:.2f}")
        print(f"Current Balance   : ₹{balance:.2f}")
        print(f"Transactions      : {len(self.transactions)}")

    def run(self):
        while True:
            display_menu()

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if choice == 1:
                self.add_income()

            elif choice == 2:
                self.add_expense()

            elif choice == 3:
                self.view_transactions()

            elif choice == 4:
                self.view_dashboard()

            elif choice == 5:
                self.edit_transaction()

            elif choice == 6:
                self.delete_transaction()

            elif choice == 7:
                print("\nThank you for using Personal Finance Manager!")
                break

            else:
                print("Invalid choice. Please try again.")