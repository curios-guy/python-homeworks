accounts = {}

def create_account(account_number, owner, balance = 0):
    """Creates a new account with the given details"""
    accounts[account_number] = {"owner": owner, "balance": balance}

def deposit(account_number, amount):
    """Deposit money into the account"""
    accounts[account_number]["balance"] += amount

def withdraw(account_number, amount):
    """Withdraws money from given account if there is sufficient balance available"""
    if accounts[account_number]["balance"] >= amount:
        accounts[account_number]["balance"] -= amount
        return True
    return False

def get_balance(account_number):
    """Gets information about given account number"""
    return accounts[account_number]["balance"]

# Example usage
create_account(213421, "Alicia", 200000000)
# create_account(987865, "Gabriel", 150000000)

print(accounts)

print(f"Alicia has {get_balance(213421)} dollars in her bank account")
withdraw(213421, 19000000)
deposit(213421, 5000000000000000000000)
print("Alicia found infinite money glitch, DAMNNN")

print(accounts)
