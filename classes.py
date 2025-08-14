class quiz:
    def __init__(self,questions,answers):
        self.quest=questions
        self.ans=answers
            
    def display_question()













class bank_account:
    def __init__(self,name,number,balance):
        self.name=name
        self.number=number
        self.balance=balance

    def deposit(self,money):
            if money> self.balance:
                 return "{money} deposited"

    def withdraw(self,money):
         if money > self.balance:
              return "insufficient funds"
         return "{money} withdrawn"    
        
credit_account=bank_account(name='chernly',number=11678,balance=78906)        
credit_account.deposit(4578)






