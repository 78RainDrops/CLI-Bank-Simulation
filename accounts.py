from pathlib import Path

path = Path('cli_bank_simulation/accounts.txt')

def accounts(account_db): #done
    account_num = input("Enter account number: ")
    if account_num in account_db:
        print("Account number is already taken")
        return
    
    name = input("Enter name: ")

    while True:
        try:
            balance = int(input("Enter initial deposit: "))
            assert balance >= 0
        except AssertionError:
            print("\nCan't have a negative balance")
        else:
            break
    
    account_info = {"name" : name, "balance" : balance}
    account_db[account_num] = account_info
    save_account(account_db)


def deposit(account_db):#done
    account_num = input("Enter account number: ")
    if account_num not in account_db:
        print("Account don't exist")
        return

    while True:
        try:
            deposit = int(input("Enter amount to deposit: "))
            assert deposit >= 0
        except AssertionError:
            print("\nCan't Deposti negative number")
        else:
            break

    balance = account_db[account_num]['balance'] + deposit
    account_db[account_num]['balance'] = balance

    save_account(account_db)

    for k, v in account_db.items():
        if k == account_num:
            print(f'Account Name: {k}')
            for acc_key, acc_value in v.items():
                print(f"{acc_key.title()}: {acc_value}")


def withdraw(account_db):
    while True:
        account_num = input("Enter account number: ")
        if account_num not in account_db:
            print("Account don't exist")
            return

        while True:
            try:
                withdraw = int(input("Enter amount to withdraw: "))
                assert withdraw >= 0
            except AssertionError:
                print("\nCan't Deposti negative number")
            else:
                balance = account_db[account_num]['balance']
                
                if withdraw > balance:
                    print("Not enough balance.")
                    print(f"\nCurrent balance {balance}")
                    return

                balance -= withdraw
                account_db[account_num]['balance'] = balance
                break
        save_account(account_db)
        
        for k, v in account_db.items():
            if k == account_num:
                print(f'Account Name: {k}')
                for acc_key, acc_value in v.items():
                    print(f"{acc_key.title()}: {acc_value}")


def check_balance(account_db):
    while True:
        account_num = input("Enter account number: ")
        if account_num not in account_db:
            print("Account don't exist")
            return
            
        for k, v in account_db.items():
            if k == account_num:
                print(f'Account Name: {k}')
                for acc_key, acc_value in v.items():
                    print(f"{acc_key.title()}: {acc_value}")
        break
    return 


def save_account(accounts):
    with open(path, "w") as f:
        for account_num, details in accounts.items():
            line = f"{account_num}, {details['name']}, {details['balance']}\n"
            f.write(line)


def load_account():

    account_db = {}

    with path.open('r') as f:
        for line in f:
            acc_num, name, balance = line.rstrip().split(',')
            account_db[acc_num] = {
                'name' : name,
                'balance' : int(balance),
            }

    return account_db
