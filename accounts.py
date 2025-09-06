
class Account:
    def __init__(self, account_num:str, name, pin, balance=0) -> None:
        self.account_num = str(account_num)
        self.name = name
        self.pin = pin
        self._balance = balance

    def __repr__(self):
        return f"Account({self.account_num}, {self.name}, Balance={self.balance})"

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def check_balance(self):
        return self.balance