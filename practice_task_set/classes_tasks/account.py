class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough balance")


account = Account("Milana", 1000)

account.deposit(500)
print(account.balance)

account.withdraw(300)
print(account.balance)

account.withdraw(2000)
print(account.balance)
