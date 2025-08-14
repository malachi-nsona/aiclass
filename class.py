
class bank_account:
    def __init__(self, account_name):
        self.account_name=account_name
        self.balance=0
         
    def deposit(self,amount):
        self.balance+=amount
        return f"deposit is successful, your current balance is{amount}"
            
    def withdraw(self,amount):
        if self.balance>=amount:
           self.balance-=amount
           return f"withdrawal successful, your current balance is {amount}"
        else: 
            return f"insufficient funds"  

account_name=["chernly","christine"]
airtel_account=bank_account("chernly")
deposit_money=input("how much money would you like to deposit")
print(deposit_money)
withdrawal_money=input("how much money would you like to withdraw")
print(withdrawal_money)