import json
from accounts import Account

class BankSystem:
    def __init__(self, filename="accounts.json") -> None:
        self.accounts = {"users":{}}
        self.filename = filename
        self.load_accounts()

    def add_account(self, acc_num, name,pin, balance=0):
        if str(acc_num) in self.accounts['users']:
            print("Account Number already in use.")
            return None

        self.accounts['users'][acc_num] = {
            'name' : name,
            'pin' : pin,
            'balance' : balance,
        }
        self.save_accounts()
        return Account(acc_num, name, pin, balance)


    def get_account(self, acc_num, pin):
        if acc_num in self.accounts["users"]:
            info = self.accounts["users"][acc_num]
            if info['pin'] == pin:
                print("Login Successfully")
                return Account(acc_num, info['name'], info['pin'],info['balance'])
            else:
                print("Incorrect Pin")
                return None
        else:
            return None


    def save_accounts(self):
        with open(self.filename, 'w') as f:
            json.dump(self.accounts, f, indent=4)


    def load_accounts(self):
        try:
            with open(self.filename) as f:
                self.accounts = json.load(f)
                # for acc_num, info in self.accounts['users'].items():
                #     account = Account(
                #         acc_num,
                #         info['name'],
                #         info['pin'],
                #         info['balance']
                #     )
                # print(json.dumps(data, indent=4))
        except FileNotFoundError:
            pass


bank = BankSystem()
acc = bank.add_account(1234, "ralph", 123, 50)
acc1 = bank.add_account(321, "lore", 111, 100)
login = bank.get_account("321",111)
if acc1:
    print(f"Check Balance: {acc1.check_balance()}")
