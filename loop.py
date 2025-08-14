#login system
usernames= ["constantine","james","christine","esther","paul"]
userinput=input("enter your name to log in")
for i in usernames:
    valid= ""
    if userinput==i:
       valid +=f"welcome{userinput}"
       break

    valid += f"{userinput} not recognised"
print(valid)    

#log in system
usernames=["malachi","christine","esther"]
userinput=input("enter your name")
password="wisdom"
userinput=input
for i in usernames:
    valid = ""
    if userinput==i:
       valid += f"welcome{userinput}"
       break
    valid += f"{userinput}not recognized"

print(valid)    