class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance>0 :
            self.balance-= amount
        else:
            print("Insufficient funds: Charging a $5 fee" )
            self.balance-= 5
        return self
    def display_account_info(self):
        print("balance:$",self.balance)
        return self
    
    
    def yield_interest(self):
        if self.balance > 0 :
            self.balance+=(self.balance * self.int_rate)
        return self
    @classmethod
    def printall(cls):
        for account in cls.accounts :
            cls.display_account_info(account)

amine=BankAccount(0.05,150)
aziz=BankAccount(0.10,1000)

amine.display_account_info().deposit(50).deposit(70).deposit(80).withdraw(50).yield_interest().display_account_info()
aziz.deposit(50).deposit(50).withdraw(100.1).withdraw(50.5).withdraw(33.3).withdraw(200).yield_interest().display_account_info()