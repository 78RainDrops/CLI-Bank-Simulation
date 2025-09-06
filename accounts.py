
class Account:
    def __init__(self, account_num, name, pin, balance=0) -> None:
        self.account_num = account_num
        self.name = name
        self._pin = pin
        self._balance = balance


    def __str__(self) -> str:
        return f"Account Number: {self.account_num} | Account Name: {self.name} | Balance: {self.balance}"


    @property
    def pin(self):
        return self._pin


    @property
    def balance(self):
        return self._balance


    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount


    def to_dict(self):
        return {
            'Name' : self.name,
            'Pin' : self._pin,
            'Balance' : self.balance
        }


    @staticmethod
    def from_dict(user, info):
        return Account(user, info['Name'], info['Pin'], info['Balance'])


    def deposit(self, amount):
        self.balance += amount
        print("Deposit Successful")


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw Successful")


    def check_balance(self):
        return self.balance
