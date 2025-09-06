import json

from accounts import Account

class BankSystem:
    def __init__(self, filename="accounts.json") -> None:
        self._accounts = {}
        self.filename = filename
        self.load_accounts()


    @property
    def accounts(self):
        return self._accounts['users']


    def add_account(self, acc_num, name,pin, balance=0):
        if acc_num in self.accounts:
            print("Account Number already in use.")
            return None

        account = Account(acc_num,name,pin,balance)
        self.accounts[acc_num] = account
        self.save_accounts()
        return account


    def login(self, acc_num, pin):
        account = self.accounts.get(acc_num)
        if account and account.pin == pin:
            print("Login Successfully")
            return account
        else:
            print("Login failed")
            return None


    def save_accounts(self):
        data = {
            'users' : {
                user: info.to_dict()
                for user, info in self.accounts.items()
            }
        }
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)


    def load_accounts(self):
        try:
            with open(self.filename) as f:
                data = json.load(f)
                self._accounts['users'] = {
                    user: Account.from_dict(user, info)
                    for user, info in data.get('users',{}).items()
                }
        except FileNotFoundError:
            pass


    def view_accounts(self):
        for contact in self.accounts.values():
            print(contact)

