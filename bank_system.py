import json
from accounts import Account

class BankSystem:
    def __init__(self, filename="accounts.json") -> None:
        self.accounts = {}
        self.filename = filename
        self.load_accounts()

    def add_account(self, name, acc_num, pin, balance=0):
        acc = Account(acc_num, name, pin, balance)
        self.accounts['users'][acc_num] = {
            'name' : name,
            'pin' : pin,
            'balance' : balance,
        }
        self.save_accounts()
        return acc


    def save_accounts(self):
        with open(self.filename, 'w') as f:
            json.dump(self.accounts, f, indent=4)


    def load_accounts(self):
        try:
            with open(self.filename) as f:
                data = json.load(f)
                for acc_data in data['users']:
                    acc = Account(*acc_data)       
                self.accounts = data
                # print(json.dumps(data, indent=4))
        except FileNotFoundError:
            pass


bank = BankSystem()
acc = bank.add_account("ralph", 1234, 123, 50)
acc = bank.add_account("Lorence", 111, 321, 100)
acc = bank.add_account("Lorence", 112, 421, 400)