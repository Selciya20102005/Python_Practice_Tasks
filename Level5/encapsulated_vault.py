class Vault:

    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def set_pin(self, new_pin):
        self.__pin = new_pin
        print("PIN changed successfully.")

    def check_balance(self, pin):
        if pin == self.__pin:
            print(f"Balance : ₹{self.__balance}")
        else:
            print("Access Denied!")

    def deposit(self, pin, amount):
        if pin == self.__pin:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Access Denied!")


vault = Vault(1234, 10000)

vault.check_balance(1234)

vault.deposit(1234, 5000)

vault.check_balance(1234)

vault.check_balance(1111)