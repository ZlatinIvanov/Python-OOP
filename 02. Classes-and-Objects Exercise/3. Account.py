class Account:

    def __init__(self, id_number: int, name: str, balance = 0):
        self.id = id_number
        self.name = name
        self.balance = balance

    def credit(self, amount: int) -> int:
        self.balance += amount
        return f"{self.balance}"

    def debit(self, amount: int) -> str:
        if amount <= self.balance:
            self.balance -= amount
            return f"{self.balance}"
        return "Amount exceeded balance"

    def info(self) -> str:
        return f"User {self.name} with account {self.id} has {self.balance} balance"

# account = Account(5411256, "Peter")
# print(account.debit(500))
# print(account.credit(1000))
# print(account.debit(500))
# print(account.info())
