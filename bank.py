"""_summary_
    landing page
"""
from bank_system import BankSystem

def main():
    bank = BankSystem()
    while True:
        print('''\nWelcome to CLI Bank!
            1. Create Account
            2. Login
            3. Exit''')
                
        operation_choice = int(input("Choose an option: "))
        if operation_choice == 1:
            accounts(bank)
        elif operation_choice == 2:
            account = login(bank)
            if account:
                menu(account,bank)

        elif operation_choice == 3:
            break
        else:
            print(f"Invalid Choice.")

    """
    functions
    """
def accounts(bank):
    account_num = input("Enter account number: ")
    if not account_num.isdigit():
        print("Account Number can only be numeric")
        return False
    name = input("Enter name: ")

    if not name.strip():
        print("Name can't be empty")
        return False

    pin = input("Set pin: ")
    if not pin.isdigit():
        print("Pin can only be numberic")

    try:
        balance = int(input("Enter initial deposit: "))
        assert balance >= 0
    except AssertionError:
        print("\nCan't have a negative balance")
        return False

    bank.add_account(account_num,name,pin,balance)


def login(bank):
    acc_num = input("Enter account number: ")
    pin = input("Enter PIN: ")
    account = bank.login(acc_num, pin)
    
    return account

def menu(account,bank):
    while True:
        print(account)
        print('''
            ---Account Name---
            1. Deposit
            2. Withdraw
            3. Check Balance
            4. Logout
            ''')
        choice = input("Choose option: ")
        
        if choice == "1":
            amount = int(input("Amount: "))
            account.deposit(amount)
            bank.save_accounts()
        elif choice == "2":
            amount = int(input("Amount: "))
            account.withdraw(amount)
            bank.save_accounts()
        elif choice == "3":
            print(f"Balance: {account.check_balance()}")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()