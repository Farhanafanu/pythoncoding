class Bank:
    def __init__(self, accountno, balance):
        self.accountno = accountno
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("You don't have sufficient balance to retrieve cash.")
        else:
            self.balance -= amount
            print(self.balance)


b = Bank("5", 500)
# print("Account details:", b.accountno, b.balance)

b.withdraw(100)
b.withdraw(600)
