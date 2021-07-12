
nofClasses = input("Enter Number of classes:")
print(nofClasses)
nofClassesAttend = input("Enter Number of classes Attended:")
print(nofClassesAttend)
percentage=(int(nofClasses)/int(nofClassesAttend)*100)
print("Your percentage is: " +str(percentage))
if str(percentage) < "75%":
    print("You are not allowed to take any class")
else:
    print("you are allowed to take classes")