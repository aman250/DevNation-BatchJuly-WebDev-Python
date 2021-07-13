classesHeld=int(input("numer of classes held"))
classesAttendent=int(input("number of classes attendent"))
attendence= int((classesAttendent/classesHeld)*100)
print(attendence)
if attendence < 75:
    print("you are not eligible to attend exams")
else:
    print("you are eligible to attend the exams")
