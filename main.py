import banking_system
import banking_system




def main_menu():
    choice = input(f"""Welcome to bank of Xavier, what would you like to do today? \n1. Create Accoumt\n
                   2. Withdrawal/Deposit\n3. Take a loan\n4. Account maintenance\n 5.Quit""")
    
    if choice == "1":
        banking_system.create_account()
    if choice == "2":
        wd = input("Would you like to:\n1. Withdrawal\n2. Deposit")
        if wd == "1":
            banking_system.withdrawal()
        if wd == "2":
            banking_system.deposit()
    if choice == "3":
        banking_system.loan()
    if choice == "4":
        print("Bye")

main_menu()


def save_account(user):
    pass