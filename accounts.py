account_db = {}
def accounts(account_num, name, balance=0):
    account_info = {"name" : name, "balance" : balance}
    account_db[account_num] = account_info
    return account_db

def deposit(account_num, deposit):
    balance = account_db[account_num]['balance'] + deposit
    account_db[account_num]['balance'] = balance

    return account_db

def withdraw(account_num, withdraw):
    balance = account_db[account_num]['balance']
    if withdraw > balance:
        print("Not enough balance.")
        print(f"\nCurrent balance {balance}")
        return False
    balance -= withdraw

    account_db[account_num]['balance'] = balance

    return balance

def check_balance(account_num):
    return account_db[account_num]['balance']

def account_checker(account_num) -> bool:
    if account_num in account_db:
        return True
    else:
        return False
    
def save_account(accounts):
    pass