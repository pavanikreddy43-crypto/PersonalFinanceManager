class Transaction:
    def __init__(self, transaction_type, amount, description):
        self.type = transaction_type
        self.amount = amount
        self.description = description

    def to_dict(self):
        return {
            "type": self.type,
            "amount": self.amount,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["type"],
            data["amount"],
            data["description"]
        )

    def __str__(self):
        return (
            f"Type: {self.type}\n"
            f"Amount: ₹{self.amount:.2f}\n"
            f"Description: {self.description}"
        )