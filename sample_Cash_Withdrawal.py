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
        


def create_account():
    user_id = ""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    characters = letters + numbers
    create = input("Would you like to create an account today?").lower()
    if create == "y" or create == "yes":
        print("Initiating user creation process.")
        dots = (".", ".", ".")
        for i in dots: 
            time.sleep(1)
            print(i)
    
    name = input("Whats your name?")
    age = int(input("How old are you?"))
    balance = float(input("what is the starting balance of the account?"))
    counter = 1 
    while counter == 1:
        pin = int(input("What is your pin"))
        confirm = int(input("confirm pin pleas`e"))
        if pin == confirm: 
            counter += 1
    
    # Generate unique ID
    id_unique = False
    while not id_unique:
        user_id = ""
        for i in range(5):
            char = random.choice(characters)
            user_id += char
        # Check if ID already exists in users
        if user_id not in [user.user_id for user in users.values()]:
            id_unique = True
    
    return name, age, balance, user_id, pin

name, age, balance, user_id, pin = create_account()

user_unid = len(users) + 1
user_key = (f'user_{user_unid}')
new_user = User(name=name, age=age, balance=balance, account_pin=pin, user_id=user_id)
users[user_key] = new_user



        


    