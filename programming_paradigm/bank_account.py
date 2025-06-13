
class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balane += amount
        print(f"Deposited: ${self.account_balance:.2f}")

    def withdraw(self, amount):

        # if insufficient funds, return false
        if amount > self.account_balance:
            return False
        
        # deduct amount if funds are sufficient
        else:
            self.account_balance -= amount
            return True


    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")