"""_summary_
    landing page
"""
import accounts as acc

def main():
    while True:
        account_db = acc.load_account()
        print("otem")
        print('''\nWelcome to CLI Bank!
            1. Create Account
            2. Deposit
            3. Withdraw
            4. Check Balance 
            5. Exit''')
                
        operation_choice = int(input("Choose an option: "))
        if operation_choice == 1:
            acc.accounts(account_db)

        elif operation_choice == 2:
            acc.deposit(account_db)

        elif operation_choice == 3:
            acc.withdraw(account_db)

        elif operation_choice == 4:
            acc.check_balance(account_db)

        elif operation_choice == 5:
            print('Thank you for using CLI Bank')
            break
        else:
            print(f"Choice {operation_choice} is invalid.")

if __name__ == "__main__":
    main()