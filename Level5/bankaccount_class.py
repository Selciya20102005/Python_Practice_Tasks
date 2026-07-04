class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Rs{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds!")
        else:
            self.balance -= amount
            print(f"Rs{amount} withdrawn successfully.")

    def get_statement(self):
        
        print(f"Owner : {self.owner}")
        print(f"Balance : Rs{self.balance}")
account = BankAccount("John", 5000)

account.deposit(2000)
account.withdraw(1000)
account.withdraw(8000)

account.get_statement()