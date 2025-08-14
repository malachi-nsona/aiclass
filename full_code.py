def kilometer_converter():
    kilometers=float(input("enter kilometers"))
    miles=kilometers*0.621371

    print(f'{kilometers} km = {miles:.2f} miles')


def temp_converter():
    temp_c =float(input("enter celsius"))
    temp_f =(temp_c*9/5)+ 32
    print(f'{temp_c} c = {temp_f:.1f} f')
    


def calculate_discount():
    cost=float(input("enter the cost: MK"))
    if cost > 100:
        final= cost * 0.8
    elif cost >= 50:
        final= cost * 0.9
    
    else:
        final= cost
    print(f'discounted cost: MK{final:.2f}')  


def main():
    print("Welcome to Smart Tools!")
    print("1.kilometers to miles converter") 
    print("2.temperature converter (c to f)")
    print("3.shop discount calculator")

    choice = input("choose an option (1-3):")
    if choice=="1":
        kilometer_converter()
    elif choice =="2":
        temp_converter()
    elif choice=='3':
        calculate_discount()        
    else:
        print("Invalid choice. Try Again")   
main() 