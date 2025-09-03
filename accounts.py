import csv
from pathlib import Path

path = Path('accounts.csv')
FIELDNAMES = ['Account Number','Name','Balance']

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
    
    account_info = {"Name" : name, "Balance" : balance}
    account_db[account_num] = account_info
    add_account(account_num,account_info)


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

    balance = account_db[account_num]['Balance'] + deposit
    account_db[account_num]['Balance'] = balance

    save_account(account_db)

    for k, v in account_db.items():
        if k == account_num:
            print(f'Account Name: {k}')
            for acc_key, acc_value in v.items():
                print(f"{acc_key.title()}: {acc_value}")


def withdraw(account_db):
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
            balance = account_db[account_num]['Balance']
                
            if withdraw > balance:
                print("Not enough balance.")
                print(f"\nCurrent balance {balance}")
                return

            balance -= withdraw
            account_db[account_num]['Balance'] = balance
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
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=['Account Number','Name','Balance'])
        writer.writeheader()
        for account_num, details in accounts.items():
            writer.writerow({
                    'Account Number': account_num,
                    'Name': details['Name'],
                    'Balance': details['Balance']
                })


def add_account(acc_number, details):
    with open(path, 'a',newline="") as f:
        writer = csv.DictWriter(f, fieldnames=['Account Number','Name','Balance'])
        writer.writerow({
            'Account Number' : acc_number,
            'Name' : details['Name'],
            'Balance' : details['Balance']
        })
    print('Account Successfully Created!')


def load_account():

    account_db = {}

    with path.open('r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            account_db[row['Account Number']] = {
                    'Name': row['Name'],
                    'Balance' : int(row['Balance'])
                }
            
    return account_db
