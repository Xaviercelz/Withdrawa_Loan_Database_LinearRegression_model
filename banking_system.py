import time
import random

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
        #for i in dots: 
         #   time.sleep(1)
          #  print(i)
    else:
        return "Fix this later"
    

    name = input("Whats your name?:")
    age = int(input("How old are you?: "))
    balance = float(input("what is the starting balance of the account?: "))
    counter = 1 
    while counter == 1:
        pin = int(input("What is your pin: "))
        confirm = int(input("confirm pin please: "))
        if pin == confirm: 
            counter += 1
        else:
            print("Pins don't match.")
    
    
    for i in range(5):
        chosen_char = random.choice(characters)
        user_id += chosen_char
    print(user_id)
    
    return pin, name, age, balance, user_id


print("Account created.")        
    



def withdrawal():
    pass

def deposit():
    pass

def loan():
    pass
