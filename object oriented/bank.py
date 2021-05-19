# class Bank:
#     bankname="SBI"
#     def account(self,accountno,name):
#         self.accountno=accountno
#         self.name=name
#         self.minbalance=10000
#         self.balance=self.minbalance
#     def deposite(self,amt):
#         self.amt=amt
#         self.balance +=self.amt
#         print("your",Bank.bankname,"account has been credited with amt",self.amt)
#         print("your current balance=",self.balance)
#     def withdraw(self,amt):
#         self.amt = amt
#         if self.amt > self.balance:
#             print("insufficient balance")
#         else:
#             print("account debited with",self.amt)
#             self.balance -=self.amt
#             print("available balance",self.balance)
# obj=Bank()
# obj.account(123,"abhi")
# obj.deposite(2500)
# obj.withdraw(1500)
#


class Bank:
    bankname="sbi"
    def account(self,accno,name):
        self.accno=accno
        self.name=name
        self.minbalance=1000
        self.balance=self.minbalance
    def deposit(self,amt):
        self.amt=amt
        self.balance+=self.amt
        print("your",Bank.bankname ,"account is credited ",self.amt)
        print("ypur curreent balance is",self.balance)
    def withdraw(self,amt):
        self.amt=amt
        if self.amt>self.balance:
            print("insufficient balance")
        else:
            print("account debited with",self.amt)
            self.balance -=self.amt
            print("your current balance",self.balance)

obj=Bank()
obj.account(1234,"abu")
obj.deposit(1000)
obj.withdraw(500)
