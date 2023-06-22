class BankAccount:
    def __init__(self, account_num):
        self._accountNum = account_num
        self._balance = 0

    # About Account Number
    def getAccountNum(self):
        return self._accountNum
    
    def _setAccountNum(self, account_num):
        self._accountNum = account_num
    
    # About Balance
    def getBalance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance < amount:
            return (-1)
        self._balance -= amount
        return 1