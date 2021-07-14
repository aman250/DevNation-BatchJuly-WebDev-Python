print("_____________________________Attendance Checker___________________________")
print("A student will not be allowed to sit in an exam if his/her attendance is less than 75%.")
cl_hld=int(input("Enter your Number of classes are held:_ "))
cl_atd=int(input("Enter Number of classes are attend:_ "))

calculating_attendance=(100*cl_atd)/cl_hld
if calculating_attendance >=75:
    print("You are allowed to sit in exam \n Your attendance percentage is :: "+str(calculating_attendance))
else:
    print("You are not allowed to sit in exam \n Your attendance percentage is :: " + str(calculating_attendance))
