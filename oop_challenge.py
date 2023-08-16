class Account:
    def __init__(self, owner, balance):
        self.owner = owner # string
        self.balance = balance # number with two decimal data
    def print(self):
        print("Account owner: {}".format(self.owner))
        print("Account balance: {}".format(self.balance))
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposit accepted. The balance now is: {}".format(self.balance))
    def withdraw(self, amount):
        if amount > self.balance:
            print("Funds Unavailable. The amount {} overpasses the balance: {}".format(amount, self.balance))
        else:
            self.balance = self.balance - amount
            print("Withdrawal accepted. The balance now is: {}".format(self.balance))


acct1 = Account('José', 100)
acct1.print()
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)