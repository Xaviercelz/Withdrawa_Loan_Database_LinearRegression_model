import time
import random
import databse
import requests
from datetime import datetime

class Account:
    def __init__(self, name, age, balance, account_pin, user_id, creditscore, username):
        self.name = name
        self.age = age
        self.balance = balance
        self.account_pin = account_pin
        self.user_id = user_id 
        self.creditscore = creditscore
        self.username = username
# create the object for users and the dictionary


def create_account():
    user_id = ""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    characters = letters + numbers
    create = input("Would you like to create an account today?: ").lower()
    if create == "y" or create == "yes":
        print("Initiating user creation process.")
        dots = (".", ".", ".")
        #for i in dots: 
         #   time.sleep(1)
          #  print(i)
    else:
        return "Fix this later"
    

    name = input("Whats your name?:")
    
    while True:
        try:
            age = int(input("How old are you?: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for age.")
    
    while True:
        try:
            balance = float(input("what is the starting balance of the account?: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for balance.")
    
    counter = 1 
    while counter == 1:
        while True:
            try:
                pin = int(input("What is your pin: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for pin.")
        
        while True:
            try:
                confirm = int(input("confirm pin please: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for pin.")
        
        if pin == confirm: 
            counter += 1
        else:
            print("Pins don't match.")
    
    
    for i in range(5):
        chosen_char = random.choice(characters)
        user_id += chosen_char
    print(user_id)
    
    username_counter = 1
    while username_counter == 1:
        username = input("What username would you like?: ")
        username_confirm = input("Confirm your username: ")
        
        if username == username_confirm:
            username_counter += 1
        else:
            print("Usernames don't match. Try again.")
    
    creditscore = random.randint(300, 840)

    user = Account(name, age, balance, pin, user_id, creditscore, username)
    
    # Save account directly to database
    databse.save_account_to_database(user)
    
    print(f"\n--- Account Created Successfully ---")
    print(f"User ID: {user_id}")
    print(f"Username: {username}")
    print(f"Name: {name}")
    print(f"Credit Score: {creditscore}")
    print("-----------------------------------\n")

    return user


def view_all_accounts():
    """Display all accounts from the database indexed by user_id"""
    accounts = databse.get_all_accounts()
    
    if not accounts:
        print("No accounts in the database.")
        return
    
    print("\n--- All Accounts in Database ---")
    for account in accounts:
        user_id, username, name, balance, creditscore = account
        print(f"User ID: {user_id} | Username: {username} | Name: {name} | Balance: ${balance} | Credit Score: {creditscore}")
    print("---------------------------------\n")


def lookup_account(user_id):
    """Look up a specific account by user_id from the database"""
    account = databse.get_account_from_database(user_id)
    
    if account:
        user_id, username, name, age, balance, pin, creditscore = account
        print(f"\n--- Account Details for {user_id} ---")
        print(f"Username: {username}")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Balance: ${balance}")
        print(f"Credit Score: {creditscore}")
        print(f"User ID: {user_id}")
        print("-----------------------------------\n")
        return account
    else:
        return None


def withdrawal():
    """Withdrawal system with validation rules"""
    user_id = input("Enter your User ID: ")
    account_data = databse.get_account_from_database(user_id)
    
    if not account_data:
        print("Account not found.")
        return
    
    # Unpack account data from database
    user_id, username, name, age, balance, pin, creditscore = account_data
    
    # Display current balance
    print(f"\n--- Withdrawal ---")
    print(f"Current Balance: ${balance:.2f}")
    
    # Check if balance is positive or negative
    if balance < 0:
        print("Your account has a negative balance. You cannot make a withdrawal.")
        return
    
    # Check if there's at least $1 in the account
    if balance < 1:
        print("You need at least $1 in your account to make a withdrawal.")
        return
    
    # Ask how much they want to withdraw
    while True:
        try:
            withdrawal_amount = float(input(f"How much would you like to withdraw (up to ${balance:.2f})?: $"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    
    # Verify that funds in account >= withdrawal amount
    if withdrawal_amount > balance:
        print(f"Insufficient funds. You cannot withdraw ${withdrawal_amount:.2f}. Your balance is ${balance:.2f}")
        return
    
    if withdrawal_amount <= 0:
        print("Withdrawal amount must be greater than $0.")
        return
    
    # Update balance
    new_balance = balance - withdrawal_amount
    
    # Create updated account object and save to database
    account = Account(name, age, new_balance, pin, user_id, creditscore, username)
    databse.save_account_to_database(account)
    
    print(f"\nWithdrawal successful!")
    print(f"Withdrawn: ${withdrawal_amount:.2f}")
    print(f"New Balance: ${new_balance:.2f}\n")


def deposit():
    """Deposit system with $150k limit"""
    user_id = input("Enter your User ID: ")
    account_data = databse.get_account_from_database(user_id)
    
    if not account_data:
        print("Account not found.")
        return
    
    # Unpack account data from database
    user_id, username, name, age, balance, pin, creditscore = account_data
    
    # Display current balance
    print(f"\n--- Deposit ---")
    print(f"Current Balance: ${balance:.2f}")
    
    # Ask how much they want to deposit
    while True:
        try:
            deposit_amount = float(input("How much would you like to deposit?: $"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    
    # Check deposit limit ($150,000)
    if deposit_amount > 150000:
        print("Deposit amount cannot exceed $150,000.")
        return
    
    if deposit_amount <= 0:
        print("Deposit amount must be greater than $0.")
        return
    
    # Update balance
    new_balance = balance + deposit_amount
    
    # Create updated account object and save to database
    account = Account(name, age, new_balance, pin, user_id, creditscore, username)
    databse.save_account_to_database(account)
    
    print(f"\nDeposit successful!")
    print(f"Deposited: ${deposit_amount:.2f}")
    print(f"New Balance: ${new_balance:.2f}\n")


def get_prime_rate():
    """Fetch the federal reserve prime rate from FRED API"""
    try:
        api_key = "7044e9a20e41f6b38ab8cd1df51b9501"
        url = f"https://api.stlouisfed.org/fred/series/data?series_id=TERMCBCCALLNS&api_key={api_key}&file_type=json"
        
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        if data.get('observations'):
            latest_rate = float(data['observations'][-1]['value'])
            return latest_rate
        else:
            print("Could not fetch prime rate, using default 7.5%")
            return 7.5
    except Exception as e:
        print(f"Error fetching prime rate: {e}. Using default 7.5%")
        return 7.5


def calculate_interest_rate(credit_score, base_rate):
    """
    Calculate interest rate based on credit score.
    Lower credit score = higher rate
    Higher credit score = lower rate
    Credit score range: 300-840
    """
    score_range = 840 - 300  # 540
    normalized_score = (credit_score - 300) / score_range  # 0 to 1
    rate_multiplier = 2 - normalized_score  # 1.5 to 0.5
    
    adjusted_rate = base_rate * rate_multiplier
    return adjusted_rate


def loan():
    """Loan system with credit score-based interest rates"""
    user_id = input("Enter your User ID: ")
    account_data = databse.get_account_from_database(user_id)
    
    if not account_data:
        print("Account not found.")
        return
    
    user_id, username, name, age, balance, pin, creditscore = account_data
    
    if databse.user_has_active_loan(user_id):
        print("You already have an active loan. You can only have one loan at a time.")
        return
    
    print(f"\n--- Loan Application ---")
    print(f"Current Balance: ${balance:.2f}")
    print(f"Credit Score: {creditscore}")
    
    while True:
        try:
            loan_amount = float(input("How much would you like to borrow (max $150,000)?: $"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    
    if loan_amount > 150000:
        print("Maximum loan amount is $150,000.")
        return
    
    if loan_amount <= 0:
        print("Loan amount must be greater than $0.")
        return
    
    total_loaned = databse.get_total_loaned()
    available_credit = databse.BANK_CREDIT_LIMIT - total_loaned
    
    if loan_amount > available_credit:
        print(f"Bank has insufficient credit available. Maximum available: ${available_credit:,.2f}")
        return
    
    base_rate = get_prime_rate()
    interest_rate = calculate_interest_rate(creditscore, base_rate)
    
    fee_amount = loan_amount * 0.03
    
    if balance < fee_amount:
        print(f"Insufficient balance to cover the 3% loan fee (${fee_amount:.2f}). Current balance: ${balance:.2f}")
        return
    
    new_balance = balance - fee_amount + loan_amount
    total_owed = loan_amount + (loan_amount * interest_rate / 100)
    
    account = Account(name, age, new_balance, pin, user_id, creditscore, username)
    databse.save_account_to_database(account)
    
    loan_id = f"LOAN_{user_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    databse.save_loan_to_database(loan_id, user_id, loan_amount, interest_rate, fee_amount, total_owed)
    
    print(f"\n--- Loan Approved ---")
    print(f"Loan Amount: ${loan_amount:,.2f}")
    print(f"Base Rate (Prime): {base_rate:.2f}%")
    print(f"Your Interest Rate: {interest_rate:.2f}%")
    print(f"3% Loan Fee: ${fee_amount:.2f}")
    print(f"Total Amount Owed: ${total_owed:,.2f}")
    print(f"New Account Balance: ${new_balance:,.2f}")
    print("-----------------------------------\n")
