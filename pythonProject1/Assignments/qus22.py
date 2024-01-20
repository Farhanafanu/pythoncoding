class BankAccount:
    def __init__(self, name, account_number):
        self._name = name
        self._account_number = account_number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def account_number(self):
        return self._account_number


    @account_number.setter
    def account_number(self, new_account_number):
        self._account_number = new_account_number

account = BankAccount("John Doe", "1234567890")
print("Account Name:", account.name)
print("Account Number:", account.account_number)
account.name = "Jane Doe"
account.account_number = "0987654321"
print("Updated Account Name:", account.name)
print("Updated Account Number:", account.account_number)
