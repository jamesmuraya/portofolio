print("Script started")

class bankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount exceeds balance or is not positive.")

    def get_balance(self):
        return self.balance

# Example usage
account = bankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
print(f"Final balance: {account.get_balance()}")
input("Press Enter to exit...")