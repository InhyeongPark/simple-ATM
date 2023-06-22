from classes.BankAccount import BankAccount

class Client:
    def __init__(self, fname='firstname', lname = 'lastname', pw='1234'):
        self._fname = fname
        self._lname = lname
        self._pw = pw
        self._accounts = {}

    # About First Name
    def getFirstName(self):
        return self._fname
    
    def setFirstName(self, fname):
        self._fname = fname

    # About Last Name
    def getLastName(self):
        return self._lname
    
    def setLastName(self, lname):
        self._lname = lname
    
    # About password
    def getPW(self):
        return self._pw
    
    def _setPW(self, pw):
        self._pw = pw

    # About Accounts
    def getAccount(self, account_num):
        return self._accounts[account_num]

    def getAllAccounts(self):
        all = list((self._accounts).keys())
        return all
    
    def setAccount(self, new_account):
        account_num = new_account.getAccountNum()
        self._accounts[account_num] = new_account

    def setAllAccounts(self, accounts):
        for account in accounts:
            self.setAccount(account)


