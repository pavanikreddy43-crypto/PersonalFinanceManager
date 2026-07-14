import re


def display_menu():
    print("\n" + "=" * 35)
    print("      Personal Finance Manager")
    print("=" * 35)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Dashboard")
    print("5. Edit Transaction")
    print("6. Delete Transaction")
    print("7. Exit")


def get_valid_amount():
    while True:
        try:
            amount = float(input("Amount: ₹"))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")


def get_valid_description(prompt):
    while True:
        description = input(prompt).strip()

        if not description:
            print("Description cannot be empty.")
            continue

        if not re.fullmatch(r"[A-Za-z ]{2,30}", description):
            print("Use only letters and spaces (2-30 characters).")
            continue

        return description