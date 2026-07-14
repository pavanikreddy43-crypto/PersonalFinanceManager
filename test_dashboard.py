import unittest
import os

from dashboard import FinanceDashboard
from transaction import Transaction


class TestDashboard(unittest.TestCase):

    def setUp(self):
        self.dashboard = FinanceDashboard()
        self.dashboard.transactions = []

    def test_add_transaction(self):
        transaction = Transaction(
            "income",
            50000,
            "Salary"
        )

        self.dashboard.transactions.append(transaction)

        self.assertEqual(len(self.dashboard.transactions), 1)

    def test_delete_transaction(self):
        transaction = Transaction(
            "expense",
            1000,
            "Food"
        )

        self.dashboard.transactions.append(transaction)

        self.dashboard.transactions.pop(0)

        self.assertEqual(len(self.dashboard.transactions), 0)

    def test_dashboard_totals(self):
        self.dashboard.transactions = [
            Transaction("income", 50000, "Salary"),
            Transaction("income", 5000, "Freelancing"),
            Transaction("expense", 2000, "Food"),
            Transaction("expense", 1000, "Travel")
        ]

        income = sum(
            t.amount
            for t in self.dashboard.transactions
            if t.type == "income"
        )

        expense = sum(
            t.amount
            for t in self.dashboard.transactions
            if t.type == "expense"
        )

        balance = income - expense

        self.assertEqual(income, 55000)
        self.assertEqual(expense, 3000)
        self.assertEqual(balance, 52000)


if __name__ == "__main__":
    unittest.main()