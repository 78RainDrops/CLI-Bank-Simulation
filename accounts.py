
class Account:
    def __init__(self, account_num, name, pin, balance=0) -> None:
        self.account_num = account_num
        self.name = name
        self.pin = pin
        self.balance = balance

    def display_info(self):
        print(f"Account Number: {self.account_num}")
        print(f"Account Name: {self.name}")
        print(f"Pin Number: {self.pin}")
        print(f"Balance: {self.balance}")
