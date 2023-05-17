class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance+=amount
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

yassin=BankAccount(0.05,150)
ahmed=BankAccount(0.10,1000)


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdraw(self,amount):
        self.account.withdraw(amount)
        return self
    def makedisplay(self):
        self.account.display_account_info()
        return self

amine=User("amine","yyyyy@gmail.com")
amine.make_deposit(100).make_withdraw(50).makedisplay()