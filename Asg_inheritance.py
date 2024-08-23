
class BankAccount:
    def __init__(self, account_holder, initial_balance):
        """Initialize the account holder's name and balance."""
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")

class SavingsAccount(BankAccount):
    def calculate_interest(self, rate):
        """Calculate and print the interest based on the current balance and specified interest rate."""
        interest = self.balance * (rate / 100)
        print(f"Interest at {rate}%: {interest}. Total balance after interest: {self.balance + interest}")


if __name__ == "__main__":
    
    savings_account = SavingsAccount("Ali", 1000) # Create an instance of SavingsAccount

    savings_account.deposit(500)  # Expected output: New balance: 1500
    savings_account.withdraw(200)  # Expected output: New balance: 1300
    savings_account.calculate_interest(5)  # Expected interest calculation and total balance after interest
