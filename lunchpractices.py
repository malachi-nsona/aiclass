class book:
    def __init__(self,title,author,page_count):
        self.name=title
        self.writer=author
        self.pages=page_count

    def display_info(self):
        print (f"the book is {self.name},written by {self.writer},{self.pages}pages")


my_book=book("diamonds in the rough", "D.Johnnes",600)        
my_book1=book("honeymoon", "J.Patterson",642)
my_book2=book("geography4", "DDM",340)

#calling method display_info
my_book.display_info()
my_book1.display_info()
my_book2.display_info()


class bankaccount:
    def __init__(self,account_holder,balance):
        self.name=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance +=amount
        return f"deposit completed, new balance is {amount}"

    def withdrawal(self,amount):
        self.balance >= amount
        self.balance -= amount
        return f"withdrawal completed , new balance is {amount}"   
    
    def display_balance(self,income):
        self.balance=income
        print (f"current balance in yoour account is {income}")
        