class BankAccount:
    def __init__(self):
        self.is_open = False
        self.initial_balance = 0

    def get_balance(self):
        if not self.is_open:
            raise ValueError("Transactions cannot be made because account is closed")
        return self.initial_balance

    def open(self):
        self.is_open = True

    def deposit(self, amount):
        if not self.is_open:
            raise ValueError("Transactions cannot be made because account is closed")
        if amount < 0:
            raise ValueError("Negative ammount is not money")

        self.initial_balance += amount
        return self.initial_balance

    def withdraw(self, amount):
        if not self.is_open:
            raise ValueError( "Transactions cannot be made because account is closed")
        if amount < 0:
            raise ValueError("amount can not be a negative")
        if amount > self.get_balance():
            raise ValueError("Negative ammount is not money")
        self.initial_balance -= amount
        return self.initial_balance

    def close(self):
        self.is_open = False
