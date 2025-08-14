#program to check points

def check_points(points):
    if points < 36:
        return "pass"
    else:
        return "fail"
    
userpoints = int(input("enter your points")) 

#invoke the function
result_points=check_points(userpoints)
print(result_points)