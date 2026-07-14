import unittest

from transaction import Transaction


class TestTransaction(unittest.TestCase):

    def test_create_transaction(self):
        transaction = Transaction(
            "income",
            50000,
            "Salary"
        )

        self.assertEqual(transaction.type, "income")
        self.assertEqual(transaction.amount, 50000)
        self.assertEqual(transaction.description, "Salary")

    def test_to_dict(self):
        transaction = Transaction(
            "expense",
            1200,
            "Food"
        )

        expected = {
            "type": "expense",
            "amount": 1200,
            "description": "Food"
        }

        self.assertEqual(transaction.to_dict(), expected)

    def test_from_dict(self):
        data = {
            "type": "income",
            "amount": 35000,
            "description": "Freelancing"
        }

        transaction = Transaction.from_dict(data)

        self.assertEqual(transaction.type, "income")
        self.assertEqual(transaction.amount, 35000)
        self.assertEqual(transaction.description, "Freelancing")

    def test_str(self):
        transaction = Transaction(
            "expense",
            250,
            "Snacks"
        )

        expected = (
            "Type: expense\n"
            "Amount: ₹250.00\n"
            "Description: Snacks"
        )

        self.assertEqual(str(transaction), expected)


if __name__ == "__main__":
    unittest.main()