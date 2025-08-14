def calculate_discount(cost):
    if cost > 100:
        return cost * 0.8
    elif cost >= 50:
        return cost * 0.9
    else:
        return cost
#invoke the function   
user_cost =float(input("enter your cost"))
result_cost=calculate_discount(user_cost)
print(result_cost)