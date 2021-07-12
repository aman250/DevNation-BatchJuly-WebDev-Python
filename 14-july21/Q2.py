Classes_held=input("enter total classes that is held: ")
Attend_Classes=input("enter total classes that are attended: ")
percentage=(int(Attend_Classes)/int(Classes_held))*100
print("Percentage is: " + str(percentage))
if percentage>=75:
    print("Student is allowed to sit in exam")
else:
    print("Student is not allowed to sit in exam")