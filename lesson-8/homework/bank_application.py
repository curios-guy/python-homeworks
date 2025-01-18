import json
import random
from farm import str_verifier, float_verifier

# unique id creator
def create_unique_int(start = 100, end = 999):

    try:
        with open("id_bank.txt", "r") as file:
            arr = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        arr = []

    unique_id = random.randint(start, end)

    # if id is existent in array unique_id will be regenerated
    while unique_id in arr:
        unique_id = random.randint(start, end)

    arr.append(unique_id)
    

    with open("id_bank.txt", "w") as file:
        json.dump(arr, file, indent=4)

    return unique_id

# verifying class for account holder
class Account():
    def __init__(self, account_number, name, balance):
        if str_verifier(name):
            raise ValueError(f"wrong value inputted: {name}")
        else: 
            self.name = name

        if float_verifier(balance):
            raise ValueError(f"wrong value entered: {balance}")
        else:
            self.balance = balance
            
        self.account_number = account_number

# bank class
class Bank():

    # creates account
    def create_account(self, name, initial_deposit):
        """gets name, initial_deposit and unique_id to create account """
        try:
            with open("accounts.txt", "r") as file:
                accounts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            accounts = {}

        account_holder = Account(create_unique_int(), name, initial_deposit)


        accounts[account_holder.account_number] = {
            "name": account_holder.name,
            "balance": account_holder.balance
        }

        
        with open("accounts.txt", "w") as file:
            json.dump(accounts, file, indent=4)

        print(f"\nAccount holder {account_holder.account_number} added successfully")

    # gets the account number and prints it if found
    def view_account(self, account_number):
        """gets the account number and prints it if found"""
        try:
            with open("accounts.txt", "r") as file:
                accounts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            accounts = {}

        if str(account_number) in accounts:
            print("\nUser found")
            return print(f"\nAccount information:\n\tID: {account_number}\n\tName: {accounts[str(account_number)]["name"]}\n\tBalance: {accounts[str(account_number)]["balance"]} dollars")
        else:
            print("\nUser not found")

    # deposit money
    def deposit_money(self, account_number, amount):
        """gets the account number and adds amount to balance if found"""
        try:
            with open("accounts.txt", "r") as file:
                accounts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            accounts = {}

        if str(account_number) in accounts:
            print("\nUser found!!!")
            if amount < 0  or amount == 0:
                print("You can't do that")
            else:
                accounts[str(account_number)]["balance"] += amount
                print(f"{amount} dollars added to account {account_number}")
        else: 
            print("\nError: User not found")
            return

        with open("accounts.txt", "w") as file:
            json.dump(accounts, file, indent=4)
        
    def withdraw_money(self, account_number, amount):
        """withdraws certain amount of money from the account if found"""
        try:
            with open("accounts.txt", "r") as file:
                accounts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            accounts = {}

        if str(account_number) in accounts:
            print("\nUser found!!!")
            if amount >= accounts[str(account_number)]["balance"]:
                print("Error: Insufficient balance")
            elif amount < 0 or amount == 0: 
                print("You can't do that")
            else:
                accounts[str(account_number)]["balance"] -= amount
                print(f"{amount} dollars withdrawn from account {account_number}")
        else: 
            print("\nError: User not found")
            return

        with open("accounts.txt", "w") as file:
            json.dump(accounts, file, indent=4)

banker = Bank()

# main control menu
while True:
    main_input = int(input("\nWelcome to our bank, what do you want?\n1. Create Account\n2. View your Account\n3. Deposit money\n4. Withdraw money\n5. Quit\nChoose wisely: "))

    if main_input in [1,2,3,4,5]:
        if main_input == 1:
            name = input("Your name: ")
            deposit = int(input("How much you want to deposit: "))
            banker.create_account(name, deposit)

        elif main_input == 2:
            account_number = int(input("Your acount number: "))
            banker.view_account(account_number)

        elif main_input == 3:
            account_number = int(input("Your acount number: "))
            amount = int(input("How much you want to deposit: "))
            banker.deposit_money(account_number, amount)

        elif main_input == 4:
            account_number = int(input("Your acount number: "))
            amount = int(input("How much you want to withdraw: "))
            banker.withdraw_money(account_number, amount)

        elif main_input == 5:
            print("Thanks for choosing us.")
            break
    else: print("Please choose from main menu")



        