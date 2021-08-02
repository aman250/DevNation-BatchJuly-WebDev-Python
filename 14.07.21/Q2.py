# attendence checker
total_classes = int(input(" enter total number of classes:"))
classes_attend = int(input(" enter number of classes attend:"))

#result
attendence = int((classes_attend/total_classes)*100)

print(str(attendence) + '%')

if attendence < 75 :
    print("you are not allowed to sit in exams")
else:
    print("you are not allowed to sit in exams")