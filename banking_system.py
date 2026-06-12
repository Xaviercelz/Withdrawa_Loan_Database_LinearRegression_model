import time
import random

class Account:
    def __init__(self, name, age, balance, account_pin, user_id, creditscore):
        self.name = name
        self.age = age
        self.balance = balance
        self.account_pin = account_pin
        self.user_id = user_id 
        self.user_id = creditscore
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
    
    creditscore = random.randint(300,840)

    user = Account(pin, age, name, balance, user_id, creditscore)

    return user 

print(user)





### What is the current problem that I must solve?
## The current problem is that I have to create a system that assigns a random credit score that can't be less than 300 but more than 840.
# How would I do this?
# We need to grab the numbers for the numbers constant
# Make a loop that loops through this loop until you create a number that is >= 840 or <= 300
# After it does that assign it to creit score for that account is create.


# We also have to confirm that there isn't a user that has the same unique user id that is apart of that account aleady
user = create_account()

       
    



def withdrawal():
    pass

def deposit():
    pass

def loan():
    pass
