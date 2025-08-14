grades={"maria":67,
    "john" :50,
    "anne" :70,
    "paul" :65,
    "dave" :98,
    "angel":95,
    "liam" :62,
    "joy"  :20,
    "larah":76,
    "sarah":96
}
average=sum(grades.values())/len(grades)
print(f"average grade:{average:.2f}")

#highest score
highest_score=max(grades.values())
for student, score in grades.items():
    if score ==highest_score:
        print(f"highest score : {student} with {score}")

grades["sarah"]= 100
for student, score in grades.items():
    if score>80:
  
    