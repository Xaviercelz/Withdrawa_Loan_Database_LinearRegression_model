import banking_system
import databse


def main_menu():
    while True:
        choice = input(f"""Welcome to bank of Xavier, what would you like to do today? 
1. Create Account
2. Withdrawal/Deposit
3. Take a loan
4. Account maintenance
5. View All Accounts
6. Look up Account by User ID
7. Quit
Choose an option: """)
        
        if choice == "1":
            new_account = banking_system.create_account()
        elif choice == "2":
            wd = input("Would you like to:\n1. Withdrawal\n2. Deposit\nChoose: ")
            if wd == "1":
                banking_system.withdrawal()
            elif wd == "2":
                banking_system.deposit()
        elif choice == "3":
            banking_system.loan()
        elif choice == "4":
            print("Account maintenance menu")
        elif choice == "5":
            banking_system.view_all_accounts()
        elif choice == "6":
            user_id = input("Enter the User ID to look up: ")
            banking_system.lookup_account(user_id)
        elif choice == "7":
            print("Thank you for using Bank of Xavier. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main_menu()