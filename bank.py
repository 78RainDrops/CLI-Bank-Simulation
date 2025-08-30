"""_summary_
    landing page
"""
import accounts as acc

def main():
    while True:
        print('''\nWelcome to CLI Bank!
            1. Create Account
            2. Deposit
            3. Withdraw
            4. Check Balance 
            5. Exit''')
                
        operation_choice = int(input("Choose an option: "))
        if operation_choice == 1:
            while True:
                account_num = int(input("Enter account number: "))
                if not acc.account_checker(account_num):
                    break
                else: 
                    print("Account number is already taken")

            name = input("Enter name: ")

            while True:
                try:
                    balance = int(input("Enter initial deposit: "))
                    assert balance >= 0
                except AssertionError:
                    print("\nCan't have a negative balance")
                else:
                    break
            current_account = acc.accounts(account_num,name,balance)
            print(current_account)

        elif operation_choice == 2:
            while True:
                account_num = int(input("Enter account number: "))
                if acc.account_checker(account_num):
                    break
                else: 
                    print("Account don't exist")

            while True:
                try:
                    deposit = int(input("Enter amount to deposit: "))
                    assert deposit >= 0
                except AssertionError:
                    print("\nCan't Deposti negative number")
                else:
                    break

            current_account = acc.deposit(account_num,deposit)
            print(current_account)

        elif operation_choice == 3:
            while True:
                account_num = int(input("Enter account number: "))
                if acc.account_checker(account_num):
                    break
                else: 
                    print("Account don't exist")

            while True:
                try:
                    withdraw = int(input("\nEnter amount to withdraw: "))
                    assert withdraw >= 0
                except AssertionError:
                    print("\nCan't Deposti negative number")
                else:
                    current_balance = acc.withdraw(account_num,withdraw)
                    if current_balance != False:
                        print(f"New balance: {current_balance}")
                        break

        elif operation_choice == 4:
            while True:
                account_num = int(input("Enter account number: "))
                if acc.account_checker(account_num):
                    break
                else: 
                    print("Account don't exist")

            current_balance = acc.check_balance(account_num)
            print(f"Current Balance: {current_balance}")

        elif operation_choice == 4:
            print('Thank you for using CLI Bank')
            break
        else:
            print(f"Choice {operation_choice} is invalid.")

main()