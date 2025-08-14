#request two numbers from user
num1=float(input("enter selected number"))
num2=float(input("enter selected number"))

#request the user for an operator
operation=input("enter{+,-,/,^}:")
def calculate():
    if operation=="+":
        result=num1 + num2
    elif operation=="-":
        result=num1 - num2
    elif operation=="*":
        result=num1 * num2  
    elif operation=="/":
        result=num1 / num2
    else:
        result="invalid operation"   

print