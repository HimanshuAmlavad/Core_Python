class Account:

    def __init__(self):
        self.__balance = 0

    def set_balance(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount # we are directly adding data into main data, which can manipulate raw data
        b.set_balance(self.__balance)

    def withdrawn(self, amount):
        remaining_balance = self.get_balance() - amount # better approach, here main data is not included directly
        b.set_balance(remaining_balance)


b = Account()
print("Current balance in account: ", b.get_balance())

b.set_balance(1000)
print("setting balance: ", b.get_balance())

b.deposit(100)
print("Amount credit: 1000 current balance: ", b.get_balance())

b.withdrawn(200)
print("Amount debit: 200 current balance",b.get_balance())
