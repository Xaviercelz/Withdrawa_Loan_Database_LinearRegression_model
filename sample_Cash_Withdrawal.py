import time
import random
users = {}
class User:
    def __init__(self, name, age, balance, account_pin, user_id):
        self.name = name
        self.age = age
        self.balance = balance
        self.account_pin = account_pin
        self.user_id = user_id 

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
        for i in dots: 
            time.sleep(1)
            print(i)
    

    name = input("Whats your name?:")
    age = int(input("How old are you?: "))
    balance = float(input("what is the starting balance of the account?: "))
    counter = 1 
    while counter == 1:
        pin = int(input("What is your pin: "))
        confirm = int(input("confirm pin please: "))
        if pin == confirm: 
            counter += 1
            return pin
        else:
            print("Pins don't match.")
    
    
    for i in range(5):
        for char in characters:
            random.choice(characters)
            user_id += char



        
    return pin, name, age, balance, user_id



def withdrawal():
    pass

def deposit():
    pass

def loan():
    pass





def main_menu():
    choice = input(f'Welcome to bank of Xavier, what would you like to do today? \n1. Create Accoumt\n2. Withdrawal/Deposit\n3. Take a loan\n4. Exit')
    
    if choice == "1":
        create_account()
    if choice == "2":
        wd = input("Would you like to:\n1. Withdrawal\n2. Deposit")
        if wd == "1":
            withdrawal()
        if wd == "2":
            deposit()
    if choice == "3":
        loan()
    if choice == "4":
        print("Bye")
    
        


    # Creating an account
   # Empy user id which is the user id
   # Create inputs to get elements to fill the objects, and than pool the strings together

   #Confirm the pin and keep creating a pin and doing it until it matches

   # Now I have to create the account and put it inside of the dictionaries
   # Create the user than put it inside of the user dictionary, have a unique userID and the key is the user ID
    # The value is the account of the unique user ID so that It matches
main_menu()




        


    